import cv2

image = cv2.imread("datasets/sample.jpeg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

enhanced = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

cv2.imwrite("outputs/enhanced_sample_v2.jpg", enhanced)

print("Enhanced V2 image saved!")