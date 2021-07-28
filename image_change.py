import numpy as np
from PIL import Image
path = '/Users/admin/projects/image/1.jpg'
def image_to_bw(path_to_image):
    path_to_save = '/Users/admin/projects/result_image/'
    image_name = path_to_image.split('/')[-1]
    print(image_name)
    img = Image.open('/Users/admin/projects/image/1.jpg')
    arr = np.asarray(img, dtype='uint8')
    x, y, _ = arr.shape

    k = np.array([[[0.2989, 0.587, 0.114]]])
    arr2 = np.round(np.sum(arr*k, axis=2)).astype(np.uint8).reshape((x, y))
    
    img2 = Image.fromarray(arr2)
    img2.save(path_to_save+image_name)

image_to_bw(path)