import cv2
import face_recognition


class FaceDetector:
    def __init__(self):
        """
        Initializes the face detector.
        """
        pass

    def detect_faces(self, frame):
        """
        Detect faces in a frame.

        Args:
            frame: Image captured from the webcam.

        Returns:
            List of face locations.
        """

        # Convert BGR (OpenCV) to RGB (face_recognition)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect face locations
        face_locations = face_recognition.face_locations(rgb_frame)

        return face_locations

    def draw_faces(self, frame, face_locations):
        """
        Draw rectangles around detected faces.

        Args:
            frame: Original frame.
            face_locations: List of detected faces.

        Returns:
            Frame with rectangles drawn.
        """

        for top, right, bottom, left in face_locations:

            cv2.rectangle(
                frame,
                (left, top),
                (right, bottom),
                (0, 255, 0),
                2
            )

        return frame