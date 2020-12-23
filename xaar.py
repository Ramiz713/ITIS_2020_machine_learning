import os
import cv2 as cv


def detect_face_and_eyes(image):
    red = (0, 0, 255)
    blue = (255, 0, 0)
    thickness = 2
    frame_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    # Распознавание лица
    faces = face_cascade.detectMultiScale(image)
    for (x, y, width, height) in faces:
        x2, y2 = x + width, y + height
        # Отрисовка рамки для лица
        cv.rectangle(image, (x, y), (x2, y2), red, thickness)
        # Распознавание глаз
        faceROI = frame_gray[y:y + height, x:x + width]
        eyes = eye_cascade.detectMultiScale(faceROI)
        for (x2, y2, width2, height2) in eyes:
            eye_center = (x + x2 + width2 // 2, y + y2 + height2 // 2)
            radius = int(round((width2 + height2) * 0.25))
            # Отрисовка круга для глаз
            cv.circle(image, eye_center, radius, blue, thickness)
    return image


face_cascade = cv.CascadeClassifier(os.path.abspath('haarcascades/haarcascade_frontalface_alt.xml'))
eye_cascade = cv.CascadeClassifier(os.path.abspath('haarcascades/haarcascade_eye_tree_eyeglasses.xml'))
for file in os.listdir('images'):
    file_name, file_extension = os.path.splitext(file)
    if file_extension == '.jpg':
        image = cv.imread('images/' + file)
        image = detect_face_and_eyes(image)
        cv.imshow("Face and eyes recognition", image)
        cv.waitKey(0)
        cv.destroyAllWindows()