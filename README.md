# 机器人视觉教程：

## 一、简介：
实验环境为Ubuntu20.04，基于python视觉项目

## 二、opencv-python基础
opencv-python视觉库的基础操作，及数字图像处理的实现。
### 1 图像的基本操作
标题|简介
---|---
[图像基础概述](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E5%9B%BE%E5%83%8F%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C/1.%E5%9B%BE%E5%83%8F%E5%9F%BA%E7%A1%80%E6%A6%82%E8%BF%B0.ipynb)|了解数字图像的组成。
[GUI操作](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E5%9B%BE%E5%83%8F%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C/2.GUI%E6%93%8D%E4%BD%9C.ipynb)|学习opencv的GUI操作，通过窗口显示图像、绘制图形、监听输入事件。
[图像的属性](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E5%9B%BE%E5%83%8F%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C/3.%E5%9B%BE%E5%83%8F%E7%9A%84%E5%B1%9E%E6%80%A7.ipynb)|了解图像的属性，使用OpenCV访问属性，并操作图像通道。
[图像运算](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E5%9B%BE%E5%83%8F%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C/4.%E5%9B%BE%E5%83%8F%E8%BF%90%E7%AE%97.ipynb)|了解图像是如何运算的，利用图像运算实现对图像的裁剪、融合等操作。
[图像直方图](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E5%9B%BE%E5%83%8F%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C/5.%E5%9B%BE%E5%83%8F%E7%9B%B4%E6%96%B9%E5%9B%BE.ipynb)|了解直方图的原理，并根据直方图优化图像。
[伽马变换](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E5%9B%BE%E5%83%8F%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C/7.%E5%9B%BE%E5%83%8F%E9%98%88%E5%80%BC%E5%A4%84%E7%90%86.ipynb)|学习伽马变换的原理，分析不同$γ$值对图像的影响
[图像阈值处理](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E5%9B%BE%E5%83%8F%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C/7.%E5%9B%BE%E5%83%8F%E9%98%88%E5%80%BC%E5%A4%84%E7%90%86.ipynb)|了解图像阈值处理的方法，包括全局阈值、自适应阈值、Otsu阈值法

### 2 图像的几何变换
标题|简介
---|---
[图像的几何变换](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E5%9B%BE%E5%83%8F%E7%9A%84%E5%87%A0%E4%BD%95%E5%8F%98%E6%8D%A2/%E5%9B%BE%E5%83%8F%E7%9A%84%E5%87%A0%E4%BD%95%E5%8F%98%E6%8D%A2.ipynb)|了解图像变换的方法和意义

### 3 图像滤波与增强
标题|简介
---|---
[图像平滑](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E5%9B%BE%E5%83%8F%E6%BB%A4%E6%B3%A2%E4%B8%8E%E5%A2%9E%E5%BC%BA/1.%E5%9B%BE%E5%83%8F%E5%B9%B3%E6%BB%91.ipynb)|了解图像平滑的意义，使用OpenCV对图像模糊处理和降低噪声。
[图像锐化](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E5%9B%BE%E5%83%8F%E6%BB%A4%E6%B3%A2%E4%B8%8E%E5%A2%9E%E5%BC%BA/2.%E5%9B%BE%E5%83%8F%E9%94%90%E5%8C%96.ipynb)|了解什么是图像锐化，它与图像平滑的相比的区别是什么。

### 4 图像形态学处理
标题|简介
---|---
[图像形态学处理](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E5%9B%BE%E5%83%8F%E5%BD%A2%E6%80%81%E5%AD%A6%E5%A4%84%E7%90%86/%E5%9B%BE%E5%83%8F%E5%BD%A2%E6%80%81%E5%AD%A6%E5%A4%84%E7%90%86.ipynb)|了解什么是图像形态学，通过对轮廓的形态学处理，了解形态学的意义及应用。
### 5 图像特征
标题|简介
---|---
[角点检测](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E5%9B%BE%E5%83%8F%E7%89%B9%E5%BE%81/%E8%A7%92%E7%82%B9%E6%A3%80%E6%B5%8B.ipynb)|角点特征检测方法
[边缘检测](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E5%9B%BE%E5%83%8F%E7%89%B9%E5%BE%81/%E8%BE%B9%E7%BC%98%E6%A3%80%E6%B5%8B.ipynb)|边缘特征检测方法
[轮廓特征](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E5%9B%BE%E5%83%8F%E7%89%B9%E5%BE%81/%E8%BD%AE%E5%BB%93%E7%89%B9%E5%BE%81.ipynb)|轮廓特征检测方法，及轮廓的属性和性质。及轮廓检测的应用。

### 6 相机标定和3D重建
标题|简介
---|---
[相机标定](https://gitee.com/lyhcyt_admin/visual_development/blob/master/Opencv-python_Tutorials/%E7%9B%B8%E6%9C%BA%E6%A0%87%E5%AE%9A%E5%92%8C3D%E9%87%8D%E5%BB%BA/%E7%9B%B8%E6%9C%BA%E6%A0%87%E5%AE%9A.ipynb)|了解相机标定的原因，及标定的原理，并对相机进行标定、畸变校正。

## 目标检测与识别

### 1 基于OpenCV的目标检测与识别
标题|简介
---|---
[轮廓检测与识别](https://gitee.com/lyhcyt_admin/visual_development/blob/master/object_detection/tutoriol/%E8%BD%AE%E5%BB%93%E6%A3%80%E6%B5%8B%E4%B8%8E%E8%AF%86%E5%88%AB.ipynb)|字母标识的检测和识别项目，基于轮廓和轮廓矩实现



### 2 基于yolov5的目标检测
标题|简介
---|---
[yolov5环境配置](https://gitee.com/lyhcyt_admin/visual_development/blob/master/object_detection/tutoriol/yolo%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE.md)|配置pytorch环境，及yolov5项目的拉取
[yolov5自训练模型](https://gitee.com/lyhcyt_admin/visual_development/blob/master/object_detection/tutoriol/yolov5%E8%87%AA%E8%AE%AD%E7%BB%83%E6%A8%A1%E5%9E%8B.ipynb)|将学习如何创建自己的数据集，然后训练自己的目标检测模型