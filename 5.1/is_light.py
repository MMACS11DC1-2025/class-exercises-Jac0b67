from PIL import Image

def is_light(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    avg = int((r + g + b) / 3)

    return avg >= 120
# white_pixel = (255, 255, 255)
print(is_light((255, 255, 255)))
print(is_light((0, 0, 0)))
# print(is_light(white_pixel))

def binarize(input_filename, output_prefix):
    output_filename = output_prefix + "output.png"
    my_image = Image.open("5.1/kid-green.jpg").load()
    output_image = Image.open("5.1/kid-green.jpg")

    img_width = output_image.width
    img_height = output_image.height

    for i in range(img_width):
        for j in range(img_height):
            pixel = my_image[i, j]
            if is_light(pixel):
                output_image.putpixel((i, j), (255, 255, 255))
            else: 
                output_image.putpixel((i, j), (0, 0, 0))
    output_image.save("5.1/light_output.png", 'png')
binarize("kid-green.jpg", "kid2")