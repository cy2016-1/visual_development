import random
import glob

class1 = glob.glob("./images/logo*.jpg")
class2 = glob.glob("./images/oryx_blue*.jpg")
class3 = glob.glob("./images/red*.jpg")

# 打开分集文件
train = open('train.txt', 'w')
val = open('val.txt', 'w')

def spilt_data(data,rate):
    i = 0
    random.shuffle(data)  # 将图像列表打乱，提高数据的随机性
    for img in data:
        if i < len(data)*rate:
            train.write(img+'\n')  # 写入文件
        else:
            val.write(img+'\n')
        i += 1

spilt_data(class1,0.8)
spilt_data(class2,0.8)
spilt_data(class3,0.8)
