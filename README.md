# Real-time Face Detection

This project implements a real-time face detection system using OpenCV and Haar Cascade Classifiers.

## Project Overview

The project uses a webcam feed to detect faces in real-time, drawing bounding boxes around detected faces. It demonstrates the use of computer vision techniques for facial recognition.

## Requirements

- Python 3.x
- OpenCV (cv2)

## Project Structure

The project consists of a single Python script `detection.py` with the following main components:

1. **Initialization**: 
   - Loading the Haar Cascade Classifier for frontal face detection
   - Setting up video capture from the default camera

2. **Face Detection Function**:
   - `create_bounding_box(vid)`: Processes each video frame to detect faces and draw bounding boxes

3. **Main Loop**:
   - Continuously captures video frames
   - Applies face detection to each frame
   - Displays the processed frame with bounding boxes

## Usage

1. Ensure OpenCV is installed (`pip install opencv-python`).
2. Run the script: `detection.py`
3. The webcam feed will open in a new window with face detection active.
4. Press 'q' to quit the application.

## Key Features

- Real-time face detection using Haar Cascade Classifier
- Drawing of green bounding boxes around detected faces
- Minimum face size setting to reduce false positives

## Demo

![image](https://github.com/user-attachments/assets/c6c9acd3-69db-4aca-92b3-23c83ae10f32)

## Performance

The face detection runs in real-time on most modern hardware. Performance may vary based on the resolution of the video feed and the number of faces in the frame.

## Future Improvements

- Implement more advanced face detection algorithms (e.g., deep learning-based methods)
- Add face recognition capabilities to identify specific individuals
- Optimize performance for higher resolution video feeds
- Include options for saving or processing detected faces
