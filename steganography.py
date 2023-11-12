from PIL import Image, ImageDraw
from pathlib import Path

def decode_image(path_to_image):
    """
    Takes in an encoded image and returns a decoded image using the LSB of each of the encoded image's pixels
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_image)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    x_size, y_size = encoded_image.size

    for x in range(x_size):
        for y in range(y_size):
            p = red_channel.getpixel((x, y))
            if p & 1: #funny bitwise operator
                decoded_image.putpixel((x, y), (255, 255, 255))

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save(f"images/decoded/{Path(path_to_image).stem}.png")

def encode_image(path_to_image, text_to_write):
    """
    Takes in a regular, non-encoded, image and encodes text within it by modifying the LSB of each pixel.
    """
    unencoded_image = Image.open(path_to_image).convert('RGB')
    red, green, blue = unencoded_image.split()
    x_size, y_size = unencoded_image.size
    txt = write_text(text_to_write, (x_size, y_size))
    for x in range(x_size):
        for y in range(y_size):
            #print(txt.getpixel((x,y)))
            if txt.getpixel((x,y)) != 0: #if pixel in text image is text
                p = red.getpixel((x, y))
                b = format(p, "b")[:-1] + "1"
                d = int(b,2)
                red.putpixel((x, y), d)
            elif red.getpixel((x,y)) & 1: #incase there is white already in the base image
                p = red.getpixel((x, y))
                b = format(p, "b")[:-1] + "0"
                d = int(b,2)
                red.putpixel((x, y), d)

    encoded_image = Image.merge(mode='RGB', bands=(red, green, blue))   
    encoded_image.save(f"images/encoded/{Path(path_to_image).stem}.png") 

def write_text(text_to_write, size):
    """
    Creates a white on black text image to be used for encoding
    """
    im = Image.new('L', size)
    txt = ImageDraw.Draw(im)
    txt.fontmode = "1"
    txt.text((0, 0), text_to_write, fill=(11111111))
    return im

def display_image(path_to_image):
    image = Image.open(path_to_image).convert('RGB')
    image.show()