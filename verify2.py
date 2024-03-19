import numpy as np
import json
import matplotlib.pyplot as plt

# Load the sky coordinates from the JSON file
with open('sky_coordinates.json', 'r') as f:
    sky_coordinates = json.load(f)

# Create an empty image array
image = np.zeros((160, 160, 3), dtype=np.uint8)

# Set pixels corresponding to sky coordinates as red (255, 0, 0)
for coord in sky_coordinates:
    image[coord[0], coord[1]] = [255, 0, 0]

# Set all other pixels as blue (0, 0, 255)
image[np.where((image == [0, 0, 0]).all(axis=2))] = [0, 0, 255]

# Display the image
plt.imshow(image)
plt.title('Sky Verification')
plt.axis('off')
plt.show()
