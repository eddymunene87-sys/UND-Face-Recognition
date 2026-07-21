import cv2

for index in range(10):
    cap = cv2.VideoCapture(index)

    if cap.isOpened():
        ret, frame = cap.read()

        if ret:
            print(f"Camera {index} is working.")
            cv2.imshow(f"Camera {index}", frame)
            cv2.waitKey(2000)
            cv2.destroyAllWindows()

        cap.release()