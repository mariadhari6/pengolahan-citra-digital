import cv2
def brigth(intensitas):
    if intensitas < 0:
        return 0
    elif intensitas > 255:
        return 255
    else:
        return intensitas
def atur_bright(citra, nilai_kecerahan):
    height, width, channels = citra.shape
    for i in range(0, height - 1):
        for j in range(0, width - 1):
            pixel = citra[i, j]
            pixel[0] = brigth(citra[i, j][0] + nilai_kecerahan)
            pixel[1] = brigth(citra[i, j][1] + nilai_kecerahan)
            pixel[2] = brigth(citra[i, j][2] + nilai_kecerahan)
            citra[i, j] = pixel
    return citra
gambar = cv2.imread("gambar.jpg",1)
cv2.imshow("Atur Kecerahan", atur_bright(gambar, 255))
cv2.waitKey(0)
cv2.destroyAllWindows()