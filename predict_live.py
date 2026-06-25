import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import pickle
import time
import pyttsx3
import warnings

# Suppress sklearn warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Load trained model
with open('gesture_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Text-to-speech setup
engine = pyttsx3.init()
last_spoken_time = 0
spoken_labels = {}

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

# OpenCV setup
cap = cv2.VideoCapture(0)

print("Starting live prediction. Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip for mirror image and convert color
    frame = cv2.flip(frame, 1)
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    feature_list = []

    if results.multi_hand_landmarks:
        landmarks_all_hands = []

        for hand_landmarks in results.multi_hand_landmarks:
            for lm in hand_landmarks.landmark:
                landmarks_all_hands.extend([lm.x, lm.y, lm.z])

        # Pad to 126 values (2 hands * 21 landmarks * 3 coords)
        while len(landmarks_all_hands) < 126:
            landmarks_all_hands.append(0.0)

        feature_list = landmarks_all_hands

        # Predict if features are filled
        if len(feature_list) == 126:
            feature_names = [f'f{i}' for i in range(126)]
            input_df = pd.DataFrame([feature_list], columns=feature_names)
            prediction = model.predict(input_df)[0]

            # Display label
            cv2.putText(frame, f'Prediction: {prediction}', (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Speak only if 60 seconds passed since last speech for this label
            current_time = time.time()
            if prediction not in spoken_labels or (current_time - spoken_labels[prediction]) > 60:
                engine.say(prediction)
                engine.runAndWait()
                spoken_labels[prediction] = current_time

        # Draw landmarks
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Show the frame
    cv2.imshow('Sign Language Prediction', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
hands.close()
engine.stop()
