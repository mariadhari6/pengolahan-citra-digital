import cv2 as cv
gambar = cv.imread("gambar.jpg", 1)
# print(gambar.shape)
def citra_binner(citra, nilai_ambang):
    height, width, channels= citra.shape #dapatkan nilai tinggi & lebar
    citra = cv.cvtColor(citra, cv.COLOR_BGR2GRAY) #konversi menjadi gray terlebih dahulu
    for i in range(height):
        for j in range(width):
            if citra[i, j] < nilai_ambang: #pengecekan nilai hitam / putih (0 - 255)
                citra[i, j] = 0
            else:
                citra[i, j] = 255
    return citra    
cv.imshow("Gambar Binner", citra_binner(gambar, 100))
cv.waitKey(0)
cv.destroyAllWIndows()