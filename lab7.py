import cv2


image = cv2.imread("example.jpg")

if image is None:
    print("Error: Unable to load image.")
    exit()


height, width = image.shape[:2]


left_quadrant = image[:, :width // 2]
right_quadrant = image[:, width // 2:]
top_quadrant = image[:height // 2, :]
bottom_quadrant = image[height // 2:, :]


cv2.imshow("Left Quadrant", left_quadrant)
cv2.imshow("Right Quadrant", right_quadrant)
cv2.imshow("Top Quadrant", top_quadrant)
cv2.imshow("Bottom Quadrant", bottom_quadrant)


cv2.waitKey(0)
cv2.destroyAllWindows()
