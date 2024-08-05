import cv2

image = cv2.imread("example.jpg")

if image is None:
    print("Error: Unable to load image.")
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

_, threshold_image = cv2.threshold(blurred_image, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

cv2.imshow("Original Image", image)
cv2.imshow("Contour Image", contour_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
