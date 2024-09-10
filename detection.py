import cv2

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

vc = cv2.VideoCapture(0)


def create_bounding_box(vid):
    """ 
        Returns bounding box for faces 
    """
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(
        gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces


while True:

    result, vf = vc.read()
    if result is False:
        break  # terminate the loop if the frame is not loaded successfully

    faces = create_bounding_box(
        vf
    )

    cv2.imshow(
        "Face Detection", vf
    ) 

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vc.release()
cv2.destroyAllWindows()
