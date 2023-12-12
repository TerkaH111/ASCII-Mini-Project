from PIL import Image, ImageFont, ImageDraw

# Image upload
image_path = "photos/dog.jpg"
img = Image.open(image_path)

# Size of ASCII image
width, height = img.size
aspect_ratio = height / width
new_width = 600
new_height = 600
# new_height = int(aspect_ratio * new_width * 0.75)
img = img.resize((new_width, new_height))

# List of ASCII chars
ascii_chars = "@%#*+=-:.^~[]`Zabcdefghijklmnopqrstuvwxyz0123456789"


font_size = 10
font = ImageFont.truetype("arial.ttf", font_size)

# Creating a drawing object
draw = ImageDraw.Draw(img)

# Conversion of the image to ASCII
ascii_image = ""
for i in range(0, new_height, font_size):
    for j in range(0, new_width, font_size):
        pixel_value = img.getpixel((j, i))[0]
        ascii_char = ascii_chars[min(max(pixel_value // (256 // len(ascii_chars)), 0), len(ascii_chars) - 1)]
        draw.text((j, i), ascii_char, font=font)
    ascii_image += "\n"


# Saving the output (JPEG)
output_image_path = "output_ascii.jpg"
img.convert("RGB").save(output_image_path)

