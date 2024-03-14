import numpy as np
import cv2
import json

# Load sky coordinates from the JSON file
with open('sky_coordinates.json', 'r') as json_file:
    sky_coordinates = json.load(json_file)

# Assuming the image size is 640x640, you may adjust this based on your actual image size
image_size = (640, 640)

# Create a blank image with blue color
image = np.zeros((image_size[0], image_size[1], 3), dtype=np.uint8)
image[:, :] = [255, 0, 0]  # Set all pixels to blue

# Convert sky coordinates to integer values
sky_coordinates = [[int(coord[0]), int(coord[1])] for coord in sky_coordinates]

# Mark sky segments as red in the image
for coord in sky_coordinates:
    image[coord[0], coord[1]] = [0, 0, 255]  # Set pixel to red

# Display the image
cv2.imshow('Sky Segments', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
