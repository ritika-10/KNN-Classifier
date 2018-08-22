# -*- coding: utf-8 -*-
"""
Created on Mon Jun 04 14:40:48 2018

@author: shivam mittal
"""

"""read from file training.csv"""
import pandas as pd
import math
train = pd.read_csv('F:/Projects/recognition of flower/trainingdata.csv')
test = pd.read_csv('F:/Projects/recognition of flower/testdata.csv')


"""replace labels with unique values"""
def changeLabel():  
    print('change label')
    differentSpecies = []
    differentSpecies = train.Species.unique().tolist()
    print(type(differentSpecies))
    for i in differentSpecies:
        for index1,row in train.iterrows():
            print('s')
            train.loc[train.Species == i, 'Species'] = differentSpecies.index(i)
            
    
    for i in differentSpecies:
        for index1,row in test.iterrows():
            test.loc[test.Species == i , 'Species'] = differentSpecies.index(i)
    
    print('end change label')
                
#train.loc[train.Species=='Iris-setosa','Species'] = 1
#train.loc[train.Species == 'Iris-versicolor','Species'] = 2
#train.loc[train.Species == 'Iris-virginica','Species'] = 3

    
#test.loc[test.Species=='Iris-setosa','Species'] = 1
#test.loc[test.Species == 'Iris-versicolor','Species'] = 2
#test.loc[test.Species == 'Iris-virginica','Species'] = 3

#print(train.loc[:,:])

def checkaccuracy(k):
    #rows = train.shape[0]
    print('check accuracy')
    columns = train.shape[1]
    
    columnsList = []
    columnsList = train.columns.values.tolist()
    
    """find distance from an instace of testdata with each instance of training data"""
    correct = 0
    for index1,row1 in test.iterrows():
        for i in range(0,columns):
            print(row1[columnsList[i]])
            print('-->')
            
        distance = {}
        for index2,row2 in train.iterrows():
        
            #print(row1['SepalLengthCm'],row2['SepalLengthCm'])
            
            """calculate sum of squares of distances"""
            sumofsquares = 0
            for j in range(0,columns):
                sumofsquares = sumofsquares + pow((row1[columnsList[j]]-row2[columnsList[j]]),2)
            dist = math.sqrt(sumofsquares)
            distance[dist] = row2[columnsList[columns-1]]
            
            #print(distance.keys()[0])
    
        """sort the dictionary and pick up first k values and find the maximum count of labels"""
        keylist = sorted(distance.iterkeys())
    
        differentLabels = []
        differentLabels = train['Species'].unique()
        count = [0] *differentLabels
        c = 0
        for i in keylist:
            label = distance[i]
            #   print(i,distance[i])
            if label in differentLabels:
                count[label] = count[label] + 1
        #elif label == 2:
         #   count2 += 1
        #elif label == 3:
         #   count3 += 1
                c += 1
                if c == k:
                    break
    #print(count1,count2,count3)
        maxofall = max(count)
    #print(maxofall)
    #print(row1['Species'])
    #print(maxofall)
    
        for i in range(0,len(differentLabels)):
            if maxofall == count[i] and row1['Species']== differentLabels[i]:
                correct += 1
            #elif maxofall == count2 and row1['Species'] == 2.0:
             #   correct +=1
              #  elif maxofall == count3 and row1['Species'] == 3.0:
               #     correct +=1
    #print(correct)
        
    accuracy = float((correct*100)/30)
    print(accuracy)

def main():
    
    """change the labels """
    changeLabel()
    
    """Enter value of k"""
    k =input('enter value of k')
    checkaccuracy(k)    
    
if __name__ == "__main__":
    main()