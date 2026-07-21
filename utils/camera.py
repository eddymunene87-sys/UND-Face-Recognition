import cv2
from config import CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT


class Camera:
    def __init__(self):
        self.cap = None

    def start(self):
        self.cap = cv2.VideoCapture(CAMERA_INDEX)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

        if not self.cap.isOpened():
            raise Exception("Unable to open camera.")

    def get_frame(self):
        """
        Capture a single frame from the webcam.

        Returns:
            frame (numpy.ndarray): The captured frame.
            Returns None if capturing fails.
        """
        if self.cap is None:
            raise Exception("Camera has not been started.")

        ret, frame = self.cap.read()

        if not ret:
            return None

        return frame

    def stop(self):
        """
        Release the webcam and close all OpenCV windows.
        """
        if self.cap is not None:
            self.cap.release()

        cv2.destroyAllWindows()