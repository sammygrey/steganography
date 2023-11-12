from steganography import encode_image, decode_image, display_image
from pathlib import Path

image_path = 'images/base/secret.png' #replace with desired image path
text = "It's a secret to everybody." #replace with desired text
display_image(image_path) #display image from path

#encode image with desired text, store path, and display image
encode_image(image_path, text)
encoded_image_path = f"images/encoded/{Path(image_path).stem}.png"
display_image(encoded_image_path)

#decode encoded image, store path, and display hidden text
decode_image(encoded_image_path)
decoded_image_path = f"images/decoded/{Path(image_path).stem}.png"
display_image(decoded_image_path)