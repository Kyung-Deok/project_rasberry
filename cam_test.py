# import necessary packages
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
#
# open webcam (웹캠 열기)
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

# loop through frames
while webcam.isOpened():

    # read frame from webcam
    status, frame = webcam.read()

    if not status:
        break

    # apply object detection (물체 검출)
    bbox, label, conf = cv.detect_common_objects(frame)

    print(bbox, label, conf)

    # draw bounding box over detected objects (검출된 물체 가장자리에 바운딩 박스 그리기)
    out = draw_bbox(frame, bbox, label, conf, write_conf=True)

    # display output
    cv2.imshow("Real-time object detection", out)

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release resources
webcam.release()
cv2.destroyAllWindows()
#
# import cv2
#
# def onChange(pos):
#     pass
#
# src = cv2.imread("D:/leekd/py4e/image/qswd1371269861418.jpg", cv2.IMREAD_GRAYSCALE)
# # src = cv2.VideoCapture(0)
# # ret, img_color = src.read()
# cv2.namedWindow("Trackbar Windows")
#
# cv2.createTrackbar("threshold", "Trackbar Windows", 0, 255, onChange)
# cv2.createTrackbar("maxValue", "Trackbar Windows", 0, 255, lambda x : x)
#
# cv2.setTrackbarPos("threshold", "Trackbar Windows", 127)
# cv2.setTrackbarPos("maxValue", "Trackbar Windows", 255)
#
# while cv2.waitKey(1) != ord('q'):
#
#     thresh = cv2.getTrackbarPos("threshold", "Trackbar Windows")
#     maxval = cv2.getTrackbarPos("maxValue", "Trackbar Windows")
#
#     _, binary = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
#
#     cv2.imshow("Trackbar Windows", binary)
#
# cv2.destroyAllWindows()