import os
import pickle
import time

import cv2
import face_recognition
import numpy as np


class Recognizer:

    def __init__(
        self,
        encodings_file="encodings/encodings.pkl",
        threshold=0.45,
        resize_scale=0.25
    ):

        if not os.path.exists(encodings_file):
            raise FileNotFoundError(
                f"Encoding file not found:\n{encodings_file}"
            )

        with open(encodings_file, "rb") as file:
            data = pickle.load(file)

        self.known_encodings = data["encodings"]
        self.known_names = data["names"]

        self.threshold = threshold
        self.resize_scale = resize_scale

        self.previous_time = time.time()

    def calculate_confidence(self, distance):
        """
        Convert face distance into a confidence percentage.
        """

        confidence = (1 - distance) * 100

        confidence = max(0, min(100, confidence))

        return confidence

    def recognize(self, frame):

        original_frame = frame.copy()

        # ----------------------------------
        # Resize for speed
        # ----------------------------------

        small_frame = cv2.resize(
            frame,
            (0, 0),
            fx=self.resize_scale,
            fy=self.resize_scale
        )

        rgb = cv2.cvtColor(
            small_frame,
            cv2.COLOR_BGR2RGB
        )

        # ----------------------------------
        # Detect Faces
        # ----------------------------------

        face_locations = face_recognition.face_locations(rgb)

        face_encodings = face_recognition.face_encodings(
            rgb,
            face_locations
        )

        # ----------------------------------
        # Recognize Faces
        # ----------------------------------

        for (top, right, bottom, left), face_encoding in zip(
                face_locations,
                face_encodings):

            top = int(top / self.resize_scale)
            right = int(right / self.resize_scale)
            bottom = int(bottom / self.resize_scale)
            left = int(left / self.resize_scale)

            name = "Unknown"
            confidence = 0

            if len(self.known_encodings) > 0:

                distances = face_recognition.face_distance(
                    self.known_encodings,
                    face_encoding
                )

                best_match = np.argmin(distances)

                distance = distances[best_match]

                if distance < self.threshold:

                    name = self.known_names[best_match]

                    confidence = self.calculate_confidence(
                        distance
                    )

                    color = (0, 255, 0)

                else:

                    color = (0, 0, 255)

            else:

                color = (0, 0, 255)

            # -----------------------------
            # Draw Face Box
            # -----------------------------

            cv2.rectangle(
                original_frame,
                (left, top),
                (right, bottom),
                color,
                2
            )

            # -----------------------------
            # Name
            # -----------------------------

            cv2.putText(
                original_frame,
                name,
                (left, top - 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

            # -----------------------------
            # Confidence
            # -----------------------------

            cv2.putText(
                original_frame,
                f"{confidence:.1f}%",
                (left, top - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.65,
                color,
                2
            )

        # ----------------------------------
        # FPS
        # ----------------------------------

        current_time = time.time()

        fps = 1 / (current_time - self.previous_time)

        self.previous_time = current_time

        cv2.putText(
            original_frame,
            f"FPS : {int(fps)}",
            (15, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2
        )

        # ----------------------------------
        # Faces Detected
        # ----------------------------------

        cv2.putText(
            original_frame,
            f"Faces : {len(face_locations)}",
            (15, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2
        )

        return original_frame