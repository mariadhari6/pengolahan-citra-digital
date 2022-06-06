import cv2 as cv
gambar = cv.imread("gambar.jpg", 1)
def citra_rotasi(citra, derajat):
    tinggi = citra.shape[0]
    lebar = citra.shape[1]
    titik_tengah = (lebar/2, tinggi/2)
    skala = 1.0
    rotasiMatrix = cv.getRotationMatrix2D(titik_tengah, derajat, skala)
    citra = cv.warpAffine(citra, rotasiMatrix, (tinggi, lebar))
    return citra
gambar = citra_rotasi(gambar, 180)
cv.imshow("Gambar", gambar)
cv.waitKey(0)
cv.destroyAllWindows()    