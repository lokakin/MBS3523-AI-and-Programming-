
import cv2
print(cv2.__version__)

capture = cv2.VideoCapture('Resources/dog.mp4')

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    success, img = capture.read()

    img = cv2.resize(img, (int(img.shape[1] / 1.5), int(img.shape[0] / 1.5)))

    # Put a red text on img
    cv2.putText(img, 'I am a cute dog!', (10, 400), font, 3, (0, 0, 255), 5)

    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
