import cv2

image = cv2.imread("example.jpg")

if image is None:
    print("Error: Unable to load image.")
    exit()

blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

smoothed_image = cv2.bilateralFilter(image, 9, 75, 75)

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Smoothed Image", smoothed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
