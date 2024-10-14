from utils import get_limits

from PIL import Image

import cv2


def main() -> None:

    # to change the color, change the values in the list
    blue = [255, 0, 0]

    video_cam = cv2.VideoCapture(0)

    while True:
        ret, frame = video_cam.read()

        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_limit, upper_limit = get_limits(color=blue)

        mask = cv2.inRange(hsv_img, lower_limit, upper_limit)

        mask_ = Image.fromarray(mask)

        bbox = mask_.getbbox()
        print(bbox)

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
