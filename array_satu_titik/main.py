import cv2 as cv

gambar = cv.imread("gambar.jpg", 1)
x = 200
y = 200
print(gambar[y, x])
cv.imshow("Gambar", gambar)
cv.waitKey(0)
cv.destroyAllWindws()
