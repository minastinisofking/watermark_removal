from PIL import Image
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # mpimg 用于读取图片
import cv2

# img = Image.open("000000.jpg")
# print(img)
# print(type(img))
# img = np.array(img)
# print(img)
# print(type(img))
# Image.fromarray(np.uint8(img))
# print(img)
# print(type(img))
# img = transforms.ToTensor()(img)
# print(img)
# print(type(img))

# load
img = mpimg.imread('000000.jpg')
print(img)
print(type(img))
# 此时 img 就已经是一个 np.array 了，可以对它进行任意处理
# height, width, channel=(360, 480, 3)
h, w, c = img.shape

# show
plt.imshow(img) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()

# save
# 适用于保存任何 matplotlib 画出的图像，相当于一个 screencapture
img = plt.savefig('fig_dog.png')
img = mpimg.imread('fig_dog.png')
print(img)
print(type(img))
img = cv2.imread('fig_dog.png')
print(img)
print(type(img))