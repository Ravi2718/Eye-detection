import cv2
import dlib
import pyttsx3
import numpy as np
from scipy.spatial import distance
from imutils import face_utils

# ====== Configuration ======
EAR_THRESHOLD = 0.21               # Eye Aspect Ratio threshold to detect eye closure
CONSEC_FRAMES_MIN = 2              # Minimum frames to validate a blink
CONSEC_FRAMES_MAX = 5              # Maximum frames to count as single blink
ENABLE_VOICE = False               # Set to True to enable voice alerts
PREDICTOR_PATH = 'shape_predictor_86_face_landmarks.dat'  # Or use 68-point version

# ====== Initialization ======
engine = pyttsx3.init()
cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(PREDICTOR_PATH)

def eye_aspect_ratio(eye):
    """Calculate Eye Aspect Ratio (EAR) to detect blinking."""
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

def speak(text):
    """Speak the given text using TTS engine."""
    if ENABLE_VOICE:
        engine.say(text)
        engine.runAndWait()

# ====== Blink Variables ======
frame_counter = 0         # Consecutive frames eyes are closed
blink_count = 0           # Total blinks detected
blink_confirmed = False   # Flag for a valid blink sequence

# ====== Main Loop ======
while True:
    success, frame = cap.read()
    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        shape = predictor(gray, face)
        shape_np = face_utils.shape_to_np(shape)

        # Extract eye regions
        left_eye = shape_np[42:48]
        right_eye = shape_np[36:42]

        # Compute EAR
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        avg_ear = (left_ear + right_ear) / 2.0

        # Draw eye contours
        cv2.polylines(frame, [left_eye], True, (0, 255, 0), 1)
        cv2.polylines(frame, [right_eye], True, (0, 255, 0), 1)

        # Check for blink
        if avg_ear < EAR_THRESHOLD:
            frame_counter += 1

            if CONSEC_FRAMES_MIN <= frame_counter <= CONSEC_FRAMES_MAX and not blink_confirmed:
                blink_count += 1
                blink_confirmed = True

                # Trigger voice alerts based on pattern
                if blink_count == 2:
                    print("I Need Water")
                    speak("I Need Water")
                elif blink_count == 3:
                    print("I Need Food")
                    speak("I Need Food")
                elif blink_count == 4:
                    print("I am Sad")
                    speak("I am Sad")

        else:
            # Reset if eyes are open
            if blink_confirmed and frame_counter >= CONSEC_FRAMES_MIN:
                blink_count = 0
            blink_confirmed = False
            frame_counter = 0

        # Show blink count on screen
        cv2.putText(frame, f"Blinks: {blink_count}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow("Eye Blink Detection", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ====== Cleanup ======
cap.release()
cv2.destroyAllWindows()
