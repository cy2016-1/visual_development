import os
import random
images = os.listdir('./images')  # 打开目录
rate = 0.8  # 训练集的比例
train = open('train.txt', 'w')  # 打开文件
val = open('val.txt', 'w')
i = 0
random.shuffle(images)  # 将图像列表打乱，提高数据的随机性
for img in images:
    if i < len(images)*rate:
        train.write('./images/' + img+'\n')  # 写入文件
    else:
        val.write('./images/' + img+'\n')
    i += 1
