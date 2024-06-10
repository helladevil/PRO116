import cv2

img=cv2.imread("planetas-nom.png")

cv2.imshow("Planetas del sistema solar :)",img)

cv2.waitKey(0)