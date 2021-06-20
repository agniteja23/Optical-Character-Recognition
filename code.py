#importing Required libraries
import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
rcParams['figure.figsize'] = 8, 16

#downloading the reader module from easyocr.
reader = easyocr.Reader(['en'])

#loading the image.
Image("Capture.jpg")
#reading the Characters in that image.
output = reader.readtext('Capture.jpg',detail=0,paragraph=True)
print(output)#prints text (output)
output #also prints text

