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

c=ndimage.gaussian_filter(a,sigma=2)
plt.imshow(c)
plt.title("blurred Image")

d=ndimage.zoom(a,(.5,.2,1))
plt.imshow(d)
plt.title("zoom Image")


# d=(img.size[0] // 2,img.size[1] // 2)
# c=img.resize(d)
# plt.title("zoom Image")
# plt.imshow(c)
