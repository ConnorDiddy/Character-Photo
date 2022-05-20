import cv2

img = cv2.imread('assets/mona-lisa.jpg', 0)
img = cv2.resize(img, (100, 100))

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
with open("ascii_image.txt", "w") as f:
        f.write('')
for row in img:
    str = ''
    for pixel in row:
        index = (pixel // 25)
        str = str + (ASCII_CHARS[index])
    with open("ascii_image.txt", "a") as f:
        f.write('\n'+str)

cv2.waitKey(0)
cv2.destroyAllWindows 