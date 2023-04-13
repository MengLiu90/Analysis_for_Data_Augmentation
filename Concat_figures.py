#Author: Gopal Srivastava
#Date: April, 13 2023 

from PIL import Image, ImageDraw
image1 = Image.open("Figure/Fig1.png")
image2 = Image.open("Figure/Legend.png")

# Get the width and height of the images
width1, height1 = image1.size
width2, height2 = image2.size

# Create a new image with the width of the larger image and the height of both images combined
new_width = max(width1, width2)
new_height = height1 + height2
new_image = Image.new('RGBA', (new_width, new_height), (255, 255, 255, 255))

# Paste the two images into the new image
new_image.paste(image1, (0, 0))
new_image.paste(image2, (0, height1))

# Draw a line to fill in the blank space between the two images
draw = ImageDraw.Draw(new_image)
draw.line((0, height1, new_width, height1), fill=(255, 255, 255, 255), width=1)

# Save the new image
new_image.save('Figure/Figure1.png')
