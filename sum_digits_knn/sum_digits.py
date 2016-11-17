from sklearn.datasets import fetch_mldata
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from skimage.color import rgb2gray
from skimage.io import imread
from skimage.measure import label, regionprops

#funkcija za izracunavanje zbira sa jedne slike
def makeSum(regions_img, img_gray):
    sum = 0
    #nalazenje slika pojedinacnih iz velike slike
    for region in regions_img:
        x = region.bbox[0]
        y = region.bbox[1]
        temp_img = np.zeros((28,28), np.float)
        temp_img[0:28, 0:28] = img_gray[x:x+28, y:y+28]*255
        #konkretan broj sa slike
        k = nNeighbours.predict(temp_img.astype('uint8').flatten().reshape(1, -1))

        sum = sum + k
    return sum


#ucenje mnist
mnist = fetch_mldata('MNIST original')
nNeighbours = KNeighborsClassifier(n_neighbors=1)
nNeighbours.fit(mnist.data, mnist.target)
f = open("out.txt", "w")
f.write("E2 58/2013 Novica Sarenac")
f.write("\nfile\tsum")

for i in range(0,100):
    img = imread('images\img-'+str(i)+'.png')
    img_gray = rgb2gray(img)
    img_bin = img_gray > 0

    labelled_img = label(1-img_bin)
    regions = regionprops(labelled_img)
    #regioni
    regions_img = []
    for region in regions:
        bbox = region.bbox;
        h = bbox[2] - bbox[0]
        w = bbox[3] - bbox[1]
        if(h==28):
            regions_img.append(region)

    sum_img = 0
    sum_img = makeSum(regions_img, img_gray)
    f.write("\nimages/img-"+str(i)+".png\t%.1f" % sum_img)

    print sum_img