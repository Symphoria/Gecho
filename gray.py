from PIL import Image
import glob
from skimage.color import rgb2gray
from skimage.io import imread, imsave
from skimage.filters import threshold_otsu
from skimage import img_as_uint

for filename in glob.glob("./tf_files/sign_photos/Music/*.jpg"):
    img = Image.open(filename).convert('LA')
    print filename
    print './greyscale/' + filename.split('/')[-2::][1].split('.')[0] + '.png'
    img.save('./greyscale/Music/' + filename.split('/')[-2::][1].split('.')[0] + '.png')
