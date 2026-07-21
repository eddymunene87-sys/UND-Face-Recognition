import os
import cv2

from utils.camera import Camera
from utils.face_detector import FaceDetector
from utils.image_quality import ImageQuality


class FaceRegistrar:

    def __init__(self,
                 dataset_path="dataset",
                 max_images=30):

        self.dataset_path = dataset_path
        self.max_images = max_images

        self.camera = Camera()
        self.detector = FaceDetector()

    def register_person(self, name):

        person_folder = os.path.join(
            self.dataset_path,
            name
        )

        os.makedirs(person_folder, exist_ok=True)

        self.camera.start()

        image_number = 0

        print("Registration Started...")

        while image_number < self.max_images:

            frame = self.camera.get_frame()

            if frame is None:
                continue

            faces = self.detector.detect_faces(frame)

            message = ""

            color = (0, 255, 0)

            # Draw rectangles
            frame = self.detector.draw_faces(
                frame,
                faces
            )

            if len(faces) == 0:

                message = "No face detected"

                color = (0, 0, 255)

            elif len(faces) > 1:

                message = "Only one face allowed"

                color = (0, 0, 255)

            else:

                top, right, bottom, left = faces[0]

                face = frame[top:bottom, left:right]

                if ImageQuality.is_too_small(face):

                    message = "Move closer"

                    color = (0, 0, 255)

                elif ImageQuality.is_blurry(face):

                    message = "Image blurry"

                    color = (0, 0, 255)

                elif ImageQuality.is_too_dark(face):

                    message = "Improve lighting"

                    color = (0, 0, 255)

                else:

                    face = cv2.resize(
                        face,
                        (300, 300)
                    )

                    filename = os.path.join(
                        person_folder,
                        f"{image_number+1}.jpg"
                    )

                    cv2.imwrite(
                        filename,
                        face
                    )

                    image_number += 1

                    message = f"Captured {image_number}/{self.max_images}"

                    color = (0, 255, 0)

            cv2.putText(
                frame,
                message,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                color,
                2
            )

            cv2.imshow(
                "Face Registration",
                frame
            )

            key = cv2.waitKey(120)

            if key == ord("q"):
                break

        self.camera.stop()

        print("Registration Finished.")