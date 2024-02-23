from PIL import Image
im = Image.open("image.png")
im.show()
print(im.format, im.size, im.mode)

# JPEG (1920, 1357) RGB