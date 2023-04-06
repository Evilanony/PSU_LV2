import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("C:/Users/student/Documents/tiger.png")
svjetlina = img*0.5
img = img[:,:,0].copy()

(h,w)=img.shape
img_rot = np.zeros((w,h))
for i in range(0,h):
    img_rot[:,h-1-i]=img[i,:]


img_flip = np.zeros((h,w))
for i in range(0,h):
    img_flip[h-1-i,:]=img[i,:]

img_flip2 = np.zeros((h,w))
for i in range(0,w):
    img_flip2[:,w-1-i,]=img[:,i]


img_zoom = img[::10,::10] 


img_cut = np.zeros((h,w))
img_cut[:,240:480] = img[:,240:480]


plt.imshow(img_cut, cmap="gray")
plt.show()