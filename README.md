# Blink Detection System

### Features
- Real-time blink detection using webcam.
- Calculation of the Eye Aspect Ratio (EAR) to detect blinks.
- Auditory feedback using `pyttsx3` to vocalize messages (commented out in the code).
- On-screen display of blink count.
- Detection of specific blink patterns to communicate different needs or emotions.

### Requirements
- Python 3.x
- OpenCV (`opencv-python`)
- Dlib (`dlib`)
- Scipy (`scipy`)
- imutils (`imutils`)
- pyttsx3 (`pyttsx3`)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/blink-detection.git
   cd blink-detection
   ```

2. **Install Dependencies:**
   ```bash
   pip install opencv-python dlib scipy imutils pyttsx3
   ```

3. **Download Dlib's Pre-trained Model:**
   - Download the `shape_predictor_68_face_landmarks.dat` file from [Dlib's model repository](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) and place it in the project directory.

### Usage

1. **Run the Script:**
   ```bash
   python blink_detection.py
   ```

2. **Operation:**
   - The application will open a video window displaying the live feed from your webcam.
   - It will continuously detect eye blinks and calculate the EAR to interpret blink patterns.
   - Based on the blink frequency, specific messages will be printed to the console (or spoken if uncommented).

3. **Commands:**
   - Press 'q' to quit the video window.

### Code Explanation

- **Eye Aspect Ratio (EAR):** The EAR is used to determine if the eyes are closed. If the EAR is below a certain threshold (0.2), it is considered a blink.
- **Blink Count:** The code tracks consecutive blinks and prints messages after a certain count is reached. These messages indicate basic needs or emotions.
- **Auditory Feedback:** The `pyttsx3` engine can be used for vocalizing messages (currently commented out in the code).

### Troubleshooting

- **No Video Feed:** Ensure that your webcam is connected and accessible.
- **Error Loading Model:** Make sure the `shape_predictor_68_face_landmarks.dat` file is in the correct directory and properly downloaded.
