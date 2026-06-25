import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import os

# Settings
SAVE_FOLDER = 'dataset'
SAMPLES_TO_COLLECT = 100  # Number of samples per label

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

# Ask user for label
label = input("Enter gesture label (e.g., hello, thank_you): ").strip().lower()
save_path = os.path.join(SAVE_FOLDER, f"{label}.csv")

# Make sure save folder exists
os.makedirs(SAVE_FOLDER, exist_ok=True)

# Webcam
cap = cv2.VideoCapture(0)
print(f"Collecting {SAMPLES_TO_COLLECT} samples for label: '{label}'. Press 'q' to quit.")

collected_data = []
sample_count = 0

while cap.isOpened() and sample_count < SAMPLES_TO_COLLECT:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    landmark_list = []

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for lm in hand_landmarks.landmark:
                landmark_list.extend([lm.x, lm.y, lm.z])

        # Pad to 126 values (2 hands * 21 landmarks * 3 coords)
        while len(landmark_list) < 126:
            landmark_list.append(0.0)

        collected_data.append(landmark_list)
        sample_count += 1

        # Draw
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.putText(frame, f"Recording '{label}' [{sample_count}/{SAMPLES_TO_COLLECT}]", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    else:
        cv2.putText(frame, "No hands detected", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Collecting Gesture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release
cap.release()
cv2.destroyAllWindows()
hands.close()

# Save to CSV
if collected_data:
    df_new = pd.DataFrame(collected_data)
    if os.path.exists(save_path):
        df_existing = pd.read_csv(save_path, header=None)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    df_combined.to_csv(save_path, index=False, header=False)
    print(f"Saved {len(collected_data)} samples to {save_path}")
else:
    print("No data collected.")
