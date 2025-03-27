import os
import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)

# Define the directory where images will be stored
directory = 'Image'

# Ensure the main directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# Create subdirectories for each letter (A-Z)
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in letters:
    os.makedirs(os.path.join(directory, letter), exist_ok=True)

# Count existing images in each folder
count = {letter.lower(): len(os.listdir(os.path.join(directory, letter))) for letter in letters}

print("Press 'A-Z' to save images. Press 'ESC' to exit.")

while True:
    # Capture frame from webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image. Exiting...")
        break

    # Define Region of Interest (ROI) for hand gestures
    cv2.rectangle(frame, (0, 40), (300, 400), (255, 255, 255), 2)
    roi = frame[40:400, 0:300]

    # Display the frames
    cv2.imshow("Webcam Feed", frame)
    cv2.imshow("ROI", roi)

    # Detect key press
    key = cv2.waitKey(10) & 0xFF
    
    if key == 27:  # Press 'Esc' to exit
        print("Exiting program...")
        break

    # Save images when a valid letter key (A-Z) is pressed
    if chr(key).upper() in letters:
        letter = chr(key).upper()
        file_path = os.path.join(directory, letter, f"{count[letter.lower()]}.png")
        cv2.imwrite(file_path, roi)
        count[letter.lower()] += 1
        print(f"Saved: {file_path}")

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
