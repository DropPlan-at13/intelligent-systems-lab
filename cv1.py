import cv2
import os
from dotenv import load_dotenv

# Load environment variables.
# Prefer project-level .env; fall back to historical .env/.env (venv-local) for compatibility.
ROOT_ENV = os.path.join(os.path.dirname(__file__), ".env")
LEGACY_ENV = os.path.join(os.path.dirname(__file__), ".env", ".env")

if os.path.isfile(ROOT_ENV):
    load_dotenv(ROOT_ENV)
elif os.path.isfile(LEGACY_ENV):
    load_dotenv(LEGACY_ENV)
else:
    load_dotenv()

CAMERA_INDEX = int(os.getenv("CAMERA_INDEX", 0))
DEFAULT_CASCADE = "haarcascade_frontalface_default.xml"
CASCADE_PATH = os.getenv("CASCADE_PATH", DEFAULT_CASCADE)
SCALE_FACTOR = float(os.getenv("SCALE_FACTOR", 1.3))
MIN_NEIGHBORS = int(os.getenv("MIN_NEIGHBORS", 5))

# Validate cascade path and load
if not os.path.exists(CASCADE_PATH):
    raise FileNotFoundError(
        f"Cascade file not found at '{CASCADE_PATH}'. "
        f"Set CASCADE_PATH or place {DEFAULT_CASCADE} in the project folder."
    )

face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

if face_cascade.empty():
    raise IOError(
        f"Failed to load cascade from '{CASCADE_PATH}'. "
        "Ensure the file is a valid Haar cascade XML."
    )

# Start camera
cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    raise IOError("Cannot open camera")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=SCALE_FACTOR,
        minNeighbors=MIN_NEIGHBORS
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Face Detector", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
