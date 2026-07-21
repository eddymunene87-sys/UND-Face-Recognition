import os
import pickle

import cv2
import face_recognition
import numpy as np

from utils.image_quality import ImageQuality


class FaceEncoder:

    def __init__(
        self,
        dataset_path="dataset",
        output_file="encodings/encodings.pkl",
        minimum_images=5
    ):

        self.dataset_path = dataset_path
        self.output_file = output_file
        self.minimum_images = minimum_images

    def encode_faces(self):

        known_encodings = []
        known_names = []

        print("=" * 60)
        print("Generating Average Face Encodings")
        print("=" * 60)

        if not os.path.exists(self.dataset_path):
            print("Dataset folder not found.")
            return

        people = sorted(os.listdir(self.dataset_path))

        if not people:
            print("No registered people found.")
            return

        for person_name in people:

            person_folder = os.path.join(
                self.dataset_path,
                person_name
            )

            if not os.path.isdir(person_folder):
                continue

            print(f"\nProcessing {person_name}")

            person_encodings = []

            images = sorted(os.listdir(person_folder))

            for image_name in images:

                image_path = os.path.join(
                    person_folder,
                    image_name
                )

                image = cv2.imread(image_path)

                if image is None:
                    print(f"  ✗ Cannot read {image_name}")
                    continue

                if ImageQuality.is_blurry(image):
                    print(f"  ✗ Blurry {image_name}")
                    continue

                rgb = cv2.cvtColor(
                    image,
                    cv2.COLOR_BGR2RGB
                )

                locations = face_recognition.face_locations(rgb)

                if len(locations) != 1:
                    print(f"  ✗ {image_name} has {len(locations)} faces")
                    continue

                encodings = face_recognition.face_encodings(
                    rgb,
                    locations
                )

                if not encodings:
                    print(f"  ✗ Encoding failed: {image_name}")
                    continue

                person_encodings.append(encodings[0])

            print(f"  Valid images: {len(person_encodings)}")

            if len(person_encodings) < self.minimum_images:

                print("  Skipped (not enough good images)")
                continue

            average_encoding = np.mean(
                person_encodings,
                axis=0
            )

            average_encoding = average_encoding.astype(np.float64)

            known_encodings.append(average_encoding)
            known_names.append(person_name)

            print("  ✓ Average encoding created")

        os.makedirs(
            os.path.dirname(self.output_file),
            exist_ok=True
        )

        with open(self.output_file, "wb") as file:

            pickle.dump(
                {
                    "encodings": known_encodings,
                    "names": known_names
                },
                file
            )

        print("\n" + "=" * 60)
        print("Encoding Complete")
        print("=" * 60)

        print(f"People Encoded : {len(known_names)}")
        print(f"Output File    : {self.output_file}")