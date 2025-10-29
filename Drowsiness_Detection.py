import cv2
import dlib
import numpy as np
from scipy.spatial import distance
from imutils import face_utils
from pygame import mixer
import argparse
import sys

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

def main():
    print("Starting drowsiness detection system...")

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Drowsiness Detection System")
    parser.add_argument("--threshold", type=float, default=0.25, help="EAR threshold")
    parser.add_argument("--frames", type=int, default=20, help="Number of frames to check")
    parser.add_argument("--show_video", action="store_true", help="Show video feed")
    args = parser.parse_args()

    print(f"Using threshold: {args.threshold}, frames: {args.frames}, show_video: {args.show_video}")

    # Initialize Pygame mixer
    try:
        mixer.init()
        mixer.music.load("music.wav")
        print("Audio system initialized successfully.")
    except Exception as e:
        print(f"Error initializing audio system: {e}")
        sys.exit(1)

    # Initialize dlib's face detector and facial landmark predictor
    try:
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")
        print("Face detector and predictor initialized successfully.")
    except Exception as e:
        print(f"Error initializing face detector or predictor: {e}")
        print("Make sure the shape_predictor_68_face_landmarks.dat file is in the 'models' directory.")
        sys.exit(1)

    # Get the indexes for left and right eyes
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

    # Start video capture
    print("Attempting to start video capture...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        sys.exit(1)
    print("Video capture started successfully.")

    frame_count = 0
    alarm_on = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(gray, 0)
        print(f"Detected {len(faces)} faces in frame")

        for face in faces:
            shape = predictor(gray, face)
            shape = face_utils.shape_to_np(shape)

            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)

            ear = (leftEAR + rightEAR) / 2.0
            print(f"Current EAR: {ear:.2f}")

            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            if ear < args.threshold:
                frame_count += 1
                print(f"Frame count: {frame_count}")
                if frame_count >= args.frames:
                    if not alarm_on:
                        alarm_on = True
                        mixer.music.play(-1)  # Loop the alarm sound
                        print("Drowsiness detected! Alarm started.")
                    cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            else:
                frame_count = 0
                if alarm_on:
                    alarm_on = False
                    mixer.music.stop()
                    print("Drowsiness alert cleared. Alarm stopped.")

            cv2.putText(frame, f"EAR: {ear:.2f}", (300, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        if args.show_video:
            cv2.imshow("Frame", frame)
            print("Displaying video frame")

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Quit signal received")
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Drowsiness detection system stopped.")

if __name__ == "__main__":
    main()