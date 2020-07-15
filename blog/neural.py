#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras import Sequential
from tensorflow.keras.optimizers import Adam
from keras.models import load_model
from keras.models import model_from_json

import numpy as np

from .models import Medicine
import random 
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


# In[2]:
answer1 = 0
answer2 = 0
answer3 = 0
answer4 = 0
answer5 = 'none'
def initializing_fe(answer_1,answer_2,answer_3,answer_4,answer_5):
    global answer1,answer2,answer3,answer4,answer5
    answer1 = answer_1
    answer2 = answer_2
    answer3 = answer_3
    answer4 = answer_4
    answer5 = answer_5
    

    #new_medicine = Medicine.objects.order_by('-date').values_list('medicine', flat=True)
    #medicine_class = Medicine.objects.order_by('-date').values_list('medicine_class', flat=True)
    #medicine_class = list(medicine_class)
    #new_medicine = list(new_medicine)

    #Class1 = ['glycomet','glychipage','gluconorm','amryl','glimistar','glim']  #[140  200]
    #for i in range(len(new_medicine)):
     #   if(medicine_class[i] == 'class3'):
      #      Class1.append(new_medicine[i])
    medicine = Neural()
    return medicine

#Medicine classes according to sugar levels




#new_medicine = Medicine.objects.latest('date')


Class1 = ['glycomet','glychipage','gluconorm','amryl','glimistar','glim']  #[140  200]
Class2 = ['K-Glim','Voglimac GM','Vogli GM1','Vogli GM2']                  #[180  300]
Class3 = ['Daonil-m','Bi-euglicon','Glykind-M','SB glic-M','glychomade-gp1','glychomade-gp2','glychomade-gp3']#[200-300]
Class4 = ['acarbose','miglitol']
Metformin = ['metformin-alogliptin','metformin-canagliflozin','metformin-dapagliflozin','metformin-empagliflozin','metformin-glipizide'
'metformin-glyburide','metformin-linagliptin','metformin-pioglitazone','metformin-pioglitazone','metformin-rosiglitazone','metformin-saxagliptin',
'metformin-sitagliptin']
DPP4 = ['alogliptin','alogliptin-metformin','linagliptin','linagliptin-empagliflozin','saxagliptin','saxagliptin-metformin','sitagliptin',
'sitagliptin-metformin']
Meglitinides = ['nategliniderepaglinide','repaglinide','repaglinide-metformin ']
Sulfonylureas = ['glimepiride','glimepiride-pioglitazone','glimepiride-rosiglitazone','gliclazide','glipizide','glipizide-metformin','glyburide','glyburide-metformin']


def predict_medicine(medicine_class):
    if(medicine_class == 1):
        if answer5 in Class1:
            i = Class1.index(answer5)
            return Class1[~i]
        elif answer5 in Class2:
            i = random.randrange(6)
            return Class1[i]
        elif answer5 in Class3:
            i = random.randrange(4)
            return Class1[i]    
    elif(medicine_class == 2):
        if answer5 in Class1:
            i = random.randrange(4)
            return Class2[i]
        elif answer5 in Class2:
            i = Class2.index(answer5)
            return Class2[~i]
        elif answer5 in Class3:
            i = random.randrange(4)
            return Class2[i]
    elif(medicine_class == 3):
        if answer5 in Class1:
            i = random.randrange(7)
            return Class3[i]
        elif answer5 in Class2:
            i = random.randrange(7)
            return Class3[i]
        elif answer5 in Class3:
            i = Class3.index(answer5)
            return Class3[~i]    

    elif(medicine_class == 4):
        return 'Diet Chart'





# In[3]:

def Neural():
    directory = '/home/mohd/Documents/Data'
    data = np.loadtxt(directory+'/data2.csv',delimiter=',',skiprows=1)
    x = data[:,0:5]
    y = data[:,5]
    model = Sequential()
    model.add(Dense(32, input_dim=5, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu')) 
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(4, activation='softmax'))
    model.compile(Adam(lr=0.001),loss="sparse_categorical_crossentropy",metrics=["accuracy"])
    model.fit(x,y,batch_size=80,epochs=80)
   
    if answer5 in Class1:
        medicine_class_previous = 1
    elif answer5 in Class2:
        medicine_class_previous = 2
    elif answer5 in Class3:
        medicine_class_previous = 3
    else:
       medicine_class_previous = 0

    Xnew = np.array([[answer1,answer2,answer3,answer4,medicine_class_previous]])
    ynew = model.predict_classes(Xnew)
   
    if(ynew == 0):
      medicine_class = 4
      return predict_medicine(medicine_class)
    if(ynew == 1):
      medicine_class = 1
      return predict_medicine(medicine_class)
    if(ynew == 2):
      medicine_class = 2
      return predict_medicine(medicine_class)
    if(ynew == 3):
      medicine_class = 3
      return predict_medicine(medicine_class)

#print(Neural())

# In[ ]:




