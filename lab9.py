import cv2
import numpy as np


image = cv2.imread("example.jpg")


if image is None:
    print("Error: Unable to load image.")
    exit()


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)


edges = cv2.Canny(blurred_image, 50, 150)


laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)

cv2.imshow("Original Image", image)
cv2.imshow("Edges", edges)
cv2.imshow("Laplacian Filter", laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()
