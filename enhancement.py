import cv2
import numpy as np

def process_all(input_path, output_folder):
    img = cv2.imread(input_path)

    # -------- CLAHE --------
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)

    clahe_img = cv2.merge((cl, a, b))
    clahe_img = cv2.cvtColor(clahe_img, cv2.COLOR_LAB2BGR)

    # -------- Gamma --------
    gamma = 1.5
    invGamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** invGamma * 255
                      for i in np.arange(256)]).astype("uint8")

    gamma_img = cv2.LUT(img, table)

    # -------- Face Detection --------
    face_img = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(face_img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # -------- Save Images --------
    cv2.imwrite(f"{output_folder}/original.jpg", img)
    cv2.imwrite(f"{output_folder}/clahe.jpg", clahe_img)
    cv2.imwrite(f"{output_folder}/gamma.jpg", gamma_img)
    cv2.imwrite(f"{output_folder}/face.jpg", face_img)

     