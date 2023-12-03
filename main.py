from PIL import Image
import numpy as np

image_array = np.array(Image.open("image/lena_color_512.tif"))

print(image_array.shape)

print (image_array [200:210,:].shape)
image_array[0:20,0:20] = 0
image_array[0:20, -20:-1] = 0
image_array[-20:-1, 0:20] = 0
image_array[-20:-1, -20:-1] = 0

im_pill = Image.fromarray(image_array)
im_pill.save("image/imgModificada.tif") 