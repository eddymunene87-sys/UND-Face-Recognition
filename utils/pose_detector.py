import cv2


class PoseDetector:

    @staticmethod
    def get_pose(face_location, frame_width):

        top, right, bottom, left = face_location

        center_x = (left + right) // 2

        margin = frame_width * 0.12

        if center_x < frame_width / 2 - margin:
            return "LEFT"

        elif center_x > frame_width / 2 + margin:
            return "RIGHT"

        return "CENTER"