import os
import skimage
from skimage.io import imread, imsave
from skimage.transform import rescale

data_dir = 'E:/Ninart/'

if __name__ == '__main__':
    for file in os.listdir(data_dir):

        if '.jpg' in file:
            img = imread(data_dir + file)

            height, width, channels = img.shape

            scale_factor = 512.0 / float(height)
            img = rescale(img, scale_factor)
            print(img.shape)

            imsave(data_dir + 'small/' + file, img)
            