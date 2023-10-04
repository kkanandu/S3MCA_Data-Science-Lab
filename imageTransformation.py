import numpy as np
from scipy import ndimage
from PIL import Image
import matplotlib.pyplot as plt
img=Image.open('rat.jpg')
plt.imshow(img)
plt.title("Original Image")
plt.show()


a=np.array(img)
b=ndimage.rotate(img,200)
plt.title("Rotated Image")
plt.imshow(b)


