import os 
import random
import cv2 as cv

dir = "./red_oryx/"
image_name = "oryx_red_"
num = []
light = 100
ddd = 0

train = open('train.txt', 'w')  # 打开文件
val = open('val.txt', 'w')

while(len(num)<80):
    index_num=random.randint(1,100)
    if num.count(index_num) == 0:
        num.append(index_num)

for i in range(100):
    if num.count(i) > 0:
        train.write('./images/' + "logo"+str(i)+'\n')  # 写入文件
        train.write('./images/' + "oryx_red"+str(i)+'\n')  # 写入文件
        train.write('./images/' + "oryx_blue"+str(i)+'\n')  # 写入文件
    else:
        train.write('./images/' + "logo"+str(i)+'\n')  # 写入文件
        train.write('./images/' + "oryx_red"+str(i)+'\n')  # 写入文件
        train.write('./images/' + "oryx_blue"+str(i)+'\n')  # 写入文件
    