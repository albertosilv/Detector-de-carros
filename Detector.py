import cv2
import glob
classificador = "cascade.xml"
Cascade = cv2.CascadeClassifier(classificador)
for x in glob.glob("4.jpeg"):
    image = cv2.imread(x)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    carros = Cascade.detectMultiScale(gray, minSize=(300, 300))
    for (x, y, w, h) in carros:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 210), 2)
    cv2.imshow("oi", image)
    cv2.waitKey(0)



