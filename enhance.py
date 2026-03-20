import cv2
import numpy as np

def enhance_image(image):
    # Convert to LAB color space
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    # Apply CLAHE
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    # Merge channels
    merged = cv2.merge((cl, a, b))

    # Convert back to BGR
    enhanced = cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)

    return enhanced


def gamma_correction(image, gamma=1.5):
    invGamma = 1.0 / gamma
    table = np.array([
        ((i / 255.0) ** invGamma) * 255 for i in np.arange(256)
    ]).astype("uint8")

    return cv2.LUT(image, table)


if __name__ == "__main__":
    # Load image
    image = cv2.imread("images/sample.jpg")

    enhanced = enhance_image(image)
    gamma_img = gamma_correction(enhanced)

    # Show results
    cv2.imshow("Original", image)
    cv2.imshow("Enhanced", enhanced)
    cv2.imshow("Gamma Corrected", gamma_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()