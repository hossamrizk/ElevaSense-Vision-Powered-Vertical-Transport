# Finger Counting

This Python script uses the MediaPipe Hands library and OpenCV to perform finger counting with a webcam. It identifies the number of raised fingers, displays the count on the video feed, and tracks changes in finger count over time.

## Prerequisites

Before using this code, make sure you have the following libraries and components installed:

- OpenCV (cv2)
- MediaPipe Hands library
- Python 3

You can install the required packages using pip:

```bash
pip install opencv-python mediapipe
```
## Code Explanation
- The script begins by importing the necessary libraries, including OpenCV, MediaPipe, and the datetime module for time tracking.
- It captures the current time and sets initial values for dfc (displayed finger count) and sec (interval for displaying the finger count).
- Configuration for MediaPipe Hands is set up, defining the parameters for the hand detection model.
- A webcam feed is established using OpenCV.
- In the main loop, frames from the webcam are captured and processed with MediaPipe Hands for hand landmark detection.
- For each detected hand, the script determines the label (left or right) and extracts the landmarks' x and y positions.
- Raised fingers are identified based on the landmark positions, and the script counts raised fingers, updating the fingerCount variable.
- Hand landmarks are drawn on the video feed for visualization.
- The finger count is displayed on the video feed.
- The script monitors the elapsed time since the last display update, updating the display when the specified interval (sec) is reached.
- Pressing the 'q' key breaks the loop, and the video feed is released.
-The script continuously captures the webcam feed, detects hand landmarks, counts raised fingers, and displays the count. It also logs the changes in finger count at specified intervals.
