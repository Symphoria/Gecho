import pygame
import pygame.camera
from PIL import Image
import glob
from skimage.color import rgb2gray
from skimage.io import imread, imsave
from skimage.filters import threshold_otsu
from skimage import img_as_uint

def invoke_webcam():
    pygame.camera.init()
    pygame.camera.list_cameras() #Camera detected or not
    cam = pygame.camera.Camera("/dev/video0",(640,480))
    cam.start()
    img = cam.get_image()
    pygame.image.save(img,"photo.jpg")
    img = Image.open("photo.jpg").convert('LA')
    img.save('./photo.png')
    cam.stop()