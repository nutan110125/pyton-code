import csv
import random
import math
import operator

#ob=open("C:\Python\Python36-32\iris.txt","r")#simple file open
#lines=csv.reader(ob)#csv mean common separated value
#dataset=list(lines)
#print(dataset)
#Step1. split the data into training dataset and test the dataset 
'''
with open('C:\Python\Python36-32\iris.txt','r') as ifile:
    lines=csv.reader(ifile)#csv is used to display data in comma seprated module
    dataset=list(lines)
    print(dataset)
    print('-'*10)
'''
'''# this is without csv 
   fn="C:\Python\Python36-32\iris.txt"
   mainlist=[]
   for i in open(fn,'r'):
       str1=i
       lst=list(str1.split(','))
       mainlist.append(lst)

       print(mainlist)
'''

'''# converting list into float value
11=['2.3','3.5','34.6','python']
def fun1(lst):
    maxlen=len(lst)-1
    i=0
    whlie i<maxlen:
          lst[i]=float(lst[i])
          i +=1
    return lst

    12=fun1(11)
    print(12)
'''

def loadDataset(filename,split,trainingSet=[],testSet=[]):#ratio 67,33
    with open(filename) as ifile:
        lines=csv.reader(ifile)#csv is used to display data in comma seprated module
        dataset=list(lines)
        print(dataset)
for x in range(len(dataset)-1):
    for y in range(4):
        dataset[x][y]=float(data[x][y])
    if random.random()<split:
        trainingSet.append(dataset[x])
    else:
        testSet.append(dataset[x])
trnglst=[]
testlst=[]
fn="C:\Python\Python36-32\iris.txt"
divide=0.70
loadDataset(fn,divide,trnglst,testlst)
print("traing list:\n",trnglst)
print("-"*20)
print("test list:\n",testlst) 

