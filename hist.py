import seaborn as sns
import skimage.io as io
import matplotlib.pyplot as plt

path = "C:/Users/juanr/Documents/fake_detector/data/*.tif"
ic = io.ImageCollection(path)
imgs = io.concatenate_images(ic)
print(imgs.shape)
plt.hist(imgs.ravel(),256,[0,256],log=True); plt.show()