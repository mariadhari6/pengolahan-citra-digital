import cv2
def brigth(intensitas):
    if intensitas < 0:
        return 0
    elif intensitas > 255:
        return 255
    else:
        return intensitas
def atur_bright(self, nilai_kecerahan):
    height, width, channels = self.shape
    for i in range(0, height - 1):
        for j in range(0, width - 1):
            pixel = self[i, j]
            pixel[0] = brigth(self[i, j][0] + nilai_kecerahan)
            pixel[1] = brigth(self[i, j][1] + nilai_kecerahan)
            pixel[2] = brigth(self[i, j][2] + nilai_kecerahan)
            self[i, j] = pixel
    return self
gambar = cv2.imread("gambar.jpg",1)
cv2.imshow("Dicerahkan", atur_bright(gambar, 255))
cv2.waitKey(0)
cv2.destroyAllWindows()