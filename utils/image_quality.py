import cv2


class ImageQuality:

    @staticmethod
    def is_blurry(image, threshold=100):
        """
        Returns True if the image is blurry.
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        variance = cv2.Laplacian(gray, cv2.CV_64F).var()

        return variance < threshold

    @staticmethod
    def is_too_dark(image, threshold=60):
        """
        Returns True if the image is too dark.
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        brightness = gray.mean()

        return brightness < threshold

    @staticmethod
    def is_too_small(face, minimum_size=150):
        """
        Reject small faces.
        """
        height, width = face.shape[:2]

        return width < minimum_size or height < minimum_size