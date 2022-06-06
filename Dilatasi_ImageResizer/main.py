import cv2

def resize_gambar(citra, skala):
    height, width, channels = citra.shape
    resize_height = int(height * skala)
    resize_width = int(width * skala)
    image_resize = cv2.resize(citra, (resize_width, resize_height), interpolation=cv2.INTER_LINEAR)
    return image_resize

gambar = cv2.imread("gambar.jpg", 1)
cv2.imshow("Gambar Real", gambar)
cv2.imshow("Resize Gambar", resize_gambar(gambar, 0.5))
cv2.waitKey(0)
cv2.destroyAllWindows()