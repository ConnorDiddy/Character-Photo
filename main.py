import cv2

# Initializes txt file
with open("ascii_image.txt", "w") as f:
        f.write('')

# Import and resize photo
img = cv2.imread('assets/mona-lisa.jpg', 0)
img = cv2.resize(img, (100, 100))

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# Loop through each pixel value and replace it with the ASCII character most closely matching the intensity
for row in img:
    str = ''
    for pixel in row:
        index = (pixel // 25)
        str = str + (ASCII_CHARS[index])
    with open("ascii_image.txt", "a") as f: # Writes the row of characters into the next line of the txt file
        f.write('\n'+str)

cv2.waitKey(0)
cv2.destroyAllWindows 