import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters.rank import otsu
from skimage.filters import threshold_adaptive
from skimage.morphology import opening, erosion
from skimage.morphology import square, disk
from skimage.measure import label
from skimage.measure import regionprops

def drawRegions(regs, img_size):
    img_r = np.ndarray((img_size[0], img_size[1]), dtype='float32')
    for reg in regs:
        coords = reg.coords
        for coord in coords:
            img_r[coord[0], coord[1]] = 1.
    return img_r

f = open("out.txt", "w")
f.write("E2 58/2013 Novica Sarenac")
f.write("\nfile circles")
for i in range(0,100):
    img1 = imread('images\img-'+str(i)+'.png')

    str_elem = disk(5)
    red_img = img1[:, :, 0]
    bin_img = red_img > 80
    img_erosion = erosion(bin_img,selem=str_elem)

    labelled_img = label(img_erosion)
    regions = regionprops(labelled_img)
    #plt.imshow(drawRegions(regions, img_erosion.shape), 'gray')

    #regioni
    regions_img = []
    for region in regions:
        bbox = region.bbox
        h = bbox[2] - bbox[0]
        w = bbox[3] - bbox[1]
        if ((float(h) / w > 0.7) and (float(h) / w <= 1.0)) or ((float(w) / h > 0.7) and (float(w) / h <= 1.0)):
            regions_img.append(region)

   # obj["images\img-"+str(i)+'.png'] = len(regions_img)
    f.write("\nimages/img-"+str(i)+'.png\t'+str(len(regions_img)))
    print(len(regions_img))


plt.show()
