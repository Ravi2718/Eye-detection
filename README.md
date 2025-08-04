# 👁️ Eye Blink Detection System

A real-time eye blink detection system using OpenCV, dlib, and facial landmarks. Designed for accessibility, gesture control, or hands-free communication.

---

## 🧠 What It Does

- 🔍 Tracks eyes using facial landmarks
- 📉 Calculates Eye Aspect Ratio (EAR)
- 🔄 Counts blinks and detects patterns
- 🔊 Triggers voice alerts based on blink frequency

---

## ⚙️ Features

| Blink Pattern | Triggered Alert     |
|---------------|---------------------|
| 2 Blinks      | "I Need Water"      |
| 3 Blinks      | "I Need Food"       |
| 4 Blinks      | "I am Sad"          |

- 👁️ Real-time detection from webcam
- 🧠 Uses dlib’s facial landmark predictor
- 🔈 Voice alerts (via `pyttsx3`) – optional
- 📊 Blink counter displayed on-screen

---

## 📦 Requirements

Add this to a `requirements.txt` file:

```

opencv-python
dlib
imutils
scipy
pyttsx3

````

Then install all dependencies:

```bash
pip install -r requirements.txt
````

---

## 🪟 Windows Users: How to Fix `dlib` Install Error

If you see a CMake or build error when installing `dlib`:

### Option 1: Install Prebuilt Wheel

1. Visit [Gohlke’s unofficial builds](https://www.lfd.uci.edu/~gohlke/pythonlibs/#dlib)
2. Download the `.whl` that matches your Python version (e.g., `cp310` for Python 3.10)
3. Install it manually:

```bash
pip install dlib‑19.24.2‑cp310‑cp310‑win_amd64.whl
```

### Option 2: Build from Source (Advanced)

* Install [CMake](https://cmake.org/download/)
* Install [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
* Make sure both are added to your system PATH

---

## 📁 Setup Instructions

1. Clone the repo or download the code
2. Download the shape predictor file:

   * [shape\_predictor\_68\_face\_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
3. Place the `.dat` file in your project folder

---

## 🚀 How to Run

```bash
python blink_detector.py
```

* Open your webcam
* Look directly into it
* Watch for blink-triggered alerts
* Press `q` to quit

---

## ⚙️ Customize

* 🔧 Change sensitivity:

  ```python
  EAR_THRESHOLD = 0.2
  ```
* 🔊 Enable voice:
  Uncomment `engine.say()` lines in the script
* ➕ Add new commands:
  Extend the blink count `if` logic

---

## 💡 Tips for Best Results

* Use good lighting
* Face the webcam directly
* Avoid glasses or head tilts (they may affect detection)

---

