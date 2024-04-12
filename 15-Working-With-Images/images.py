# documentation:: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#using-the-image-class

from PIL import Image
im = Image.open("example.jpeg")
print(type(im))
print(im.format, im.size, im.mode)
# im.show()


# ? cropping
x = 0
y = 0
w = 800/6
h = 450/20

im.crop((x, y, w, h))
im.show()


# ? color transparency

red = Image.open('s5.jpg')
red.putalpha(128)
red.show()
