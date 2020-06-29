# -*- coding: utf-8 -*-
"""
ESA 10 - Instance Based Algs KNN Exercise
@author: Susanne Mitschke
"""
import numpy as np
import pandas as pd
from sklearn import datasets
from collections import Counter

class knn:
    
    def __init__(self, df, target, test_val, k):
        self.df = df
        self.test_val = test_val
        self.min_val = self.df.min()
        self.max_val = self.df.max()
        self.distance_list = []
        self.target = target
        self.k = k
    
    def vote(self,neighbors):
        class_counter = Counter()
        for i in range(len(neighbors)):
            class_counter[neighbors.iloc[i][4]] += 1
        return class_counter.most_common(1)[0][0]
                
    def check_data(self):
        self.normalize_and_cald_distance()
        #Ergänze Distanzen und Klassen zum df
        self.df.insert(4,4,self.target)
        self.df.insert(5,5,self.distance_list)
        #Ermittle k Nachbarn
        neighbors = self.df.sort_values(by=5)[:self.k]
        
        #Prüfe Klasse der Nachbarn und gib Klasse der Testdaten zurück
        return self.vote(neighbors)
        
    def calc_distance(self, row):
        wurzel = 0
    
        for i in range(len(row)):
            wurzel += (row[i]-self.test_val[i])**2
            
        self.distance_list.append(np.sqrt(wurzel))
        
    def normalize_and_cald_distance(self):
        for i in range(len(self.test_val)):
            self.test_val[i] = (self.test_val[i]-self.min_val[i])/(self.max_val[i]-self.min_val[i])
            
        for index, row in self.df.iterrows():
            new_row = []
            for i in range(len(row)):
                new_row.append((row[i]-self.min_val[i])/(self.max_val[i]-self.min_val[i])) 
                self.df[i][index] = new_row[i]
            self.calc_distance(new_row)
            
iris = datasets.load_iris()
iris_data = iris.data
df = pd.DataFrame(iris.data)
test_val= [4.8,2.5,5.3,2.4]

knn = knn(df, iris.target, test_val, 5)

print(knn.check_data())
#Gibt 2.0 zurück. Es handelt sich also um eine Iris Virginica
