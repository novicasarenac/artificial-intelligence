from sklearn.datasets import fetch_mldata
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential,load_model
from keras.layers.core import Activation, Dense
from keras.optimizers import SGD
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.measure import label, regionprops
from skimage.morphology import erosion,disk,opening,square,dilation,closing,diamond

model = load_model('nn15000test4.h5')
f = open("out.txt", "w")
f.write("E2 58/2013 Novica Sarenac")
f.write("\nfile\tsum")
for counter in range(0,100):
    img = imread("images/img-"+str(counter)+".png")
    #convert to grayscale
    img_gray = rgb2gray(img)
    img_bin = img_gray > 0
    str_elem = square(3)
    str_elem_d = square(15)
    im_er = erosion(img_bin, selem=str_elem)
    im_d = dilation(im_er, selem=str_elem_d)

    labelled_img = label(im_d)
    regions = regionprops(labelled_img)

    digitSum = 0
    for region in regions:
        center = region.centroid
        row = center[0]
        col = center[1]
        rezUkupno = np.zeros(10)
        for j in range(-2,2):
           for k in range(-2,2):
                frame = img_gray[row+j-14:row+j+14, col+k-14:col+k+14]
                rez = model.predict(np.array([frame.flatten()]), verbose=0)
                for i in range(0,10):
                    rezUkupno[i] = rezUkupno[i] + rez[0,i]
        max = np.argmax(rezUkupno)
        digitSum = digitSum + max

    print digitSum
    f.write("\nimages/img-"+str(counter)+".png\t%.1f" % digitSum)
plt.show()