# Intelligent Systems Lab – Face Detection Demo

_The zone where I experiment my ideas_

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.12.0-brightgreen.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)
[![Repo](https://img.shields.io/badge/GitHub-DropPlan--at13%2Fintelligent--systems--lab-black.svg)](https://github.com/DropPlan-at13/intelligent-systems-lab)

Lightweight face detection demo using OpenCV Haar cascades. Runs on webcam input and draws bounding boxes around detected faces.

## Quick Start

```bash
# Clone and enter
git clone https://github.com/DropPlan-at13/intelligent-systems-lab.git
cd intelligent-systems-lab

# Create venv
python3 -m venv .env
source .env/bin/activate

# Install deps
pip install -r requirements.txt

# Run
python cv1.py
```

Press `ESC` to exit the camera window.

## Configuration

By default values are read from `.env` (preferred). For compatibility this script also looks for `.env/.env` if present (e.g., when keeping the venv in `.env/`).

```env
CAMERA_INDEX=0
CASCADE_PATH=haarcascade_frontalface_default.xml
SCALE_FACTOR=1.3
MIN_NEIGHBORS=5
```

- `CAMERA_INDEX`: Which camera to open (0 is default).
- `CASCADE_PATH`: Path to Haar cascade XML (included in repo).
- `SCALE_FACTOR`: How much the image size is reduced at each scale.
- `MIN_NEIGHBORS`: How many neighbors each candidate rectangle should have to retain it.

## Project Structure

```
cv1.py                         # Main script
haarcascade_frontalface_default.xml  # Haar cascade
requirements.txt               # Runtime dependencies
.env/                          # (optional) Python virtual environment
.env/.env                      # (legacy) Runtime configuration file if you keep venv in .env/
.env.example                   # Sample env values to copy to .env
```

## Troubleshooting

- **Camera not opening**: Set the correct `CAMERA_INDEX`. Laptop cam: `0`. External cams: try `1` or `2`.
- **Cascade load error**: Ensure `haarcascade_frontalface_default.xml` exists and `CASCADE_PATH` points to it.
- **Wayland warning**: If on Wayland, set `QT_QPA_PLATFORM=wayland` or run under X11.

## Contributing

1. Fork the repo and create a feature branch.
2. Make changes with clear commits.
3. Open a PR against `main` with a concise description.

## License

MIT License. See LICENSE for details.
