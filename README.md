# Steganography with Python Pillow

🖼️🖊️ Python microservice for text encryption and decryption within images

## Usage

### `example.py`

`example.py` gives example usage of the image encryption, decription, and display methods from steganography.py. Please feel free to replace the sample text and paths with your own images and text.

If you plan on using this program seriously I recommend automating the processes available in steganography.py to encrypt/decrypt content.

### Importing Elsewhere

You can import the tools used for this project by getting "github.com/sammygrey/dh-key.go/steganography.py" and adding it to the imports of your project.

### Features:

#### What is LSB?

LSB, short for least-significant-bit is a term that refers to the last bit in a piece of data. In this case, it is referring to the last binary digit of a pixel from an image. For images, these bits are unimportant and changing them will not change the image in question. Because of this we can change the LSBs turning them on or off, to hide extra information within images. Below are more in-depth explanations on how LSBs are used in this function to encode and decode text within an image.

#### Image Text Encoding Using LSB

Using `encode_image` you can encode text within images. This function takes in two parameters: `path_to_image` and `text_to_write`. Encoding is done by splitting images into their respective RGB bands, creating an image of the same size with only text, and then editing the pixels in the base image where the text is present, adding a new least significant bit of each pixel to 1 if text is present. True to name, this pixel is insignificant and will not affect how the image looks, but can be used to hide messages within an image. In the case that a least significant bit of 1 is already present where there is no text, a new least significant bit of 0 is added.

Example image:

![example unencoded image](https://user-images.githubusercontent.com/49354894/282283130-46aa9f9f-2360-4441-b1c3-ae01acd16689.png)

Example image after encryption:

![example encoded image](https://user-images.githubusercontent.com/49354894/282283132-2f4a46bf-1169-4c45-8637-e2cb914ed103.png)

#### Image Text Decoding Using LSB

Using `decode_image` the text within images can be similarly decoded by reverse engineering the above method. This function only takes in one parameter: `path_to_image`. Text from images is decoded by checking if each pixel has its least significant bit set to 1 or 0. Pixels that have a LSB of 1 are set as being white (256,256,256) and pixels with an LSB of 0 are set to black (0,0,0). This displays the text clearly without any clutter that may be in the original image

Example encrypted image:

![example encoded image](https://user-images.githubusercontent.com/49354894/282283132-2f4a46bf-1169-4c45-8637-e2cb914ed103.png)

Example image after decryption:

![example decoded text](https://user-images.githubusercontent.com/49354894/282283140-d7899e38-1449-456c-9f0d-16cddd6d42da.png)

#### Displaying Images

Images can be displayed via using the `display_image` function which takes in the path of an image as a parameter. This can be done just as easily using the `show` method from Pillow, but I decided not to import Pillow into the example program. 


