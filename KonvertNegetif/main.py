import cv2
def negative_convert(gambar):
    for i in range(0, height - 1):
        for j in range(0, width - 1):
            pixel = gambar[i, j]
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
            gambar[i, j] = pixel
    return gambar
gambar = cv2.imread("image.jpeg", 1)
height, width, channels = gambar.shape
gambar = negative_convert(gambar)

cv2.imshow("Hasil Konversi", gambar)
cv2.waitKey(0)
cv2.destroyAllWindows()