#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import os
import numpy as np

def load_images_from_folder(folder):
    images = []
    channels=[]
    channels_rgb=[]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
        channels.append(cv2.mean(img))
    for i in range(len(channels)):
        channels_rgb.append([channels[i][2], channels[i][1], channels[i][0]])
    return channels_rgb


image_list = load_images_from_folder("/Users/Nika/Desktop/Images")
#image_list

label_list=[]
for i in range (len(image_list)):
    if (image_list[i][0] < image_list[i][2]):
        label_list.append('Chelsea')
    else:
        label_list.append('Manchester United')
#print("label_list: ", label_list)


actual_label=[]
for filename in os.listdir("/Users/Nika/Desktop/Images"):
    if (filename[0] == 'c'):
        actual_label.append('Chelsea')
    else:
        actual_label.append('Manchester United')
#print("actual_label: ", actual_label)

TP=FN=FP=TN=0
for i in range (len(image_list)):
    if (label_list[i] == "Chelsea" and actual_label[i] == "Chelsea"):
        TP+=1
    elif(label_list[i] == "Manchester United" and actual_label[i] == "Chelsea"):
        FN+=1
    elif(label_list[i] == "Chelsea" and actual_label[i] == "Manchester United"):
        FP+=1
    else:
        TN+=1


Confusion_Matrix=[[TP,FN],[FP,TN]]
print("Confusion Matrix = ", Confusion_Matrix)
print("accuracy = ", (TP+TN)/(TP+TN+FP+FN))
print("precision = ", TP/(TP+FP))
print("recall = ", TP/(TP+FN))

