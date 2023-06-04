
summary_useful_readme

main2

aggregate_us_stock_performance_v2

minute_data_preparation

extract_futures_from_barchart_tradingview

index_price_individual_strategy_us_stock_pick

dash_example_data_processing_window

app

dash_example

index_price_hsi_minutedata_production

api_morning_mindata_production.main


api_morning_mindata_production_runas_admin.bat

api_morning_mindata_production.bat


run_python_dash.bat



us_stock_factor



monthly_update_us



krow_summary


sql_query.sql




























summary_useful_readme.py

# https://winpython.github.io/
# need to install winpython to C:\\
# place all the file in C:\WinPython-64bit-3.4.4.2\notebooks
# F9 run selection/custom changed to shift+page up
# F5 run all
# place curser in front of a object and press ctrl+I then will get help
# ctrl+1 is comment, ctrl+4 is block comment



import imp
imp.find_module("pandas")  #check module location/path
imp.find_module("code2pdf") 



import pandas
pandas.__version__
pandas.__file__


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
      # Press Ctrl+F8 to toggle the breakpoint.

name='jonathan'
print(f'Hi, {name}')

#if fail to install pip, use below
.\python C:\Users\jonathanjames\Desktop\python\get-pip\get-pip.py
#the upgade with depenency
.\pip install -U ib_insync


len(y_pred)
#check version
import tensorflow as tf
tf.__version__
import numpy as np

y_pred = [0, 2, 1, 3]
np.array(y_pred)#disable chrome update
#https://www.webnots.com/7-ways-to-disable-automatic-chrome-update-in-windows-and-mac/
#cmd, services.msc
#Look for “Google Update (gupdate)” and “Google Update (gupdatem)” on the list.
#choose disable
#restart

import numpy as np
np.__version__

import scipy
scipy.__version__
import cython
cython.__version__

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


a=0.7
x=np.array([1,0.9,a,0.9,1,0.8,a,0.8,1])
x=np.reshape(x,(3,3))

np.all(np.linalg.eigvals(x) >= 0)


import random
import math
inside=0
total=1000
for i in range(0,total):
    x2=random.random()**2
    y2=random.random()**2
    if math.sqrt(x2+y2)<1:
        inside=inside+1
number=(float(inside)/total)*4




#asterisk - unpack a list
shared_items = [1, 2, 3]

items1 = [*shared_items, 4, 5, 6]
items1

#varied argument
def f1(*mm):
    for k in mm:
        print(k)

f1(1,2,3,4)


#double asterisk - unpack dict
science_scores = {"math": 90, "physics": 95, "chemistry": 92}
art_scores = {"english": 93, "spanish": 94}

combined_scores = {**science_scores, **art_scores}
combined_scores


def send_info_to_server(**kwargs):
    print(kwargs)  #is a dict
    for k,v in kwargs.items():
        print(k+'->'+v)
    

send_info_to_server(postId="abc", userId="user") #can pass multiple argument with name














import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

          
b=4

#Multiple variables can be assigned on the same line using commas,
x, y, z = 1, 3.1415, 'a'
x



#To input a floating data type, it is necessary to include a . (period,
#dot) in the expression
x = 1.0
type(x)

x = 2 + 3j
x = complex(1)

#Python contains another type of integer, known as a long
#integer, which has no effective range limitation. Long integers are 
#entered using the syntax x = 1L or by calling long().
x = 1L
x
type(x)
x=long(1)

x='appleisgood'
x[3:10:2]


"""forloop"""
for i in range(10):
    print (i)



def f(x,y):
    return x*x
print(f(3))


def foo(param1, secondparam):
    res=param1+secondparam
    return res

res    
foo(300,500)

print ('%s plus %s is equal to %s' % (3, 2, 5))




#A list is a collection of other objects
#– floats, integers, complex numbers, strings or even other lists.

my_list = []
my_list.append(18) 
my_list.append(22) 
my_list2 = [55.55,"Hi",3,99,222,222]
my_list2[0]=333.333
print(my_list)
print (len(my_list),sum(my_list),my_list2.count(222))

print(my_list2)
print (my_list2[0])
print(my_list2[-1])
print(my_list2[1:3])
print(my_list2[2:5])   #be careful the 5
print(my_list2[2:])

# 2dimensional list (list of lists)
x = [[1,2,3,4], [5,6,7,8]]
x[1]
x[1][2]

# Mixed data types
x = [1,1.0,1+0j,'one',None,True]
x
    
x = [0,1,2,3,4,5,6,7,8,9]
x.append(0)
x
x.extend([11,12,13])
x
x.pop(1)
x
del x[0]
x
del x[1:3]
x










admins = set()    #assign empty set
users = {'Smile', 'Tony','Happy','Sherry','Allen','Andy', 'Mars'}
admins.add('ihc')
admins.add('Mars')

print (admins & users)
print (admins | users)
print (admins ^ users)
print (admins - users )  
print (users - admins )

#字串可用雙引號"或用單引號'來進行標示

# encoding: utf-8

s = "Hello"  
s += 'World'
s1 = "HelloWorld".replace("ll","1")
s2 = "Hello"[0]+"i" 
print (s,s1,s2,len(s))



#其中python字串內建的分割函式string.split()很好用，可以將字串依指定的字元(字串)切割

s3 = "This is a sentence."
s3_split=s3.split(' ')
print (s3_split)









#每個流程的結尾是用冒號:
#屬於該流程底下的執行動作不需要任何括號，而是使用縮排
#縮排可以使用Tab或四格Space，但不可混用，建議是把編輯器設定成Tab對應四格空白

b=range(0,10)
my_list=[]
for i in range(0,10):  #for(i=0;i<10;i++) i=0...to 9
    my_list.append(i+1)
    print(i)
    print(my_list[i])

    
if my_list[0]==1 and len(my_list)<10:
    my_list[0]+=1
    print ("1 state")
elif (10 in my_list) or not(len(my_list)==10):
    print ("2 state")
    print ("range(i,j) is i~j-1")
else:
    print ("3 state")
    print ("none of above")

my_list=['jonathan','apple','anna']
for i in my_list:      #for(i=0;i<my_list.length();i++)
    print (i)          #cout<<my_list[i]


#[自定義函式Function]
def my_function(x,y):
    return x-10,y+10
x,y = my_function(10,20)
print (x,y)


#Class的初始化函式是由兩條底線包含著init做宣告。
class Student:  
    def __init__(self, name, grade, age):  
        self.name = name  
        self.grade = grade  
        self.age = age  

student_objects=[]
student_objects.append( Student('john', 'B', 15) )
student_objects.append( Student('dave', 'A', 12) )
student_objects.append( Student('jane', 'A', 10) )

for i in student_objects:
    print (i.name,i.grade,i.age)


'''[導入外部資源import]
可以用import直接導入整個python檔中所有的函式
或是用from檔案import函式，插入特定的函式'''

import test #插入sys檔案中所有函式，使用sys檔中的write函式前須加檔名
a=test.f(3)
print(a)

from test import f #從time檔案插入time()函式，使用time()前不需要加檔名
a=f(3)
print(a)


import os
print (os.getcwd()) # Prints the working directory


#os.chdir(r'C:\Users\Ava james\Desktop\python\test_new')
#print (os.getcwd())
#import test4
#a=test4.f(3)
#print(a)




#write text file
file = open("newfile.txt", "w")
file.write("hello world in the new file")
file.write("and another line")
file.close()









#read variables from text file
file = open('data.txt')
for line in file:
    name,age = line.strip().split()
    print (name,age)


    
    
f = open( "data.txt" )
lines = f.readlines()
f.close()
for line in lines:
    print (line)





#排序是用程式處理資料中最常用到功能，python提供了很方便的sort函式
#lambda是簡易型函式，只能回傳一個值，因此如果需要兩個值以上的排列順序，會用attrgetter

class Student:  
    def __init__(self, name, grade, age):  
        self.name = name  
        self.grade = grade  
        self.age = age  

student_objects=[]
student_objects.append( Student('john', 'B', 15) )
student_objects.append( Student('dave', 'A', 12) )
student_objects.append( Student('jane', 'A', 10) )

student_objects.sort(key=lambda i: i.grade) 
for i in student_objects:
    print (i.name,i.grade,i.age)


from operator import attrgetter 

student_objects.sort(key=attrgetter('grade', 'age'),reverse=True)  
for i in student_objects:
    print (i.name,i.grade,i.age) 



matrix = [ [0,0,0,1,0],
[0,0,0,0,0],
[0,2,0,0,0],
[0,0,0,0,0],
[0,0,0,3,0] ]
print(matrix)

matrix = [ [1,2,2],
[2,2,1],
[1,2,1],]

np.linalg.det(matrix)
inverse = np.linalg.inv(matrix)
np.linalg.det(inverse)



from sympy import * # we are importing everything for ease of use
x = Symbol("x")
y = Symbol("y")     # create the two variables
equation = Eq(x**3-2*x-5, y) # create the equation
solve(equation, x)





# install pandas is very troublesome, go to https://blogs.msdn.microsoft.com/pythonengineering/2016/04/11/unable-to-find-vcvarsall-bat/
# for download Visual C++ Build Tools 2015
# then go to program\python\python36\scripts, then shift+right click, open command window then
# type pip install pandas

import pandas
data = pandas.read_csv('try.csv', sep=',', na_values=".")
print(data) 




print ('this is an apple'.split())


#它匯入了最常用的 sys 內建模組。如果我們想處理指令行引數，就要靠 sys 模組裡的變數 argv：
import sys
print (sys.argv)













                #### Below is the example from Scripylecture ####
                # http://www.scipy-lectures.org/index.html

                
                
############################
############################
############################
############################
############################
######Start chapter 1#######
############################
############################
############################
############################
############################
                
                
                #1.2. The Python language
            
#1.2.2. Basic types
print?
a=4
type(a) 


test = (3 > 4)
test

#list
l = ['red', 'blue', 'green', 'black', 'white']
l[2:4]
#Note that l[start:stop] contains the elements with indices i such as 
#start<= i < stop (i ranging from start to stop-1)

#slicing
l[3:]
l[:3]
#append
l.append('pink')
l
l.extend(['pink', 'purple'])
l
#concatenate
r = ['red', 'pk']
l+r
#sort
sorted(l)

'''Methods and Object-Oriented Programming
The notation r.method() (e.g. r.append(3) and L.pop()) 
is our first example of object-oriented programming (OOP). Being a list, 
the object r owns the method function that is 
called using the notation. is necessary for going through this tutorial'''
# r is a list, type r. then press tab, we can see all r objects

help(r)

'''The newline character is \n, and the tab character is \t.
 Strings are collections like lists. '''
a = "hello I am happy to see you"
a[0]
a[2:27:2] # Syntax: a[start:stop:step]
a.replace('e', 'x', 2)
help(replace)
a.replace('e', 'x')

#A dictionary is basically an efficient table that maps keys to values. It is an unordered container
d = {'a':1, 'b':2, 3:'hello'}
d.keys()
d.values()

d['a']
d['jonathan']='hand'
d
del d['jonathan']

#Tuples are basically immutable lists. The elements of a tuple are written between parentheses, or just separated by commas:
t = 46855, 54321, 'hello!'
t[0]="e"

x =(0,1,2,3,4,5,6,7,8,9) # remember  () is tuple
type(x)
#It is not possible to add or remove elements forma tuple. However, if a tuple contains
#a mutable data type, for example a tuple that contains a list, 
#the contents mutable data type can change.
x= ([1,2],[3,4])
x[0][1] = 10
x # Contents can change, elements cannot









#Sets: unordered, unique items:
x = set(['MSFT','GOOG','AAP','HPQ','SFT'])


x.add('CSCO')
y = set(['XOM', 'GOOG'])
x.intersection(y)
x = x.union(y)
x
x.remove('XOM')



#As a result, when one variable is assigned to another (e.g. to y = x), these will actually point
#to the same data in the computer’s memory. To verify this, id() can be used to determine the unique
#identification number of a piece of data.5
x=1
y=x
id(x)
id(y)



#id is object memory address
a = [1, 2, 3]
id(a)
print(id(1))




#1.2.3. Control Flow
a = 10
if a == 1:
    print(1)
elif a == 2:
    print(2)
else:
    print('A lot')

for i in range(4):
    print(i)

for word in ('cool', 'powerful', 'readable'):
    print('Python is %s' % word)

z = 1 + 1j
while abs(z) < 100:
    z = z**2 + 1
    print(abs(z),z)

import numbers, math, cmath, decimal
math.sqrt(20)

# break out of enclosing for/while loop:
z = 1 + 1j
while abs(z) < 100:
    if z.imag == 0:
        break
    z = z**2 + 1

#continue the next iteration of a loop, skip beneth code and go to next loop
a = [1, 0, 2, 4]
for element in a:
    if element == 0:
        continue
    print(1/element)
    print('go')

1 is 1
b = [1, 2, 3]
2 in b


vowels = 'aeiouy'

for i in 'powerful':
    if i in vowels:
        print(i)

#Could use while loop with a counter as above. Or a for loop:
words = ('cool', 'powerful', 'readable')



for i in range(0, len(words)):
    print((i, words[i]))
#But, Python provides a built-in function - enumerate - for this:
for index, item in enumerate(words):
    print((index, item))

d = {'a': 1, 'b':1.2, 'c':1j}
>>> for key, val in sorted(d.items()):
        print('Key: %s has value: %s' % (key, val))

this_is_list=[i**2 for i in range(4)]
this_is_list
type(this_is_list)

#1.2.4. Defining functions
def disk_area(radius):
     return 3.14 * radius * radius
disk_area(1.5)

def double_it(x=2):
   return x * 2
double_it()

x = 5
def setx(y):
    x = y
    print('x is %d' % x)

setx(10)
x
    
def setx(y):
    global x
    x = y
    print('x is %d' % x)

setx(10)
x

#1.2.5. Reusing code: scripts and modules

%run test.py

import os
os

import numpy
import numpy as np
np.linspace(0, 10, 6)

from pylab import *
import scipy

from importlib import reload
reload(test)


#How does python find packages?
#https://leemendelowitz.github.io/blog/how-does-python-find-packages.html
#Python imports work by searching the directories listed in sys.path.
import sys
print ('\n'.join(sys.path))
#sys.path is populated using the current working directory, followed
# by directories listed in your PYTHONPATH environment variable, followed
# by installation-dependent default paths, which are controlled by the site module.


# Create a hi module in your home directory.
home_dir = os.path.expanduser("~")
my_module_file = os.path.join(home_dir, "hi.py")
with open(my_module_file, 'w') as f:
  f.write('print ("hi")\n')
  
  f.write('a=10\n')

# Add the home directory to sys.path
sys.path.append(home_dir)

# Now this works, and prints hi!
import hi 
print (hi.a)

#When you import a module, you usually can check 
#the __file__ attribute of the module to see where the module is in your filesystem:

import numpy
numpy.__file__
import selenium
selenium.__file__
#find_module can be used to find a module:

import imp
imp.find_module('numpy')

# Load the hi module using imp
hi = imp.load_source('hi', my_module_file)

# Now this works, and prints hi!
import hi 
print (hi.a) # a is 10!
print (type(hi)) # it's a module!











#The list of directories searched by Python is given by the sys.path variable
import sys
sys.path

#Modules must be located in the search path, therefore you can: 
    #creat new search directory
    
import test2

import sys
new_path = '/WinPython-64bit-3.4.4.2/new_module'
if new_path not in sys.path:
    sys.path.append(new_path)

import test2

#1.2.6. Input and Output

#1.2.7. Standard Library
import os
os.getcwd() #current directory
os.listdir(os.curdir)

#make a directory (directory=file)
os.mkdir('junkdir')
#Rename the directory:
os.rename('junkdir', 'foodir')
os.remove('junk.txt')

a = os.path.abspath('data.txt')
a
os.path.split(a)
os.path.dirname(a)
os.path.basename(a)

os.path.exists('junk.txt')
os.path.isfile('junk.txt')
os.path.isdir('junk.txt')
os.path.join(os.path.expanduser('~'), 'local', 'bin')

#Walking a directory
#os.path.walk generates a list of filenames in a directory tree.
for dirpath, dirnames, filenames in os.walk(os.curdir):
        for fp in filenames:
            print (os.path.abspath(fp))

#Environment variables: see teaching

#Find all files ending in .txt:
import glob
glob.glob('*.txt')


import raw_input

1.2.8. Exception handling in Python see teaching when necessary
https://www.programiz.com/python-programming/exception-handling
while True:
    try:
        x = int(input('Please enter a number: '))
        break
    except ValueError:
        print('That was no valid number. Try again...')

        
#They are not equivalent. Finally code is run no matter what else happens. It is useful for cleanup code that has to run.    
        
try:
    x = int(input('Please enter a number: '))
finally:
    print('Thank you for your input')

    
    
    
    
# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2, 'b',4]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break                          #if put a break here, it will quite for loop until no error happen
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()

print("The reciprocal of",entry,"is",r)
        

        
        
        
#except Exception as e can access the attributes of the exception object:
import sys
def catch():
    try:
        asd()
    except Exception as e:
        print (e.message,'\n', e.args,'\n',e.__doc__,'\n',sys.exc_info())

catch()


import sys
def catch():
    try:
        asd()
    except Exception as e:
        return False


catch()
print("ee")
        



#http://www.runoob.com/python/python-exceptions.html        
触发异常
#我们可以使用raise语句自己触发异常            
# 定义函数
def mye( level ):
    if level < 1:
        raise Exception,"Invalid level!"
        #raise Exception("Invalid level!", level)
        print("not") # 触发异常后，后面的代码就不会再执行
        
try:
    mye(0)            # 触发异常
except Exception,err:
    print 1,err
else:
    print 2        
        
print(3)        
        
        



class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
#在你定义以上类后，你可以触发该异常，如下所示：

try:
    raise Networkerror("Bad hostname")
except Networkerror,e:
    print e.args





#http://c.biancheng.net/view/2360.html        
def main():
    try:
        # 使用try...except来捕捉异常
        # 此时即使程序出现异常，也不会传播给main函数
        mtd(3)
    except Exception as e:
        print('abnormal', e)
    # 不使用try...except捕捉异常，异常会传播出来导致程序中止
    mtd(3)
def mtd(a):
    if a > 0:
        raise ValueError("value >0")
main()    

        
        
        

#1.2.9. Object-oriented programming (OOP)
class Student(object):
    def __init__(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def set_major(self, major):
        self.major = major

anna = Student('anna')
anna.set_age(21)
anna.set_major('physics')

anna.name
anna.age
anna.major




import pandas as pd
x1=pd.DataFrame({'capital':[100,200,200],'signal':[1,0,1]})

class Student(object):
    def __init__(self, x1):
        self.capital = x1.capital
        self.signal = x1.signal
    def trade(self):
        temp = sum(self.capital)
        self.signal=10
        return temp


x=Student(x1)

x.trade()
x.signal





#                1.3. NumPy: creating and manipulating numerical data »
#                    1.3.1. The Numpy array object

import numpy as np
a = np.array([0, 1, 2, 3])
a
type(a)
np.lookfor('create array') 
np.lookfor('find unique')
np.con*?

a = np.array([0, 1, 2, 3])
a.ndim
a.shape
len(a)
b = np.array([[0, 1, 2], [3, 4, 5]])    # 2 x 3 array
b
b[1,2]

c = np.array([[[1,2], [2,3]], [[3,3], [2,4]]])
c
c.shape
type(c)
c.dtype

x = [0.0, 1, 2, 3, 4] # Any float makes all float
y = np.array(x)
y
y * y # Elementbyelement
z = np.asmatrix(x)
z

import numpy as np
x=np.array([1.0,2.0,3.0,4.0,5.0]) #entered as a 1-dimensional array using
np.ndim(x)
x.shape #this is a array with 5 element, not that it is placed horizontally
x[2]



x=np.array([[1.0,2.0,3.0,4.0,5.0]]) #If an array with 2-dimensions is required, it is necessary to use a trivial nested list.
np.ndim(x)
x.shape #1x5
x[0,3]

x=np.matrix([1.0,2.0,3.0,4.0,5.0])#A matrix is always 2-dimensional and so a nested list is not required to initialize a a row matrix
np.ndim(x)
x.shape #1x5
x[0,3]

x=np.matrix([[1.0],[2.0],[3.0],[4.0],[5.0]])
np.ndim(x)
x.shape #5x1
x[2,0]

x = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]])
x
x.shape



#1.3.1.2.2. Functions for creating arrays
a = np.arange(10) # 0 .. n-1  (!)
a
b = np.arange(1, 9, 2) # start, end (exclusive), step
b
a = np.ones((3, 3))  # reminder: (3, 3) is a tuple
a
b = np.zeros((2, 2))
b
c = np.eye(3)
c
d = np.diag(np.array([1, 2, 3, 4]))
d
#random numbers 
a = np.random.rand(4)       # uniform in [0, 1]
a
b = np.random.randn(4)      # Gaussian
b  
np.random.seed(4685)        # Setting the random seed

#You may have noticed that, in some instances, array elements are 
#displayed with a trailing dot (e.g. 2. vs 2). 
#This is due to a difference in the data-type used:
>>>
a = np.array([1, 2, 3])
a.dtype
b = np.array([1., 2., 3.])
b.dtype

c = np.array([1, 2, 3], dtype=float)
d = np.array([1+2j, 3+4j, 5+6*1j])
d.dtype


#Basic visualization
import matplotlib.pyplot as plt  # the tidy way
x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)       # line plot    
plt.plot(x, y, 'o')  # dot plot

#2D plot
image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.hot)    
plt.colorbar()  



#Indexing and slicing
a = np.diag(np.arange(3))
a
a[1, 1]
a[2, 1] = 10 # third line, second column
a
a[2]

a = np.arange(10)
a
a[2:9:1] # [start:end:step]
#All three slice components are not required: by default, 
#start is 0, end is the last and step is 1:
a = np.arange(10)
a
a[1:3]
a[::3] #::s is the same as 0:n:s where n is the length of the array (or list).
a[3:]

x = np.array([1.0,2.0,3.0,4.0,5.0])
y = x[1::2]
y

y = np.array([[0.0, 1, 2, 3, 4],[5, 6, 7, 8, 9]])
y
y[:1,:] # Row 0, all columns
y[:1] # Same as y[:1,:]
y[:,:1] # all rows, column 0
y[:1,0:3] # Row 0, columns 0 to 2
y[0,:]

y = np.reshape(range(25),(5,5))
y
y[0] # Same as y[0,:], first row

y.flat[0] # Scalar slice, flat is 1dimensional
y.flat[13] # Scalar slice, flat is 1dimensional
y.flat[:] # All element slice

>>> x = np.reshape(range(4),(2,2))
>>> s1 = np.copy(x[0,:]) # Function copy
>>> s2 = x[:,0].copy() # Method copy
>>> s3 = np.array(x[0,:]) # Create a new array







#if elif example
#only enter into one condition, if met, then leave the if statement, won't go to next one
x=20
if x>=10:
    y=0
elif x>=30:
    y=10
else:
    y=100
print(y)






is_prime = np.ones((100,), dtype=bool)

#Using boolean masks
np.random.seed(3)
a = np.random.random_integers(0, 20, 15)
a
mask = (a % 3 == 0)
extract_from_a = a[mask] # or,  a[a%3==0]
extract_from_a           # extract a sub-array with the mask

#Indexing with a mask can be very useful to assign a new value to a sub-array:
a[a % 3 == 0] = -1
a

#Indexing with an array of integers
a = np.arange(0, 100, 10)
a
a[[9, 7]] = -100
c
type(a[[9, 7]])

#1.3.2. Numerical operations on arrays
b = np.ones(4)

b = np.ones(4) + 1
a - b
a * b
j = np.arange(5)
2**(j + 1) - j

a = np.arange(10000)
%timeit a + 1  

l = range(10000)
%timeit [i+1 for i in l] 

#Matrix multiplication:
c = np.ones((3, 3))
c
c.dot(c)

#Logical operations:
a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
np.logical_or(a, b)

np.logical_and(a, b)

x = np.array([[1,2],[3,4]])
x>0

#Transcendental functions:
a = np.arange(5)
np.sin(a)
np.log(a)
np.exp(a)
#Shape mismatches
a = np.arange(4)
a + np.array([1, 2]) 

help(np.triu)

#   Transposition:
a = np.triu(np.ones((3, 3)), 1)   # see help(np.triu)
a
a.T


#Computing sums
import numpy as np
from numpy import matrix
from numpy import linalg

x = np.array([[1, 1], [2, 2]])
x
x.sum(axis=0)   # columns (first dimension)
x[:, 0].sum(), x[:, 1].sum()
x.sum(axis=1)   # rows (second dimension)
x[0, :].sum(), x[1, :].sum()

x = np.random.rand(2, 2, 2);y=3
x
x.sum(axis=2)[0, 1]     

x[0, 1, :].sum() 


#np.array([[1,2,3],[1,2,3]]).mul(np.array([[1,2,3],[1,2,3]]),axis=0)


#Logical operations:
a = np.zeros((100, 100))
np.any(a != 0)

np.all(a == a)


a = np.array([10, 100, 300, 211])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])
((a <= b) & (b <= c)).all()



#statistics
x = np.array([1, 2, 3, 1])
y = np.array([[1, 2, 3], [5, 6, 1]])
x.mean()
np.median(x)
np.mean(y, axis=-1) # last axis
x.std()          # full population standard dev.

#Worked Example: data statistics
data = np.loadtxt('populations.txt')
year, hares, lynxes, carrots = data.T  # trick: columns to variables
from matplotlib import pyplot as plt
plt.axes([0.2, 0.1, 0.5, 0.8]) 
plt.plot(year, hares, year, lynxes, year, carrots) 
plt.legend(('Hare', 'Lynx'), loc=(1.05, 0.5)) 

populations = data[:, 1:]
populations.mean(axis=0)
populations.std(axis=0)

help(plt.legend)


#Worked Example: diffusion using a random walk algorithm
n_stories = 1000 # number of walkers
t_max = 200      # time during which we follow the walker
#We randomly choose all the steps 1 or -1 of the walk:
t = np.arange(t_max)
steps = 2 * np.random.random_integers(0, 1, (n_stories, t_max)) - 1
np.unique(steps) # Verification: all steps are 1 or -1

#We build the walks by summing steps along the time:

positions = np.cumsum(steps, axis=1) # axis = 1: dimension of time
sq_distance = positions**2

#We get the mean in the axis of the stories:

mean_sq_distance = np.mean(sq_distance, axis=0)
#Plot the results:

plt.figure(figsize=(4, 3)) 

plt.plot(t, np.sqrt(mean_sq_distance), 'g.', t, np.sqrt(t), 'y-') 

plt.xlabel(r"$t$") 

plt.ylabel(r"$\sqrt{\langle (\delta x)^2 \rangle}$") 


#Broadcasting
help(np.tile)
a = np.tile(np.arange(0, 40, 10), (3, 1)).T
a
b = np.array([0, 1, 2])
a + b

a = np.arange(0, 40, 10)
a.shape
a = a[:, np.newaxis]  # adds a new axis -> 2D array
a.shape
a
a + b
#Worked Example: Broadcasting
mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544,1913, 2448])
distance_array = np.abs(mileposts - mileposts[:, np.newaxis])
distance_array

x, y = np.arange(5), np.arange(5)[:, np.newaxis]
distance = np.sqrt(x ** 2 + y ** 2)
distance
plt.pcolor(distance)    
plt.colorbar()


x, y = np.mgrid[0:4, 0:4]
x
y

#Flattening
a = np.array([[1, 2, 3], [4, 5, 6]])
a.ravel()
a.T
a.T.ravel()


a = np.arange(4*3*2).reshape(4, 3, 2)
a.shape
a[0, 2, 1]
b = a.transpose(1, 2, 0)
b.shape
b[2, 1, 0]


#Sorting data
#Sorting along an axis:
a = np.array([[4, 3, 5], [1, 2, 1]])
b = np.sort(a, axis=0)
b
#Note Sorts each row separately!
#In-place sort:
a.sort(axis=1)
a


#Sorting with fancy indexing:
a = np.array([4, 3, 1, 2])
j = np.argsort(a)
j
a[j]
#Finding minima and maxima:
a = np.array([4, 3, 1, 2])
j_max = np.argmax(a)
j_min = np.argmin(a)
j_max, j_min



#1.3.3. More elaborate arrays


import numpy as np
a = np.array([1, 2, 3])
a.dtype

a[0] = 1.9     # <-- float is truncated to integer
a


#Forced casts:
a = np.array([1.7, 1.2, 1.6])
b = a.astype(int)  # <-- truncates to integer
b

#Rounding:
a = np.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])
b = np.around(a)
b                    # still floating-point

c = np.around(a).astype(int)





############################
############################
############################
############################
############################
######good use #######
############################
############################
############################
############################
############################


#Import Data
from pandas import read_excel
data = read_excel('train.xlsx','Sheet1')
data2 = read_excel('train2.xlsx','Sheet1')
data['Gender'].ndim


#https://www.analyticsvidhya.com/blog/2016/01/12-pandas-techniques-python-data-manipulation/

d1=data.loc[(data["Gender"]=="F") & (data["Education"]=="Non-degree") & (data["Loan_Status"]=="Y"),
          ["Gender","Education","Loan_Status"]]


#Create a new function:
def num_missing(x):
  return sum(x.isnull())

#Applying per column:
print ("Missing values per column:")
print (data.apply(num_missing, axis=0)) #axis=0 defines that function is to be applied on each column

#Applying per row:
print ("\nMissing values per row:")
print (data.apply(num_missing, axis=1).head()) #axis=1 defines that function is to be applied on each row


#First we import a function to determine the mode
from scipy.stats import mode
mode(data['Loan_Amount']).mode[0]
     
data['Gender'].fillna('F',inplace=True)

data['Loan_Amount'].fillna(mode(data['Loan_Amount']).mode[0], inplace=True)



#7 – Merge DataFrames

merged_inner = pd.merge(left=data2,right=data,how='inner', left_on='Property_Area', right_on='Property_Area')
merged_left = pd.merge(left=data2,right=data,how='left', left_on='Property_Area', right_on='Property_Area')
merged_right = pd.merge(left=data2,right=data,how='right', left_on='Property_Area', right_on='Property_Area')

merged_right['happy'].fillna('e', inplace=True)

word=['jonathan','apple']
key_lower=list(map(lambda x:x.upper(),word))

a=[]
a
b=[1,2,5]*3
b
type([]*3)

#class detail example
#https://www.tutorialspoint.com/python/python_classes_objects.htm

class Employee:
   'Common base class for all employees'
   empCount = 0 #empCount is a class variable whose value is shared among all instances of a this class
#__init__() is a special method, which is called class constructor or initialization 
#method that Python calls when you create a new instance of this class.
   def __init__(self, name, salary):                         #attribute name are name and salary
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):                                   # method name is displaycount
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)


Employee.empCount

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp1.displayCount()

emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
del emp1.age  # Delete 'age' attribute.

emp1.displayEmployee() # return the value of the method
emp1.displayEmployee  #only call the method

emp1.displayEmployee()
Employee.displayEmployee(emp1) #pass emp1 to employee class so need to include emp1 in()

import class_sample as cs
cc=cs.Employee
emp3 = cc("jonathan", 2000)
emp3.displayEmployee()



hasattr(emp1, 'name')    # Returns true if 'age' attribute exists
getattr(emp1, 'name')    # Returns value of 'age' attribute
setattr(emp1, 'age', 8) # Set attribute 'age' at 8
delattr(empl, 'age')    # Delete attribute 'age'

#Built-In Class Attributes
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__








#Class Inheritance
class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method




import pandas
import numpy as np
data = pandas.read_csv('demo.csv', sep=',', na_values=".")
data['mean']=data['money'].groupby(data['name']).transform('mean')
ee=data[['money']] #is dataframe
ee=data['money'] #is series
data['mean_2']=data.groupby(['name'])['money'].transform('mean')
data['std_unbiased']=data['money'].groupby(data['name']).transform('std') #return unbiased std
data['std_unbiased_2']=data.groupby(['name'])['money'].transform('std') #return unbiased std
data['count']=data.groupby(['name'])['name'].transform('count')
data['std_biased']=np.sqrt(np.square(data['std_unbiased'])*(data['count']-1)/data['count'])

a=np.array([100,200,300])
np.std(a)  # bias std
np.std(a,ddof=1) #sample std or unbiased std


http://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/



#python loc
http://pythonjourney.com/python-pandas-dataframe-loc-my-understanding-so-far/


#chapter4 array and matrix
import numpy as np
x = [0.0, 1, 2, 3, 4]
y = np.array(x)
y
z=asmatrix(y)

type(y)
y.dtype

import numpy as np
x=np.array([[2],[1,[2],[3,[3,[8,[[8,['p']]]],66,8]]],3])
print(x)
x.shape

x=np.array([[2],['2q'],[3]])
print(x)
x.shape


y=np.array([1,2,3])
print(y)
y.shape

y=np.array([[1],2])
print(y)
y.shape

y=np.array([[1,[2]],[3,[9]]])
print(y)
y.shape

y=np.array([[[1], [2]], [[3], [4]]])
print(y)
y.shape


y=np.array([[1,'p'],7,'p',3])
print(y)
y.shape
y[0][1]



help(np.randn())
np.random.randn(2,2) #normal 0,1

#Numbers which differ by less than 2.220410􀀀16 are numerically the same. to
np.finfo(float).eps

eps = np.finfo(float).eps
x=1
x = x+eps/2
x==1

x=4
y=10
np.allclose(x,y,atol=6) #absolute tolerant


#tile replicates an array
#according to a specified size vector.
x = np.array([[1,2],[3,4]])
x
np.tile(x,(2,3))




>>> x = np.random.randn(10,1)
x
>>> y = np.tile(x,2)
y
np.array_equal(x,y)

#tests if two arrays are equivalent, even if they do not have the exact same shape. Equivalence
#is defined as one array being broadcastable to produce the other.
np.array_equiv(x,y)

#numerical index
import numpy as np
x = np.arange(5)
x.shape
x.ndim
x
sel = np.array([[4,2],[3,1]]) # 2 by 2 array
x[sel]

sel = np.array([0.0,1]) # Floating point data
x[sel] #error, coz index must be integet
x[sel.astype(int)] # No error
x[[1,2]]
x[[0]]
x[[0]].ndim  
x[0].ndim  

x[0:1]

#ix_
x = np.reshape(range(25),(5,5))
x
x[np.ix_([2,3],[0,1,2])] # Rows 2 & 3, cols 0, 1 and 2
x[2:4,:3] # Same, standard slice

  

x = np.reshape(range(10), (2,5))
x
sel = np.array([0,1])
>>> x[sel,sel] # 1dim, 0,1 and 0,1 so will choose 00,11 (direct pair)

>>> x[sel, sel+1]#0,1 and 1,2 so will choose 01, 12
np.array([ 1., 7.])

sel_row = np.array([[0,0],[1,1]])
sel_col = np.array([[0,1],[0,1]])
>>> x[sel_row,sel_col] # 2 by 2, no broadcasting # will choose 00,01, 10,11

>>> sel_row = array([[0],[1]])
>>> sel_col = array([[0,1]])
>>> x[sel_row,sel_col] # 2 by 1 and 1 by 2 difference
shapes, broadcasted as 2 by 2

#12.1.1 Mixing Numerical Indexing with Scalar Selection
sel=np.array([[1],[2]]) # 2 by 1
x[0,sel] # Row 0, elements sel

#12.1.2 Mixing Numerical Indexing with Slicing
x[:,[1]]
x[:,[1]].shape #two dimensional 1x2

x[[1],:]
x[[1],:].shape #two dimensional 1x2
#Note that the mixed numerical indexing and slicing uses a list ([1]) so that it is not a scalar. This is important
#since using a scalar will result in dimension reduction.
x[:,1] # 1dimensional

x = np.reshape(np.arange(3**3), (3,3,3)) # 3d


#12.1.3 Linear Numerical Indexing using flat
x.flat[[[3,4,9],[1,5,3]]]

#12.2 Logical Indexing
x = np.arange(-3,3)
x
x < 0
x[x < 0]

x = np.reshape(np.arange(-8,8), (4,4))
x[x < 0]

x = np.reshape(np.arange(-8,8),(-4,4))
cols = np.any(x < -6, 0)
rows = np.any(x < 0, 1)
x[np.ix_(cols,rows)] # Upper 2 by 2

sum(x,0)
x[0,sum(x,0)>0]

np.extract(x>0,x)

x = np.reshape(np.arange(-10,10),(4,5))
x[np.sum(x,1)<0,:] = np.arange(5.0) # Replace rows w/ negative sum
x

x = np.reshape(np.arange(-10,10),(4,5))
x[:,np.sum(x,1)<0] = np.arange(4) # Error array is 1 by 4 array,*************************

x[:,np.sum(x,1)<0] = np.reshape(np.arange(4),(4,1)) # Correct col replacement
x

x = np.zeros((4,3))
x
np.size(x,0)
np.size(x,1)
help(np.size)

x = np.linspace(0,100,11)
enumerate(x)
for i,y in enumerate(x):
    print('i is :', i)
    print('y is :', y)


x = np.random.randn(1000)
for i in x:
    print(i)
    if i > 2:
        break
x=np.arange(-2,10)
for i in x:
    if i >= 0:
        continue
    print(i)

    
    
    
    #13.6 List Comprehensions
x = np.arange(5)
y = []
for i in x:
    y.append(np.exp(x[i]))
y


z = [np.exp(x[i]) for i in x]
z
type(z)

x = np.arange(5)
z = [x[i]**2 for i in x if np.floor(i/2)==i/2]
z

x1 = np.arange(5.0)
x1
x2 = np.arange(3.0)
x2
z = [x1[i]*x2[j] for i in x1 for j in x2]
z


z_dict = {i:np.exp(i) for i in x}
type(z_dict)
z_dict.keys()
z_dict.values()

z_tuple = tuple(i**3 for i in x)









#14.1 Creating Dates and Times
import datetime as dt
yr, mo, dd = 2012, 12, 21
dt.date(yr, mo, dd)

hr, mm, ss, ms= 12, 21, 12, 21
dt.time(hr, mm, ss, ms)
dt.time(12,21,12,21)

d=dt.datetime(yr, mo, dd, hr, mm, ss, ms)

d1 = dt.datetime(yr, mo, dd, hr, mm, ss, ms)
d2 = dt.datetime(yr + 1, mo, dd, hr, mm, ss, ms)
d2-d1
d2
d2 + dt.timedelta(30,0,0) #days
dt.date(2012,12,21) + dt.timedelta(30,12,0)
dt.date(2012,12,21) + dt.timedelta(30,0,0)

#If times stamps are important, date types can be promoted to datetime using combine and a time.
d3 = dt.date(2012,12,21)
dt.datetime.combine(d3, dt.time(0))

#Values in dates, times and datetimes can be modified using replace through keyword arguments.
d3 = dt.datetime(2012,12,21,12,21,12,21)
d3.replace(month=11,day=10,hour=9,minute=8,second=7,microsecond=6)

#16.1 Mixed Arrays with Column Names
x = np.zeros(4,[('date','int'),('ret','float')])
x
x = np.zeros(4,{'names': ('date','ret'), 'formats': ('int', 'float')})
x.ndim
x['date']
x['ret']

x[0] # Data tuple 0
x[:3] # Data tuples 0, 1 and 2

#import time data and try to subset
from pandas import read_excel
import datetime as dt
data = read_excel('time_data.xlsx','Sheet1')
data.dtypes
data.loc[data['Date']>dt.date(2014,12,21),]



#pandas
#Series are the primary building block of the data structures in pandas, 
#and in many ways a Series behaves similarly to a NumPy array. A Series
# is initialized using a list or tupel, or directly from a NumPy array.
from pandas import Series
import numpy as np
a = np.array([0.1, 1.2, 2.3, 3.4, 4.5])
s = Series([0.1, 1.2, 2.3, 3.4, 4.5])
s
s.dtype
type(s)
s = Series(a) # NumPy array to Series
s = Series([0.1, 1.2, 2.3, 3.4, 4.5], index = ['a','b','c','d','e'])
s
s['a']
s[0]

s[['a','c']]
s[:2]

s = Series([0.1, 1.2, 2.3, 3.4, 4.5], index = ['a','b','c','a','b'])
s['a']

#Series can also be initialized directly from dictionaries.
s = Series({'a': 0.1, 'b': 1.2, 'c': 2.3})

s1 = Series([1.0,2,3])
s1.values
s1.index

s['a']
s[0]
s[['a','c']]
s[:2]
s[s>2]

s1 = Series([1.0,2,3],index=['a']*3)

s1 = Series(np.arange(10,20))
s1.describe()
summ = s1.describe()
summ['mean']
s1.unique()
s1.nunique()

>>> s1 = Series(np.arange(1,4),index=['a','b','c'])
>>> s2 = Series(np.arange(1,4),index=['c','d','e'])
>>> s3 = s1 + s2
s3
s3.dropna()

# pandas dataframe
#a DataFrame is composed of
#Series and each Series has its own data type, and so not allDataFrames are representable as homogeneous
#NumPy arrays.
from pandas import DataFrame
df = DataFrame(np.array([[1,2],[3,4]]),columns=['a','b'])

df = DataFrame(np.array([[1,2],[3,4]]))
df.columns = ['dogs','cats']
#
#Index values are similarly assigned using either the keyword 
#argument index or by setting the index property. (row label)
df = DataFrame(np.array([[1,2],[3,4]]), columns=['dogs','cats'], index=['Alice','Bob'])

#DataFrames can also be created from NumPy arrays with structured data.
import numpy as np
import datetime
x=np.array([(datetime.datetime(2013, 1, 1, 0, 0), 99.98999786376953)],dtype=[('datetime', 'O'), ('value', '<f4')])
df=DataFrame(x)
df.dtypes

s1 = Series(np.arange(0.0,5))
s2 = Series(np.arange(1.0,3))
>>> DataFrame({'one': s1, 'two': s2}) #create a DataFrame uses a dictionary containing Series

              
              
              
from pandas import read_excel
import pandas as pd
data = read_excel('train.xlsx','Sheet1')
data.head()
data['Gender'].head() # Series
type(data['Gender'])
data['Gender'][0]
data[['Gender']].head() # DataFrame
key=data['Gender']=='M'
key.ndim
key.shape
key2=np.array(key, dtype=pd.Series)
key2.ndim
key2.shape
check1=data[key]   # so not much different between series and np array
check2=data[key2]   # so not much different between series and np array

#Selecting Rows and Columns
#ix is the normal selector
data3=data.ix[0:1,0]  # Select row 0,1 with column 0 and return a series
data3=data.ix[1:2,:2]  # Select row 1,2 with column 0,1

data.ix[key,'Gender']
data.ix[0:3,'Credit_History']   #select row 0 to 3
type(data.ix[0:3,'Credit_History']) #series
data.loc[0:3,'Credit_History']  #select row 0 to 3
type(data.loc[0:3,'Credit_History']) #series
data['Credit_History'][0:3]     #select row 0 to 2
type(data['Credit_History'])

data3=data[1:3] #select row 1,2
data3=data[1:2] #select row 1 and it is also a dataframe



data.ix[key,0]
data2=data[['Gender','Education','Self_Employed']]
data2.insert(0,'Self_Employed_2',data2['Self_Employed'])   #move Self_Employed to the front and rename
data2

del data2['Self_Employed']  # drop Self_Employed
data2

data2.rename(columns = {'Self_Employed_2':'Self_Employed'}, inplace = True) #rename back to Self_Employed

data2.head()


del data2['Education']
data2.head()

data3=data2.drop('Gender',axis=1)
data3.head()
data4=data3.pop('Self_Employed')
data3.head()
data4.head()


>>> df = DataFrame(np.array([[1, np.nan],[np.nan, 2],[3,4],[0,6]]))
>>> df.columns = ['one','two']
>>> replacements = {'one':1,'two':2}
>>> df=df.fillna(value=replacements)
df
df.sort(columns=['one','two'],ascending=[0,1])

import pandas as pd
df1 = DataFrame([1,2,3],index=['a','b','c'],columns=['one'])
df2 = DataFrame([4,5,6],index=['c','d','e'],columns=['two'])
pd.concat((df1,df2), axis=1)
pd.concat((df1,df2), axis=1, join='inner')


#merge join
from pandas import DataFrame
import numpy as np
import pandas as pd
left = DataFrame([[1,2,np.nan],[3,4,np.nan],[5,6,2]],columns=['one','two','three'])
left
right = DataFrame([[1,2,3],[3,4,np.nan],[7,8,10]],columns=['one','jonathan','three'])
right
left.merge(right,on='one') # Same as how=’inner’
left.merge(right,on='one', how='left')
left.merge(right,on='one', how='outer')

pd.merge(left,right,how='left',on=['one'])
pd.merge(left,right,how='right',on=['one'])
pd.merge(left,right,how='inner',on=['one'])
pd.merge(left,right,how='outer',on=['one'])



left = DataFrame([[1,2,np.nan],[3,4,np.nan],[5,6,2]],columns=['one','two','three'])
left
right = DataFrame([[1,2,3],[3,4,np.nan],[7,8,10],[1,10,10]],columns=['one','two','three'])
right


pd.merge(left,right[['one','two','three']],how='left',left_on=['one','two'],right_on=['one','two'])
pd.merge(left,right[['one','two','three']],how='right',on=['one'])
pd.merge(left,right[['one','two','three']],how='inner',on=['one'])
pd.merge(left,right[['one','two','three']],how='outer',on=['one'])




#cbind and rbind
a=pd.concat([left,right],axis=1) #equivalent to R cbind, row name/index need to be equal
a
b=pd.concat([left,right],axis=0) #equivalent to R rbind, column name need to be equal
b

c=left.loc[2:2,]
c
d=right.loc[1:1,]
d                             

e=pd.concat([c,d],axis=1)  # concat column (axis=1)
e
e['one'] 

c=c.reset_index(drop=True)
c
c=c.drop('index',axis=1)
c

d=d.reset_index()
d
d.drop('index',axis=1,inplace=True) # drop without haveing to reassign df
d

e=pd.concat([c,d],axis=1)  
e                   




test = DataFrame([[1,2,np.nan,3],[3,4,np.nan,np.nan],[5,6,2,4],[1,1,3,3]],columns=['one','two','three','four'])
test
test.dropna()
test2=test.loc[test.three!=test.four]
test2
#note in np.isnan and pd.isnull are equivalent, null means nan, no Na in python
test3=test2[~(np.isnan(test2.three) & np.isnan(test2.four))]  
test3

test3=test2[~(pd.isnull(test2.three) & pd.isnull(test2.four))]
test3









check= data.groupby(by='Gender')
check.groups # Lists group names and index labels for group membership
check.mean()
check.std()

data5=data[['Loan_Amount']]
data5.apply(np.mean, axis=0).head()
data.Gender.value_counts()


from pandas import date_range
date_range('20130103','20130105')
date_range('20130103',periods=3)
date_range('20130103',periods=4, freq='Q').values




#Performance and Code Optimization
import numpy as np
x = np.random.randn(1000,1000)

#%time simply runs the code
#and reports the time needed. 
#%timeit is smarter in that it will vary the number of iterations to increase
#the accuracy of the timing.
%timeit np.linalg.inv(np.dot(x.T,x))
%time np.linalg.inv(np.dot(x.T,x))


#profiling
#Profiling provides detailed information about the number of times a line is executed as well as the execution
#time spent on each line



#python equivalent to dyplr in R
import pandas as pd
data = pd.DataFrame(
    {'col1':[1,1,1,1,1,2,2,2,2,2],
    'col2':[1,2,3,4,5,6,7,8,9,0],
     'col3':[-1,-2,-3,-4,-5,-6,-7,-8,-9,0]
    }
)
data
data[1:2]

data
data.groupby('col1').agg({'col2': max, 'col3': min})
data.groupby('col1').agg({'col2': max, 'col3': min}).reset_index()

data.groupby('col1').agg({'col2': [max, min], 'col3': [min, 'count']})

#If you want to label each returning output you can use a dictionary of dictionaries:

data.groupby('col1').agg({'col2': {'col2_max': max, 'col2_min': min}, 
                            'col3': {'col3_min': min, 'col3_count': 'count'}})

#If the operation involves multiple columns (maximum of col2 * col3),
# you can assign a new column and use groupby agg:

data2=data.assign(col2_col3 = lambda x: x.col2 * x.col3)
data2.groupby('col1')['col2_col3'].agg(max)

data.groupby('col1').apply(lambda x: (x.col2 * x.col3).max())






import pandas as pd
from pandas import DataFrame
data = pd.DataFrame(
    {'horse':['jonathan','jonathan','jonathan','tom','tom','tom','sam','sam'],
    'col2':[1,1,1,2,2,1,3,4],
     'col3':[-1,-2,-3,-4,-5,-6,-7,-8]
    }
)
type(data)
data
col=data.columns.tolist();print(type(col));print(col)
a=data.columns.get_loc("horse")

a1=[col[a]] #chnage a single string to list

col=[col[a]]+col[0:a]
data=data[col]

def find_no_unique(y,name):
    out=y[name].unique()  #array
    out2=len(out)         #int
    output=DataFrame({'elements':out,
                     'counts':out2})
    return output

m=DataFrame(data.groupby('horse').apply(lambda x: find_no_unique(x,'col2')))
m.columns = ['out']
m.index.tolist()
m.ix[[('sam',0),('sam',1)],]
m.dtypes

type(len(data.col2.unique()))


def find_no_unique(y,name):
    out=3
    out2=len(y[name].unique())
    df = DataFrame(np.array([[out,out2]]), columns=['elements','counts'])
    return df
m=DataFrame(data.groupby('horse').apply(lambda x: find_no_unique(x,'col2')))


def find_no_unique(y,name):
    out=3  
    out2=len(y[name].unique())         
    output=DataFrame({'elements':[out],
                     'counts':[out2]})
    return output

m=DataFrame(data.groupby('horse').apply(lambda x: find_no_unique(x,'col2')))
m



def find_no_unique(y,name):    
    out2=y[name]  
    out=y['col3'] 
    output=DataFrame({'col3':out,
                      'col2':out2})    
    return output

m=DataFrame(data.groupby('horse').apply(lambda x: find_no_unique(x,'col2')))
m

new=DataFrame(data.horse.unique())
new.columns=['name']
new






import scipy.stats
scipy.stats.norm(4.2, 1.04).cdf(3.5)

          

23.2 Timing Code
import numpy as np
np.random.randn(2,2) #normal 0,1
x = np.random.randn(1000,1000)
%timeit np.linalg.inv(np.dot(x.T,x))
%time np.linalg.inv(np.dot(x.T,x))

x = np.zeros(1000000)
x += 0.0





#24.1 map and related functions
#map is a built-in method to apply a function to a generic iterable. 
#It is used as map( function , iterable ),
#and returns a list containing the results of applying function to each
# item of iterable. The list returned can
#be either a simple list if the function returns a single item, or a list 
#of tuples if the function returns more
#than 1 value.
def powers(x):
    return x**2, x**3, x**4
y = [1.0, 2.0, 3.0, 4.0]
x=list(map(powers, y))
x

def powers(x,y):
    if x is None or y is None:
        return None
    else:
        return x**2, x*y, y**2

x = [10.0, 20.0, 30.0]
y = [1.0, 2.0, 3.0, 4.0]
list(map(powers, x, y))

#A related function is zip which combines two or more lists into a single list of tuples
list(zip(x,y))




a=datetime.datetime.strptime('2005-06-15','%Y-%m-%d')  # parse (convert) string to datetime object.
type(a)

a1=datetime.datetime.strptime('2006-06-15','%Y-%m-%d')  # parse (convert) string to datetime object.
type(a1)
a1>a

c=datetime.datetime.strptime('2005-06-20','%Y-%m-%d')
c-a
c>a

#strftime(format) method, to create a string representing 
#the time under the control of an explicit format string
b=a.strftime('%d-%m-%Y') 
type(b)
b1=a1.strftime('%d-%m-%Y') 
b>b1

d="2016-03-21"
d1="2017-03-22"
d<d1

import py_compile                     #create pyc file
py_compile.compile('xxxx.py')


#python logging
#http://yu-liang.logdown.com/posts/195882/python-logging-module
import logging

logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='C:\\Users\\notebook\\file.log',filemode='w')

logging.warning('Hello world!')
logging.info('Hello world again!')





def fake(elem,lt=[]):
    lt=[]
    lt.insert(0,elem)
    return lt
fake(0,lt=[])
fake(1)
fake(6)


lt=[]
lt.insert(0,1)
lt
lt.insert(0,2)
lt

a=fake(1)
b=fake(1)
c=1
a=c
c=3



#python pip Fatal error in jamesncher: Unable to create process using '"'
#go to python.exe page, open cmd
#python -m pip install selenium
#http://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
#download geckodriver from https://github.com/mozilla/geckodriver/releases for firefox (suggest now use firefox, use chrome)
#download https://sites.google.com/a/chromium.org/chromedriver/downloads for chromedriver
#download selectorgadget https://chrome.google.com/webstore/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb
#note that for selecting button, use both xpath and ccs selector also ok. for xpath need to download selectorgadget
#for ccs selector, need to look at html code
import os
os.chdir(r'C:\Users\jonathanjames\Desktop\python\WinPython-64bit-3.5.2.3Qt5\notebooks')
print (os.getcwd())


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox(executable_path=r'C:\Users\jonathanjames\Desktop\python\geckodriver.exe')
driver.get(r"file:///C:/Users/jonathanjames/Desktop/python/testhtml.html")
element = driver.find_element_by_xpath(".//a[@id='gb_23']")
element.click()

#search in google using firefox
browser = webdriver.Firefox(executable_path=r'C:\Users\jonathanjames\Desktop\python\geckodriver.exe')
browser.get('http://www.google.com')
search = browser.find_element_by_name('q')
search = browser.find_element_by_xpath('//*[(@id = "lst-ib")]')
search.send_keys("google search through python")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results
browser.quit()


#example in elit trader
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(executable_path=r'C:\Users\jonathanjames\Desktop\python\chromedriver.exe')
browser.get('https://www.elitetrader.com/et/forums/programming.65/')
search = browser.find_element_by_xpath('//*[(@id = "QuickSearchQuery")]')
search.send_keys(" search through python")
search.send_keys(Keys.RETURN)

browser.get('https://www.elitetrader.com/et/forums/programming.65/')
browser.find_element_by_css_selector('dl[class="choosers"]').click()

browser.get('https://www.elitetrader.com/et/forums/programming.65/')
browser.find_element_by_css_selector('li[class="navTab nodetab69 PopupClosed"]').click()
#click on commission button
browser.find_element_by_css_selector('a[href="http://ninjatrader.com/Futures?utm_source=EliteTrader&utm_medium=cpc&utm_content=brokersponsor&utm_campaign=Commissions"]').click()


browser.get('https://www.elitetrader.com/et/forums/programming.65/')
search = browser.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "nodetab71", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "navLink", " " ))]')
search.click()
browser.quit()


#example in CQG
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(executable_path=r'C:\Users\jonathanjames\Desktop\python\chromedriver.exe')
browser.get('https://www.cqg.com/products/cqg-integrated-client/cqg-ic-2-week-free-trial')
search = browser.find_element_by_xpath('//*[(@id = "edit-submitted-first-name")]')
search.send_keys("jonathan james")
search = browser.find_element_by_xpath('//*[(@id = "edit-submitted-last-name")]')
search.send_keys("lei wai")
#click check-box
search = browser.find_element_by_xpath('//*[(@id = "edit-submitted-00n60000002gqco")]') #check box for energy
search.click()
#click dropdown menu (proprietary firm)
search=browser.find_element_by_xpath("//select[@name='submitted[00N60000002Gk5o]']/option[text()='Proprietary Firm']")
search.click()
#click "submit"
search = browser.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "form-submit", " " ))]')
search.click()


#get all items in a dropdown menu
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as UI
import contextlib

browser = webdriver.Chrome(executable_path=r'C:\Users\jonathanjames\Desktop\python\chromedriver.exe')
browser.get('https://www.cqg.com/products/cqg-integrated-client/cqg-ic-2-week-free-trial')
items=[]
select = UI.Select(browser.find_element_by_xpath('//select[@name="submitted[00N60000002Gk5o]"]'))
for i in range(len(select.options)):
    items.append(select.options[i].get_attribute('value'))
items







#upload file to a upload button
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(executable_path=r'C:\Users\jonathanjames\Desktop\python\chromedriver.exe')
browser.get('https://smallpdf.com/word-to-pdf')
browser.find_element_by_css_selector('input[type="file"]').send_keys(r"C:\Users\jonathanjames\Desktop\try.pdf")





#upload file to multiple upload button
#html exampl below
#<input type="file" class="file" name="files" size="40" tabindex="1" accept="application/pdf" onmousedown="gaTracker.choosefile()">

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(executable_path=r'C:\Users\jonathanjames\Desktop\python\chromedriver.exe')
browser.get('https://www.pdfmerge.com/')

browser.find_element_by_css_selector('input[tabindex="1"]').send_keys(r"C:\Users\jonathanjames\Desktop\try.pdf")
browser.find_element_by_css_selector('input[tabindex="2"]').send_keys(r"C:\Users\jonathanjames\Desktop\try.pdf")
browser.find_element_by_css_selector('input[tabindex="3"]').send_keys(r"C:\Users\jonathanjames\Desktop\try.pdf")
browser.find_element_by_css_selector('input[tabindex="4"]').send_keys(r"C:\Users\jonathanjames\Desktop\try.pdf")
browser.find_element_by_css_selector('input[id="btnSubmit"]').click()   #click merge button

                                     
                             
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     


#upload file to a upload button
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(executable_path=r'C:\Users\jonathanjames\Desktop\python\chromedriver.exe')
browser.get('http://bet.hkjc.com/football/default.aspx')
search = browser.find_element_by_xpath('//*[(@id = "leftTxtFBHIL")]') #Hilo
search.click()




#multi process
from joblib import Parallel, delayed
import numpy as np
import numpy as np
import os


from adhot import happy,happy2, f


b=1
res = Parallel(n_jobs=4,verbose=5)(delayed(happy)(a) for a in range(2)) #verbose for output progress
res








# multiprocessing_example
import multiprocessing as mp
import matplotlib.pyplot as plt
import numpy as np
from adhot import supf_wrapper
if __name__ == '__main__':
    reps = 1000
    T = 200
    setup = []
    for i in range(reps):
        y = np.random.standard_normal(T)
        x = np.random.standard_normal((T, 1))
        p = 0.2
        setup.append((y, x, p))
# Non parallel map
# res = map(surf_wrapper, setup)
# Parallel map
    po = mp.Pool(processes=2)
    res = po.map(supf_wrapper, setup)
    print(len(res))
    po.close()
    ax = plt.hist(res)
    ax = ax[2]
    fig = ax[0].get_figure()
    fig.savefig('multiprocessing.pdf')



    
#multi process on apply group
import pandas as pd
from joblib import Parallel, delayed
import multiprocessing
from adhot import tmpFunc
from adhot import applyParallel

if __name__ == '__main__':
    df = pd.DataFrame({'a': [6, 2, 2], 'b': [4, 5, 6]},index= ['g1', 'g1', 'g2'])
    print (applyParallel(df.groupby(df.a), tmpFunc))

for group in df.groupby(df.a):
    print (group)
for name in df.groupby(df.a):
    print (name)
for key in df.groupby(df.a):
    print (key)
    
    
df = pd.DataFrame({'a': ['jonathan', 'jonathan', 'simon'], 'b': [4, 5, 6],'c':[5,6,7]})
df
d=df
d['a'][0]='ee'
df #note that it will change df, so need to use d=df.copy


a=[2,3] 
y=a.copy #list is also mutable so need to use copy
y[1]=4
a
    
b=3,4,'t'
b
bb=b
bb[0]=2   #tuple is immutable



#In short , use this 'if __name__ == "main" ' block to prevent (certain) 
#code from being run when the module is imported.





import pandas as pd
df = pd.DataFrame({'a': ['jonathan', 'lam', 'simon'], 'b': [4, 5, 6],'c':[5,6,7]})
def mo(x):
    yes=x.loc[:,'c']
    return yes
    
newcol=df.groupby(['a']).apply(lambda x:mo(x)) #after groupby the index is tuple with level 0 = group name, level1=index
df['new']=newcol.reset_index(level=0, drop=True) #error occure

newcol2=newcol
newcol2.reset_index(drop=True)

%timeit -n100 -r20 df.groupby(['a']).apply(lambda x:mo(x)) #100 loop best 20










import pandas as pd
x=hkdb_with_track_work=hkdb_with_track_work.head(1)
period1='2016-06-12';field1='TW_P';field2='TW_T';test1=0;test2=4
def DBA(x):
    period=x.loc[:,'Date'];field1='TW_P';field2='TW_T'
    test1=x.loc[:,'TW_P']
    test2=x.loc[:,'TW_T']
    dataset_copy=trackwork_use.copy()
    dataset_copy=dataset_copy[(dataset_copy['Date'].apply(lambda x: datetime.datetime.strftime(x, '%Y-%m-%d')) < period1)]
    dataset_copy['test1']=test1.values[0]
    dataset_copy['test2']=test2.values[0]
    dataset_copy['distance']=np.sqrt(pow(dataset_copy['TW_P']-dataset_copy['test1'],2)+pow(dataset_copy['TW_T']-dataset_copy['test2'],2))
    output=dataset_copy.loc[dataset_copy['distance']<=2,'nfp_c'].mean()
    ave_fp=output if ~np.isnan(output) else dataset_copy.loc[dataset_copy['distance']<=3,'nfp_c'].mean()
    ave_fp_out=pd.DataFrame({'ave_fp':[ave_fp]})
    return ave_fp_out

%timeit DBA(period1='2016-01-31',field1='TW_P',field2='TW_T',test1=0,test2=4)

hkdb_with_track_work=hkdb_with_track_work.head(1)
hkdb_with_track_work.sort_index(inplace=True)

hkdb_with_track_work['revised_tony_paul']=hkdb_with_track_work.groupby(['racekey','horse_no','Date']).apply(lambda x:DBA(x))

%timeit DBA(x)

    
df = pd.DataFrame({'a': ['jonathan', 'lam', 'simon'], 'b': [4, 5, 6],'c':[5,6,7]})

def mo(x):
    yes=x.loc[:,'c']
    return yes
    
newcol=df.groupby(['a']).apply(lambda x:mo(x)) #after groupby the index is tuple with level 0 = group name, level1=index
df['new']=newcol.reset_index(level=0, drop=True)

df.index




#pip issue
#put python.exe to envirnment path
#reopen computer
#go to C:\Users\jonathanjames\Desktop\python\get-pip, open cmd, python get-pip.py (install latest pip)
#go to python.exe folder, open cmd, type "python -m pip install xxxx"

#or
#add pip.exe to environment variable
#reopen computer

#if package cannot be install, go to python package index, download whl file, unzip it, then
#import the file name, for example like below "constraint" package


#constraint optimization
#https://labix.org/python-constraint
import os
os.chdir(r'C:\Users\jonathanjames\Desktop\python\constraint')
import constraint


import os
os.chdir(r'C:\Users\jonathanjames\Desktop\python\WinPython-64bit-3.4.4.5Qt5\notebooks')


from constraint import *
problem = Problem()
problem.addVariable("a", [1,2,3])
problem.addVariable("b", [4,5,6])
problem.getSolutions()


problem.addConstraint(lambda a, b: a*2 == b,("a", "b"))
problem.getSolutions()










#hsi
import pandas as pd
import os
#hsi_path =r"C:\Users\jonathan.james\Desktop\adhot\hsi\HSI.csv"
#data = pd.read_csv(hsi_path)
 
import fix_yahoo_finance as yf
data = yf.download('^HSI', start = '2014-01-01', end='2018-06-26')
 
 
import stockstats
from stockstats import StockDataFrame as Sdf
import numpy as np
 
#convert’ a pandas dataframe to a stockstats dataframe
#hsi2=hsi.copy()
stock_df = Sdf.retype(data)
data['rsi']=stock_df['rsi_14']
del data['close_-1_s']
del data['close_-1_d']
del data['rs_14']
del data['rsi_14']
 
#replicate rsi
x=data.copy()
parameter=20
def rsi(x,parameter):
    x['change']=x['close']-x['open']
    x.loc[x['change']>=0,'gain']=x['change'];x.loc[x['change']<0,'gain']=0
    x.loc[x['change']<0,'loss']=-1*x['change'];x.loc[x['change']>=0,'loss']=0
    x['ave_gain']=x.gain.rolling(window=parameter).mean()
    x['ave_loss']=x.loss.rolling(window=parameter).mean()
    x['RS']=x['ave_gain']/x['ave_loss']
    x.loc[x['RS']==0,'RSI']=100;x.loc[x['RS']>0,'RSI']=100-100/(1+x['RS'])
    x=x.fillna(0)
    x['RSI_shift1']=x['RSI'].shift(1)
    x['RSI_shift1']=x['RSI_shift1'].fillna(0)
    x['RSI_shift2']=x['RSI'].shift(2)
    x['RSI_shift2']=x['RSI_shift2'].fillna(0)
    x['RSI_change']=x['RSI_shift1']-x['RSI_shift2']
    return x#pd.Series((x['RSI_change'].values,x['RSI_shift1'].values))
 
data_new=rsi(data,80)
 
data_new['change_sign']=np.sign(data_new['change'])
data_new['RSI_change_sign']=np.sign(data_new['RSI_change'])
data_new['same?']=data_new['change_sign']==data_new['RSI_change_sign']
 
data_new=data_new.loc[~(data_new['RSI_change_sign']==0),:]
 
sum(data_new['same?'])/data_new.shape[0]





import time
log_name=os.path.join('log','log_data_part_'+time.strftime("%Y%m%d")+'_'+time.strftime("%H%M%S")+'.log')
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# create a file handler
handler = logging.FileHandler(log_name)
handler.setLevel(logging.INFO)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)
logger.info('Hello baby')

logger.info('date in '+data.Name_use_python[i]+' not distinct')
logger.info(output)



logging.shutdown()

















import requests


TWILIO_SID = "AC15cb8d527aad95bca1bf6b0a3b21dd21"
TWILIO_AUTHTOKEN = "04f77bd53a489c51fe587e0541935bc4"
TWILIO_MESSAGE_ENDPOINT = "https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json".format(TWILIO_SID=TWILIO_SID)

TWILIO_NUMBER = "whatsapp:+447754279265"

def send_whatsapp_message(to, message):

    message_data = {
        "To": to,
        "From": TWILIO_NUMBER,
        "Body": message,
    }
    response = requests.post(TWILIO_MESSAGE_ENDPOINT, data=message_data, auth=(TWILIO_SID, TWILIO_AUTHTOKEN))
    
    response_json = response.json()
    
    
    return response_json


to_number = "whatsapp:+447754279265"   
appointment_msg = """Your appointment is coming up on August 20th at 6:00PM""" 
msg = send_whatsapp_message(to_number, appointment_msg)

print(msg['sid']) # SM5xxxafa561e34b1e84c9d22351ae08a0
print(msg['status']) # queued







import os
os.chdir(r'C:\Users\jonathanjames\Desktop\python\twilio')
import twilio
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC15cb8d527aad95bca1bf6b0a3b21dd21'
auth_token = '04f77bd53a489c51fe587e0541935bc4'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+85255480236',
                              to='whatsapp:+447754279265'
                          )

print(message.sid)












import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 565)
server.starttls()
server.login("random9522@gmail.com", "95229522")
 
msg = "YOUR MESSAGE!"
server.sendmail("jonathan.leiwai@gmail.com", "THE EMAIL ADDRESS TO SEND TO", msg)
server.quit()




import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("random9522@gmail.com", "95229522")
server.sendmail(
  "random9522@gmail.com", 
  "jonathan.leiwai@gmail.com", 
  "this message is from python")
server.quit()









#python send email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = "test python"
#The mail addresses and password
sender_address = 'random9522@gmail.com'
sender_pass = '95229522'
receiver_address = 'lei.jonathan2016@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')











#python regular expression
#https://www.analyticsvidhya.com/blog/2015/06/regular-expression-python/



Operators	Description
.	 Matches with any single character except newline ‘\n’.
?	 match 0 or 1 occurrence of the pattern to its left
+	 1 or more occurrences of the pattern to its left
*	 0 or more occurrences of the pattern to its left



result=re.findall(r'\d','AV is largest Analytics community of India 3749 eruabcd 309')
print (result) 
['3', '7', '4', '9', '3', '0', '9']

result=re.findall(r'\d+','AV is largest Analytics community of India 3749 eruabcd 309')
print (result) 
['3749', '309']

# * allow zero d, so include white space and resulting many white space
result=re.findall(r'\d*','AV is largest Analytics community of India 3749 eruabcd 309')
print (result) 
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '3749', '', '', '', '', '', '', '', '', '', '309', '']

#using ? to include 3749 and 309 becasue 0 or 1 occurance of . or ,
result=re.findall(r'\d+[.,]?\d*','AV is largest Analytics 103.45 1,000   3,000  of India 3749 eruabcd 309')
print (result) 
['103.45', '1,000', '3,000', '3749', '309']

result=re.findall(r'\d+[.,]\d*','AV is largest Analytics 103.45 1,000   3,000  of India 3749 eruabcd 309')
print (result) 
['103.45', '1,000', '3,000']

#if without * then it require exactly 1 digit
result=re.findall(r'\d+[.,]\d','AV is largest Analytics 103.45 1,000   3,000  of India 3749 eruabcd 309')
print (result) 
['103.4', '1,0', '3,0']

result=re.findall(r' [A-Z] ','AV is D largest Analytics 103.45 1,000   3,000  of India 3749 eruabcd 309')
print (result) 
[' D ']


https://stackoverflow.com/questions/10804732/difference-between-and
#?: meaning

result=re.findall(r'a(\d)','a7 bcd abcd')
print (result) 
['7']

result=re.findall(r'a(?:\d)c','a7 a8c bcd abcd')
print (result) 
['a8c']

result=re.findall(r'a(?=\d)','a7 bcd abcd')
print (result) 
['a']








import re
#Use “r” at the start of the pattern string, it designates a python raw string.
result = re.match(r'AV', 'AV Analytics Vidhya AV')
result.group(0)

result = re.match(r'Analytics', 'AV Analytics Vidhya AV')
print (result) 


#There are methods like start() and end() to know the start and end position of matching pattern in the string.
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print (result.start())
print (result.end())


# Return words starts with alphabets (using [])
result=re.findall(r'[aeiouAEIOU]\w+','AV is largest Analytics community of India 3749 eru 309')
print (result)

#“\b” for word boundary.
result=re.findall(r'\b[aeiouAEIOU]\w+','AV is largest Analytics community of India 3749 eruabcd 309 &3apple')
print (result) 


#In similar ways, we can extract words those starts with constant using “^” within square bracket.
result=re.findall(r'\b[^aeiouAEIOU]\w+','AV is largest Analytics community of India 3749 eruabcd 309')
print (result) 


import re
s = 'I love book()'
result = re.search(r'\(\)',s)
print (result.group())



s1 = 'I love book(s)'
result2 = re.sub(r'[\(\)]','',s1)
print (result2)








fill_example="Fill(contract=Stock(conId=4875668, symbol='HSBC', exchange='SMART', primaryExchange='NYSE', currency='USD', localSymbol='HSBC', tradingClass='HSBC'), execution=Execution(execId='00012ec5.5c5ade3e.01.01', time=datetime.datetime(2019, 2, 6, 17, 57, 6, tzinfo=datetime.timezone.utc), acctNumber='DU1349023', exchange='NYSE', side='BOT', shares=100.0, price=42.18, permId=1433082775, clientId=1, orderId=85, cumQty=200.0, avgPrice=42.18, lastLiquidity=2), commissionReport=CommissionReport(execId='00012ec5.5c5ade3e.01.01', currency='USD'), time=datetime.datetime(2019, 2, 6, 18, 0, 56, 105886, tzinfo=datetime.timezone.utc))"

#find string between "Execution"
#\( because there is really ( symbol in the string, cannot use ( directly
#() is python syntac to find substring between()
#.* is to find all substring between()
#? is to find the first occurance of substring
find_Execution=re.findall(r'execution=Execution\((.*?), tzinfo',fill_example)
time_is=re.findall(r'time=datetime.datetime\((.*)',find_Execution[0])[0]
time_is=time_is.split(',')
time_is=[int(i.strip()) for i in time_is]

execution_time_is=dt(time_is[0],time_is[1],time_is[2],time_is[3],time_is[4],time_is[5])

#datatime default is 'naive, so assign UTC to it'
execution_time_is_utc = execution_time_is.replace(tzinfo=tz.gettz('UTC'))

#convert time hong kong
to_zone = tz.gettz('Asia/Hong_Kong')
execution_time_is_hk=execution_time_is_utc.astimezone(to_zone)


From: "Mr. Ben Suleman" <bensul2004nng@spinfinder.com>
From: "PRINCE OBONG ELEME" <obong_715@epatra.com>




side=[i for i in fill_report_list if "side" in i][0].strip().replace("side=","").replace("'","")
side



from datetime import datetime as dt
from dateutil import tz

# METHOD 1: Hardcode zones:
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Asia/Hong_Kong')

# utc = datetime.utcnow()
utc = dt.strptime('2011-01-21 02:37:21', '%Y-%m-%d %H:%M:%S')

# Tell the datetime object that it's in UTC time zone since 
# datetime objects are 'naive' by default
utc = utc.replace(tzinfo=from_zone)

# Convert time zone
central = utc.astimezone(to_zone)



################################################################################
################################################################################
####################################3data masking###############################
################################################################################
################################################################################

import pandas as pd
import numpy as np
import random

data=pd.DataFrame({'name_eng':['chan siu ming','chan tai ming','wong tai sin','wong lei man','au yuen kwan ho'],
                   'name_chi':['陳小明','陳大明','黃大仙','黃利民','歐陽君好'],
                   'email':['chansiuming@gmail.com','abc@gmail.com','oop@gmail.com','pol@gmail.com','qwe@gmail.com'],
                   'address':['12/F, AIA Tower','Room 1201, 12/f, AIA Tower','香港北角電器道183號 13樓','香港北角電器道183號 19樓','香港北角電器道183號 13樓']})


#shuffle eng name
temp_np=data['name_eng'].str.split(" ",n=10,expand=True).values
all_name=temp_np.flatten()

all_name_distinct_original=[x for x in list(set(all_name)) if x !=None]
all_name_distinct_new=all_name_distinct_original.copy()
random.shuffle(all_name_distinct_new)

distinct_pair={all_name_distinct_original[i]:all_name_distinct_new[i] for i in range(len(all_name_distinct_original))}
all_name_new=np.vectorize(distinct_pair.get)(temp_np)

temp=[' '.join(i) for i in all_name_new.tolist()]
temp=[i.replace(' None','') for i in temp]
data['name_eng_shuffle']=temp

#create one-one ch to ch mapping
alphabet_string_original=[chr(num) for num in list(range(ord('a'),ord('z')+1))]
alphabet_string=alphabet_string_original.copy()
random.shuffle(alphabet_string)

distinct_pair={alphabet_string_original[i]:alphabet_string[i] for i in range(len(alphabet_string))}

distinct_pair.get('a','p')  #p is replacement if not found

f_temp=lambda din: "".join([distinct_pair.get(x,x) for x in din])

data['name_eng_shuffle_ch']=np.vectorize(f_temp)(data['name_eng_shuffle'].values)
temp=data['email'].str.split('@', n=2,expand=True)[0].values
data['email_ch']=np.vectorize(f_temp)(temp)


#shuffle chi name
temp=data['name_chi'].str.split(" ",n=10,expand = True)
all_name_distinct_original=[x for x in list(set(np.sum(temp.values))) if x != None]
all_name_distinct_new=all_name_distinct_original.copy()
random.shuffle(all_name_distinct_new)

distinct_pair={all_name_distinct_original[i]:all_name_distinct_new[i] for i in range(len(all_name_distinct_original))}
data['name_chi_shuffle']=np.vectorize(f_temp)(data['name_chi'].values)


import re
def address_remove(target_address):
    t_chi='室|房|樓|層'
    target_address=re.sub('(\d+)([\s]*)'+"("+t_chi+")",'',target_address)
    
    t_eng1='|'.join(['Suite','room','ROOM'])
    t_eng2 = '|'.join(["/f","/F"])
    
    temp1=re.sub("("+t_eng1+")"+'([\s]*)(\w*)(,*)'+"|"+"(\d*)"+"([\s]*)"+"("+t_eng2+")(,*)",'',target_address)
    temp1=temp1.strip()
    return temp1

data['address_remove_room_floor']=np.vectorize(address_remove)(data['address'].values)




















#GBM

#https://github.com/h2oai/h2o-3/blob/master/h2o-docs/src/product/tutorials/gbm/gbmTuning.ipynb
import sys
sys.path.append(r'C:\Users\jonathanjames\aws\notebooks\gbm\GBM\dist\h2o-3.24.0.3')
sys.path.append(r'C:\Users\jonathanjames\aws\notebooks\gbm\tabulate\dist\tabulate-0.8.3')
sys.path.append(r'C:\Users\jonathanjames\aws\notebooks\gbm\future\dist\future-0.17.1\src')
#sys.path.append(r'C:\Users\jonathanjames\Desktop\python\six\dist\six-1.12.0')

import h2o
import numpy as np
import math
from h2o.estimators.gbm import H2OGradientBoostingEstimator
from h2o.grid.grid_search import H2OGridSearch

#h2o.cluster().shutdown()
h2o.init(nthreads=-1, strict_version_check=True)

## pick a response for the supervised problem
response = "survived"


### 'path' can point to a local file, hdfs, s3, nfs, Hive, directories, etc.
#df = h2o.import_file(path = "http://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/titanic.csv")
#print (df.dim)
#print (df.head)
#print (df.tail)
#print (df.describe)
### the response variable is an integer, we will turn it into a categorical/factor for binary classification
#df[response] = df[response].asfactor()           
#
### use all other columns (except for the name & the response column ("survived")) as predictors
#predictors = df.columns
#del predictors[1:3]
#print (predictors)
##split data
#train, valid, test = df.split_frame(
#    ratios=[0.6,0.2], 
#    seed=4685, 
#    destination_frames=['train.hex','valid.hex','test.hex'])



import pandas as pd
#h2o.import_file(path = "http://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/titanic.csv")
df=pd.read_csv(r"C:\Users\jonathanjames\aws\notebooks\gbm\titanic.csv")
train= h2o.H2OFrame(df)
train[response] = train[response].asfactor()  
predictors = train.columns
del predictors[1:3]
print (predictors)

test=h2o.H2OFrame(df.loc[:,df.columns!=response])
#test[response] = test[response].asfactor() 

 
valid=h2o.H2OFrame(df)
valid[response] = valid[response].asfactor()  










#We only provide the required parameters, everything else is default
gbm = H2OGradientBoostingEstimator(seed = 0xDECAF,max_depth=4,score_tree_interval = 1)
gbm.train(x=predictors, y=response, training_frame=train)

## Show a detailed model summary
#https://docs.h2o.ai/h2o/latest-stable/h2o-docs/performance-and-prediction.html
a=gbm



train_pred = gbm.predict(train).as_data_frame()
train_pred['actual']=df[response]


train_pred.loc[train_pred['p1']>=0.5182773621503548,'pred_threshold']=1
train_pred=train_pred.fillna(0)

sum(train_pred['actual']==train_pred['pred_threshold'])/train_pred.shape[0]


train_pred_model_perf=gbm.model_performance(train)
train_pred_model_perf.accuracy()

[[0.5182773621503548, 0.9900687547746372]] #first number is thresdhold



print (gbm)
help(gbm.train)
gbm.accuracy()
gbm.confusion_matrix()

perf = gbm.model_performance(train)
perf.accuracy()

## Get the AUC on the validation set
perf = gbm.model_performance(valid)
print (perf.auc())

perf.accuracy()
perf.mse()
perf.confusion_matrix()
perf.plot(type = "roc")

help(perf)

#importancy plot
gbm.varimp_plot()

#get prediction
preds = gbm.predict(test).as_data_frame()






gbm.params



gbm = H2OGradientBoostingEstimator(ntrees=10,seed = 0xDECAF,max_depth=4,score_tree_interval = 1)
gbm.train(x=predictors, y=response, training_frame=train,validation_frame=valid)

#plot scoring history
import pandas as pd
sh = gbm.score_history()
sh = pd.DataFrame(sh)
print(sh.columns)

import matplotlib.pyplot as plt
#%matplotlib inline 
# plot training logloss and auc
sh.plot(x='number_of_trees',y = ['validation_logloss', 'training_logloss'])
sh.plot(x='number_of_trees',y = ['validation_auc', 'training_auc'])

0.997933
#it use last epho to predict
perf = gbm.model_performance(train)
print (perf.auc())








#https://www.oreilly.com/library/view/practical-machine-learning/9781491964590/ch04.html
#check point, model b will continue from a
gbm = H2OGradientBoostingEstimator(model_id='a',ntrees=10,seed = 0xDECAF,max_depth=4,score_tree_interval = 1)
gbm.train(x=predictors, y=response, training_frame=train)

gbm.scoring_history()

gbm2 = H2OGradientBoostingEstimator(model_id='b',checkpoint='a',ntrees=20,seed = 0xDECAF,max_depth=4,score_tree_interval = 1)
gbm2.train(x=predictors, y=response, training_frame=train)

gbm2.scoring_history()


help(gbm.score_history(valid))




















# save the model
model_path = h2o.save_model(gbm,r"C:\Users\jonathanjames\aws\notebooks\gbm\gbm_output1", force=True)
print(model_path)


# load the model
saved_model = h2o.load_model(model_path)





#below is to visualize tree
from IPython.display import Image
import subprocess
import os

gbm_dir=r"C:\Users\jonathanjames\aws\notebooks\gbm"
#download from http://h2o-release.s3.amazonaws.com/h2o/rel-zahradnik/3/index.html
h2o_jar_path= r'C:\Users\jonathanjames\Desktop\python\GBM\h2o-3.30.0.3\h2o.jar'#r'C:\Users\jonathanjames\Desktop\python\GBM\dist\h2o-3.24.0.3.tar'
gbm_model_name='saved_model' #'gbm'
tree_id=3

mojo_full_path = os.path.join(gbm_dir,gbm_model_name+'_mojo.zip')
#download mojo and save as zip file
gbm_cv3 = vars()[gbm_model_name].download_mojo(path=mojo_full_path)#, get_genmodel_jar=True)
print("Model saved to " + gbm_cv3)

#save as gv file (Graphviz Dot File)
gv_file_path = os.path.join(gbm_dir,gbm_model_name+'_'+str(tree_id)+'.gv')
subprocess.call(["java", "-cp", h2o_jar_path, "hex.genmodel.tools.PrintMojo", "--tree",
                 str(tree_id), "-i", mojo_full_path , "-o", gv_file_path ], shell=False)

#copy gv file content to below and get png
https://dreampuf.github.io/GraphvizOnline/


























0.9995883807169346


#remember, cross validation only give you more information
#on differenthold-out data. trained estimates are the same

cv_gbm = H2OGradientBoostingEstimator(nfolds = 4, seed = 0xDECAF)
cv_gbm.train(x = predictors, y = response, training_frame = train)
perf = cv_gbm.model_performance(valid)
print (perf.auc())

#get prediction
preds1 = cv_gbm.predict(test).as_data_frame()


cv_gbm = H2OGradientBoostingEstimator(seed = 0xDECAF)
cv_gbm.train(x = predictors, y = response, training_frame = train)
perf = cv_gbm.model_performance(valid)
print (perf.auc())

#get prediction
preds2 = cv_gbm.predict(test).as_data_frame()


#The second model is another default GBM, but trained on 80%
# of the data (here, we combine the training and validation splits
# to get more training data), and cross-validated using 4 folds.
# Note that cross-validation takes longer and is not usually done for really large datasets.
## rbind() makes a copy here, so it's better to use split_frame with `ratios = c(0.8)` instead above
cv_gbm = H2OGradientBoostingEstimator(nfolds = 4, seed = 0xDECAF)
cv_gbm.train(x = predictors, y = response, training_frame = train.rbind(valid))

cv_gbm.auc()

perf = cv_gbm.model_performance(train.rbind(valid))
print (perf.auc())




## Show a detailed summary of the cross validation metrics
## This gives you an idea of the variance between the folds
cv_summary = cv_gbm.cross_validation_metrics_summary().as_data_frame()
A=cv_summary ## Full summary of all metrics
print(cv_summary.iloc[4]) ## get the row with just the AUCs

## Get the cross-validated AUC by scoring the combined holdout predictions.
## (Instead of taking the average of the metrics across the folds)
help(cv_gbm.model_performance)
perf_cv = cv_gbm.model_performance(xval=True)
print (perf_cv.auc())

perf_cv = cv_gbm.model_performance(train.rbind(valid))
print (perf_cv.auc())




from IPython.display import Image
import subprocess
import os

gbm_dir=r"C:\Users\jonathanjames\aws\notebooks\gbm"
h2o_jar_path= r'C:\Users\jonathanjames\Desktop\python\GBM\h2o-3.30.0.3\h2o.jar'#r'C:\Users\jonathanjames\Desktop\python\GBM\dist\h2o-3.24.0.3.tar'
gbm_model_name='cv_gbm' #'gbm'
tree_id=3

mojo_full_path = os.path.join(gbm_dir,gbm_model_name+'_mojo.zip')
#download mojo and save as zip file
gbm_cv3 = vars()[gbm_model_name].download_mojo(path=mojo_full_path)#, get_genmodel_jar=True)
print("Model saved to " + gbm_cv3)

#save as gv file (Graphviz Dot File)
gv_file_path = os.path.join(gbm_dir,gbm_model_name+'_'+str(tree_id)+'.gv')
subprocess.call(["java", "-cp", h2o_jar_path, "hex.genmodel.tools.PrintMojo", "--tree",
                 str(tree_id), "-i", mojo_full_path , "-o", gv_file_path ], shell=False)












import os
path = '/home/jonathanjames/my_storage/360files'
#we shall store all the file names in this list
filelist = []
subfolders = [ f.path for f in os.scandir(path) if f.is_dir() ]
subfolders
x=['"'+x.split('/')[-1]+'"' for x in subfolders]
' '.join(x)





#no of tree ntrees default 50

#max_depth default: 5
    

#col_sample_rate_per_tree, initial portion of columns to form the tree at beginning
it is multiplicative with col_sample_rate, so setting both parameters to 0.8,
for example, results in 64% of columns being considered at any given node to split.
Note that this method is sample without replacement.   
#col_sample_rate, portion of columns in later split
    
 
    

#https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/gbm-faq/splitting.html
#min_split_improvement
This option specifies the minimum relative improvement 
in squared error reduction in order for a split to occur
min_split_improvement turned ON by default (0.00001)

#When does the algo stop splitting on an internal node?
when there are no more splits that satisfy the minimum rows parameter,
 if it reaches max_depth, or if there are no splits that satisfy the min_split_improvement parameter.    
    
#How does the minimum rows parameter work?
min_rows specifies the minimum number of observations for a leaf. 
If a user specifies min_rows = 500, and they still have 500 TRUEs and 400 FALSEs,
 we won’t split because we need 500 on both sides. 
 The default for min_rows is 10, so this option rarely affects the GBM splits 
 because GBMs are typically shallow, but the concept still applies.
    

#How does GBM decide which feature to split on?
It splits on the column and level that results in the greatest reduction in 
residual sum of the squares (RSS) in the subtree at that point. It considers all 
fields available from the algorithm.


#bin in historgram
In a histogram, the total range of data set (i.e from minimum value to maximum value) 
is divided into 8 to 15 equal parts. These equal parts are known as bins or class intervals.



#bins, default is 20
#nbins_cats for categoricals, 

#nbins_top_level
is the number of bins to use at the top of each tree. 
It then divides by 2 at each ensuing level to find a new number.
This option defaults to 1024 and is used with nbins, which controls when the algorithm stops dividing by 2.

To make a model more general, decrease nbins_top_level and nbins_cats.
To make a model more specific, increase nbins and/or nbins_top_level and 
nbins_cats. Keep in mind that increasing nbins_cats can lead to in overfitting on the training set.












#Next, we train a GBM with "I feel lucky" parameters. 
#We'll use early stopping to automatically tune the 
#number of trees using the validation AUC.
gbm_lucky = H2OGradientBoostingEstimator(
  ## more trees is better if the learning rate is small enough 
  ## here, use "more than enough" trees - we have early stopping
  ntrees = 10000,                                                            

  ## smaller learning rate is better (this is a good value for most datasets, but see below for annealing)
  learn_rate = 0.01,                                                         

  ## early stopping once the validation AUC doesn't improve by at least 0.01% for 5 consecutive scoring events
  stopping_rounds = 5, stopping_tolerance = 1e-4, stopping_metric = "AUC", 

  ## sample 80% of rows per tree
  sample_rate = 0.8,                                                       

  ## sample 80% of columns per split
  col_sample_rate = 0.8,                                                   

  ## fix a random number generator seed for reproducibility
  seed = 4685,                                                             

  ## score every 10 trees to make early stopping reproducible (it depends on the scoring interval)
  score_tree_interval = 10)

gbm_lucky.train(x=predictors, y=response, training_frame=train, validation_frame=valid)

perf_lucky = gbm_lucky.model_performance(valid)
print (perf_lucky.auc())


#Hyper-Parameter Search
#Next, we'll do real hyper-parameter optimization to see if we can beat the best AUC so far (around 94%).


## Depth 10 is usually plenty of depth for most datasets, but you never know
hyper_params = {'max_depth' : [1,3,5,11,12,13,14,20]}
                #'ntrees': [200,400,600,800,1000]}
#hyper_params = {max_depth = [4,6,8,12,16,20]} ##faster for larger datasets

#Build initial GBM Model
gbm_grid = H2OGradientBoostingEstimator(
        ## more trees is better if the learning rate is small enough 
        ## here, use "more than enough" trees - we have early stopping
        ntrees=10000,
        ## smaller learning rate is better
        ## since we have learning_rate_annealing, we can afford to start with a 
        #bigger learning rate
        learn_rate=0.05,
        ## learning rate annealing: learning_rate shrinks by 1% after every tree 
        ## (use 1.00 to disable, but then lower the learning_rate)
        learn_rate_annealing = 0.99,
        ## sample 80% of rows per tree
        sample_rate = 0.8,
        ## sample 80% of columns per split
        col_sample_rate = 0.8,
        ## fix a random number generator seed for reproducibility
        seed = 4685,
        ## score every 10 trees to make early stopping reproducible 
        #(it depends on the scoring interval)
        score_tree_interval = 10, 
        ## early stopping once the validation AUC doesn't improve by at least 0.01% for 
        #5 consecutive scoring events
        stopping_rounds = 5,
        stopping_metric = "AUC",
        stopping_tolerance = 1e-4)

#Build grid search with previously made GBM and hyper parameters
grid = H2OGridSearch(gbm_grid,hyper_params,
                         grid_id = 'depth_grid',
                         search_criteria = {'strategy': "Cartesian"})
#Train grid search
grid.train(x=predictors, 
           y=response,
           training_frame = train,
           validation_frame = valid)






## by default, display the grid search results sorted by increasing logloss (since this is a classification task)
print (grid)
## sort the grid models by decreasing AUC or below metric
#logloss","residual_deviance"``, ``"mse"``, ``"auc"``, ``"r2"``, ``"accuracy"``, ``"precision"``, ``"recall"`

sorted_grid = grid.get_grid(sort_by='auc',decreasing=True)
print(sorted_grid)


m1 = h2o.get_model(sorted_grid.sorted_metric_table()['model_ids'][0])
m1.model_performance(valid).auc()  #so grid auc is on validation data



sorted_grid = grid.get_grid(sort_by='accuracy',decreasing=True)
print(sorted_grid)



help(grid.get_grid)

#It appears that max_depth values of 9 to 27 are best suited for this dataset, which is unusally deep!

#In [13]:
max_depths = sorted_grid.sorted_metric_table()['max_depth'][0:5]
new_max = int(max(max_depths, key=int))
new_min = int(min(max_depths, key=int))

print ("MaxDepth", new_max)
print ("MinDepth", new_min)

new_min=2
new_max=5


#Now that we know a good range for max_depth, we can tune all other parameters
# in more detail. Since we don't know what combinations of hyper-parameters 
#will result in the best model, we'll use random hyper-parameter search to 
#"let the machine get luckier than a best guess of any human".









#GBM grid search

#https://github.com/h2oai/h2o-3/blob/master/h2o-docs/src/product/tutorials/gbm/gbmTuning.ipynb
import sys
sys.path.append(r'C:\Users\jonathanjames\aws\notebooks\gbm\GBM\dist\h2o-3.24.0.3')
sys.path.append(r'C:\Users\jonathanjames\aws\notebooks\gbm\tabulate\dist\tabulate-0.8.3')
sys.path.append(r'C:\Users\jonathanjames\aws\notebooks\gbm\future\dist\future-0.17.1\src')
#sys.path.append(r'C:\Users\jonathanjames\Desktop\python\six\dist\six-1.12.0')

import h2o
import numpy as np
import math
from h2o.estimators.gbm import H2OGradientBoostingEstimator
from h2o.grid.grid_search import H2OGridSearch

h2o.cluster().shutdown()
h2o.init(nthreads=-1, strict_version_check=True)
## pick a response for the supervised problem
response = "survived"
import pandas as pd
#h2o.import_file(path = "http://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/titanic.csv")
df=pd.read_csv(r"C:\Users\jonathanjames\aws\notebooks\gbm\titanic.csv")
train= h2o.H2OFrame(df)
train[response] = train[response].asfactor()  
predictors = train.columns
del predictors[1:3]
print (predictors)
test=h2o.H2OFrame(df.loc[:,df.columns!=response])
#test[response] = test[response].asfactor() 
valid=h2o.H2OFrame(df)
valid[response] = valid[response].asfactor() 







# create hyperameter and search criteria lists (ranges are inclusive..exclusive))
hyper_params_tune = {'max_depth' : list(range(5,16,7))
                     #'sample_rate': [x/100. for x in range(20,101)],
                     #'col_sample_rate' : [x/100. for x in range(20,101)],
                     #'col_sample_rate_per_tree': [x/100. for x in range(20,101)],
                     #'col_sample_rate_change_per_level': [x/100. for x in range(90,111)],
                     #'min_rows': [2**x for x in range(0,int(math.log(train.nrow,2)-1)+1)],
                     #'nbins': [2**x for x in range(4,11)],
                     #'nbins_cats': [2**x for x in range(4,13)],
                     #'min_split_improvement': [0,1e-8,1e-6,1e-4],
                     #'histogram_type': ["UniformAdaptive","QuantilesGlobal","RoundRobin"]
                     }
search_criteria_tune = {'strategy': "RandomDiscrete",
                   'max_runtime_secs': 3600,  ## limit the runtime to 60 minutes
                   'max_models': 100,  ## build no more than 100 models
                   'seed' : 4685,
                   'stopping_rounds' : 5,
                   'stopping_metric' : "AUC",
                   'stopping_tolerance': 1e-3
                   }
#In [15]:
gbm_final_grid = H2OGradientBoostingEstimator(distribution='bernoulli',
                    ## more trees is better if the learning rate is small enough 
                    ## here, use "more than enough" trees - we have early stopping
                    ntrees=10000,
                    ## smaller learning rate is better
                    ## since we have learning_rate_annealing, we can afford to start with a 
                    #bigger learning rate
                    learn_rate=0.05,
                    ## learning rate annealing: learning_rate shrinks by 1% after every tree 
                    ## (use 1.00 to disable, but then lower the learning_rate)
                    learn_rate_annealing = 0.99,
                    ## score every 10 trees to make early stopping reproducible 
                    #(it depends on the scoring interval)
                    score_tree_interval = 10,
                    ## fix a random number generator seed for reproducibility
                    seed = 4685,
                    ## early stopping once the validation AUC doesn't improve by at least 0.01% for 
                    #5 consecutive scoring events
                    stopping_rounds = 5,
                    stopping_metric = "AUC",
                    stopping_tolerance = 1e-4)
            
#Build grid search with previously made GBM and hyper parameters
final_grid = H2OGridSearch(gbm_final_grid, hyper_params = hyper_params_tune,
                                    grid_id = 'final_grid',
                                    search_criteria = search_criteria_tune)
                                    
                                    
                                    
help(H2OGridSearch)
#Train grid search
final_grid.train(x=predictors,#nfolds=1,
           y=response,
           ## early stopping based on timeout (no model should take more than 1 hour - modify as needed)
           max_runtime_secs = 3600, 
           training_frame = train,#train,
           validation_frame = valid
           )

print (final_grid)



0          12  final_grid_model_2  0.025229576546583022  #this logloss is on validation data
1           5  final_grid_model_1  0.034057970495574165


#even now use 6 fold, 0.02522 also in output, so 6 fold must include one fold valid, 5 folds in train
final_grid.train(x=predictors,nfolds=6,
           y=response,
           ## early stopping based on timeout (no model should take more than 1 hour - modify as needed)
           max_runtime_secs = 3600, 
           training_frame = train,#train,
           validation_frame = valid
           )

print (final_grid)
















dir(final_grid)

a=final_grid.get_grid()
a1=final_grid.model_performance()

a1=final_grid.sorted_metric_table()
a1=final_grid.summary()

a1=final_grid.get_grid()







#python may be condused, so need to close and reopen cluster
#h2o.cluster().shutdown()

## Sort the grid models by AUC
sorted_final_grid = final_grid.get_grid(sort_by='auc',decreasing=True)

print (sorted_final_grid)



#look at what is in sorted_final_grid
dir(sorted_final_grid)

a=sorted_final_grid.sorted_metric_table()


#Let's see how well the best model of the grid search 
#(as judged by validation set AUC) does on the held out test set:


#Get the best model from the list (the model name listed at the top of the table)
best_model = h2o.get_model(sorted_final_grid.sorted_metric_table()['model_ids'][0])
performance_best_model = best_model.model_performance(test)
print (performance_best_model.auc())




#plot scoring history
import pandas as pd
sh =best_model.score_history()
sh = pd.DataFrame(sh)
print(sh.columns)

import matplotlib.pyplot as plt
#%matplotlib inline 
# plot training logloss and auc
sh.plot(x='number_of_trees',y = ['training_auc','validation_auc'])

sh.plot(x='number_of_trees',y = ['training_logloss','validation_logloss'])







#We can inspect the winning model's parameters:


params_list = []
for key, value in best_model.params.items():
    params_list.append(str(key)+" = "+str(value['actual']))
params_list



#Keeping the same "best" model, we can make test set predictions as follows:

#In [23]:
preds = best_model.predict(test).as_data_frame()


best_model.model_performance(valid)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# write-html.py

f = open(r'C:\Users\jonathanjames\aws\notebooks\index_analysis\mis\helloworld.html','w')

message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()
    






from sqlalchemy import create_engine
import configparser
import re
#import MySQLdb as mdb
import pandas as pd
import numpy as np
import pymysql

connection=create_engine("mysql+pymysql://jonathan:46855678@localhost:3306/test1")

x=pd.DataFrame(np.array([[1,2],[3,4]]),columns=['a','b'])

x.to_sql('try9',connection,if_exists='replace',chunksize=1000,index=False)




import numpy as np
initialInvestment   = -100; # Negative, since it results in an outflow of cash

cashFlows           = [-49800,-49800,-49800,-49800,-49800, 0,0,0,0,300000];

# Calculate the IRR
irr = round(np.irr(cashFlows),4);
    




https://kknews.cc/zh-hk/code/qbklego.html
Numba是python的即時編譯器，也就是說，每當您調用python函數時，您的全部或部分代碼都將轉換為機器代碼「即時」執行，然後它將在您的本機代碼速度上運行
加快所有的計算重點和計算繁重的python函數(如循環)。它還支持numpy庫
為什麼選擇Numba？
當有很多其他編譯器時，比如cython，或者pypy，或者任何類似的編譯器。
原因很簡單，在這裏您不必離開使用python編寫代碼的舒適區。你根本不需要改變你的代碼來實現基本的加速
numba使用LLVM compiler infrastructure從純python代碼生成優化的機器碼。使用numba運行的代碼速度與使用C、c++或Fortran的類似代碼的速度相當







http://zhaoxuhui.top/blog/2019/01/17/PythonNumba.html
Numba, a Python compiler from Anaconda that can compile Python code for execution on CUDA-capable GPUs, 
provides Python developers with an easy entry into GPU-accelerated computing and a path for using 
increasingly sophisticated CUDA code with a minimum of new syntax and jargon. 

With Numba, it is now possible to write standard Python functions and run them on a CUDA-capable GPU. 
Numba is designed for array-oriented computing tasks, much like the widely used NumPy library. 
The data parallelism in array-oriented computing tasks is a natural fit for accelerators like GPUs.



nopython模式会完全编译这个被修饰的函数，函数的运行与Python解释器完全无关，不会调用Python的C语言API。如果想获得最佳性能
推荐使用此种模式。同时由于@jit(nopython=True)太常用了，Numba提供了@njit修饰符，


# coding=utf-8
from numba import jit
from numpy import arange


@jit(nopython=True)
def sum2d(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i, j]
    return result


a = arange(9).reshape(3, 3)
def try1():
    for i in range(100):
        sum2d(a)

%timeit -n100 -r10 try1()


Numba对于jit也提供了参数，叫做function signature
@jit(float64(int32, int32))
def f(x, y):
    # A somewhat trivial example
    return (x + y) / 3.14
float64表示输出数据类型，int32表示输入数据类型。如果嫌太麻烦还可以简写成@jit(f8(i4,i4))


Numba在第一次运行你写的代码时会即时编译，编译会消耗一定的时间。编译好之后Numba会将机器码先缓存起来，
第二次再调用的时候就不会再编译而是直接运行了。这与Numba的运行原理有关


from numba import jit
import numpy as np
import time

x = np.arange(100).reshape(10, 10)


@jit(nopython=True)
#@jit(parallel=True)
def go_fast(a):  # Function is compiled and runs in machine code
    trace = 0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace


# DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!
start = time.time()
go_fast(x)
end = time.time()
print("Elapsed (with compilation) = %s" % (end - start))

# NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
start = time.time()
go_fast(x)
end = time.time()
print("Elapsed (after compilation) = %s" % (end - start))

#A universal function (or ufunc for short) is a function that operates on NumPy arrays (ndarrays) in 
an element-by-element fashion. 
type(np.sin)










#https://zhuanlan.zhihu.com/p/72789048
已经提到计算机只能执行二进制的机器码，C、C++等编译型语言依靠编译器将源代码转化为可执行文件后才能运行，Python
Java等解释型语言使用解释器将源代码翻译后在虚拟机上执行。对于Python，由于解释器的存在，其执行效率比C语言慢几倍甚至几十倍。
C语言经过几十年的发展，优化已经达到了极致。以C语言为基准，大多数解释语言，如Python、R会慢十倍甚至一
百倍。Julia这个解释语言是个“奇葩”，因为它采用了JIT编译技术。

reason why python slow
1)python source code --> bytecode complier to virtual machine

jit complier direclty to mahcine code
Just-In-Time（JIT）技术为解释语言提供了一种优化，它能克服上述效率问题
，极大提升代码执行速度，同时保留Python语言的易用性。使用JIT技术时，JIT编译器将Python源代码编译
成机器直接可以执行的机器语言，并可以直接在CPU等硬件上运行。这样就跳过了原来的虚拟机，执行速度几乎与用C语言编程速度并无二致。

Numba真正牛逼之处在于其nopython模式。将装饰器改为@jit(nopython=True)或者@njit，Numba会假设你已经
对所加速的函数非常了解，强制使用加速的方式，不会进入object模式

Numba使用了LLVM和NVVM技术，这个技术可以将Python、Julia这样的解释语言直接翻译成CPU或GPU可执行的机器码。




above is numba in CPU. 





#numba in GPU
https://devblogs.nvidia.com/numba-python-cuda-acceleration/
import numpy as np
from numba import vectorize
import numpy as np

@vectorize(['float32(float32, float32)'], target='cuda')
def Add(a, b):
  return a + b

# Initialize arrays
N = 100000
A = np.ones(N, dtype=np.float32)
B = np.ones(A.shape, dtype=A.dtype)
C = np.empty_like(A, dtype=A.dtype)

# Add arrays on GPU
C = Add(A, B)



dx=2000
dy=500000
x=np.random.uniform(0,1,(dx,dy))



import tensorflow as tf
x=tf.random.uniform((dx,dy), minval=0, maxval=None, dtype=tf.dtypes.float32)



#GPU-Accelerated Libraries for Python
import numpy as np
from pyculib import rand as curand

prng = curand.PRNG(rndtype=curand.PRNG.XORWOW)
rand = np.empty(100000)
prng.uniform(rand)
print rand[:10]











import time
from numba import cuda
@cuda.jit(device=True)
def mandel(x, y, max_iters):
  """
  Given the real and imaginary parts of a complex number,
  determine if it is a candidate for membership in the Mandelbrot
  set given a fixed number of iterations.
  """
  c = complex(x, y)
  z = 0.0j
  for i in range(max_iters):
    z = z*z + c
    if (z.real*z.real + z.imag*z.imag) >= 4:
      return i

  return max_iters

@cuda.jit
def mandel_kernel(min_x, max_x, min_y, max_y, image, iters):
  height = image.shape[0]
  width = image.shape[1]

  pixel_size_x = (max_x - min_x) / width
  pixel_size_y = (max_y - min_y) / height

  startX = cuda.blockDim.x * cuda.blockIdx.x + cuda.threadIdx.x
  startY = cuda.blockDim.y * cuda.blockIdx.y + cuda.threadIdx.y
  gridX = cuda.gridDim.x * cuda.blockDim.x;
  gridY = cuda.gridDim.y * cuda.blockDim.y;

  for x in range(startX, width, gridX):
    real = min_x + x * pixel_size_x
    for y in range(startY, height, gridY):
      imag = min_y + y * pixel_size_y 
      image[y, x] = mandel(real, imag, iters)

gimage = np.zeros((1024, 1536), dtype = np.uint8)
blockdim = (32, 8)
griddim = (32,16)

start = time.time()
d_image = cuda.to_device(gimage)
mandel_kernel[griddim, blockdim](-2.0, 1.0, -1.0, 1.0, d_image, 20) 
d_image.to_host()
dt =time.time() - start

print ("Mandelbrot created on GPU in %f s" % dt)

imshow(gimage)








if numba in GPU, need to use cuda inside numba like below

but remember cuda is another concept
初始化，并将必要的数据拷贝到GPU设备的显存上。
CPU调用GPU函数，启动GPU多个核心同时进行计算。
CPU与GPU异步计算。
将GPU计算结果拷贝回主机端，得到计算结果。


https://zhuanlan.zhihu.com/p/77307505




from numba import cuda
print(cuda.gpus)

def cpu_print():
    print("print by cpu.")

@cuda.jit
def gpu_print():
    # GPU核函数
    print("print by gpu.")

def main():
    gpu_print[1, 2]()
    cuda.synchronize()
    cpu_print()

if __name__ == "__main__":
    main()




from numba import cuda

def cpu_print(N):
    for i in range(0, N):
        print(i)

@cuda.jit
def gpu_print(N):
    idx = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x 
    if (idx < N):
        print(idx)

def main():
    print("gpu print:")
    gpu_print[2, 4](8)
    cuda.synchronize()
    print("cpu print:")
    cpu_print(8)

if __name__ == "__main__":
    main()






from numba import cuda
import numpy as np
import math
from time import time

@cuda.jit
def gpu_add(a, b, result, n):
    idx = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x   #this is for index only so that can locate every index
    if idx < n:
        result[idx] = a[idx] + b[idx]

def main():
    n = 200000
    x = np.arange(n).astype(np.int32)
    y = 2 * x

    gpu_result = np.zeros(n)
    cpu_result = np.zeros(n)

    threads_per_block = 1024
    blocks_per_grid = math.ceil(n / threads_per_block)
    start = time()
    gpu_add[blocks_per_grid, threads_per_block](x, y, gpu_result, n)   #output is in gpu_result
    cuda.synchronize()
    print("gpu vector add time " + str(time() - start))
    start = time()
    cpu_result = np.add(x, y)
    print("cpu vector add time " + str(time() - start))

    if (np.array_equal(cpu_result, gpu_result)):
        print("result correct")

if __name__ == "__main__":
    main()


运行结果，GPU代码竟然比CPU代码慢10+倍！

说好的GPU比CPU快几十倍上百倍呢？这里GPU比CPU慢很多原因主要在于：

向量加法的这个计算比较简单，CPU的numpy已经优化到了极致，无法突出GPU的优势，我们要解决实际问题往往比这个复杂得多，当解决复杂问题时，优化后的GPU代码将远快于CPU代码。

这份代码使用CUDA默认的统一内存管理机制，没有对数据的拷贝做优化。CUDA的统一内存系统是当GPU运行到某块数据发现不在设备端时，再去主机端中将数据拷贝过来，当执行完核函数后
，又将所有的内存拷贝回主存。在上面的代码中，输入的两个向量是只读的，没必要再拷贝回主存。

这份代码没有做流水线优化。CUDA并非同时计算2千万个数据，一般分批流水线工作：一边对2000万中的某批数据进行计算，一边将下一批数据从
主存拷贝过来。计算占用的是CUDA核心，数据拷贝占用的是总线，所需资源不同，互相不存在竞争关系。这种机制被称为流水线。这部分内容将在下篇文章中讨论。


from numba import cuda
import numpy as np
import math
from time import time

@cuda.jit
def gpu_add(a, b, result, n):
    idx = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x
    if idx < n :
        result[idx] = a[idx] + b[idx]

def main():
    n = 20000000
    x = np.arange(n).astype(np.int32)
    y = 2 * x

    # 拷贝数据到设备端
    x_device = cuda.to_device(x)
    y_device = cuda.to_device(y)
    # 在显卡设备上初始化一块用于存放GPU计算结果的空间
    gpu_result = cuda.device_array(n)
    cpu_result = np.empty(n)

    threads_per_block = 1024
    blocks_per_grid = math.ceil(n / threads_per_block)
    start = time()
    gpu_add[blocks_per_grid, threads_per_block](x_device, y_device, gpu_result, n)
    cuda.synchronize()
    print("gpu vector add time " + str(time() - start))
    start = time()
    cpu_result = np.add(x, y)
    print("cpu vector add time " + str(time() - start))

    if (np.array_equal(cpu_result, gpu_result.copy_to_host())):
        print("result correct!")

if __name__ == "__main__":
    main()








#https://zhuanlan.zhihu.com/p/78557104
在上一篇文章中，我曾提到，CUDA的执行配置：[gridDim, blockDim]中的blockDim最大只能是1024，
但是并没提到gridDim的最大限制。英伟达给出的官方回复是gridDim最大为一个32位整数的最大值，也就是2,147,483,648，大约二十亿。


from numba import cuda

@cuda.jit
def gpu_print(N):
    idxWithinGrid = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x 
    gridStride = cuda.gridDim.x * cuda.blockDim.x
    # 从 idxWithinGrid 开始
    # 每次以整个网格线程总数为跨步数
    x=[0]*100
    for i in range(idxWithinGrid, N, gridStride):
        x[i]=i
        print(i)

def main():
    gpu_print[2, 4](32)
    cuda.synchronize()

if __name__ == "__main__":
    main()



for i in range(1,5,2):
    print(i)


from numba import cuda
import numpy as np
import math
from time import time

@cuda.jit
def gpu_add(a, b, result, n):
    idx = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x
    if idx < n :
        result[idx] = a[idx] + b[idx]

def main():
    n = 20000000
    x = np.arange(n).astype(np.int32)
    y = 2 * x

    start = time()
    x_device = cuda.to_device(x)
    y_device = cuda.to_device(y)
    out_device = cuda.device_array(n)

    threads_per_block = 1024
    blocks_per_grid = math.ceil(n / threads_per_block)

    # 使用默认流
    gpu_add[blocks_per_grid, threads_per_block](x_device, y_device, out_device, n)
    gpu_result = out_device.copy_to_host()
    cuda.synchronize()
    print("gpu vector add time " + str(time() - start))

    start = time()

    # 使用5个stream
    number_of_streams = 5
    # 每个stream处理的数据量为原来的 1/5
    # 符号//得到一个整数结果
    segment_size = n // number_of_streams

    # 创建5个cuda stream
    stream_list = list()
    for i in range (0, number_of_streams):
        stream = cuda.stream()
        stream_list.append(stream)

    threads_per_block = 1024
    # 每个stream的处理的数据变为原来的1/5
    blocks_per_grid = math.ceil(segment_size / threads_per_block)
    streams_out_device = cuda.device_array(segment_size)
    streams_gpu_result = np.empty(n)

    # 启动多个stream
    for i in range(0, number_of_streams):
        # 传入不同的参数，让函数在不同的流执行
        x_i_device = cuda.to_device(x[i * segment_size : (i + 1) * segment_size], stream=stream_list[i])
        y_i_device = cuda.to_device(y[i * segment_size : (i + 1) * segment_size], stream=stream_list[i])

        gpu_add[blocks_per_grid, threads_per_block, stream_list[i]](
                x_i_device, 
                y_i_device, 
                streams_out_device,
                segment_size)

        streams_gpu_result[i * segment_size : (i + 1) * segment_size] = streams_out_device.copy_to_host(stream=stream_list[i])

    cuda.synchronize()
    print("gpu streams vector add time " + str(time() - start))

if __name__ == "__main__":
    main()




from numba import cuda
import numpy as np
import math
from time import time

@cuda.jit
def matmul(A, B, C):
    """  矩阵乘法 C = A * B
    """
    # Numba库提供了更简易的计算方法
    # x, y = cuda.grid(2)
    # 具体计算公式如下
    row = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x
    col = cuda.threadIdx.y + cuda.blockDim.y * cuda.blockIdx.y


    if row < C.shape[0] and col < C.shape[1]:
        tmp = 0.
        for k in range(A.shape[1]):
            tmp += A[row, k] * B[k, col]
        C[row, col] = tmp

def main():
    # 初始化矩阵
    M = 6000
    N = 4800
    P = 4000
    A = np.random.random((M, N)) # 随机生成的 [M x N] 矩阵
    B = np.random.random((N, P)) # 随机生成的 [N x P] 矩阵

    start = time()
    A = cuda.to_device(A)
    B = cuda.to_device(B)
    C_gpu = cuda.device_array((M, P))

    # 执行配置
    threads_per_block = (16, 16)
    blocks_per_grid_x = int(math.ceil(A.shape[0] / threads_per_block[0]))
    blocks_per_grid_y = int(math.ceil(B.shape[1] / threads_per_block[1]))
    blocksPerGrid = (blocks_per_grid_x, blocks_per_grid_y)

    # 启动核函数
    matmul[blocksPerGrid, threads_per_block](A, B, C_gpu)

    # 数据拷贝
    C = C_gpu.copy_to_host()
    cuda.synchronize()

    print("gpu matmul time :" + str(time() - start))

    start = time()
    C_cpu = np.empty((M, P), np.float)
    np.matmul(A, B, C_cpu)
    print("cpu matmul time :" + str(time() - start))

    # 验证正确性
    if np.allclose(C_cpu, C):
        print("gpu result correct")

if __name__ == "__main__":
    main()





from numba import cuda, float32
import numpy as np
import math
from time import time

# thread per block
# 每个block有 BLOCK_SIZE x BLOCK_SIZE 个元素
BLOCK_SIZE = 16

@cuda.jit
def matmul(A, B, C):
    """  矩阵乘法 C = A * B
    """
    row = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x
    col = cuda.threadIdx.y + cuda.blockDim.y * cuda.blockIdx.y

    if row < C.shape[0] and col < C.shape[1]:
        tmp = 0.
        for k in range(A.shape[1]):
            tmp += A[row, k] * B[k, col]
        C[row, col] = tmp

@cuda.jit
def matmul_shared_memory(A, B, C):
    """
    使用Shared Memory的矩阵乘法 C = A * B
    """
    # 在Shared Memory中定义向量
    # 向量可被整个Block的所有Thread共享
    # 必须声明向量大小和数据类型
    sA = cuda.shared.array(shape=(BLOCK_SIZE, BLOCK_SIZE), dtype=float32)
    sB = cuda.shared.array(shape=(BLOCK_SIZE, BLOCK_SIZE), dtype=float32)

    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    row = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x
    col = cuda.threadIdx.y + cuda.blockDim.y * cuda.blockIdx.y

    if row >= C.shape[0] and col >= C.shape[1]:
        # 当(x, y)越界时退出
        return

    tmp = 0.
    # 以一个 BLOCK_SIZE x BLOCK_SIZE 为单位
    for m in range(math.ceil(A.shape[1] / BLOCK_SIZE)):
        sA[tx, ty] = A[row, ty + m * BLOCK_SIZE]
        sB[tx, ty] = B[tx + m * BLOCK_SIZE, col]
        # 线程同步，等待Block中所有Thread预加载结束
        # 该函数会等待所有Thread执行完之后才执行下一步
        cuda.syncthreads()
        # 此时已经将A和B的子矩阵拷贝到了sA和sB

        # 计算Shared Memory中的向量点积
        # 直接从Shard Memory中读取数据的延迟很低
        for n in range(BLOCK_SIZE):
            tmp += sA[tx, n] * sB[n, ty]

        # 线程同步，等待Block中所有Thread计算结束
        cuda.syncthreads()

    # 循环后得到每个BLOCK的点积之和
    C[row, col] = tmp

def main():
    # 初始化矩阵
    M = 6000
    N = 4800
    P = 4000
    A = np.random.random((M, N)) # 随机生成的 [M x N] 矩阵
    B = np.random.random((N, P)) # 随机生成的 [N x P] 矩阵

    A_device = cuda.to_device(A)
    B_device = cuda.to_device(B)
    C_device = cuda.device_array((M, P)) # [M x P] 矩阵

    # 执行配置
    threads_per_block = (BLOCK_SIZE, BLOCK_SIZE)
    blocks_per_grid_x = int(math.ceil(A.shape[0] / BLOCK_SIZE))
    blocks_per_grid_y = int(math.ceil(B.shape[1] / BLOCK_SIZE))
    blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)

    start = time()
    matmul[blocks_per_grid, threads_per_block](A_device, B_device, C_device)
    cuda.synchronize()
    print("matmul time :" + str(time() - start))

    start = time()
    matmul_shared_memory[blocks_per_grid, threads_per_block](A_device, B_device, C_device)
    cuda.synchronize()
    print("matmul with shared memory time :" + str(time() - start))
    C = C_device.copy_to_host()

if __name__ == "__main__":
    main()























https://blog.csdn.net/huyaoyu/article/details/89742577
numba可以在没有CUDA支持时使用CPU进行加速，而这里我只感兴趣CUDA的部分。
@cuda.jit(device=True)   #device means using GPU


#https://stackoverflow.com/questions/23119413/how-do-i-install-python-opencv-through-conda
#anaconda install opencv
conda install --channel https://conda.anaconda.org/menpo opencv3
    


from __future__ import print_function

import cv2
import math
import matplotlib.pyplot as plt
import numpy as np
from numba import cuda
import time

@cuda.jit(device=True)
def d_radius_validate(cx, cy, R, width, x, y):
    x = x - cx
    y = y - cy

    r = math.sqrt( x * x + y * y )

    if ( r >= R - width and r <= R + width ):
        return 255
    else:
        return 0

@cuda.jit(device=True)
def d_polar_line_segment_validate(cx, cy, theta, length, width, x, y):
    n0 = length * math.cos(theta) / length
    n1 = length * math.sin(theta) / length

    v0 = x - cx
    v1 = y - cy

    proj = n0 * v0 + n1 * v1

    if ( proj < 0 ):
        return 0
    elif ( proj > length ):
        return 0
    
    oth0 = v0 - proj*n0
    oth1 = v1 - proj*n1

    d = math.sqrt( oth0 * oth0 + oth1 * oth1 )

    if ( d <= width ):
        return 255
    else:
        return 0

@cuda.jit
def k_validate(imgOut):
    tx = cuda.blockIdx.x*cuda.blockDim.x + cuda.threadIdx.x
    ty = cuda.blockIdx.y*cuda.blockDim.y + cuda.threadIdx.y

    xStride = cuda.blockDim.x * cuda.gridDim.x
    yStride = cuda.blockDim.y * cuda.gridDim.y

    cx, cy = 2056, 1504
    R = 1504*0.75
    halfWidth = 10.0

    for y in range( ty, imgOut.shape[0], yStride ):
        for x in range( tx, imgOut.shape[1], xStride ):
            flag = d_radius_validate( cx, cy, R, halfWidth, 1.0*x, 1.0*y )
            if ( 0 != flag ):
                imgOut[y, x] = flag

            flag = d_polar_line_segment_validate( cx, cy, -math.pi/2, R, halfWidth, 1.0*x, 1.0*y )
            if ( 0 != flag ):
                imgOut[y, x] = flag

            flag = d_polar_line_segment_validate( cx, cy, -math.pi/4, R, halfWidth, 1.0*x, 1.0*y )
            if ( 0 != flag ):
                imgOut[y, x] = flag
            
            flag = d_polar_line_segment_validate( cx-halfWidth, cy, 0.0, R + halfWidth, halfWidth, 1.0*x, 1.0*y )
            if ( 0 != flag ):
                imgOut[y, x] = flag
            
            flag = d_polar_line_segment_validate( cx, cy, math.pi/4, R, halfWidth, 1.0*x, 1.0*y )
            if ( 0 != flag ):
                imgOut[y, x] = flag
            
            flag = d_polar_line_segment_validate( cx, cy, math.pi/2, R, halfWidth, 1.0*x, 1.0*y )
            if ( 0 != flag ):
                imgOut[y, x] = flag

if __name__ == "__main__":
    # Create an image.
    img = np.zeros((3008, 4112), dtype=np.int32)

    # Record the starting time.
    start = time.time()

    dImg = cuda.to_device(img)

    cuda.synchronize()
    k_validate[[100, 100, 1], [16, 16, 1]](dImg)
    cuda.synchronize()

    img = dImg.copy_to_host()

    # Record the ending time.
    end = time.time()

    print(end - start)

    # Save the image.
    cv2.imwrite("ValidPixels_numba.png", img)

    print("Done.")





































import time

#numba
import numpy as np
def happy4(x):
    for i in np.arange(x):
        y=i
%timeit -n100 -r10 happy4(10000)


from numba import jit
@jit
def happy5(x):
    for i in np.arange(x):
        y=i

%timeit -n100 -r10 happy5(10000)  #should be faster using numba
    







from pandas import read_excel
data = read_excel('train.xlsx','Sheet1')

def happy6(x):
    y=x.copy()
    z=y[y['Loan_ID']>3]

@jit
def happy7(x):
    y=x.copy()
    z=y[y['Loan_ID']>3]

%timeit -n100 -r10 happy6(data) 
%timeit -n100 -r10 happy7(data) 








import numpy as np
from timeit import default_timer as timer
from numba import vectorize
 
# This should be a substantially high value. On my test machine, this took
# 33 seconds to run via the CPU and just over 3 seconds on the GPU.
NUM_ELEMENTS = 100000000
 
# This is the CPU version.
def vector_add_cpu(a, b):
  c = np.zeros(NUM_ELEMENTS, dtype=np.float32)
  for i in range(NUM_ELEMENTS):
    c[i] = a[i] + b[i]
  return c
 
# This is the GPU version. Note the @vectorize decorator. This tells
# numba to turn this into a GPU vectorized function.
@vectorize(["float32(float32, float32)"], target='cuda')
def vector_add_gpu(a, b):
  return a + b;
 
def main():
  a_source = np.ones(NUM_ELEMENTS, dtype=np.float32)
  b_source = np.ones(NUM_ELEMENTS, dtype=np.float32)
 
  # Time the CPU function
  start = timer()
  vector_add_cpu(a_source, b_source)
  vector_add_cpu_time = timer() - start
 
  # Time the GPU function
  start = timer()
  vector_add_gpu(a_source, b_source)
  vector_add_gpu_time = timer() - start
 
  # Report times
  print("CPU function took %f seconds." % vector_add_cpu_time)
  print("GPU function took %f seconds." % vector_add_gpu_time)
 
  return 0
 
if __name__ == "__main__":
  main()





#url redirection/redirect
  #https://subscription.packtpub.com/book/networking_and_servers/9781784395414/1/ch01lvl1sec18/tracking-redirection-of-the-request-using-request-history
import requests
r = requests.get('http:google.com')
r.url #u'http://www.google.co.in/?gfe_rd=cr&ei=rgMSVOjiFKnV8ge37YGgCA'
>>> r.status_code
200
>>> r.history


#ROTATING PROXY
from lxml.html import fromstring
import requests
from itertools import cycle
import traceback

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'): #within tbody, there are many tr
        if i.xpath('.//td[7][contains(text(),"yes")]'):  #td7 is yes/no indicator
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)  #in set, only unique element allowed
    return proxies


proxies = get_proxies()

proxy_pool = cycle(proxies)

url = 'https://httpbin.org/ip'
for i in range(1,11):
    #Get a proxy from the pool
    proxy = next(proxy_pool)
    print("Request #%d"%i)
    try:
        response = requests.get(url,proxies={"http": proxy, "https": proxy})
        print(response.json())
    except:
        #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
        #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
        print("Skipping. Connnection error")


x=cycle(['2','5','8','90','3'])

next(x)



import requests
url_use='https://bet.hkjc.com/racing/getJSON.aspx?type=win&date=2019-09-21&venue=ST&raceno=1'
try:
    proxy = next(proxy_pool)
    output=requests.post(url_use, allow_redirects=False,proxies={"http": proxy, "https": proxy},timeout=3).json()
    print("ok ",proxy)
except:
    print(sys.exc_info()[0])

output=requests.post(url_use, allow_redirects=False).json()













#multi process on dataframe apply
data=main_data.loc[(main_data['Date']=='2019-10-20')&(main_data['Horse_Brand']=="i'm the conquist_B155"),:]
def trackwork_swim_extract(data):
    data_index=data.index
    #data=data.reset_index(drop=True)
    target_horse=data['Horse_Brand'].values[0]
    
    target_date=data['Date'].values[0]
    target_date_lag_two=dt.strptime(target_date,'%Y-%m-%d')-timedelta(days=2)
    target_date_lag_two=target_date_lag_two.strftime("%Y-%m-%d")
    
    target_date_lag_14=dt.strptime(target_date,'%Y-%m-%d')-timedelta(days=14)
    target_date_lag_14=target_date_lag_14.strftime("%Y-%m-%d")

    target_date_lag_22=dt.strptime(target_date,'%Y-%m-%d')-timedelta(days=22)
    target_date_lag_22=target_date_lag_22.strftime("%Y-%m-%d")    

    target_date_lag_30=dt.strptime(target_date,'%Y-%m-%d')-timedelta(days=30)
    target_date_lag_30=target_date_lag_30.strftime("%Y-%m-%d") 

    #count_14=count_22=count_30=0
    key_horse=trackwork_swim[:,1]==target_horse
    trackwork_swim_temp=trackwork_swim[key_horse]
    trackwork_swim_use=trackwork_swim_temp[(trackwork_swim_temp[:,0]<=target_date_lag_two)&(trackwork_swim_temp[:,0]>=target_date_lag_14)]
    count_14=np.shape(trackwork_swim_use)[0]

    trackwork_swim_use=trackwork_swim_temp[(trackwork_swim_temp[:,0]<=target_date_lag_two)&(trackwork_swim_temp[:,0]>=target_date_lag_22)]
    count_22=np.shape(trackwork_swim_use)[0]

    trackwork_swim_use=trackwork_swim_temp[(trackwork_swim_temp[:,0]<=target_date_lag_two)&(trackwork_swim_temp[:,0]>=target_date_lag_30)]
    count_30=np.shape(trackwork_swim_use)[0]    
    
    output=pd.DataFrame({'swim_14':[count_14],'swim_22':[count_22],'swim_30':[count_30]},index=data_index)
    return output


    
out=main_data[['Date','Horse_Brand']][0:1000].groupby(['Date','Horse_Brand'],group_keys=False).apply(lambda x:trackwork_swim_extract(x))

i=0
all_out=pd.DataFrame([])
for i in range(0,main_data[0:30].shape[0]):
    out=trackwork_swim_extract(main_data[['Date','Horse_Brand']][i:i+1])
    all_out=all_out.append(out)
    print(i)


from multiprocessing import Pool, cpu_count

def applyParallel(dfGrouped, func):
    with Pool(cpu_count()) as p:
        ret_list = p.map(func, [group for name, group in dfGrouped])
    return pd.concat(ret_list)

out=applyParallel(main_data[['Date','Horse_Brand']][0:10000].groupby(['Date','Horse_Brand'],group_keys=False), trackwork_swim_extract)














#below is an example to use dark


#below is an example to use dark

#data_temp=main_data.loc[(main_data['Date']=='2019-09-01')&(main_data['RaceNo']==1),:]
def DNF_UR_FE_TNP_PU_treat_last(data_temp):
    index_out=data_temp.index
    data_temp=data_temp.reset_index(drop=True)
    if data_temp['DNF_UR_FE_TNP_PU_race'].values[0]==1:
        all_fp=list(data_temp.FP.values)
        all_fp_old=all_fp.copy()
        #remove text in all_fp
        for k in all_fp_old:
            if any(x==k for x in ['DNF','UR','FE','TNP','PU','WXNR', 'WV-A', 'WX-A','WV','WX','WR']):#note that till to now no data is WR
                    all_fp.remove(k)
        #convert to integer
        all_fp=[int(x) for x in all_fp]
        fp_max=max(all_fp)
        fp_start=fp_max+1
        #i=0
        for i in range(0,data_temp.shape[0]):
            if data_temp[i:i+1]['FP'].values[0] in DNF_UR_FE_TNP_PU:
                data_temp.loc[i,'FP']=str(fp_start)
                fp_start=fp_start+1
    output=pd.DataFrame({'FP':data_temp['FP'].values},index=index_out)   #output must be a dataframe with name specified in meta
    return output

from dask import dataframe as dd
from dask.multiprocessing import get 
from dask.distributed import Client



#client = Client(n_workers=8, threads_per_worker=8)
client = Client()

ddf = dd.from_pandas(main_data[['Date','RaceNo','FP','DNF_UR_FE_TNP_PU_race']].copy(), npartitions=5)

meta = [("FP", str)]
g=ddf.groupby(['Date','RaceNo'],group_keys=False).apply(lambda x:DNF_UR_FE_TNP_PU_treat_last(x),meta=meta)

out=g.compute()

main_data['FP']=out






#use cuda in python for parallel
#https://weeraman.com/put-that-gpu-to-good-use-with-python-e5a437168c01

#step to install cuda
# ./conda update conda
#./conda install accerate
#./conda install cudatoolkit
#./conda install numba

#without using GPT the time is 31s
import numpy as np
from timeit import default_timer as timer

def pow(a, b, c):
    for i in range(a.size):
         c[i] = a[i] ** b[i]

def main():
    vec_size = 50000000

    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)

    start = timer()
    pow(a, b, c)
    duration = timer() - start

    print(duration)

if __name__ == '__main__':
    main()






#after installing accerate, use below to perform parallel using GPU
import numpy as np
from timeit import default_timer as timer
from numba import vectorize

#@vectorize(['float32(float32, float32)'], target='cuda')
def pow(a, b):
    return a ** b

def main():
    vec_size = 100000000

    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)

    start = timer()
    pow(a, b)
    duration = timer() - start

    print(duration)

if __name__ == '__main__':
    main()









#https://www.geeksforgeeks.org/running-python-script-on-gpu/
from numba import jit, cuda 
import numpy as np 
# to measure exec time 
from timeit import default_timer as timer    


# normal function to run on cpu 
def func(a):                                 
    for i in range(n): 
        b[i]+= 1      
  
# function optimized to run on gpu  
@jit(target ="cuda")                          
def func2(a): 
    for i in range(n): 
        a[i]+= 1
        #print('5')

n=5000000
if __name__=="__main__":                          
    a = np.ones(n, dtype = np.float64) 
    b = np.ones(n, dtype = np.float32) 
      
    start = timer() 
    func(a) 
    print("without GPU:", timer()-start)     
      
    start = timer() 
    func2(a) 
    print("with GPU:", timer()-start) 




import random
from time import sleep


# normal function to run on cpu 
def func(a):                                 
    for i in range(n): 
        b[i]+= 1      
  
# function optimized to run on gpu  
@jit(target ="cuda")                          
def func2(a):
    for i in range(n):
        sleep(random.randint(2,5))
        print(i)

n=20

if __name__=="__main__":                          
    a = np.ones(n, dtype = np.float64) 
    b = np.ones(n, dtype = np.float32) 
      
    start = timer() 
    func(a) 
    print("without GPU:", timer()-start)     
      
    start = timer() 
    func2(a) 
    print("with GPU:", timer()-start) 
















import os
import threading

lock = threading.Lock()

def synchronized_open_file(*args, **kwargs):
    with lock:
        return tb.open_file(*args, **kwargs)

def synchronized_close_file(self, *args, **kwargs):
    with lock:
        return self.close(*args, **kwargs)

import numpy as np
import tables as tb





filename='simple_threading.h5'
path='/array'
inqueue=queue.Queue()
outqueue=queue.Queue()

def run(filename, path, inqueue, outqueue):
    try:
        yslice = inqueue.get()
        h5file = synchronized_open_file(filename, mode='r')
        h5array = h5file.get_node(path)
        data = h5array[yslice, ...]
        psum = np.sum(data)
    except Exception as e:
        outqueue.put(e)
    else:
        outqueue.put(psum)
    finally:
        synchronized_close_file(h5file)

os.chdir('/home/jonathanjames/aws/notebooks/horse/model')

import os
import queue
import threading

import numpy as np
import tables as tb

SIZE = 10
NTHREADS = 5
FILENAME = 'simple_threading.h5'
H5PATH = '/array'

def create_test_file(filename):
    data = np.random.rand(SIZE, SIZE)

    with tb.open_file(filename, 'w') as h5file:
        h5file.create_array('/', 'array', title="Test Array", obj=data)

def chunk_generator(data_size, nchunks):
    chunk_size = int(np.ceil(data_size / nchunks))
    for start in range(0, data_size, chunk_size):
        yield slice(start, start + chunk_size)

def main():
    # generate the test data
    if not os.path.exists(FILENAME):
        create_test_file(FILENAME)

    threads = []
    inqueue = queue.Queue()
    outqueue = queue.Queue()

    # start all threads
    for i in range(NTHREADS):
        thread = threading.Thread(
            target=run, args=(FILENAME, H5PATH, inqueue, outqueue))
        thread.start()
        threads.append(thread)

    # push requests in the input queue
    for yslice in chunk_generator(SIZE, len(threads)):
        inqueue.put(yslice)

    # collect results
    try:
        mean_ = 0.

        for i in range(len(threads)):
            out = outqueue.get()
            if isinstance(out, Exception):
                raise out
            else:
                mean_ += out

        mean_ /= SIZE * SIZE

    finally:
        for thread in threads:
            thread.join()

    # print results
    print('Mean: {}'.format(mean_))

if __name__ == '__main__':
    main()







a=[1, 1, 1, 0, 0, 0, 1, 1, 0, 0]

def island_cumsum_vectorized(a):
    a_ext = np.concatenate(( [0], a, [0] ))
    idx = np.flatnonzero(a_ext[1:] != a_ext[:-1])
    a_ext[1:][idx[1::2]] = idx[::2] - idx[1::2]
    return a_ext.cumsum()[1:-1]



island_cumsum_vectorized(a)












values=[1,2,3,4]

import numpy as np

from math import sqrt

def min_max_scaler(values):
    values_normalized=(values-np.mean(values))/np.std(values)
    return values_normalized



def standardize(values):
    length_values = len(values)
    diffs = [value - min(values) for value in values]
    std = sqrt(sum([diff**2 for diff in diffs]) / length_values)
    meanvalue = sum(values)/length_values
    values_standardized = []
    for value in values:
        values_standardized.append((value - meanvalue) / std)
    return values_standardized

    (np.array(values)-min(values))/(max(values)-min(values))




from stop_words import get_stop_words
from collections import namedtuple
import numpy as np

stopwords = get_stop_words('en')


sentence = "Repeating a word, any word in English is incorrect syntactically."


a=('a',0.25)

def find_frequent_words(sentence):
    # Your code goes here
    return []



sentence= "Repeating a word, any word in English is is incorrect syntactically."
sentence=sentence.split()

sentence_unique=list(set(sentence))

word_freq = []
for w in sentence_unique:
    word_freq.append(sentence.count(w))
word_freq_count=sum(word_freq)
output=[i/word_freq_count for i in word_freq]

list(zip(sentence_unique,output))





from collections import namedtuple

Dimensions = namedtuple("Dimensions", "columns rows")

matrixA=np.array([[1,2],[3,4],[5,6]])
matrixB=np.array([[1,2],[3,4]])

def compute_product(matrixA, matrixB):
    matrixA_dim = Dimensions(len(matrixA[0]), len(matrixA))
    matrixB_dim = Dimensions(len(matrixB[0]), len(matrixB))
    product = []
    for col in range(matrixA_dim.columns):
        product.append([0 for row in range(matrixB_dim.rows)])
    for i in range(matrixA_dim.rows):
        for j in range(matrixB_dim.columns):
            product[i][j] += matrixA[i][j] * matrixB[j][j]
    return product









#my sql example
from math import cos, pi, floor
import requests

Employee = pd.DataFrame({'EmployeeId': [11,12,13,14],
                         'FirstName': ['lei wai','lung sing','wai man','mei yan'],
                         'LastName': ['james','lam','wong','chan']},index=False)

Address = pd.DataFrame({'AddressId': [1,2,3,4],'EmployeeId': [11,12,13,14],
                        'Street': ['aa','bb','cc',None],
                        'District': ['tsuen wan','central','wan chai',None]},index=False)


Bank = pd.DataFrame({'Id': [1,2,3],'AssetSize':[100,200,300]})
    
    
    
connection=create_engine("mysql+pymysql://jonathan:46855678@localhost:3306/sql_learning")
    
Employee.to_sql('Employee',connection,if_exists='replace',chunksize=1000,index=False)
Address.to_sql('Address',connection,if_exists='replace',chunksize=1000,index=False)
Employee.to_sql('Employee',connection,if_exists='replace',chunksize=1000,index=False)
Bank.to_sql('Bank',connection,if_exists='replace',chunksize=1000,index=False)

    











import paramiko
from scp import SCPClient
source = r'C:\Users\jonathanjames\aws\notebooks\index_analysis\IB_live_trade\client_everything\try.txt'
dest = r'/home/customer/www/poseidontech.org/public_html/client_use_daily/version1/try.txt'
# web site link is http://poseidontech.org/client_use_daily/version1/try.txt
hostname = 'gsgpm1029.siteground.biz'
port = 18765 # default port for SSH
username = 'u427-3uutm94zey9v'
password = '36467323'



def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient(hostname, port, username, password)

scp = SCPClient(ssh.get_transport())

#copy file to destination without asking existenct
scp.put(source,dest)




#execute linux command
command='pwd'
std_in, std_out, std_err = ssh.exec_command(command)
stdout=std_out.readlines()[0]
stdout


ssh.close()







#average aggregate example
import pandas as pd

import numpy as np

df=pd.DataFrame({'symbol':['a','a','b','b','c'],'volume':[10,20,10,20,10],'price':[2,4,3,1,6]})
df

#find sum of volume and max price
output=df.groupby('symbol').agg({'volume': 'sum','price':'max'})


#find avergae price
temp_fun=lambda x : np.average(list(x.price), weights=list(x.volume))
temp=df.groupby('symbol').apply(temp_fun)
temp

output['average price']=temp

output=output.reset_index(drop=False)

output



import sys
sys.executable









#telegram send message
#find botfather to set a bot first, my bot is PoseidonTech_bot
#https://zaoldyeck.medium.com/%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E6%80%8E%E9%BA%BC%E6%89%93%E9%80%A0-telegram-bot-a7b539c3402a

#pip install python-telegram-bot
https://blog.csdn.net/yiqiushi4748/article/details/103994364




#if you're looking to simply send a message to a specific user, you need to provide your
#bot with the user's ID. To get the user's ID, use @RawDataBot in the search bar  https://www.wikihow.com/Know-Chat-ID-on-Telegram-on-Android#:~:text=Locate%20%22Chat.%22%20It's%20about,Last%20Name%2C%20and%20your%20Username.&text=Note%20the%20number%20next%20to,is%20your%20personal%20Chat%20ID.
#  所以要叫對方search @RawDataBot, 再俾個id 我
# then need to ask 55480236 to chat with PoseidonTech_bot first then PoseidonTech_bot can send message to him

poseidon_admin user id is 1404242736
55480236 user id is 1164425261


#code for send message
https://github.com/SaltNego/telegram_python_bot/blob/master/telegram_bot.py

import telegram
bot = telegram.Bot(token='1354258543:AAFOdEGomqwHu3n9u_qjxBALKOn2doUseNo')
print (bot.get_me())
info = bot.get_webhook_info()
#print (info)
bot.send_message(chat_id='1404242736', text=str(bot.get_me())) # id of poseidon_admin


bot.send_message(chat_id='1164425261', text='你好嗎')# id of 55480236

#when using bot to send message to channel, need to add this bot to the channel first
bot.send_message(chat_id='@poseidontech', text='testing')# poseidon channel


href = "https://baidu.com"
title = "嘿嘿嘿马"
#发送带标题网址链接
bot.send_message(chat_id='@poseidon_admin',
    text='<a href="http://slowread.net/monitor-hostloc/">HOSTLOC 交易贴提醒</a>.',
    parse_mode=telegram.ParseMode.HTML)
#发送无预览带标题网址链接
bot.send_message(chat_id='@testonet',
    text='<a href="' + href + '">' + title + '</a>.',
    parse_mode=telegram.ParseMode.HTML,
    disable_web_page_preview=True)
chat_id = '@testonet'
#其它文字样式
bot.send_message(chat_id=chat_id,
    text='<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.',
    parse_mode=telegram.ParseMode.HTML)
#发送图片
bot.send_photo(chat_id=chat_id,
    photo=open("115171338.png",'rb'))

bot.sendPhoto(chat_id = chat_id,
    photo=open("115171339.png",'rb'),
    caption="Sample photo Done")






#telegram send table
import telegram
bot = telegram.Bot(token='1354258543:AAFOdEGomqwHu3n9u_qjxBALKOn2doUseNo') #this is my bot token
#bot.send_message(chat_id='@poseidontech', text='testing')# poseidon channel
bot.send_message(chat_id='1164425261', text='testing')# poseidon channel

import prettytable as pt
from telegram import ParseMode
from telegram.ext import CallbackContext, Updater


def send_msg(text):
    token = "1354258543:AAFOdEGomqwHu3n9u_qjxBALKOn2doUseNo"
    chat_id = "1164425261"
    bot = telegram.Bot(token=token)
    #backticked_text = "```\n" + text + "\n```"
    backticked_text = text
    bot.sendMessage(chat_id=chat_id, text=backticked_text,parse_mode="Markdown")

myTable = pt.PrettyTable(["Student", "Class", "Section"],border=False)
  
# Add rows
myTable.add_row(["Leanord", "X", "B"])
myTable.add_row(["Penny", "X", "C"])
myTable.add_row(["Howard", "X", "A"])
myTable.add_row(["Bernadette", "X", "D"])
myTable.add_row(["Sheldon", "X", "A"])
myTable.add_row(["Raj", "X", "B"])
myTable.add_row(["Amy", "X", "B"])


table_txt=myTable.get_string()

send_msg("```\n" + table_txt + "\n```")
















.\python -m pip install telethon

telegram get api_hash
https://docs.telethon.dev/en/latest/basic/signing-in.html



#55480236
api_id = '6166311'
api_hash = '6d6e7f24e14f3ccc98f89480b441381a'

#horse quant
api_id = '6864164'
api_hash = '061fb4bb81d3fddf29103693a2c7d091'

#poseidon_admin
api_id_p='6486098'
api_hash_p='b2e4642b0071334fcc076a83d6a85095'















#spark tutorial, spark learning
#ry spark

import os
import sys

os.chdir('/home/jonathanjames/aws/notebooks/spark_learn')


#https://cloud.tencent.com/developer/article/1604610?from=article.detail.1528360
SPARK_HOME='/usr/software/spark/spark-3.2.1-bin-hadoop3.2'

sys.path.append(SPARK_HOME+'/python')
sys.path.append(SPARK_HOME+'/python/pyspark')
sys.path.append(SPARK_HOME+'/python/lib/py4j-0.10.9.3-src.zip')


    
    

import pyspark

from pyspark import SparkConf,SparkContext
conf=SparkConf().setMaster('local').setAppName('word_count')
sc = SparkContext(conf=conf)
d = ['a b c d', 'b c d e', 'c d e f']
d_rdd = sc.parallelize(d)
rdd_res = d_rdd.flatMap(lambda x: x.split(' ')).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
print(rdd_res.collect())



#read csv file
from pyspark.sql import SparkSession
# 创建一个Spark会话对象
spark=SparkSession.builder.appName('data_processing').getOrCreate()
# 加载csv数据集
df=spark.read.csv('/home/jonathanjames/aws/notebooks/spark_learn/factorDB_left.csv',inferSchema=True,header=True)

print((df.count(), len(df.columns)))
df.select('HorseName', 'HorseNo').show(10)
df.describe().show()






#read csv file
from pyspark.sql import SparkSession

appName = "Python Example - PySpark Read CSV"
master = 'local'

# Create Spark session
spark = SparkSession.builder \
    .master(master) \
    .appName(appName) \
    .getOrCreate()
file_path='/home/jonathanjames/aws/notebooks/spark_learn/factorDB_left.csv'
# Convert list to data frame
df = spark.read.format('csv') \
                .option('header',True) \
                .option('multiLine', True) \
                .load(file_path)
df.show()
print(f'Record count is: {df.count()}')
























#save as parquet
file_path='/home/jonathanjames/aws/notebooks/spark_learn/factorDB_left.csv'
import pandas as pd
df = pd.read_csv(file_path)
df.to_parquet('factorDB_left.parquet')

#read from aprquet
df=pd.read_parquet('factorDB_left.parquet', engine='pyarrow')




import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore("factorDB.hdf5", "w", complib=str("zlib"), complevel=5)
store.put("factorDB_dataframe",df, data_columns=df.columns)
store.close()







#difference between iloc and loc
import pandas as pd
import sys
import os
target_dir='/home/jonathanjames/aws/notebooks/docs/niantic'
os.chdir(target_dir)

#read data
pokemon_data=pd.read_csv('pokemon_data_science.csv')

pokemon_data=pokemon_data[['Name','HP']].copy()
pokemon_data=pokemon_data.head(10)
pokemon

Out[9]: 
         Name  HP
0   Bulbasaur  45
1     Ivysaur  60
2    Venusaur  80
3  Charmander  39
4  Charmeleon  58
5   Charizard  78
6    Squirtle  44
7   Wartortle  59
8   Blastoise  79
9    Caterpie  45


#1)
#loc is to locate the index
pokemon_data.loc[2,'Name']      #locate the index
Out[16]: 'Venusaur'


pokemon_data.loc[0:3,'Name']    #include end point
Out[10]: 
0     Bulbasaur
1       Ivysaur
2      Venusaur
3    Charmander
Name: Name, dtype: object


#iloc only accept the form a:b
pokemon_data.iloc[2,'Name']       #fail
pokemon_data.iloc[0:22,'Name']    #fail



pokemon_data.iloc[2]  
Out[20]: 
Name    Venusaur
HP            80
Name: 2, dtype: object


pokemon_data.iloc[2:4]     #exclude end point
Out[22]: 
         Name  HP
2    Venusaur  80
3  Charmander  39



#2)
pokemon_data=pokemon_data[4:8].copy()
pokemon_data

         Name  HP
4  Charmeleon  58
5   Charizard  78
6    Squirtle  44
7   Wartortle  59


pokemon_data.loc[2,'Name']      #loc locate the index, so 2 not exist


pokemon_data.loc[4,'Name'] 
Out[27]: 'Charmeleon'

pokemon_data.loc[5:7,'Name'] 

Out[28]: 
5    Charizard
6     Squirtle
7    Wartortle
Name: Name, dtype: object


#iloc is to find out the number of row, instead of locate the index
pokemon_data.iloc[2]  
Out[31]: 
Name    Squirtle
HP            44
Name: 6, dtype: object



pokemon_data.iloc[2:4] 
Out[32]: 
        Name  HP
6   Squirtle  44
7  Wartortle  59



#reorder search path
import os
import sys

sys.path


sys.path[0]

#append an element
sys.path.append('/root/anaconda3/lib/python36.zip')

#remove first element
sys.path.pop(0)

#remove element by name
sys.path.pop(sys.path.index('/root/anaconda3/lib/python36.zip'))


























#####################
#####################
#install all packages
#####################
#####################

#install quandl
.\python -m pip install quandl

#install selenium
.\python -m pip install selenium


#if fail to install pip, use below
.\python C:\Users\jonathanjames\Desktop\python\get-pip\get-pip.py


#when install python 3.6.7 edward already at 
#C:\Users\jonathanjames\Desktop\python\WPy-3670\python-3.6.7.amd64\Lib\site-packages

# install tensorflow version
#it will install at C:\Users\jonathanjames\AppData\Roaming\Python\Python36\site-packages
.\pip install --user tensorflow==1.2.1

##*****very important******
#if in case need to reinstall python, go to 
#delete C:\Users\jonathanjames\AppData\Roaming\Python first
#then normally install and also install tensorflow==1.2.1 otherwise edward may have error



#install mysql
.\pip install pymysql

#for h5 file need to use numpy version less than numpy=1.15.4 (python 3.6.7 use 1.14.6)
numpy version
https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
    
.\pip install --user C:\Users\jonathanjames\Desktop\python\numpymkl\numpy-1.15.4+mkl-cp36-cp36m-win_amd64.whl


#install ib_insync version 0.9.64
.\python -m pip install ib_insync==   
.\python -m pip install ib_insync==0.9.64  #this can use multiple clients id to login    

#also neeed to install dataclasses
.\python -m pip install dataclasses

use .\python -m pip install -U ib_insync
it will update to latest package version



#note
#note that when using python 3.6.7, ib API fail, error occure "RuntimeError: This event loop is already running"
so need to use util.patchAsyncio()
    
#convert csv to xlsx
https://stackoverflow.com/questions/17684610/python-convert-csv-to-xlsx
.\pip install pyexcel pyexcel-xlsx


#install telegram
#need to close python becasue sometime may not be installed and have alert in cmd
.\pip install python-telegram-bot

#install talib in window in python 3.6, not python 3.7
#becasue talib need to use numpy 1.19.4 but python 3.7 is using numpy 1.14.6 in order to use hdf5
pip install C:\Users\jonathanjames\Desktop\python\talib\TA_Lib-0.4.19-cp36-cp36m-win_amd64.whl



#in index_price, below append the path, so if change python version , need to update this
#add pyexcel.cookbook to python search path
import sys
sys.path
sys.path.append("C:\\Users\\jonathanjames\\Desktop\\python\\WPy-3670\\python-3.6.7.amd64\\lib\\site-packages")





#concept
#if add --user, it will be installed at (A) C:\Users\jonathanjames\AppData\Roaming\Python\Python36\site-packages
.\pip install --user xxxx
#if not adding --user, it will install normally at (B) C:\Users\jonathanjames\Desktop\python\WPy-3670\python-3.6.7.amd64\Lib\site-packages

#if already at A cannot install at B


















#########
##install package in linux (in default environment )

##install older version python
./conda update conda
./conda install python=3.6.7



#install mysql
./pip install pymysql


#if need to use import mysql.connector
./pip install mysql-connector-python


#install crontab
python -m pip install python-crontab

#python -m pip install --upgrade tensorflow-gpu
#
##install tensorflow probability
##https://github.com/tensorflow/probability
#python -m pip install pip --upgrade --user
#python -m pip install tf-nightly-2.0-preview tfp-nightly --upgrade --user

    



 

#https://tf.wiki/zh/basic/installation.html
#在安装 GPU 版本的 TensorFlow 前，你需要具有一块不太旧的 NVIDIA 显卡，以及正确安装 NVIDIA 显卡驱动程序、CUDA Toolkit 和 cuDNN。
#在安装前，可使用 conda search cudatoolkit 和 conda search cudnn 搜索 conda 源中可用的版本号。
./conda install cudatoolkit=10.2
./conda install cudnn=7.6.5

#install edward
#edward is moved to tensorflow-probability   (not sure whether need to install below, if not exist then install below)
./pip install --upgrade tensorflow-probability  

##########
#install tensorflow 2.1, for edward 2, at least 2.1  (for horse, not using edward 2, so not necessary use 2.1)

./pip install tensorflow-gpu==2.1   

#current using 2.4
./pip install tensorflow-gpu==2.4  

#for safety, use spyder 3.2.8 not 4.0

#current version of spyder
./conda install spyder=4.2.4























#in linux, if need to use tensorflow 1.2.1, need to create another environment
#for linux anaconda, if use two environment, firstanaconda-navigator then create new environment called old1
conda create --name old1 python=3.6.7   #note that installed packages is in /root/anaconda3/envs/old1/lib/python3.6/site-packages
then in terminal type  "anaconda-navigator", install spyder in this environment

#then for everytime open the computer
#need to activate the enirnment
1) in terminal     "conda activate old1"       #(this is old tensorflow 1.2.1)
2)then type "spyder"


if want to switch to default envirnment, use "conda deactivate"



#install tensorflow in environment "old1"
1) in terminal     "conda activate old1"
2_ cd /root/anaconda3/envs/old1/bin

3)./pip install tensorflow==1.2.1


#install quandl
./pip -m pip install quandl




#install mysql
./pip install pymysql

#install matplotlib 1.0.3 to avoid the error "normed" deprerciated need to use "density"
./pip install matplotlib==1.0.3


#read_excel may not work in pandas so need to use  xlrd==1.2.0
./pip install xlrd==1.2.0

#hdf5 may not work, need to use
./pip install --upgrade tables

#pandas use 0.23.4 to aviod the error KeyError: 'Passing list-likes to .loc or [] with any missing labels is no longer supported, see https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#deprecate-loc-reindex-listlike'
./pip install pandas==0.23.4


#as degraded pandas to 0.23.4, need to instrall openpyxl and xlsxwriter before using pd.ExcelWriter
./pip install openpyxl
./pip install xlsxwriter

#us joblib
./pip install joblib==0.12.5



#beautiful soup
./pip install BeautifulSoup4==4.6.3

#install pyexcel for doenloading hkex FHSI report
./pip install pyexcel==0.6.6
./pip install pyexcel-xlsx==0.6.0


#download yahoo need
./pip install pandas_datareader


#install ta-lib
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz \
  && sudo tar -xzf ta-lib-0.4.0-src.tar.gz \
  && sudo rm ta-lib-0.4.0-src.tar.gz \
  && cd ta-lib/ \
  && sudo ./configure --prefix=/usr \
  && sudo make \
  && sudo make install \
  && pip install ta-lib

make, make install (explanation)
https://www.cnblogs.com/tinywan/p/7230039.html










######## (currently not using inferpy)
#install inferpy  #https://readthedocs.org/projects/inferpy/downloads/pdf/develop/  #2020-jan-15 version
#./pip install inferpy
#note that 
./pip install inferpy[all]  #this will install both cpu and gpu version. note that it will downgrade tensorflow to suitable version say 1.15


























Ssh connect to siteground
Follow https://www.siteground.com/tutorials/ssh/putty/
Bear in mind that Hostname: gsgpm1029.siteground.biz  , never use Poseidon_admin
Hostname: gsgpm1029.siteground.biz
Username: u427-3uutm94zey9v
Port: 18765
Password is 36467323

#python ssh
./python -m pip install --user paramiko
./python -m pip install --user scp










import sys
sys.exit(0)

a=1
print(a)

















import xlwings as xw

# Connect to existing workbook containing VBA macro
wb = xw.Book(r'C:\Users\jonathanjames\aws\notebooks\data_output.xlsm')

# Run the VBA macro named 'MacroName'
wb.macro('mm')()








#dash tutorial
look at scripts
/home/jonathanjames/aws/notebooks/materials-python-dash/apps/app_4/app.py
/home/jonathanjames/aws/notebooks/materials-python-dash/dash_example/dash_example.py


#deploy dash app to web 
#https://towardsdatascience.com/the-easiest-way-to-deploy-your-dash-app-for-free-f92c575bb69e





#import pandas as pd
#with open(r"C:\Users\jonathanjames\aws\notebooks\index_analysis\log\stan_out_mindata_temp.log",'r',encoding='utf-16le') as f:
#    lines=f.readlines()
#lines








































main2.py
#read FHSI_minute_20051201to20190326.hdf5



import os
import numpy as np
from pandas import HDFStore,DataFrame
import pandas as pd
from datetime import datetime as dt
import datetime
from pandas import read_excel





#main_dir=r'C:\Users\jonathanjames\aws\notebooks\index_analysis'
#folder_path='mis'
#plot_path=os.path.join(main_dir,'plot')
#calendar_path=os.path.join(main_dir,'daily_prediction_production')






main_dir='/home/jonathanjames/aws/notebooks/index_analysis'
main_dir_new='/home/jonathanjames/my_storage/tradelog/index_analysis_cumulative'
folder_path='mis'
plot_path=os.path.join(main_dir_new,'backtest_linux/plot')
calendar_path=os.path.join(main_dir,'daily_prediction_production')

os.chdir(main_dir)










fn = os.path.join(folder_path,"FHSI_minute_20051201to_cum.hdf5")

#fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
store = pd.HDFStore(fn)
print(store)
data_all_final= store.select('FHSI_minute')
 
store.close()


data_all_final_check=data_all_final.head(10)
data=data_all_final[['date_ymd_hms','date_ymd','Open','High','Low','Close','TotalVolume']].copy()
data=data.rename(columns={'date_ymd_hms':'Date1','date_ymd':'Date2'})

#data=data.loc[~(data['Date2']=='2007-02-19'),:] #one row only
#data=data.reset_index(drop=True)


#starting from 2017-07-31, IB open may not be the same as HKEX. so revise the number from IB
#15_to_30
hsi_y = read_excel('hsi_y.xlsx','Sheet1')
hsi_y_temp=hsi_y[['Date2','Open_HSI','Close_HSI']].copy()
hsi_y_temp=hsi_y_temp.loc[hsi_y_temp['Open_HSI']!=100,:].copy()
hsi_y_temp=hsi_y_temp.reset_index(drop=True)

data_use=data.loc[data['Date2']=='2023-02-27',:]
def revise_open(data_use):
    data_use2=data_use.sort_values(by=['Date1'],ascending=True)
    data_use2=data_use2.reset_index(drop=True)

    data_use2=data_use2[0:1].copy()
    date=data_use2['Date2'].values[0]    
    if date>='2017-07-31' and date in list(hsi_y_temp.Date2.values):
        open1=hsi_y_temp.loc[hsi_y_temp['Date2']==date,'Open_HSI'].values[0]    
        high1=max(data_use2['High'].values[0],open1)
        low1=min(data_use2['Low'].values[0],open1)
        close1=data_use2['Close'].values[-1]
    
        print(date)
        
        data_use.loc[0,'Open']=open1
        data_use.loc[0,'High']=high1
        data_use.loc[0,'Low']=low1
        data_use.loc[0,'Close']=close1
    else:
        data_use=data_use.reset_index(drop=True)
    
    return data_use


temp1=data.groupby(["Date2"]).apply(lambda x:revise_open(x.reset_index(drop=True)))
data=temp1.reset_index(drop=True)





#read prediction

target='hsi_minuteA'
target='standard'
target='model_15_to_30'

from pandas import read_excel
import pandas as pd
from datetime import datetime as dt
import os
train_test_Setting = read_excel(os.path.join(main_dir,'index_table_v2_for_test_backtest.xlsx'),'Sheet2')
train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']==target,:]
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='guess_wrong',:]
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='model_0_to_13',:]
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='model_15_to_30',:]
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='model_45_to_165',:]
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='model_15_to_45',:]
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='phase1',:]
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='standard_oi',:]
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='hhi_standard',:]
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='use_10min_open_close',:]
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='japan_0_to_60',:]
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='japan_fullday',:]
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='yes',:]

train_test_Setting=train_test_Setting.reset_index(drop=True)



if target=='hsi_minuteA':
    use_daily=True
else:
    use_daily=False

d0=pd.DataFrame([])
all_number=train_test_Setting['Number'].values.tolist()
i=0
for i in range(0,train_test_Setting.shape[0]):
    #file_name='20190517_test_2019.xlsx'
    file_name=str(int(train_test_Setting['Number'][i]))+'_test_'+str(train_test_Setting['Test_start'][i].strftime("%Y"))+'.xlsx'
    #d1 = read_excel(os.path.join(plot_path,file_name),'daily_detail_summary')
    if use_daily==True:
        d1 = read_excel(os.path.join(plot_path,file_name),'daily_detail_summary_daily')
    else:
        d1 = read_excel(os.path.join(plot_path,file_name),'daily_detail_summary')
    d0=d0.append(d1)
    print('finished ',i,' out of ',train_test_Setting.shape[0])

d0.to_csv(os.path.join(folder_path,"all_prediction.csv"))
#d0.to_csv(os.path.join(folder_path,"all_prediction_guess_wrong.csv"))
#d0.to_csv(os.path.join(folder_path,"all_prediction_phase1.csv"))
#d0.to_csv(os.path.join(folder_path,"all_prediction_15_to_30.csv"))
#d0.to_csv(os.path.join(folder_path,"all_prediction_45_to_165.csv"))
#d0.to_csv(os.path.join(folder_path,"all_prediction_japan_0_to_60.csv"))
#d0.to_csv(os.path.join(folder_path,"all_prediction_japan_fullday.csv"))
#d0.to_csv(os.path.join(folder_path,"all_prediction_hsi_minuteA.csv"))

#in_sample_fitting_05_to_10=pd.read_excel(os.path.join(main_dir,"mis","30013_test_2005_to_2010_insample_model2021.xlsx"),'daily_detail_summary')
#d0=d0.append(in_sample_fitting_05_to_10)
#d0=d0.sort_values(by=['Date2'],ascending=True)
#d0=d0.reset_index(drop=True)






use_guess_wrong_mode=False
#use_guess_wrong_mode=True

if use_guess_wrong_mode==True:
    full_day=pd.read_csv(os.path.join(main_dir,"mis","all_prediction_guess_wrong.csv"))
    temp=full_day[['Date2','up_prediction_prob']].copy()
    from pandas import read_excel
    #this need to manually run all in sample fit for 2005 to 2010
    #in_sample_fitting=pd.read_excel(r"C:\Users\jonathanjames\aws\notebooks\index_analysis\plot\30011_test_2005_to_2010_insample.xlsx",'daily_detail_summary')
    in_sample_fitting=pd.read_excel(os.path.join(main_dir,"mis","30013_test_2005_guess_wrong.xlsx"),'daily_detail_summary')
    
    in_sample_fitting=in_sample_fitting[['Date2','up_prediction_prob']].copy()
    
    in_sample_fitting=in_sample_fitting.append(temp)  
    d0_guess_wrong=in_sample_fitting.copy()
    d0_guess_wrong=d0_guess_wrong.rename(columns={'up_prediction_prob':'guess_wrong_prob'})



    d0_temp=d0[['Date2','up_prediction_prob','HSI_change']].copy()

    #read fullmodel year 05 to 10
    in_sample_fitting_05_to_10=pd.read_excel(os.path.join(main_dir,"mis","30013_test_2005_to_2010_insample_model2021.xlsx"),'daily_detail_summary')
#    d0=d0.append(in_sample_fitting_05_to_10)
#    d0=d0.sort_values(by=['Date2'],ascending=True)
    
    in_sample_fitting_05_to_10=in_sample_fitting_05_to_10[['Date2','up_prediction_prob','HSI_change']].copy()
    d0_temp=d0_temp.append(in_sample_fitting_05_to_10)
    d0_temp=d0_temp.sort_values(by=['Date2'],ascending=[True])

    #read current year
    today_morning_prediction_filename='20210331_test_2021.xlsx'
    today_path=os.path.join(os.path.join(main_dir,"plot",today_morning_prediction_filename))
    
    today_morning_prediction=pd.read_excel(today_path,'daily_detail_summary')
    temp=today_morning_prediction[['Date2','up_prediction_prob','HSI_change']].copy()
    d0_temp=d0_temp.append(temp)
    
    d0_temp['Y_up']=(d0_temp['HSI_change']>=0)*1

    d0_temp=pd.merge(d0_temp,d0_guess_wrong,how='left',on=['Date2'])

    d0_temp.loc[d0_temp['up_prediction_prob']>=0.5,'guess_wrong_prob_revised']=1-d0_temp['guess_wrong_prob']
    d0_temp.loc[d0_temp['up_prediction_prob']<0.5,'guess_wrong_prob_revised']=d0_temp['guess_wrong_prob']

    #temp solution
    d0_temp['up_prediction_prob2']=d0_temp['up_prediction_prob'].copy()
    d0_temp.loc[(d0_temp['up_prediction_prob']>=0.5)&(d0_temp['guess_wrong_prob']>=0.99),'up_prediction_prob2']=0.1
    d0_temp.loc[(d0_temp['up_prediction_prob']<0.5)&(d0_temp['guess_wrong_prob']>=0.99),'up_prediction_prob2']=0.9
    
    
    
    d0_temp.loc[d0_temp['up_prediction_prob2']>=0.5,'Y_up_predict2']=1
    d0_temp.loc[d0_temp['up_prediction_prob2']<0.5,'Y_up_predict2']=0
    d0_temp['bet2']=d0_temp['Y_up_predict2'].copy()
    d0_temp.loc[d0_temp['bet2']==0,'bet2']=-1
    
    d0=pd.merge(d0,d0_temp[['Date2','Y_up_predict2','bet2']].copy(),how='left',on=['Date2'])
    d0['Y_up_predict']=d0['Y_up_predict2'].copy()
    d0['bet']=d0['bet2'].copy()


    d0_guess_wrong.loc[d0_guess_wrong['guess_wrong_prob']<0.43,'use']=1
    d0=pd.merge(d0,d0_guess_wrong[['Date2','use']].copy(),how='left',on=['Date2'])
    d0=d0.loc[d0['use']==1,:]
    d0=d0.reset_index(drop=True)







combine_indicator=True
if combine_indicator==True:
#use_guess_wrong_mode=True


    HSI_source=read_excel(os.path.join(main_dir,'HSI_with_tidy.xlsx'),'Sheet1')
    #read data
    fn = os.path.join(main_dir,'hsi_y_x.hdf5')
    store = pd.HDFStore(fn, 'r')
    print(store)
    hsi_y_x= store.select('hsi_y_x_dataframe')
    list(hsi_y_x.columns.values)
    store.close()
    
    d0=pd.merge(d0,hsi_y_x[['Date2','sar_talib_modified_original_percentile']].copy(),how='left',on=['Date2'])

    d0.loc[(d0['up_prediction_prob']>=0.5)&(d0['sar_talib_modified_original_percentile']>0),'up_prediction_prob2']=0.9
    d0.loc[(d0['up_prediction_prob']<0.5)&(d0['sar_talib_modified_original_percentile']<0),'up_prediction_prob2']=0.1
#    d0.loc[(d0['up_prediction_prob']>=0.5)&(d0['sar_talib_modified_original_percentile']>0),'up_prediction_prob2']=0.9
#    d0.loc[(d0['up_prediction_prob']<0.5)&(d0['sar_talib_modified_original_percentile']<0),'up_prediction_prob2']=0.1

    d0=d0.loc[~pd.isnull(d0['up_prediction_prob2']),:]

    d0.loc[d0['up_prediction_prob2']>=0.5,'Y_up_predict2']=1
    d0.loc[d0['up_prediction_prob2']<0.5,'Y_up_predict2']=0
    d0['bet2']=d0['Y_up_predict2'].copy()
    d0.loc[d0['bet2']==0,'bet2']=-1

    d0['Y_up_predict']=d0['Y_up_predict2'].copy()
    d0['bet']=d0['bet2'].copy()





#create afternoon prediction
train_test_Setting = read_excel(os.path.join(main_dir,'index_table_v2_for_test_backtest.xlsx'),'Sheet2')
train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='afternoon',:]
train_test_Setting=train_test_Setting.reset_index(drop=True)

d0_afternoon=pd.DataFrame([])
all_number=train_test_Setting['Number'].values.tolist()
i=0
for i in range(0,train_test_Setting.shape[0]):
    #file_name='20190517_test_2019.xlsx'
    file_name=str(int(train_test_Setting['Number'][i]))+'_test_'+str(train_test_Setting['Test_start'][i].strftime("%Y"))+'.xlsx'
    d1 = read_excel(os.path.join(plot_path,file_name),'daily_detail_summary')
    d0_afternoon=d0_afternoon.append(d1)
    print('finished ',i,' out of ',train_test_Setting.shape[0])

d0_afternoon.to_csv(os.path.join(folder_path,"all_prediction_afternoon.csv"))





##if need to use HSI prediction to apply to HHI and find pnl, replace d0 file as below
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))
#d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet']].copy()
#
#hhif=pd.read_excel(r"C:\Users\jonathanjames\aws\notebooks\index_analysis\data\hhi_20051103_to_cum.xlsx")
#
#
##check between hsi hhi
#hhif_check=pd.merge(hhif,d0[['Date2','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','bet']].copy(),how='left',on=['Date2'])
#hhif_check=hhif_check.loc[~pd.isnull(hhif_check['Open_HSI']),:].copy()
#hhif_check['year']=hhif_check['Date2'].apply(lambda x:x[0:4]).astype(int)
#hhif_check['hhi_diff']=hhif_check['Close']-hhif_check['Open']
#hhif_check['hsi_diff']=hhif_check['Close_HSI']-hhif_check['Open_HSI']
#
#hhif_check.loc[((hhif_check['hsi_diff']>=0)&(hhif_check['hhi_diff']>=0))|((hhif_check['hsi_diff']<0)&(hhif_check['hhi_diff']<0)),'sign_same']=1
#hhif_check['sign_same']=hhif_check['sign_same'].fillna(0)
#
#sum(hhif_check['sign_same'])/hhif_check.shape[0]
#
#hhif_check.groupby(["year"])['sign_same'].sum()
#
#hhif_check['PnL_hhi']=(hhif_check['Close']-hhif_check['Open'])*hhif_check['bet']*10
#hhif_check['PnL_hhi_cumsum']=hhif_check.groupby(["year"])['PnL_hhi'].cumsum()
#hhif_check['PnL_hsi']=(hhif_check['Close_HSI']-hhif_check['Open_HSI'])*hhif_check['bet']*10
#hhif_check['PnL_hsi_cumsum']=hhif_check.groupby(["year"])['PnL_hsi'].cumsum()
#
#hhif_check.groupby(["year"])['PnL_hsi'].sum()
#hhif_check.groupby(["year"])['PnL_hhi'].sum()
#
#hhif_check.to_csv(r"C:\Users\jonathanjames\aws\notebooks\index_analysis\data\hhif_check.csv")
#
#hhif=pd.merge(hhif,d0[['Date2', 'Y_up_predict','bet']].copy(),how='left',on=['Date2'])
#hhif=hhif.loc[~pd.isnull(hhif['Y_up_predict']),:].copy()
#
#hhif_use=hhif[['Date2', 'Y_up_predict','Open', 'High', 'Low', 'Close','DateNum','bet']].copy()
#hhif_use=hhif_use.rename(columns={'Open':'Open_HSI', 'High':'High_HSI', 'Low':'Low_HSI', 'Close':'Close_HSI'})
#hhif_use=hhif_use.reset_index(drop=True)
#hhif_use.to_csv(os.path.join(folder_path,"all_prediction.csv"))



#if need to use HSI prediction to apply to 15_to_999999 and find pnl
d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))
d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet']].copy()

hhif=pd.read_excel("HSI_15_to_999999_with_tidy.xlsx")

hhif=pd.merge(hhif,d0[['Date2', 'Y_up_predict','bet']].copy(),how='left',on=['Date2'])
hhif=hhif.loc[~pd.isnull(hhif['Y_up_predict']),:].copy()

hhif_use=hhif[['Date2', 'Y_up_predict','Open_HSI_afternoon', 'High_HSI_afternoon', 'Low_HSI_afternoon', 'Close_HSI_afternoon','DateNum','bet']].copy()
hhif_use=hhif_use.rename(columns={'Open_HSI_afternoon':'Open_HSI', 'High_HSI_afternoon':'High_HSI', 'Low_HSI_afternoon':'Low_HSI', 'Close_HSI_afternoon':'Close_HSI'})
hhif_use=hhif_use.reset_index(drop=True)
hhif_use.to_csv(os.path.join(folder_path,"all_prediction_15_to_999999_use_fullday.csv"))
























#grid search for stop loss level
d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))

#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_phase1.csv"))
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_15_to_30.csv"))
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_afternoon.csv"))
d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet','up_prediction_prob']].copy()

#d0=d0.loc[d0['up_prediction_prob']>0.55,:].copy()
#d0=d0.reset_index(drop=True)

#d0.loc[d0['bet']==1,'bet1']=-1
#d0.loc[d0['bet']==-1,'bet1']=1
#d0['bet']=d0['bet1'].copy()
#del d0['bet1']
#
#d0.loc[d0['Y_up_predict']==1,'Y_up_predict1']=0
#d0.loc[d0['Y_up_predict']==0,'Y_up_predict1']=1
#d0['Y_up_predict']=d0['Y_up_predict1'].copy()
#del d0['Y_up_predict1']

d0_gridsearch_stop=d0.copy()
d0_gridsearch_stop=d0_gridsearch_stop.reset_index(drop=True)
d0_gridsearch_stop['year']=d0_gridsearch_stop['Date2'].apply(lambda x:x[0:4]).astype(int)

##if last racing day is 4 day before, not to trade, and find the pnl
#
#d0_gridsearch_stop['last_trading_date']=d0_gridsearch_stop['Date2'].shift(1)
#d0_gridsearch_stop=d0_gridsearch_stop.loc[~(pd.isnull(d0_gridsearch_stop['last_trading_date'])),:].reset_index(drop=True).copy()
#d0_gridsearch_stop['last_trading_date']=d0_gridsearch_stop['last_trading_date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
#d0_gridsearch_stop['Date2_dt']=d0_gridsearch_stop['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
#d0_gridsearch_stop['last_trading_diff'] = (d0_gridsearch_stop.Date2_dt-d0_gridsearch_stop.last_trading_date).astype("timedelta64[D]").astype(np.int64)
#
#d0_gridsearch_stop=d0_gridsearch_stop.loc[d0_gridsearch_stop['last_trading_diff']<4,:].copy()


#check high open difference
d0_gridsearch_stop['high_open']=abs(d0_gridsearch_stop['High_HSI']-d0_gridsearch_stop['Open_HSI'])
d0_gridsearch_stop.groupby(['year'])['high_open'].apply(lambda x:x.mean())

d0_gridsearch_stop['low_open']=abs(d0_gridsearch_stop['Low_HSI']-d0_gridsearch_stop['Open_HSI'])
d0_gridsearch_stop.groupby(['year'])['low_open'].apply(lambda x:x.mean())

d0_gridsearch_stop['close_open']=abs(d0_gridsearch_stop['Close_HSI']-d0_gridsearch_stop['Open_HSI'])
d0_gridsearch_stop.groupby(['year'])['close_open'].apply(lambda x:x.mean())



stop_grid_search=[*range(10,500,10)]+[10000]
stop_grid_search=[*range(1,215,5)]+[10000]

#stop_level=30
for stop_level in stop_grid_search:

    stop_col_name='stop_indicate_'+str(stop_level)
    pnl_name='pnl_with_stop_'+str(stop_level)

    #indicate if triggered stop
    d0_gridsearch_stop2=d0_gridsearch_stop.copy()
    d0_gridsearch_stop2.loc[(d0_gridsearch_stop2['Y_up_predict']==1)&(d0_gridsearch_stop2['Low_HSI']<=d0_gridsearch_stop2['Open_HSI']-stop_level),'stop_indicate_up']=1
    d0_gridsearch_stop2['stop_indicate_up']=d0_gridsearch_stop2['stop_indicate_up'].fillna(0)
    
    d0_gridsearch_stop2.loc[(d0_gridsearch_stop2['Y_up_predict']==0)&(d0_gridsearch_stop2['High_HSI']>=d0_gridsearch_stop2['Open_HSI']+stop_level),'stop_indicate_down']=1
    d0_gridsearch_stop2['stop_indicate_down']=d0_gridsearch_stop2['stop_indicate_down'].fillna(0)
    d0_gridsearch_stop2[stop_col_name]=d0_gridsearch_stop2['stop_indicate_up']-d0_gridsearch_stop2['stop_indicate_down']

    d0_gridsearch_stop2.loc[d0_gridsearch_stop2[stop_col_name]!=0,pnl_name]=-1*stop_level*10-7.62
    d0_gridsearch_stop2.loc[d0_gridsearch_stop2[stop_col_name]==0,pnl_name]=(d0_gridsearch_stop2['Close_HSI']-d0_gridsearch_stop2['Open_HSI'])*d0_gridsearch_stop2['bet']*10-7.62
    d0_gridsearch_stop2[pnl_name+'_cum']=d0_gridsearch_stop2.groupby(['year'])[pnl_name].cumsum()
    
    d0_gridsearch_stop2_check=d0_gridsearch_stop2.loc[d0_gridsearch_stop2['year']==2021,:].copy()
    
    d0_gridsearch_stop[pnl_name]=d0_gridsearch_stop2[pnl_name].copy()
    d0_gridsearch_stop[pnl_name+'_cum']=d0_gridsearch_stop2[pnl_name+'_cum'].copy()
    
    print(sum(d0_gridsearch_stop[pnl_name]))


def find_pnl_for_diff_stop(xx,pnl_name):
    return sum(xx[pnl_name].values)

def find_drawdown(xx,pnl_name):
    return max(np.maximum.accumulate(xx[pnl_name+'_cum'])-xx[pnl_name+'_cum'])

def find_wincount(xx,pnl_name):
    return sum(xx[pnl_name].values>0)

def find_maxloss(xx,pnl_name):
    return min(xx[pnl_name].values.cumsum())

#stop_level=10
count=0
stop_level=1
for stop_level in stop_grid_search:
    
    pnl_name='pnl_with_stop_'+str(stop_level)
    yearly_pnl='pnl_stop_'+str(stop_level)
    yearly_downside='downside_stop_'+str(stop_level)
    yearly_wincount='wincount_stop_'+str(stop_level)
    yearly_maxloss='maxloss_stop_'+str(stop_level)
    
    
    temp=d0_gridsearch_stop.groupby(['year']).apply(lambda x:find_pnl_for_diff_stop(x.reset_index(drop=True),pnl_name))
    temp=temp.reset_index(drop=False)
    temp=temp.rename(columns={0:yearly_pnl})
    
    #temp_downside=d0_gridsearch_stop.groupby(['year'])[pnl_name+'_cum'].min()
    temp_downside=d0_gridsearch_stop.groupby(['year']).apply(lambda x:find_drawdown(x.reset_index(drop=True),pnl_name))
    temp_downside=temp_downside.reset_index(drop=False)
    temp_downside.columns=['year',yearly_downside]
    
    #find win count
    temp_wincount=d0_gridsearch_stop.groupby(['year']).apply(lambda x:find_wincount(x.reset_index(drop=True),pnl_name))
    temp_wincount=temp_wincount.reset_index(drop=False)
    temp_wincount=temp_wincount.rename(columns={0:yearly_wincount})

    #findmax loss
    temp_maxloss=d0_gridsearch_stop.groupby(['year']).apply(lambda x:find_maxloss(x.reset_index(drop=True),pnl_name))
    temp_maxloss=temp_maxloss.reset_index(drop=False)
    temp_maxloss=temp_maxloss.rename(columns={0:yearly_maxloss})
    
    if count==0:
        yearly_pnl_stop_summary=temp.copy()
        yearly_downside_stop_summary=temp_downside.copy()
        yearly_wincount_stop_summary=temp_wincount.copy()
        yearly_maxloss_stop_summary=temp_maxloss.copy()
    else:
        yearly_pnl_stop_summary[yearly_pnl]=temp[yearly_pnl]
        yearly_downside_stop_summary[yearly_downside]=temp_downside[yearly_downside].copy()
        yearly_wincount_stop_summary[yearly_wincount]=temp_wincount[yearly_wincount]
        yearly_maxloss_stop_summary[yearly_maxloss]=temp_maxloss[yearly_maxloss]        
        
    count=count+1


yearly_downside_stop_summary.loc['Mean',:]= yearly_downside_stop_summary.mean(axis=0)
yearly_pnl_stop_summary.loc['Mean',:]= yearly_pnl_stop_summary.mean(axis=0)
yearly_wincount_stop_summary.loc['Mean',:]= yearly_wincount_stop_summary.mean(axis=0)
yearly_maxloss_stop_summary.loc['Mean',:]= yearly_maxloss_stop_summary.mean(axis=0)

yearly_pnl_stop_summary_validation=yearly_pnl_stop_summary.loc[yearly_pnl_stop_summary['year']<=2014,:].copy()
yearly_downside_stop_summary_validation=yearly_downside_stop_summary.loc[yearly_downside_stop_summary['year']<=2014,:].copy()
yearly_wincount_stop_summary_validation=yearly_wincount_stop_summary.loc[yearly_wincount_stop_summary['year']<=2014,:].copy()
yearly_maxloss_stop_summary_validation=yearly_maxloss_stop_summary.loc[yearly_maxloss_stop_summary['year']<=2014,:].copy()

#Total sum per column: 
yearly_pnl_stop_summary_validation.loc['Mean',:]= yearly_pnl_stop_summary_validation.mean(axis=0)
yearly_downside_stop_summary_validation.loc['Mean',:]= yearly_downside_stop_summary_validation.mean(axis=0)
yearly_wincount_stop_summary_validation.loc['Mean',:]= yearly_wincount_stop_summary_validation.mean(axis=0)



import numpy as np
import matplotlib.pyplot as plt

x = np.array(stop_grid_search)
y = yearly_pnl_stop_summary_validation.loc['Mean',:][1:].values/yearly_downside_stop_summary_validation.loc['Mean',:][1:].values
plt.scatter(x, y)
plt.xlim(stop_grid_search[1],stop_grid_search[-2])
plt.show()

x = np.array(stop_grid_search)
y = yearly_pnl_stop_summary.loc['Mean',:][1:].values/yearly_downside_stop_summary.loc['Mean',:][1:].values
plt.scatter(x, y)
plt.xlim(stop_grid_search[1],stop_grid_search[-2])
plt.show()


x = np.array(stop_grid_search)
y = yearly_downside_stop_summary_validation.loc['Mean',:][1:].values
plt.scatter(x, y)
plt.xlim(stop_grid_search[1],stop_grid_search[-2])
plt.show()



xy=pd.DataFrame([])
xy['stop_level']=x
xy['pnl/loss']=y
















#check stop percentage
lookat=200

#d0_gridsearch_stop2=d0_gridsearch_stop2[['Date2','year','Open_HSI','High_HSI','Low_HSI','Close_HSI','Y_up_predict']].copy()

d0_gridsearch_stop2_check=d0_gridsearch_stop2.loc[d0_gridsearch_stop2['year']==2020,['Date2','pnl_with_stop_'+str(lookat),'stop_indicate']].copy()

#sum((d0_gridsearch_stop2['Y_up_predict']==1)&(d0_gridsearch_stop2['Low_HSI']<=d0_gridsearch_stop2['Open_HSI']-lookat))

d0_gridsearch_stop2['stop_indicate_up']=0
d0_gridsearch_stop2.loc[(d0_gridsearch_stop2['Y_up_predict']==1)&(d0_gridsearch_stop2['Low_HSI']<=d0_gridsearch_stop2['Open_HSI']-lookat),'stop_indicate_up']=1
d0_gridsearch_stop2['stop_indicate_up']=d0_gridsearch_stop2['stop_indicate_up'].fillna(0)

d0_gridsearch_stop2['stop_indicate_down']=0
d0_gridsearch_stop2.loc[(d0_gridsearch_stop2['Y_up_predict']==0)&(d0_gridsearch_stop2['High_HSI']>=d0_gridsearch_stop2['Open_HSI']+lookat),'stop_indicate_down']=1
d0_gridsearch_stop2['stop_indicate_down']=d0_gridsearch_stop2['stop_indicate_down'].fillna(0)

#sum(d0_gridsearch_stop2['stop_indicate_down'])

d0_gridsearch_stop2['triggered_stop']=d0_gridsearch_stop2['stop_indicate_up']+d0_gridsearch_stop2['stop_indicate_down']


#sum(d0_gridsearch_stop2['triggered_stop'])

a=d0_gridsearch_stop2.groupby(['year'])['triggered_stop'].sum()
a

b=d0_gridsearch_stop2.groupby(['year'])['year'].count()

#stop portion
a/b














#check bet in first minute

d0=pd.read_csv(os.path.join(main_dir,folder_path,"all_prediction_phase1.csv"))
d0['Close_HSI_shift1']=d0['Close_HSI'].shift(1)
d0['break_open']=d0['Open_HSI']-d0['Close_HSI_shift1']

d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet','break_open','DateNum']].copy()

d0.dtypes
d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
 
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))



fn = os.path.join(main_dir,folder_path,"FHSI_minute_20051201to_cum.hdf5")

#fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
store = pd.HDFStore(fn)
print(store)
data_all_final= store.select('FHSI_minute')
 
store.close()


data_all_final_check=data_all_final.tail(4000)
data=data_all_final[['date_ymd_hms','date_ymd','Open','High','Low','Close','TotalVolume']].copy()
data['hms']=data['date_ymd_hms'].apply(lambda x: x.strftime('%H:%M:%S'))
data=data.rename(columns={'date_ymd_hms':'Date1','date_ymd':'Date2'})

data_use=data.groupby('Date2').head(1)

data_use=pd.merge(data_use,d0[['Date2','Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','bet','break_open','DateNum']].copy(),how='left',on=['Date2'])
data_use=data_use.loc[(data_use['Date2']>='2011-01-01')&(~pd.isnull(data_use['break_open'])),:].copy()





target_profit=150
commission=7.62
stop=50


data_use['Open_HSI']=(data_use['Open']+data_use['High']+data_use['Low']+data_use['Close'])/4

d0=data_use.copy()

stop_level=90

d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet']].copy()
d0.dtypes
d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
 
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

#indicate if triggered stop
d0.loc[(d0['Y_up_predict']==1)&(d0['Low_HSI']<=d0['Open_HSI']-stop_level),'stop_indicate_up']=1
d0['stop_indicate_up']=d0['stop_indicate_up'].fillna(0)

d0.loc[(d0['Y_up_predict']==0)&(d0['High_HSI']>=d0['Open_HSI']+stop_level),'stop_indicate_down']=1
d0['stop_indicate_down']=d0['stop_indicate_down'].fillna(0)
d0['stop_indicate']=d0['stop_indicate_up']-d0['stop_indicate_down']


#for hong kong
d0.loc[d0['stop_indicate']!=0,'PnL']=-1*stop_level*10
d0.loc[d0['stop_indicate']==0,'PnL']=(d0['Close_HSI']-d0['Open_HSI'])*d0['bet']*10
d0['PnL_after_commission']=d0['PnL']-7.62
d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
d0_check=d0.loc[d0['Date2_y']=='2019',:]


data_use.loc[(data_use['bet']==1)&((data_use['Open']-data_use['Low'])>=stop),'profit2_stop']=-1*stop*10-commission
data_use.loc[(data_use['bet']==-1)&((data_use['High']-data_use['Open'])>=stop),'profit2_stop']=-1*stop*10-commission


data_use.loc[(data_use['bet']==1)&((data_use['High']-data_use['Open'])>=target_profit+2)&(pd.isnull(data_use['profit2_stop'])),'make_target']=1
data_use.loc[(data_use['bet']==-1)&((data_use['Open']-data_use['Low'])>=target_profit+2)&(pd.isnull(data_use['profit2_stop'])),'make_target']=-1
data_use.loc[(pd.isnull(data_use['make_target']))&(pd.isnull(data_use['profit2_stop'])),'make_target']=0

data_use.loc[(data_use['make_target']==1)|(data_use['make_target']==-1),'profit1']=target_profit*10-commission

data_use.loc[data_use['make_target']==0,'profit2_no_stop']=data_use['bet']*(data_use['Close']-data_use['Open'])*10-commission


data_use.shape[0]

sum(data_use.profit1>0)
sum(data_use.profit2_no_stop>0)
sum(data_use.profit2_stop<0)
sum(data_use.profit2_no_stop<0)

sum(data_use.profit1.values[data_use.profit1>0])
sum(data_use.profit2_no_stop.values[data_use.profit2_no_stop>0])
sum(data_use.profit2_stop.values[data_use.profit2_stop<0])
sum(data_use.profit2_no_stop.values[data_use.profit2_no_stop<0])

sum(data_use.profit1.values[data_use.profit1>0])+sum(data_use.profit2.values[data_use.profit2>0])+sum(data_use.profit2.values[data_use.profit2<0])

data_use.loc[data_use['profit2']<0,'profit3']=data_use['bet']*(data_use['Close_HSI']-data_use['Open_HSI'])*10-commission

sum(data_use.profit3.values[data_use.profit3>0])
sum(data_use.profit3.values[data_use.profit3<0])












#version for only stop profit
profit_target=150

#summary statistics for all_prediction
d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))


d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet']].copy()
d0.dtypes
d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
 
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

#indicate if triggered stop
d0.loc[(d0['Y_up_predict']==1)&(d0['High_HSI']-d0['Open_HSI']>=profit_target),'profit_indicate_up']=1
d0['profit_indicate_up']=d0['profit_indicate_up'].fillna(0)

d0.loc[(d0['Y_up_predict']==0)&(d0['Open_HSI']-d0['Low_HSI']>=profit_target),'profit_indicate_down']=1
d0['profit_indicate_down']=d0['profit_indicate_down'].fillna(0)
d0['profit_indicate']=d0['profit_indicate_up']-d0['profit_indicate_down']


#for hong kong
d0.loc[d0['profit_indicate']!=0,'PnL']=profit_target*10
d0.loc[d0['profit_indicate']==0,'PnL']=(d0['Close_HSI']-d0['Open_HSI'])*d0['bet']*10
d0['PnL_after_commission']=d0['PnL']-7.62
d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
d0_check=d0.loc[d0['Date2_y']=='2022',:]










#normal version
stop_level=200

#summary statistics for all_prediction
d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_phase1.csv"))
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_15_to_30.csv"))
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_45_to_165.csv"))
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_15_to_999999_use_fullday.csv"))


#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_japan_0_to_60.csv"))
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_japan_fullday.csv"))



d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet']].copy()
d0.dtypes
d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
 
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

#indicate if triggered stop
d0.loc[(d0['Y_up_predict']==1)&(d0['Low_HSI']<=d0['Open_HSI']-stop_level),'stop_indicate_up']=1
d0['stop_indicate_up']=d0['stop_indicate_up'].fillna(0)

d0.loc[(d0['Y_up_predict']==0)&(d0['High_HSI']>=d0['Open_HSI']+stop_level),'stop_indicate_down']=1
d0['stop_indicate_down']=d0['stop_indicate_down'].fillna(0)
d0['stop_indicate']=d0['stop_indicate_up']-d0['stop_indicate_down']


#for hong kong
d0.loc[d0['stop_indicate']!=0,'PnL']=-1*stop_level*10
d0.loc[d0['stop_indicate']==0,'PnL']=(d0['Close_HSI']-d0['Open_HSI'])*d0['bet']*10
d0['PnL_after_commission']=d0['PnL']-7.62
d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
d0_check=d0.loc[d0['Date2_y']=='2019',:]

d0_check=d0.groupby(['Date2_y']).head(1)


##for japan
#d0.loc[d0['stop_indicate']!=0,'PnL']=-1*stop_level*100/14
#d0.loc[d0['stop_indicate']==0,'PnL']=(d0['Close_HSI']-d0['Open_HSI'])*d0['bet']*100/14
#d0['PnL_after_commission']=d0['PnL']-80/14
#d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
#d0_check=d0.loc[d0['Date2_y']=='2019',:]



#d0.to_csv(os.path.join(folder_path,"d0_model_0_to_13.csv"))
#d0.to_csv(os.path.join(folder_path,"d0_model_15_to_30.csv"))
#d0.to_csv(os.path.join(folder_path,"d0_model_45_to_165.csv"))
#d0.to_csv(os.path.join(folder_path,"d0_model_15_to_999999_use_fullday.csv"))
#d0.to_csv(os.path.join(folder_path,"d0_standard.csv"))
#d0.to_csv(os.path.join(folder_path,"d0_japan_0_to_60.csv"))
#d0.to_csv(os.path.join(folder_path,"d0_japan_fullday.csv"))












#hsi_2019_check=read_excel(r"C:\Users\jonathanjames\aws\notebooks\index_analysis\plot\30010_test_2019.xlsx",'daily_detail_summary')
#hsi_2019_check['PnL']=hsi_2019_check['PnL']*10
#hsi_2019_check['Cum.Sum']=hsi_2019_check['Cum.Sum']*10
#d0_check=pd.merge(d0_check,hsi_2019_check[['Date2', 'Y_up_predict','HSI_change','PnL', 'Cum.Sum']].copy(),how='left',on=['Date2'])
#hsi_2019_check.columns.values


sum(d0['PnL'])
sum(d0['PnL'])
sum(d0['PnL_after_commission'])


#d0=d0.loc[d0['advantage']>-9999999,:]


d0=d0.reset_index(drop=True)

#check whether high low is higher or lower than open

d0['H_O']=d0['High_HSI']-d0['Open_HSI']
 
sum(d0['H_O'].values<=5)



##try to remove some day around settlement as simulation
#settlement_day = read_excel(os.path.join(calendar_path,'calendar.xlsx'),'settlement')
#settlement_day['Date2']=settlement_day['settlement_day'].astype(str)      
#settlement_day['settlement']=1
#
#tradeday_before20181224=read_excel(os.path.join(calendar_path,'calendar.xlsx'),'tradingdate_before20181227')
#calendar = read_excel(os.path.join(calendar_path,'calendar.xlsx'),'calendar')
#calendar['Date2']=calendar['Date'].astype(str)
#calendar=calendar.loc[calendar['trading_date']==1,:]  
#
#all_trading_date=tradeday_before20181224.append(calendar[['Date2']])
#all_trading_date=all_trading_date.reset_index(drop=True)
#
#all_trading_date=pd.merge(all_trading_date,settlement_day[['Date2','settlement']].copy(),how='left',on=['Date2'])
#all_trading_date['settlement']=all_trading_date['settlement'].fillna(0)
#
##all_trading_date['s1']=all_trading_date['settlement'].shift(-1)
##all_trading_date['a1']=all_trading_date['settlement'].shift(1)
##all_trading_date=all_trading_date.fillna(0)
##all_trading_date['one']=all_trading_date['settlement']+all_trading_date['s1']+all_trading_date['a1']
##d0=pd.merge(d0,all_trading_date[['Date2','settlement','s1','a1','one']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])            
#
#
#all_trading_date['one']=all_trading_date['settlement']
#d0=pd.merge(d0,all_trading_date[['Date2','settlement','one']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])   
#
#
#d0=d0.loc[d0['one']==0,:]
#d0=d0.reset_index(drop=True)







































#use last n mins mean as close price and find pnl
#
#data.dtypes
#data_check=data.head(10)

enter_number_of_bar=2
stop_number_of_bar=2
exit_number_of_bar=2

data_use=data.loc[data['Date2']=='2014-12-31',:]
def find_min_6min(data_use):
    data_use2=data_use.sort_values(by=['Date1'],ascending=False)
    data_use2=data_use2.head(exit_number_of_bar)
    #data_use2['mean']=(data_use2['High']+data_use2['Low'])/2
    data_use2['mean']=(data_use2['High']+data_use2['Low']+data_use2['Open']+data_use2['Close'])/4
    output=np.mean(data_use2['mean'].values)
    return output

new_column=data.groupby("Date2").apply(lambda x:find_min_6min(x))
new_column=new_column.reset_index(drop=False)
new_column=new_column.rename(columns={0:'close_adjusted_6min_mean'})

d0=pd.merge(d0,new_column,how='left',left_on=['Date2'],right_on=['Date2'])
d0=d0.loc[~pd.isnull(d0['close_adjusted_6min_mean']),:]


data_use=data.loc[data['Date2']=='2014-12-31',:]
def find_min_6min_adj_open(data_use):
    data_use2=data_use.sort_values(by=['Date1'],ascending=True)
    data_use2=data_use2.head(enter_number_of_bar)
    #data_use2['mean']=(data_use2['High']+data_use2['Low'])/2
    data_use2['mean']=(data_use2['High']+data_use2['Low']+data_use2['Open']+data_use2['Close'])/4
    output=np.mean(data_use2['mean'].values)
    #output=data_use2['Open']
    return output

new_column=data.groupby("Date2").apply(lambda x:find_min_6min_adj_open(x))
new_column=new_column.reset_index(drop=False)
new_column=new_column.rename(columns={0:'open_adjusted_6min_mean'})

d0=pd.merge(d0,new_column,how='left',left_on=['Date2'],right_on=['Date2'])
d0=d0.loc[~pd.isnull(d0['open_adjusted_6min_mean']),:]

#d0['open_adjusted_6min_mean']=d0['Open_HSI'].copy()
#d0.to_csv(r"C:\Users\jonathanjames\aws\notebooks\index_analysis\d0_adjusted_open_close.csv")


#create new stop

#for each date, select rows after first few row, as first few rows is used to open position, then create new high and
#new low
data2=data.copy()
data2_new_high_low=data2.groupby(['Date2']).head(enter_number_of_bar)
data2_new_high_low['one']=1
data2_new_stop=pd.merge(data2,data2_new_high_low[['Date1','one']].copy(),how='left',on=['Date1'])
data2_new_stop=data2_new_stop.loc[pd.isnull(data2_new_stop.one),:]
del data2_new_stop['one']

#also remove some bar before close
data2_new_high_low=data2.groupby(['Date2']).tail(exit_number_of_bar)
data2_new_high_low['one']=1
data2_new_stop=pd.merge(data2_new_stop,data2_new_high_low[['Date1','one']].copy(),how='left',on=['Date1'])
data2_new_stop=data2_new_stop.loc[pd.isnull(data2_new_stop.one),:]
del data2_new_stop['one']


df_max=data2_new_stop.groupby('Date2')['High'].max().reset_index(drop=False)
df_min=data2_new_stop.groupby('Date2')['Low'].min().reset_index(drop=False)

d0_for_new_stop=d0.copy()

d0_for_new_stop=pd.merge(d0_for_new_stop,df_max[['Date2','High']].copy(),how='left',on=['Date2'])
d0_for_new_stop=pd.merge(d0_for_new_stop,df_min[['Date2','Low']].copy(),how='left',on=['Date2'])
d0_for_new_stop=d0_for_new_stop.rename(columns={'High':'High_new','Low':'Low_new'})

#create new stop level
d0_for_new_stop.loc[d0_for_new_stop['Y_up_predict']==1,'new_stop']=d0_for_new_stop[['Open_HSI','open_adjusted_6min_mean']].min(axis=1)-stop_level
d0_for_new_stop.loc[d0_for_new_stop['Y_up_predict']==0,'new_stop']=d0_for_new_stop[['Open_HSI','open_adjusted_6min_mean']].max(axis=1)+stop_level


d0_for_new_stop.loc[(d0_for_new_stop['Y_up_predict']==1)&(d0_for_new_stop['Low_new']<=d0_for_new_stop['new_stop']),'stop_indicate_up_revised']=1
d0_for_new_stop['stop_indicate_up_revised']=d0_for_new_stop['stop_indicate_up_revised'].fillna(0)

d0_for_new_stop.loc[(d0_for_new_stop['Y_up_predict']==0)&(d0_for_new_stop['High_new']>=d0_for_new_stop['new_stop']),'stop_indicate_down_revised']=1
d0_for_new_stop['stop_indicate_down_revised']=d0_for_new_stop['stop_indicate_down_revised'].fillna(0)
d0_for_new_stop['stop_indicate_new']=d0_for_new_stop['stop_indicate_up_revised']-d0_for_new_stop['stop_indicate_down_revised']


#d0_for_new_stop.loc[d0_for_new_stop['stop_indicate_new']!=0,'PnL_new']=-1*stop_level*10
#d0_for_new_stop.loc[d0_for_new_stop['stop_indicate_new']==0,'PnL_new']=(d0_for_new_stop['close_adjusted_6min_mean']-d0_for_new_stop['open_adjusted_6min_mean'])*d0_for_new_stop['bet']*10





#handle stop loss, if triggered stop loss, for next 10 bars, each bar settled 50 contracts
ii=208
ii=1048
ii=983 #2014/12/31
ii=1109 #2015-07-08
revised_stop=[]
data2=data.sort_values(by=['Date2','Date1'],ascending=[True,True]).copy()
data2=data2.loc[data2['Date2']>='2011-01-01',:]

data2=pd.merge(data2,d0_for_new_stop[['Date2','Open_HSI',
                         'stop_indicate_new',
                         'open_adjusted_6min_mean',
                         'close_adjusted_6min_mean']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])

#ii_old=all_links[963] #2014-12-01
#ii_old=all_links[1134] #2015-08-12 this is guess up with stop
#ii_old=all_links[6] #2011-01-11 this is guess up without stop
#ii_old=all_links[1] #2011-01-04 this is guess down with stop
def revise_stop(ii_old):
    ii=ii_old[1] #ii_old is tuple, 1 is the second item, stored the dataframe
    ii=ii.reset_index(drop=True)
    target_date=ii['Date2'].values[0]
    #stop_indicate=ii['stop_indicate'].values[0]
    stop_indicate=ii['stop_indicate_new'].values[0]
    output=9999999
    first_index=9999999
    
    no_of_bar_to_settle=stop_number_of_bar
    
    if stop_indicate==1:
        #stop_price=ii['Open_HSI'].values[0]-stop_level
        old_stop=ii['Open_HSI'].values[0]-stop_level
        #stop_price=ii['open_adjusted_6min_mean'].values[0]-stop_level
        stop_price=min(old_stop,ii['open_adjusted_6min_mean'].values[0]-stop_level)
        
       
        ii=ii.iloc[enter_number_of_bar:-1*exit_number_of_bar,:]
        
        ii['stop_series']=(ii['Low'].values<=stop_price)*1
        first_index=(ii.stop_series.values==1).argmax()
        data_use2_use=ii[first_index+1:first_index+1+no_of_bar_to_settle]
        data_use2_use=data_use2_use.reset_index(drop=True)
        #data_use2_use['mean']=(data_use2_use['High']+data_use2_use['Low'])/2
        data_use2_use['mean']=(data_use2_use['High']+data_use2_use['Low']+data_use2_use['Open']+data_use2_use['Close'])/4
        
        output=np.mean(data_use2_use['mean'].values)

        if data_use2_use.shape[0]<no_of_bar_to_settle:
            output=9999999

    if stop_indicate==-1:
        #stop_price=ii['Open_HSI'].values[0]+stop_level
        old_stop=ii['Open_HSI'].values[0]+stop_level
        #stop_price=ii['open_adjusted_6min_mean'].values[0]+stop_level
        stop_price=max(ii['open_adjusted_6min_mean'].values[0]+stop_level,old_stop)
        
        
        ii=ii.iloc[enter_number_of_bar:-1*exit_number_of_bar,:]
        
        ii['stop_series']=(ii['High'].values>=stop_price)*1
        first_index=(ii.stop_series.values==1).argmax()
        data_use2_use=ii[first_index+1:first_index+1+no_of_bar_to_settle]
        data_use2_use=data_use2_use.reset_index(drop=True)
        #data_use2_use['mean']=(data_use2_use['High']+data_use2_use['Low'])/2
        data_use2_use['mean']=(data_use2_use['High']+data_use2_use['Low']+data_use2_use['Open']+data_use2_use['Close'])/4
        
        output=np.mean(data_use2_use['mean'].values)
        
        if data_use2_use.shape[0]<no_of_bar_to_settle:
            output=9999999
    print("finished ",target_date)
    return target_date+'#'+str(output)+'#'+str(first_index+enter_number_of_bar)+'#'+str(stop_indicate)


import requests
from concurrent.futures import ThreadPoolExecutor


    
all_links=list(data2.groupby("Date2"))
output=[]
with ThreadPoolExecutor(max_workers=20) as pool:
    output=list(pool.map(revise_stop,all_links))




output=pd.DataFrame(output)
output['Date2']=output[0].apply(lambda x:x.split("#")[0])
output['revised_Stop']=output[0].apply(lambda x:x.split("#")[1])
output['revised_Stop']=output['revised_Stop'].astype(np.float64)

output['first_index']=output[0].apply(lambda x:x.split("#")[2])
output['first_index']=output['first_index'].astype(np.float64)

output['stop_indicate_new']=output[0].apply(lambda x:x.split("#")[3])
output['stop_indicate_new']=output['stop_indicate_new'].astype(np.float64)

d0=pd.merge(d0,output[['Date2','revised_Stop','first_index','stop_indicate_new']].copy(),how='left',on=['Date2'])

d0.loc[d0['revised_Stop']!=9999999,'close_adjusted_6min_mean']=d0['revised_Stop']

d0['close_open_diff_adjusted_6min_mean']=d0['close_adjusted_6min_mean']-d0['open_adjusted_6min_mean']
#12 is commission, 10 is assume lost 1 tick
d0['PnL_after_commission_adjusted_6min_mean']=d0['close_open_diff_adjusted_6min_mean']*d0['bet']*10-12-10-10


#for below one case
#as triggered stop loss nearly market close, so above d0['revised_Stop']==9999999
#so assumed it settled at close
d0_check=d0.loc[(d0['revised_Stop']==9999999)&(d0['stop_indicate_new']!=0),:]





#frequency plot for days with stop
import matplotlib.pyplot as plt
diff_stop=d0.loc[d0['revised_Stop']!=9999999,'PnL_after_commission_adjusted_6min_mean'].values
plt.hist(d0.loc[d0['revised_Stop']!=9999999,'PnL_after_commission_adjusted_6min_mean'].values,normed=False,bins=30,range=(-6000,120))  #ravel=flatten
np.mean(d0.loc[d0['revised_Stop']!=9999999,'PnL_after_commission_adjusted_6min_mean'].values)
plt.title('Frequency plot of loss if triggered stop')
plt.xlabel('loss')
plt.ylabel('Frequency')

sum(diff_stop)/diff_stop.shape[0]


#frequency plot,difference between original close and close_adjusted_6min_mean, for days without stop
diff=d0.loc[d0['revised_Stop']==9999999,'close_adjusted_6min_mean'].values-d0.loc[d0['revised_Stop']==9999999,'Close_HSI'].values
plt.hist(diff,normed=False,bins=30,range=(-100,100))  #ravel=flatten
#plt.title('Frequency plot of difference between original exit price and randomized exit price without triggering stop')
plt.xlabel('difference')
plt.ylabel('Frequency')

np.mean(diff)








#frequency plot
diff_open_1=d0.loc[d0['Y_up_predict']==1,'open_adjusted_6min_mean'].values-d0.loc[d0['Y_up_predict']==1,'Open_HSI'].values
plt.hist(diff,normed=False,bins=30,range=(min(diff_open_1),max(diff_open_1)))  #ravel=flatten
#plt.title('Frequency plot of difference between original exit price and randomized exit price without triggering stop')
plt.xlabel('difference')
plt.ylabel('Frequency')

sum(diff_open_1)
diff_open_1.shape[0]


diff_open_0=d0.loc[d0['Y_up_predict']==0,'open_adjusted_6min_mean'].values-d0.loc[d0['Y_up_predict']==0,'Open_HSI'].values
plt.hist(diff,normed=False,bins=30,range=(min(diff_open_0),max(diff_open_0)))  #ravel=flatten
#plt.title('Frequency plot of difference between original exit price and randomized exit price without triggering stop')
plt.xlabel('difference')
plt.ylabel('Frequency')

sum(diff_open_0)
diff_open_0.shape[0]






#frequency plot
diff_close_1=d0.loc[(d0['Y_up_predict']==1)&(d0['revised_Stop']==9999999),'close_adjusted_6min_mean'].values-d0.loc[(d0['Y_up_predict']==1)&(d0['revised_Stop']==9999999),'Close_HSI'].values
plt.hist(diff_close_1,normed=False,bins=30,range=(min(diff_close_1),max(diff_close_1)))  #ravel=flatten
#plt.title('Frequency plot of difference between original exit price and randomized exit price without triggering stop')
plt.xlabel('difference')
plt.ylabel('Frequency')

sum(diff_close_1)  #so this is better
diff_close_1.shape[0]


diff_close_0=d0.loc[(d0['Y_up_predict']==0)&(d0['revised_Stop']==9999999),'close_adjusted_6min_mean'].values-d0.loc[(d0['Y_up_predict']==0)&(d0['revised_Stop']==9999999),'Close_HSI'].values
plt.hist(diff_close_0,normed=False,bins=30,range=(min(diff_close_0),max(diff_close_0)))  #ravel=flatten
#plt.title('Frequency plot of difference between original exit price and randomized exit price without triggering stop')
plt.xlabel('difference')
plt.ylabel('Frequency')

sum(diff_close_0)
diff_close_0.shape[0]



sum(diff_open_1)*-1
sum(diff_open_0)
sum(diff_close_1)
sum(diff_close_0)*-1



#investigate different bewteen single bet and block bet
sum(d0['PnL_after_commission_adjusted_6min_mean'])

sum(d0['PnL_after_commission'])


d0['diff_block_single']=d0['PnL_after_commission_adjusted_6min_mean']-d0['PnL_after_commission']

sum(d0['diff_block_single'])

d0['opendiff_block_single']=d0['open_adjusted_6min_mean']-d0['Open_HSI']
d0.loc[d0['stop_indicate_new']==0,'closediff_block_single']=d0['close_adjusted_6min_mean']-d0['Close_HSI']


a_check=data2.loc[data2['Date2']=='2015-07-09',:]

d0.loc[d0['stop_indicate']!=0,:].shape[0]
d0.loc[d0['stop_indicate_new']!=0,:].shape[0]


data_check=data.head(1000)
data_1min=data.groupby(['Date2']).nth(0)
np.mean(data_1min.TotalVolume)

data_2min=data.groupby(['Date2']).nth(1)
np.mean(data_2min.TotalVolume)

data_2min=data.groupby(['Date2']).nth(2)
np.mean(data_2min.TotalVolume)

data_last1min=data.groupby(['Date2']).nth(-1)
np.mean(data_last1min.TotalVolume)

data_last2min=data.groupby(['Date2']).nth(-2)
np.mean(data_last2min.TotalVolume)

data_last2min=data.groupby(['Date2']).nth(-3)
np.mean(data_last2min.TotalVolume)












################################################################################################################
###############################################type1############################################################
################################################################################################################

#use 150 tick stop profit and exit at 10am

entry_number_of_bar=1  #1 is (9:15)   16 is (9:30)
exit_number_of_bar=45 #45 30 15
profit_target=150 #150 100 50

data_use=data.loc[data['Date2']=='2023-02-08',:]
def split_interval(data_use):
    data_use2=data_use.sort_values(by=['Date1'],ascending=True)
    data_use2=data_use2.reset_index(drop=True)
    #data_use2=data_use2.head(exit_number_of_bar)
    data_use2=data_use2[entry_number_of_bar-1:exit_number_of_bar].copy()    
    date=data_use2['Date2'].values[0]    
    open1=data_use2['Open'].values[0]     
    high1=np.max(data_use2['High'].values)
    low1=np.min(data_use2['Low'].values)
    close1=data_use2['Close'].values[-1]

    output=pd.DataFrame({'Date2':[date],'Open_HSI':[open1],'High_HSI':[high1],'Low_HSI':[low1],'Close_HSI':[close1]})
    print(date)
    return output

d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_15_to_30.csv"))
temp1=data.groupby("Date2").apply(lambda x:split_interval(x.reset_index(drop=True)))
temp1=temp1.reset_index(drop=True)
d0=pd.merge(temp1,d0[['Date2','Y_up_predict','DateNum','bet']].copy(),how='left',on=['Date2'])
d0=d0.loc[~pd.isnull(d0['bet']),:].copy()
d0=d0.loc[d0['Close_HSI']!=0,:].copy()  #may be zero data issue

d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet']].copy()
d0.dtypes
d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
 
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

#indicate if triggered stop
d0.loc[(d0['Y_up_predict']==1)&(d0['High_HSI']-d0['Open_HSI']>=profit_target),'profit_indicate_up']=1
d0['profit_indicate_up']=d0['profit_indicate_up'].fillna(0)

d0.loc[(d0['Y_up_predict']==0)&(d0['Open_HSI']-d0['Low_HSI']>=profit_target),'profit_indicate_down']=1
d0['profit_indicate_down']=d0['profit_indicate_down'].fillna(0)
d0['profit_indicate']=d0['profit_indicate_up']-d0['profit_indicate_down']

#for hong kong
d0.loc[d0['profit_indicate']!=0,'PnL']=profit_target*10
d0.loc[d0['profit_indicate']==0,'PnL']=(d0['Close_HSI']-d0['Open_HSI'])*d0['bet']*10
d0['PnL_after_commission']=d0['PnL']-7.62
d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
d0_check=d0.loc[d0['Date2_y']=='2022',:]

print(d0.groupby(['Date2_y']).tail(1)[['Date2','PnL_after_commission_cum']])
print(d0.groupby(['Date2_y']).tail(1)[['PnL_after_commission_cum']].values.mean())
d00=d0[['Date2','PnL_after_commission']].copy()
d00=d00.rename(columns={'PnL_after_commission':'PnL_after_commission1'})



#version for stop loss and exit at 10am
entry_number_of_bar=1  #1 is (9:15)   16 is (9:30)
exit_number_of_bar=45 #45 30 15
stop_level=30   #50

data_use=data.loc[data['Date2']=='2023-02-08',:]
def split_interval(data_use):
    data_use2=data_use.sort_values(by=['Date1'],ascending=True)
    data_use2=data_use2.reset_index(drop=True)
    #data_use2=data_use2.head(exit_number_of_bar)
    data_use2=data_use2[entry_number_of_bar-1:exit_number_of_bar].copy()
    date=data_use2['Date2'].values[0]    
    open1=data_use2['Open'].values[0]     
    high1=np.max(data_use2['High'].values)
    low1=np.min(data_use2['Low'].values)
    close1=data_use2['Close'].values[-1]
    output=pd.DataFrame({'Date2':[date],'Open_HSI':[open1],'High_HSI':[high1],'Low_HSI':[low1],'Close_HSI':[close1]})
    print(date)
    return output

d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))
temp1=data.groupby("Date2").apply(lambda x:split_interval(x.reset_index(drop=True)))
temp1=temp1.reset_index(drop=True)
d0=pd.merge(temp1,d0[['Date2','Y_up_predict','DateNum','bet']].copy(),how='left',on=['Date2'])
d0=d0.loc[~pd.isnull(d0['bet']),:].copy()
d0=d0.loc[d0['Close_HSI']!=0,:].copy()  #may be zero data issue

d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet']].copy()
d0.dtypes
d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

#indicate if triggered stop
d0.loc[(d0['Y_up_predict']==1)&(d0['Low_HSI']<=d0['Open_HSI']-stop_level),'stop_indicate_up']=1
d0['stop_indicate_up']=d0['stop_indicate_up'].fillna(0)
d0.loc[(d0['Y_up_predict']==0)&(d0['High_HSI']>=d0['Open_HSI']+stop_level),'stop_indicate_down']=1
d0['stop_indicate_down']=d0['stop_indicate_down'].fillna(0)
d0['stop_indicate']=d0['stop_indicate_up']-d0['stop_indicate_down']

#for hong kong
d0.loc[d0['stop_indicate']!=0,'PnL']=-1*stop_level*10
d0.loc[d0['stop_indicate']==0,'PnL']=(d0['Close_HSI']-d0['Open_HSI'])*d0['bet']*10
d0['PnL_after_commission']=d0['PnL']-7.62
d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
d0_check=d0.loc[d0['Date2_y']=='2019',:]

print(d0.groupby(['Date2_y']).tail(1)[['Date2','PnL_after_commission_cum']])
print(d0.groupby(['Date2_y']).tail(1)[['PnL_after_commission_cum']].values.mean())

d0['PnL_after_commission2']=d0['PnL_after_commission'].copy()
del d0['PnL_after_commission']
d0=pd.merge(d0,d00,how='left',on=['Date2'])
d0['PnL_after_commission']=(d0['PnL_after_commission1']+d0['PnL_after_commission2'])/2
d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
print(d0.groupby(['Date2_y']).tail(1)[['PnL_after_commission_cum']].values.mean())





















################################################################################################################
###############################################type2############################################################
################################################################################################################

#version for stop loss and exit at 10am
entry_number_of_bar=16  #1 is (9:15)   16 is (9:30)
exit_number_of_bar=999999 #45 30 15
stop_level=70   #50

data_use=data.loc[data['Date2']=='2023-02-08',:]
def split_interval(data_use):
    data_use2=data_use.sort_values(by=['Date1'],ascending=True)
    data_use2=data_use2.reset_index(drop=True)
    #data_use2=data_use2.head(exit_number_of_bar)
    data_use2=data_use2[entry_number_of_bar-1:exit_number_of_bar].copy()
    date=data_use2['Date2'].values[0]    
    open1=data_use2['Open'].values[0]     
    high1=np.max(data_use2['High'].values)
    low1=np.min(data_use2['Low'].values)
    close1=data_use2['Close'].values[-1]
    output=pd.DataFrame({'Date2':[date],'Open_HSI':[open1],'High_HSI':[high1],'Low_HSI':[low1],'Close_HSI':[close1]})
    print(date)
    return output

#d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))
d0=pd.read_csv(os.path.join(folder_path,"all_prediction_15_to_30.csv"))
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_phase1.csv"))

temp1=data.groupby("Date2").apply(lambda x:split_interval(x.reset_index(drop=True)))
temp1=temp1.reset_index(drop=True)
d0=pd.merge(temp1,d0[['Date2','Y_up_predict','DateNum','bet']].copy(),how='left',on=['Date2'])
d0=d0.loc[~pd.isnull(d0['bet']),:].copy()
d0=d0.loc[d0['Close_HSI']!=0,:].copy()  #may be zero data issue

d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet']].copy()
d0.dtypes
d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

#indicate if triggered stop
d0.loc[(d0['Y_up_predict']==1)&(d0['Low_HSI']<=d0['Open_HSI']-stop_level),'stop_indicate_up']=1
d0['stop_indicate_up']=d0['stop_indicate_up'].fillna(0)
d0.loc[(d0['Y_up_predict']==0)&(d0['High_HSI']>=d0['Open_HSI']+stop_level),'stop_indicate_down']=1
d0['stop_indicate_down']=d0['stop_indicate_down'].fillna(0)
d0['stop_indicate']=d0['stop_indicate_up']-d0['stop_indicate_down']

#for hong kong
d0.loc[d0['stop_indicate']!=0,'PnL']=-1*stop_level*10
d0.loc[d0['stop_indicate']==0,'PnL']=(d0['Close_HSI']-d0['Open_HSI'])*d0['bet']*10
d0['PnL_after_commission']=d0['PnL']-7.62
d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
d0_check=d0.loc[d0['Date2_y']=='2019',:]

print(d0.groupby(['Date2_y']).tail(1)[['Date2','PnL_after_commission_cum']])
print(d0.groupby(['Date2_y']).tail(1)[['PnL_after_commission_cum']].values.mean())

d00=d0[['Date2','PnL_after_commission']].copy()
d00=d00.rename(columns={'PnL_after_commission':'PnL_after_commission1'})



#version for stop loss and exit at 10am
entry_number_of_bar=1  #1 is (9:15)   16 is (9:30)
exit_number_of_bar=99999#45 30 15
stop_level=50   #50

data_use=data.loc[data['Date2']=='2023-02-08',:]
def split_interval(data_use):
    data_use2=data_use.sort_values(by=['Date1'],ascending=True)
    data_use2=data_use2.reset_index(drop=True)
    #data_use2=data_use2.head(exit_number_of_bar)
    data_use2=data_use2[entry_number_of_bar-1:exit_number_of_bar].copy()
    date=data_use2['Date2'].values[0]    
    open1=data_use2['Open'].values[0]     
    high1=np.max(data_use2['High'].values)
    low1=np.min(data_use2['Low'].values)
    close1=data_use2['Close'].values[-1]
    output=pd.DataFrame({'Date2':[date],'Open_HSI':[open1],'High_HSI':[high1],'Low_HSI':[low1],'Close_HSI':[close1]})
    print(date)
    return output

d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))
temp1=data.groupby("Date2").apply(lambda x:split_interval(x.reset_index(drop=True)))
temp1=temp1.reset_index(drop=True)
d0=pd.merge(temp1,d0[['Date2','Y_up_predict','DateNum','bet']].copy(),how='left',on=['Date2'])
d0=d0.loc[~pd.isnull(d0['bet']),:].copy()
d0=d0.loc[d0['Close_HSI']!=0,:].copy()  #may be zero data issue

d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet']].copy()
d0.dtypes
d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

#indicate if triggered stop
d0.loc[(d0['Y_up_predict']==1)&(d0['Low_HSI']<=d0['Open_HSI']-stop_level),'stop_indicate_up']=1
d0['stop_indicate_up']=d0['stop_indicate_up'].fillna(0)
d0.loc[(d0['Y_up_predict']==0)&(d0['High_HSI']>=d0['Open_HSI']+stop_level),'stop_indicate_down']=1
d0['stop_indicate_down']=d0['stop_indicate_down'].fillna(0)
d0['stop_indicate']=d0['stop_indicate_up']-d0['stop_indicate_down']

#for hong kong
d0.loc[d0['stop_indicate']!=0,'PnL']=-1*stop_level*10
d0.loc[d0['stop_indicate']==0,'PnL']=(d0['Close_HSI']-d0['Open_HSI'])*d0['bet']*10
d0['PnL_after_commission']=d0['PnL']-7.62
d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
d0_check=d0.loc[d0['Date2_y']=='2019',:]

print(d0.groupby(['Date2_y']).tail(1)[['Date2','PnL_after_commission_cum']])
print(d0.groupby(['Date2_y']).tail(1)[['PnL_after_commission_cum']].values.mean())

d0['PnL_after_commission2']=d0['PnL_after_commission'].copy()
del d0['PnL_after_commission']
d0=pd.merge(d0,d00,how='left',on=['Date2'])

d0=d0.loc[~pd.isnull(d0['PnL_after_commission1']),:].copy()

#d0['PnL_after_commission']=(d0['PnL_after_commission1']+d0['PnL_after_commission2'])/2
d0['PnL_after_commission']=(d0['PnL_after_commission1']+d0['PnL_after_commission2'])/2
d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
print(d0.groupby(['Date2_y']).tail(1)[['PnL_after_commission_cum']].values.mean())


sum(d0['PnL_after_commission1']>0)/d0.shape[0]
sum(d0['PnL_after_commission2']>0)/d0.shape[0]
sum(d0['PnL_after_commission']>0)/d0.shape[0]





















################################################################################################################
###############################################type3############################################################
################################################################################################################

#15_to_30
entry_number_of_bar=16  #1 is (9:15)   16 is (9:30)
exit_number_of_bar=25 #45 30 15
stop_level=70   #50

data_use=data.loc[data['Date2']=='2023-03-24',:]
def split_interval(data_use):
    data_use2=data_use.sort_values(by=['Date1'],ascending=True)
    data_use2=data_use2.reset_index(drop=True)
    #data_use2=data_use2.head(exit_number_of_bar)
    data_use2=data_use2[entry_number_of_bar-1:exit_number_of_bar].copy()
    date=data_use2['Date2'].values[0]    
    open1=data_use2['Open'].values[0]     
    high1=np.max(data_use2['High'].values)
    low1=np.min(data_use2['Low'].values)
    close1=data_use2['Close'].values[-1]
    output=pd.DataFrame({'Date2':[date],'Open_HSI':[open1],'High_HSI':[high1],'Low_HSI':[low1],'Close_HSI':[close1]})
    print(date)
    return output
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))
d0=pd.read_csv(os.path.join(folder_path,"all_prediction_15_to_30.csv"))
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_phase1.csv"))
temp1=data.groupby("Date2").apply(lambda x:split_interval(x.reset_index(drop=True)))
temp1=temp1.reset_index(drop=True)
d0=pd.merge(temp1,d0[['Date2','Y_up_predict','DateNum','bet']].copy(),how='left',on=['Date2'])



#d0_minA=pd.read_csv(os.path.join(folder_path,"all_prediction_hsi_minuteA.csv"))
#d0=pd.merge(d0,d0_minA[['Date2','bet_min16']].copy(),how='left',on=['Date2'])
#d0=d0.loc[~pd.isnull(d0['bet_min16']),:].copy()
#del d0['bet']
#d0=d0.rename(columns={'bet_min16':'bet'})


d0=d0.loc[~pd.isnull(d0['bet']),:].copy()
d0=d0.loc[d0['Close_HSI']!=0,:].copy()  #may be zero data issue

d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet']].copy()
d0.dtypes
d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

#indicate if triggered stop
d0.loc[(d0['Y_up_predict']==1)&(d0['Low_HSI']<=d0['Open_HSI']-stop_level),'stop_indicate_up']=1
d0['stop_indicate_up']=d0['stop_indicate_up'].fillna(0)
d0.loc[(d0['Y_up_predict']==0)&(d0['High_HSI']>=d0['Open_HSI']+stop_level),'stop_indicate_down']=1
d0['stop_indicate_down']=d0['stop_indicate_down'].fillna(0)
d0['stop_indicate']=d0['stop_indicate_up']-d0['stop_indicate_down']

#for hong kong
d0.loc[d0['stop_indicate']!=0,'PnL']=-1*stop_level*10
d0.loc[d0['stop_indicate']==0,'PnL']=(d0['Close_HSI']-d0['Open_HSI'])*d0['bet']*10
d0['PnL_after_commission']=d0['PnL']-7.62
d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
d0_check=d0.loc[d0['Date2_y']=='2019',:]

print(d0.groupby(['Date2_y']).tail(1)[['Date2','PnL_after_commission_cum']])
print(d0.groupby(['Date2_y']).tail(1)[['PnL_after_commission_cum']].values.mean())

d00=d0[['Date2','PnL_after_commission','bet']].copy()
d00=d00.rename(columns={'PnL_after_commission':'PnL_after_commission1','bet':'bet1'})



#version for stop loss and exit at 10am
entry_number_of_bar=1  #1 is (9:15)   16 is (9:30)
exit_number_of_bar=10 #45 30 15
stop_level=50   #50

data_use=data.loc[data['Date2']=='2023-03-20',:]
def split_interval(data_use):
    data_use2=data_use.sort_values(by=['Date1'],ascending=True)
    data_use2=data_use2.reset_index(drop=True)
    #data_use2=data_use2.head(exit_number_of_bar)
    data_use2=data_use2[entry_number_of_bar-1:exit_number_of_bar].copy()
    date=data_use2['Date2'].values[0]    
    open1=data_use2['Open'].values[0]     
    high1=np.max(data_use2['High'].values)
    low1=np.min(data_use2['Low'].values)
    close1=data_use2['Close'].values[-1]
    output=pd.DataFrame({'Date2':[date],'Open_HSI':[open1],'High_HSI':[high1],'Low_HSI':[low1],'Close_HSI':[close1]})
    print(date)
    return output

d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_15_to_30.csv"))
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_phase1.csv"))

temp1=data.groupby("Date2").apply(lambda x:split_interval(x.reset_index(drop=True)))
temp1=temp1.reset_index(drop=True)
d0=pd.merge(temp1,d0[['Date2','Y_up_predict','DateNum','bet']].copy(),how='left',on=['Date2'])
d0=d0.loc[~pd.isnull(d0['bet']),:].copy()
d0=d0.loc[d0['Close_HSI']!=0,:].copy()  #may be zero data issue

d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet']].copy()
d0.dtypes
d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

#indicate if triggered stop
d0.loc[(d0['Y_up_predict']==1)&(d0['Low_HSI']<=d0['Open_HSI']-stop_level),'stop_indicate_up']=1
d0['stop_indicate_up']=d0['stop_indicate_up'].fillna(0)
d0.loc[(d0['Y_up_predict']==0)&(d0['High_HSI']>=d0['Open_HSI']+stop_level),'stop_indicate_down']=1
d0['stop_indicate_down']=d0['stop_indicate_down'].fillna(0)
d0['stop_indicate']=d0['stop_indicate_up']-d0['stop_indicate_down']

#for hong kong
d0.loc[d0['stop_indicate']!=0,'PnL']=-1*stop_level*10
d0.loc[d0['stop_indicate']==0,'PnL']=(d0['Close_HSI']-d0['Open_HSI'])*d0['bet']*10
d0['PnL_after_commission']=d0['PnL']-7.62
d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
d0_check=d0.loc[d0['Date2_y']=='2019',:]

print(d0.groupby(['Date2_y']).tail(1)[['Date2','PnL_after_commission_cum']])
print(d0.groupby(['Date2_y']).tail(1)[['PnL_after_commission_cum']].values.mean())

d01=d0[['Date2','PnL_after_commission','bet']].copy()
d01=d01.rename(columns={'PnL_after_commission':'PnL_after_commission2','bet':'bet2'})





#read minuteA
d0=pd.read_csv(os.path.join(folder_path,"all_prediction_hsi_minuteA.csv"))

d0=d0.loc[d0['Date2']>='2011-01-01',:].copy()

d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d")) #string to dt, dt to string
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m")) 
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

#indicate if triggered stop
d0['PnL_after_commission']=d0['PnL']*10-7.62*0
d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
d0_check=d0.loc[d0['Date2_y']=='2019',:]


print(d0.groupby(['Date2_y']).tail(1)[['Date2','PnL_after_commission_cum']])
print(d0.groupby(['Date2_y']).tail(1)[['PnL_after_commission_cum']].values.mean())

d02=d0[['Date2','PnL_after_commission','bet_min1','bet_min16']].copy()
d02=d02.rename(columns={'PnL_after_commission':'PnL_after_commission3'})






#version for stop loss and exit at 10am
entry_number_of_bar=1  #1 is (9:15)   16 is (9:30)
exit_number_of_bar=99999#45 30 15
stop_level=50   #50

data_use=data.loc[data['Date2']=='2023-02-08',:]
def split_interval(data_use):
    data_use2=data_use.sort_values(by=['Date1'],ascending=True)
    data_use2=data_use2.reset_index(drop=True)
    #data_use2=data_use2.head(exit_number_of_bar)
    data_use2=data_use2[entry_number_of_bar-1:exit_number_of_bar].copy()
    date=data_use2['Date2'].values[0]    
    open1=data_use2['Open'].values[0]     
    high1=np.max(data_use2['High'].values)
    low1=np.min(data_use2['Low'].values)
    close1=data_use2['Close'].values[-1]
    output=pd.DataFrame({'Date2':[date],'Open_HSI':[open1],'High_HSI':[high1],'Low_HSI':[low1],'Close_HSI':[close1]})
    print(date)
    return output

d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))
temp1=data.groupby("Date2").apply(lambda x:split_interval(x.reset_index(drop=True)))
temp1=temp1.reset_index(drop=True)

#check open diff between IB and HKEX 
temp1_check=temp1.rename(columns={'Open_HSI':'Open_HSI_min'})
d0_check=pd.merge(temp1_check,d0[['Date2','Open_HSI']].copy(),how='left',on=['Date2'])
d0_check['diff']=d0_check['Open_HSI']-d0_check['Open_HSI_min']

d0=pd.merge(temp1,d0[['Date2','Y_up_predict','DateNum','bet']].copy(),how='left',on=['Date2'])
d0=d0.loc[~pd.isnull(d0['bet']),:].copy()
d0=d0.loc[d0['Close_HSI']!=0,:].copy()  #may be zero data issue

d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet']].copy()
d0.dtypes
d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

#indicate if triggered stop
d0.loc[(d0['Y_up_predict']==1)&(d0['Low_HSI']<=d0['Open_HSI']-stop_level),'stop_indicate_up']=1
d0['stop_indicate_up']=d0['stop_indicate_up'].fillna(0)
d0.loc[(d0['Y_up_predict']==0)&(d0['High_HSI']>=d0['Open_HSI']+stop_level),'stop_indicate_down']=1
d0['stop_indicate_down']=d0['stop_indicate_down'].fillna(0)
d0['stop_indicate']=d0['stop_indicate_up']-d0['stop_indicate_down']

#for hong kong
d0.loc[d0['stop_indicate']!=0,'PnL']=-1*stop_level*10
d0.loc[d0['stop_indicate']==0,'PnL']=(d0['Close_HSI']-d0['Open_HSI'])*d0['bet']*10
d0['PnL_after_commission']=d0['PnL']-7.62
d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
d0_check=d0.loc[d0['Date2_y']=='2019',:]

print(d0.groupby(['Date2_y']).tail(1)[['Date2','PnL_after_commission_cum']])
print(d0.groupby(['Date2_y']).tail(1)[['PnL_after_commission_cum']].values.mean())

d0['PnL_after_commission0']=d0['PnL_after_commission'].copy()
del d0['PnL_after_commission']

d0['bet0']=d0['bet'].copy()




d0=pd.merge(d0,d00,how='left',on=['Date2'])
d0=d0.loc[~pd.isnull(d0['PnL_after_commission1']),:].copy()

d0=pd.merge(d0,d01,how='left',on=['Date2'])
d0=d0.loc[~pd.isnull(d0['PnL_after_commission2']),:].copy()

d0=pd.merge(d0,d02,how='left',on=['Date2'])
d0['PnL_after_commission3']=d0['PnL_after_commission3'].fillna(0) #cox some day may not have bet

d0.columns.values




#d0['PnL_after_commission12']=d0['PnL_after_commission1']+d0['PnL_after_commission2']
#d0['PnL_after_commission12_cum']=d0.groupby(['Date2_y'])['PnL_after_commission12'].cumsum()


#d0['PnL_after_commission']=d0['PnL_after_commission1']*2*5+d0['PnL_after_commission2']*2*5+d0['PnL_after_commission0']*0*5

d0['PnL_after_commission']=(d0['PnL_after_commission1']*1*1+\
                           d0['PnL_after_commission2']*1*1+\
                           d0['PnL_after_commission3']*1*0+\
                           d0['PnL_after_commission0']*1*0)*5

d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()

print(d0.groupby(['Date2_y']).tail(1)[['Date2','PnL_after_commission_cum']])
print(d0.groupby(['Date2_y']).tail(1)[['PnL_after_commission_cum']].values.mean())


sum(d0['PnL_after_commission1']>0)/d0.shape[0]  
sum(d0['PnL_after_commission2']>0)/d0.shape[0]
#sum(d0['PnL_after_commission12']>0)/d0.shape[0]
sum(d0['PnL_after_commission3']>0)/d0.shape[0]
sum(d0['PnL_after_commission']>0)/d0.shape[0]


d0.PnL_after_commission0.corr(d0.PnL_after_commission3)
d0.PnL_after_commission0.corr(d0.PnL_after_commission1)
d0.PnL_after_commission0.corr(d0.PnL_after_commission2)
d0.PnL_after_commission3.corr(d0.PnL_after_commission1+d0.PnL_after_commission2)


total_count=sum(~pd.isnull(d0.bet_min1))
sum(d0['bet_min1']==d0['bet1'])/total_count
sum(d0['bet_min1']==d0['bet2'])/total_count

total_count=sum(~pd.isnull(d0.bet_min16))
sum(d0['bet_min16']==d0['bet1'])/total_count
sum(d0['bet_min16']==d0['bet2'])/total_count

sum(d0.PnL_after_commission3>0)/sum(d0.PnL_after_commission1<0)
sum(d0.PnL_after_commission3>0)/sum(d0.PnL_after_commission2<0)
sum(d0.PnL_after_commission3>0)/sum(d0.PnL_after_commission0<0)


d0_SR,monthly_summary,monthly_summary_pnl_asas,monthly_summary_downside_asas=gen_pnl(d0)










################################################################################################################
###############################################type4############################################################
################################################################################################################
#both profit target and stop loss
entry_number_of_bar=1  #1 is (9:15)   16 is (9:30)
exit_number_of_bar=45 #45 30 15
stop_level=30  #50
profit_target=300  #50

data_use=temp1.loc[data['Date2']=='2023-02-24',:]
data_use=temp1.loc[data['Date2']=='2011-01-04',:]
data_use=temp1.loc[data['Date2']=='2023-03-01',:]
def split_interval(data_use):
    data_use2=data_use.sort_values(by=['Date1'],ascending=True)
    data_use2=data_use2.reset_index(drop=True)
    #data_use2=data_use2.head(exit_number_of_bar)
    data_use2=data_use2[entry_number_of_bar-1:exit_number_of_bar].copy()
    
    bet=data_use2['bet'].values[0]   
    entry_price=data_use2['Open'].values[0]    
    date=data_use2['Date2'].values[0]    
    close1=data_use2['Close'].values[-1]
    data_use2['high_entry']=data_use2['High']-entry_price
    data_use2['entry_low']=entry_price-data_use2['Low']

    s=999999
    p=999999    
    if bet==1:
        data_use2.loc[data_use2['high_entry']>=profit_target,'profit']=1
        data_use2.loc[data_use2['entry_low']>=stop_level,'stop']=1
        if len(np.where(data_use2['stop'].values==1)[0])!=0:
            s=np.where(data_use2['stop'].values==1)[0][0] 
        if len(np.where(data_use2['profit'].values==1)[0])!=0:
            p=np.where(data_use2['profit'].values==1)[0][0]             
        if s<p:
            exit_price=entry_price-stop_level
        if (s==p)&(s!=999999):
            exit_price=entry_price-stop_level   
        if s>p:
            exit_price=entry_price+profit_target      
        if (s==999999)&(p==999999):
            exit_price=close1 

    if bet==-1:
        data_use2.loc[data_use2['high_entry']>=stop_level,'stop']=1
        data_use2.loc[data_use2['entry_low']>=profit_target,'profit']=1
        if len(np.where(data_use2['stop'].values==1)[0])!=0:
            s=np.where(data_use2['stop'].values==1)[0][0] 
        if len(np.where(data_use2['profit'].values==1)[0])!=0:
            p=np.where(data_use2['profit'].values==1)[0][0]             
        if s<p:
            exit_price=entry_price+stop_level
        if (s==p)&(s!=999999):
            exit_price=entry_price+stop_level   
        if s>p:
            exit_price=entry_price-profit_target      
        if (s==999999)&(p==999999):
            exit_price=close1 

    PnL_after_commission=(exit_price-entry_price)*10*bet-7.62
    output=pd.DataFrame({'Date2':[date],'PnL_after_commission':[PnL_after_commission],'bet':[bet],'s':[s],'p':[p]})
    print(date)
    
    return output


d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_15_to_30.csv"))
#d0=pd.read_csv(os.path.join(folder_path,"all_prediction_phase1.csv"))

temp1=pd.merge(data,d0[['Date2','Y_up_predict','DateNum','bet']].copy(),how='left',on=['Date2'])
temp1=temp1.loc[~pd.isnull(temp1['bet']),:].copy()

temp1['stop']=0
temp1['profit']=0

temp2=temp1.groupby("Date2").apply(lambda x:split_interval(x.reset_index(drop=True)))
temp2=temp2.reset_index(drop=True)

d0=temp2.copy()
d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
print(d0.groupby(['Date2_y']).tail(1)[['PnL_after_commission_cum']].values.mean())

sum(d0['PnL_after_commission']>0)/d0.shape[0]









################################################################################################################
###############################################use universal indicator############################################################
################################################################################################################
import talib
from talib import abstract
hsi_y = read_excel('hsi_y.xlsx','Sheet1')
hsi_y_temp=hsi_y[['Date2','Open_HSI','Close_HSI']].copy()
hsi_y_temp=hsi_y_temp.loc[hsi_y_temp['Open_HSI']!=100,:].copy()
hsi_y_temp=hsi_y_temp.reset_index(drop=True)


hsi_y_temp['year_cohord']=hsi_y_temp['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y")).astype(int)
hsi_y_temp=hsi_y_temp.rename(columns={'Close_HSI':'close'})
hsi_y_temp['ema_10']=abstract.EMA(hsi_y_temp,7)
hsi_y_temp['f2']=(hsi_y_temp['close']-hsi_y_temp['ema_10'])/hsi_y_temp['ema_10']

year_min=hsi_y_temp['year_cohord'].unique()
year_min=min(year_min)
year_min_plus=year_min+2 #make sure use at least 2 year historical data


#use emprical distribution
target_variable='f2'
new_variable='Indicator'+'_'+'fhsi'     #new variable name
distinct_year=hsi_y_temp['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=year_min_plus] 
yy=2020
output=pd.DataFrame([])
for yy in distinct_year:
    data_use=hsi_y_temp.loc[(hsi_y_temp['year_cohord']>=yy-100)&(hsi_y_temp['year_cohord']<yy),target_variable].values
    data_use=data_use[~np.isnan(data_use)]
    data_use=pd.DataFrame(data_use)
    data_use.columns=['historical_indicator']
    data_use['key']='k'
    data_use_count=data_use.shape[0]
    
    temp=hsi_y_temp.loc[hsi_y_temp['year_cohord']==yy,['Date2',target_variable]].copy()
    temp['key']='k'
    
    temp=pd.merge(temp,data_use,how='left',on='key')
    temp['check']=1*(temp.historical_indicator<=temp[target_variable])
    
    temp=temp.groupby(['Date2'])['check'].sum()  
    temp=100*temp/data_use_count
    temp=pd.DataFrame(temp)
    temp=temp.reset_index(drop=False)
    temp.columns=['Date2',new_variable]
    output=output.append(temp)

output[new_variable]=output[new_variable].shift(1)



#version for stop loss and exit at 10am
entry_number_of_bar=46  #1 is (9:15)   16 is (9:30)
exit_number_of_bar=9999999#45 30 15
stop_level=1000000   #50

data_use=data.loc[data['Date2']=='2023-02-08',:]
def split_interval(data_use):
    data_use2=data_use.sort_values(by=['Date1'],ascending=True)
    data_use2=data_use2.reset_index(drop=True)
    #data_use2=data_use2.head(exit_number_of_bar)
    data_use2=data_use2[entry_number_of_bar-1:exit_number_of_bar].copy()
    date=data_use2['Date2'].values[0]    
    open1=data_use2['Open'].values[0]     
    high1=np.max(data_use2['High'].values)
    low1=np.min(data_use2['Low'].values)
    close1=data_use2['Close'].values[-1]
    output=pd.DataFrame({'Date2':[date],'Open_HSI':[open1],'High_HSI':[high1],'Low_HSI':[low1],'Close_HSI':[close1]})
    print(date)
    return output

d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))

d0=pd.merge(d0,output[['Date2',new_variable]].copy(),how='left',on=['Date2'])

#del d0['bet']
#d0.loc[d0[new_variable]<=30,'bet']=1
#d0.loc[d0[new_variable]>=70,'bet']=-1
#d0=d0.loc[~pd.isnull(d0['bet']),:].copy()

d0=d0.loc[((d0['bet']==1)&(d0[new_variable]<=20))|((d0['bet']==-1)&(d0[new_variable]>80)),:].copy()


temp1=data.groupby("Date2").apply(lambda x:split_interval(x.reset_index(drop=True)))
temp1=temp1.reset_index(drop=True)
d0=pd.merge(temp1,d0[['Date2','Y_up_predict','DateNum','bet']].copy(),how='left',on=['Date2'])
d0=d0.loc[~pd.isnull(d0['bet']),:].copy()
d0=d0.loc[d0['Close_HSI']!=0,:].copy()  #may be zero data issue

d0=d0[['Date2', 'Y_up_predict','Open_HSI', 'High_HSI', 'Low_HSI', 'Close_HSI','DateNum','bet']].copy()
d0.dtypes
d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

#indicate if triggered stop
d0.loc[(d0['Y_up_predict']==1)&(d0['Low_HSI']<=d0['Open_HSI']-stop_level),'stop_indicate_up']=1
d0['stop_indicate_up']=d0['stop_indicate_up'].fillna(0)
d0.loc[(d0['Y_up_predict']==0)&(d0['High_HSI']>=d0['Open_HSI']+stop_level),'stop_indicate_down']=1
d0['stop_indicate_down']=d0['stop_indicate_down'].fillna(0)
d0['stop_indicate']=d0['stop_indicate_up']-d0['stop_indicate_down']

#for hong kong
d0.loc[d0['stop_indicate']!=0,'PnL']=-1*stop_level*10
d0.loc[d0['stop_indicate']==0,'PnL']=(d0['Close_HSI']-d0['Open_HSI'])*d0['bet']*10
d0['PnL_after_commission']=d0['PnL']-7.62
d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()
d0_check=d0.loc[d0['Date2_y']=='2019',:]

print(d0.groupby(['Date2_y']).tail(1)[['Date2','PnL_after_commission_cum']])
print(d0.groupby(['Date2_y']).tail(1)[['PnL_after_commission_cum']].values.mean())



sum(d0['PnL_after_commission']>0)/d0.shape[0]























































#incorportae both full dat prediction and afternoon prediction
#if 
d0_afternoon=pd.read_csv(os.path.join(folder_path,"all_prediction_afternoon.csv"))
d0_afternoon=d0_afternoon.rename(columns={'Y_up_predict':'Y_up_predict_afternoon'})
d0=pd.merge(d0,d0_afternoon[['Date2','Y_up_predict_afternoon']],how='left',on='Date2')


stop_level=200


sum(d0['Y_up_predict']==d0['Y_up_predict_afternoon'])/d0.shape[0]


data2=data.loc[data['Date2']>='2011-01-01',:]

data2_check=data2.head(100)
data2=pd.merge(data2,d0,how='left',on=['Date2'])
data2_check=data2.tail(100)



sum(pd.isnull(data2['DateNum']))

#ii_old=all_links[963] #2014-12-01
#ii_old=all_links[1134] #2015-08-12 this is guess up with stop
#ii_old=all_links[6] #2011-01-11 this is guess up without stop
#ii_old=all_links[1] #2011-01-04 this is guess down with stop
#ii_old=all_links[0] 
#ii_old=all_links[2263] #2020-03-13


#logic is, if triggered morning stop loss, not enter if afternoon is the same direction as morning
#if morning not trigger stop loss, if afternoon same signal, keep the order till close
#if morning not trigger stop loss, if afternoon opposite signal,
#close morning order and enter afternoon order at 11:59:59
def morning_afternoon_strategy1(ii_old):
    ii=ii_old[1] #ii_old is tuple, 1 is the second item, stored the dataframe
    ii=ii.reset_index(drop=True)
    target_date=ii['Date2'].values[0]
    
    full_day_predict=ii['Y_up_predict'].values[0]
    afternoon_predict=ii['Y_up_predict_afternoon'].values[0]

    morning_stop=0
    afternoon_stop=0
    entry_morning=999999
    exit_morning=999999
    entry_afternoon=999999
    exit_afternoon=999999
    
    mor_after_either_one=0


    data_use2=ii.copy()
    data_use2['Date1_shift1']=data_use2['Date1'].shift(1)
    data_use2['time_diff']=data_use2['Date1']-data_use2['Date1_shift1']
    data_use2['time_diff_min']=data_use2['time_diff'].apply(lambda x:x.total_seconds()/60)


    ind=data_use2['time_diff_min']>=60
    ind=ind[ind==True]
    ind_size=len(ind)
    
    

    
    if ind_size!=0:
        ind=ind.index[0]
        
        #below use fix point
        data_use2_morning=data_use2.iloc[0:ind-1]  
        data_use2_afternoon1=data_use2.iloc[ind-1:]    
        
        open_morning=data_use2_morning['Open'].values[0]     
        high_morning=np.max(data_use2_morning['High'].values)
        low_morning=np.min(data_use2_morning['Low'].values)
        #close_morning=data_use2_morning['Open'].values[-1]    #use 1158 open
        
        open_afternoon=data_use2_afternoon1['Close'].values[0]   #use 1159 close
        high_afternoon=np.max(data_use2_afternoon1['High'].values[1:])
        low_afternoon=np.min(data_use2_afternoon1['Low'].values[1:])
        close_afternoon=data_use2_afternoon1['Close'].values[-1]
        
        
        #check if morning trigger stop loss
        #if triggered morning stop loss, not enter if afternoon is the same direction as morning
        if full_day_predict==1:
            entry_morning=open_morning
            stop_exit_morning=entry_morning-stop_level
            if low_morning<=stop_exit_morning:
                exit_morning=stop_exit_morning
                morning_stop=1
                
#                if (afternoon_predict==1):
#                    entry_afternoon=open_afternoon
#                    stop_exit_afternoon=entry_afternoon-stop_level  
#                    if low_afternoon<=stop_exit_afternoon:
#                        exit_afternoon=stop_exit_afternoon
#                        afternoon_stop=1
#                    else:
#                        exit_afternoon=close_afternoon
                        
                if (afternoon_predict==0):
                    entry_afternoon=open_afternoon
                    stop_exit_afternoon=entry_afternoon+stop_level
                    if high_afternoon>=stop_exit_afternoon:
                        exit_afternoon=stop_exit_afternoon
                        afternoon_stop=-1
                    else:
                        exit_afternoon=close_afternoon
            else:
                if (afternoon_predict==1)&(low_afternoon<=stop_exit_morning):
                    exit_morning=stop_exit_morning
                    afternoon_stop=1
                if (afternoon_predict==1)&(low_afternoon>stop_exit_morning):
                    exit_morning=close_afternoon                   
                if (afternoon_predict==0):
                    exit_morning=open_afternoon
                    entry_afternoon=open_afternoon
                    stop_exit_afternoon=entry_afternoon+stop_level
                    if high_afternoon>=stop_exit_afternoon:
                        exit_afternoon=stop_exit_afternoon
                        afternoon_stop=-1
                    else:
                        exit_afternoon=close_afternoon
                 
                    
        if full_day_predict==0:
            entry_morning=open_morning
            stop_exit_morning=entry_morning+stop_level
            if high_morning>=stop_exit_morning:
                exit_morning=stop_exit_morning
                morning_stop=-1
                
                if (afternoon_predict==1):
                    entry_afternoon=open_afternoon
                    stop_exit_afternoon=entry_afternoon-stop_level  
                    if low_afternoon<=stop_exit_afternoon:
                        exit_afternoon=stop_exit_afternoon
                        afternoon_stop=1
                    else:
                        exit_afternoon=close_afternoon
                        
#                if (afternoon_predict==0):
#                    entry_afternoon=open_afternoon
#                    stop_exit_afternoon=entry_afternoon+stop_level
#                    if high_afternoon>=stop_exit_afternoon:
#                        exit_afternoon=stop_exit_afternoon
#                        afternoon_stop=-1
#                    else:
#                        exit_afternoon=close_afternoon
            else:
                if (afternoon_predict==0)&(high_afternoon>=stop_exit_morning):
                    exit_morning=stop_exit_morning
                    afternoon_stop=-1
                if (afternoon_predict==0)&(high_afternoon<stop_exit_morning):
                    exit_morning=close_afternoon                   
                if (afternoon_predict==1):
                    exit_morning=open_afternoon
                    entry_afternoon=open_afternoon
                    stop_exit_afternoon=entry_afternoon-stop_level
                    if low_afternoon<=stop_exit_afternoon:
                        exit_afternoon=stop_exit_afternoon
                        afternoon_stop=1
                    else:
                        exit_afternoon=close_afternoon                
        
    else:
        mor_after_either_one=1
    

    output=pd.DataFrame({'Date2':[target_date],
                         'morning_stop':[morning_stop],
                         'afternoon_stop':[afternoon_stop],
                         'entry_morning':[entry_morning],
                         'exit_morning':[exit_morning],
                         'entry_afternoon':[entry_afternoon],
                         'exit_afternoon':[exit_afternoon],
                         'mor_after_either_one':[mor_after_either_one]})
    print("finished ",target_date)
    return output     










import requests
from concurrent.futures import ThreadPoolExecutor



all_links=list(data2.groupby("Date2"))
output=[]
with ThreadPoolExecutor(max_workers=20) as pool:
    output=list(pool.map(morning_afternoon_strategy1,all_links))


output_morning_afternoon=pd.DataFrame([])
for i in output:
    output_morning_afternoon=output_morning_afternoon.append(i)



d0=pd.merge(d0,output_morning_afternoon,how='left',on=['Date2'])




d0.dtypes

d0['bet_morning']=d0['Y_up_predict'].copy()
d0.loc[d0['Y_up_predict']==0,'bet_morning']=-1

d0['bet_afternoon']=d0['Y_up_predict_afternoon'].copy()
d0.loc[d0['Y_up_predict_afternoon']==0,'bet_afternoon']=-1

d0.loc[d0['mor_after_either_one']==0,'morning_pnl']=(d0['exit_morning']-d0['entry_morning'])*d0['bet_morning']*10-12

d0.loc[(d0['mor_after_either_one']==0)&(d0['entry_afternoon']!=999999),'afternoon_pnl']=(d0['exit_afternoon']-d0['entry_afternoon'])*d0['bet_afternoon']*10-12
d0['afternoon_pnl']=d0['afternoon_pnl'].fillna(0)

d0.loc[d0['mor_after_either_one']==0,'PnL_after_commission']=d0['morning_pnl']+d0['afternoon_pnl']




















#only use hsi time tie with stock market start and end
data_check=data.head(1000)
data_new_open=data.groupby(['Date2']).nth(15)
data_new_open=data_new_open.reset_index(drop=False)

data_new_close=data.groupby(['Date2']).nth(-30)
data_new_close=data_new_close.reset_index(drop=False)

d0=pd.merge(d0,data_new_open[['Date2','Open']].copy(),how='inner',on=['Date2'])
d0=pd.merge(d0,data_new_close[['Date2','Close']].copy(),how='inner',on=['Date2'])
d0=d0.rename(columns={'Open':'Open_15mins','Close':'Close_30mins'})
d0['close_open_diff_adjusted_6min_mean']=d0['Close_30mins']-d0['Open_15mins']
d0['PnL_after_commission_adjusted_6min_mean']=d0['close_open_diff_adjusted_6min_mean']*d0['bet']-12





#applied to individual stock

#stock=read_excel(r'C:\Users\jonathanjames\aws\notebooks\index_analysis\HK_XHKG_1398_wsj_with_tidy.xlsx','Sheet1')
stock=read_excel(os.path.join(main_dir,'index_HK_XHKG_HSI_wsj_with_tidy.xlsx'),'Sheet1')
stock=read_excel(os.path.join(main_dir,'HK_16_wsj_with_tidy.xlsx'),'Sheet1')
stock=read_excel(os.path.join(main_dir,'index_JP_XTKS_NIK_wsj_with_tidy.xlsx'),'Sheet1')
stock=read_excel(os.path.join(main_dir,'index_CN_SHCOMP_wsj_with_tidy.xlsx'),'Sheet1')
stock=pd.read_csv(os.path.join(main_dir,'singapore_index.csv'))

if 'Date2' not in stock.columns:
    stock['Date2']=stock['Date'].apply(lambda x:dt.strptime(x,'%m/%d/%y'))
    stock['Date2']=stock['Date2'].apply(lambda x:x.strftime('%Y-%m-%d'))
    stock.columns= [i.strip() for i in stock.columns.tolist()]
    del stock['Date']

#del stock['DateNum']

stock.dtypes

d0=pd.merge(d0,stock,how='inner',on=['Date2'])


#d0['close_open_diff_adjusted_6min_mean']=d0['Close_HK_XHKG_1398_wsj']-d0['Open_HK_XHKG_1398_wsj']
d0['close_open_diff_adjusted_6min_mean']=d0['Close_index_HK_XHKG_HSI_wsj']-d0['Open_index_HK_XHKG_HSI_wsj']
d0['close_open_diff_adjusted_6min_mean']=d0['Close_HK_16_wsj']-d0['Open_HK_16_wsj']
d0['close_open_diff_adjusted_6min_mean']=d0['Close_index_JP_XTKS_NIK_wsj']-d0['Open_index_JP_XTKS_NIK_wsj']
d0['close_open_diff_adjusted_6min_mean']=d0['Close_index_CN_SHCOMP_wsj']-d0['Open_index_CN_SHCOMP_wsj']
d0['close_open_diff_adjusted_6min_mean']=d0['Close']-d0['Open']

#12 is commission, 10 is assume lost 1 tick
d0['PnL_after_commission_adjusted_6min_mean']=d0['close_open_diff_adjusted_6min_mean']*d0['bet']













































#use grouped d0
d0_1=pd.read_csv(os.path.join(folder_path,"d0_model_0_to_13.csv"))
#d0_2=pd.read_csv(os.path.join(folder_path,"d0_model_15_to_45.csv"))
d0_2=pd.read_csv(os.path.join(folder_path,"d0_standard.csv"))

d0=pd.merge(d0_1,d0_2[['Date2','PnL_after_commission','stop_indicate']],how='left',on=['Date2'])


#d0['PnL_after_commission']=d0['PnL_after_commission_x']+d0['PnL_after_commission_y']
d0['PnL_after_commission']=d0['PnL_after_commission_y']
d0['stop_indicate']=d0['PnL_after_commission_x']


d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

d0=d0.loc[~(pd.isnull(d0['PnL_after_commission'])),:].copy()















#use4 fullday to 0_to_999999 for facebook ads
d0=pd.read_csv(os.path.join(folder_path,"d0_model_15_to_999999_use_fullday.csv"))

d0.columns.values

d0['PnL_after_commission_cum']=d0['PnL_after_commission'].cumsum()


d0['Return']=d0['PnL_after_commission_cum']/50000


pnl_csv=d0.copy()

#plot
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
fig = plt.figure(figsize=(20,6))
ax = fig.add_subplot(121)

#ax.set_facecolor('black')

ax.set_xlabel('Number of Trading Days (2011-2021)')
ax.set_ylabel('Cumulative Return')

ax.text(.2,.9,'HSI Futures Return',horizontalalignment='center',transform=ax.transAxes,color='white')


ax.xaxis.label.set_color('white')        #setting up X-axis label color to yellow
ax.yaxis.label.set_color('white')          #setting up Y-axis label color to blue

ax.tick_params(axis='x', colors='lightcyan')    #setting up X-axis tick color to red
ax.tick_params(axis='y', colors='lightcyan')  #setting up Y-axis tick color to black

ax.spines['left'].set_color('None')        # setting up Y-axis tick color to red
ax.spines['right'].set_color('None')        # setting up Y-axis tick color to red
ax.spines['top'].set_color('None')         #setting up above X-axis tick color to red
ax.spines['bottom'].set_color('springgreen')         #setting up above X-axis tick color to red

ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 

plt.rcParams.update({'font.size': 12,"font.weight":"bold","axes.labelweight":"bold"})
#plt.rcParams["font.weight"] = "bold"
#plt.rcParams["axes.labelweight"] = "bold"
plt.plot(range(0,d0.shape[0]), pnl_csv['Return'].values,'cyan')
#plt.show()
plt.savefig("15_to_999999_use_fullday_plot_facebook.png", transparent=True,bbox_inches="tight")


#pnl_csv['Date']=pnl_csv['Date'].apply(lambda x: x.strftime("%Y-%m-%d")) #dt to string

temp=pd.DataFrame({'Date':['string'],'Return':['number']})

pnl_csv=temp.append(pnl_csv)
pnl_csv=pnl_csv.reset_index(drop=True)
output_path=os.path.join(main_dir,'IB_live_trade','cum_pnl_15_to_999999_use_fullday.csv')
pnl_csv.to_csv(output_path,index=None)































#combine phase 1

d0=pd.read_csv(os.path.join(folder_path,"d0_standard.csv"))
d0=d0.rename(columns={'PnL_after_commission':'PnL_after_commission_original','bet':'bet_original'})

d0_phase1=pd.read_csv(os.path.join(folder_path,"d0_model_0_to_13.csv"))
d0_phase1=d0_phase1.rename(columns={'PnL_after_commission':'PnL_after_commission_phase1','bet':'bet_phase1'})

d0_15_to_30=pd.read_csv(os.path.join(folder_path,"d0_model_15_to_30.csv"))
d0_15_to_30=d0_15_to_30.rename(columns={'PnL_after_commission':'PnL_after_commission_15_to_30','bet':'bet_15_to_30'})

d0_45_to_165=pd.read_csv(os.path.join(folder_path,"d0_model_45_to_165.csv"))
d0_45_to_165=d0_45_to_165.rename(columns={'PnL_after_commission':'PnL_after_commission_45_to_165','bet':'bet_45_to_165'})



#d0_japan_fullday=pd.read_csv(os.path.join(folder_path,"d0_japan_fullday.csv"))
#d0_japan_fullday=d0_japan_fullday.rename(columns={'PnL_after_commission':'PnL_after_commission_japan_fullday','bet':'bet_japan_fullday'})
#
d0_japan_0_to_60=pd.read_csv(os.path.join(folder_path,"d0_japan_0_to_60.csv"))
d0_japan_0_to_60=d0_japan_0_to_60.rename(columns={'PnL_after_commission':'PnL_after_commission_japan_0_to_60','bet':'bet_japan_0_to_60'})
#d0=d0_japan_0_to_60.copy()
#d0=d0.rename(columns={'bet_japan_0_to_60':'bet_original'})

d0=pd.merge(d0,d0_phase1[['Date2','PnL_after_commission_phase1','bet_phase1',]].copy(),how='left',left_on=['Date2'],right_on=['Date2'])
d0=pd.merge(d0,d0_15_to_30[['Date2','PnL_after_commission_15_to_30','bet_15_to_30',]].copy(),how='left',left_on=['Date2'],right_on=['Date2'])
d0=pd.merge(d0,d0_45_to_165[['Date2','PnL_after_commission_45_to_165','bet_45_to_165',]].copy(),how='left',left_on=['Date2'],right_on=['Date2'])
d0=pd.merge(d0,d0_japan_0_to_60[['Date2','PnL_after_commission_japan_0_to_60','bet_japan_0_to_60',]].copy(),how='left',left_on=['Date2'],right_on=['Date2'])


#d0=pd.merge(d0,d0_japan_fullday[['Date2','PnL_after_commission_japan_fullday','bet_japan_fullday']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])
#d0=pd.merge(d0,d0_japan_0_to_60[['Date2','PnL_after_commission_japan_0_to_60','bet_japan_0_to_60']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])
    

d0=d0.loc[~pd.isnull(d0['PnL_after_commission_phase1']),:]
d0=d0.loc[~pd.isnull(d0['PnL_after_commission_15_to_30']),:]
d0=d0.loc[~pd.isnull(d0['PnL_after_commission_45_to_165']),:]
#d0=d0.loc[~pd.isnull(d0['PnL_after_commission_japan_0_to_60']),:]






contract1=1
contract2=2
contract3=2
contract4=6

contract1=1
contract2=1
contract5=1
contract6=1
contract7=1

contract1=3*5
contract2=3*5
contract5=3*5
contract6=0*5
contract7=0*10

#contract1=1
#contract2=1
#contract3=1
#contract4=1
#contract5=1
#contract6=1



d0['p1']=contract1*1*d0['PnL_after_commission_original']
d0['p2']=contract2*1*d0['PnL_after_commission_phase1']

d0['p5']=contract5*1*d0['PnL_after_commission_15_to_30']
#d0['p6']=contract6*1*d0['PnL_after_commission_45_to_165']

#d0['p3']=contract3*1*d0['PnL_after_commission_japan_fullday']
#d0['p7']=contract7*1*d0['PnL_after_commission_japan_0_to_60']


d0['PnL_after_commission']=d0['p7']
d0['PnL_after_commission']=d0['p2']
d0['PnL_after_commission']=d0['p2']+d0['p7']
d0['PnL_after_commission']=d0['p2']+d0['p5']
d0['PnL_after_commission']=d0['p1']+d0['p2']+d0['p5']+d0['p7']
d0['PnL_after_commission']=d0['p1']+d0['p2']+d0['p5']

#d0['PnL_after_commission']=d0['p1']+d0['p2']+d0['p5']+d0['p6']
#d0['PnL_after_commission']=d0['p2']+d0['p5']
#
#d0['PnL_after_commission']=d0['p1']
#d0['PnL_after_commission']=d0['p2']+d0['p5']
#d0['PnL_after_commission']=d0['p2']+d0['p5']+d0['p6']
#d0['PnL_after_commission']=d0['p1']+d0['p6']
#d0['PnL_after_commission']=d0['p6']



d0['PnL_after_commission_cum']=d0.groupby(['Date2_y'])['PnL_after_commission'].cumsum()



























#d0['PnL_after_commission']=5*d0['PnL_after_commission_original']+2*5*d0['PnL_after_commission_phase1']+1*10*d0['PnL_after_commission_japan_fullday']+2*10*d0['PnL_after_commission_japan_0_to_60']
#d0['PnL_after_commission']=1*10*d0['PnL_after_commission_japan_fullday']+2*10*d0['PnL_after_commission_japan_0_to_60']
#d0['PnL_after_commission']=3*5*d0['PnL_after_commission_original']+2*5*d0['PnL_after_commission_phase1']+1*10*d0['PnL_after_commission_japan_fullday']+1*10*d0['PnL_after_commission_japan_0_to_60']

d0['Date2']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m-%d"))
d0['Date2_ym']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y-%m"))
d0['Date2_ym_number']=d0['Date2'].apply(lambda x:float(dt.strptime(x,"%Y-%m-%d").strftime("%Y%m")))
d0['Date2_y']=d0['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y"))

d0_check=d0.groupby(['Date2_ym']).tail(1)
d0_check=d0_check.groupby(['Date2_ym']).head(1)
d0_check['month_temp']=d0_check['Date2_ym'].apply(lambda x:x.split('-')[1])
d0_check=d0_check.loc[d0_check['month_temp']=='10',:].copy()




##check
#sum(d0['bet_original']==d0['bet_phase1'])/d0.shape[0]
#sum(d0['bet_original']==d0['bet_15_to_30'])/d0.shape[0]
#sum(d0['bet_original']==d0['bet_45_to_165'])/d0.shape[0]
#
#
writer = pd.ExcelWriter('mis/d0_temp.xlsx', engine='xlsxwriter')
d0.to_excel(writer, sheet_name='summary')
writer.save()
writer.close()





















def gen_pnl(d0):
    #generate monthly data- pnl
    xx=d0.loc[d0['Date2_ym']=="2019-01",:]
    def monthly_pnl(xx,pnl_col_name='PnL_after_commission'):
        month_pnl=xx[pnl_col_name].sum()
        month_output=xx['Date2_ym'].values[0]
     
        #downside as if starting each month
        pnl_series=d0.loc[(d0['Date2_ym_number']>=xx['Date2_ym_number'].values[0])&(d0['Date2_y']<=month_output[0:4]),pnl_col_name]
        pnl_series_cum=pnl_series.cumsum()
        downside_as_as=min(pnl_series_cum)
        pnl_as_as=pnl_series_cum[-1:].values[0]
        return pd.Series([month_output,month_pnl,downside_as_as,pnl_as_as])
     
    # choose between PnL_after_commission or PnL_after_commission_adjusted_6min_mean
        
    pnl_look_at='PnL_after_commission'
    #pnl_look_at='PnL_after_commission_adjusted_6min_mean'
    #pnl_look_at='afternoon_pnl'
    d0_monthly=d0.groupby(["Date2_ym"]).apply(lambda x:monthly_pnl(x.reset_index(drop=True),pnl_look_at))
    d0_monthly=d0_monthly.rename(columns={0:'year_month',1:'monthly_pnl',2:'downside_as_as',3:'pnl_as_as'})
    d0_monthly['year']=d0_monthly['year_month'].apply(lambda x:x[0:4])
    
    d0_monthly=d0_monthly.sort_values(by=['year_month'],ascending=[True])
    
    all_year=d0_monthly.year.unique().tolist()
    
    #i=2014
    #j="07"
    for i in all_year:
        for j in ["01","02","03","04","05","06","07","08","09","10","11","12"]:
            aim=str(i)+"-"+j
            year_month_in=d0_monthly['year_month'].unique()
            if not (aim in year_month_in):
                new_data = pd.DataFrame(np.asarray([[aim,0,0,0,i]]), columns=d0_monthly.columns)
                d0_monthly = d0_monthly.append(new_data)
    
    d0_monthly['monthly_pnl']=d0_monthly['monthly_pnl'].apply(lambda x: float(x))
    d0_monthly['downside_as_as']=d0_monthly['downside_as_as'].apply(lambda x: float(x))
    d0_monthly['pnl_as_as']=d0_monthly['pnl_as_as'].apply(lambda x: float(x))
    
    year_distinct=list(d0_monthly['year'].unique())
    monthly_summary=pd.DataFrame({'month':['01','02','03','04','05','06','07','08','09','10','11','12']})
    monthly_summary_downside_asas=pd.DataFrame({'month':['01','02','03','04','05','06','07','08','09','10','11','12']})
    monthly_summary_pnl_asas=pd.DataFrame({'month':['01','02','03','04','05','06','07','08','09','10','11','12']})
     
    i='2020'
    for i in year_distinct:
        temp=d0_monthly.loc[d0_monthly['year']==i,'monthly_pnl']
        if temp.values.shape[0]!=12:
            out1=np.concatenate((temp.values,np.zeros(12-temp.values.shape[0])))
        else:
            out1=temp.values
        monthly_summary[i]=out1
     
    temp_matrix=monthly_summary.iloc[:,1:].values>0
    
    
    #monthly_summary.iloc[:,1:].as_matrix().sum(axis=0)
    
    monthly_summary['count_positive']=temp_matrix.sum(axis=1)
    monthly_summary['sum_pnl']=monthly_summary.iloc[:,1:-1].values.sum(axis=1)
     
    
    #find total pnl
    sum(monthly_summary['sum_pnl'].values)
    
    monthly_summary.to_csv('monthly_summary.csv')
    
    
    
    #yearly plot
    #plot weight (this is the posterior mean of each weight after 2000 run)
    import matplotlib.pyplot as plt
    plt.figure(figsize=(20,10), dpi=80, facecolor='w', edgecolor='k')
    
    Ws={1:d0.loc[d0['Date2_y']=='2011','PnL_after_commission_cum'].values,
        2:d0.loc[d0['Date2_y']=='2012','PnL_after_commission_cum'].values,
        3:d0.loc[d0['Date2_y']=='2013','PnL_after_commission_cum'].values,
        4:d0.loc[d0['Date2_y']=='2014','PnL_after_commission_cum'].values,
        5:d0.loc[d0['Date2_y']=='2015','PnL_after_commission_cum'].values,
        6:d0.loc[d0['Date2_y']=='2016','PnL_after_commission_cum'].values,
        7:d0.loc[d0['Date2_y']=='2017','PnL_after_commission_cum'].values,
        8:d0.loc[d0['Date2_y']=='2018','PnL_after_commission_cum'].values,
        9:d0.loc[d0['Date2_y']=='2019','PnL_after_commission_cum'].values,
        10:d0.loc[d0['Date2_y']=='2020','PnL_after_commission_cum'].values,
        11:d0.loc[d0['Date2_y']=='2021','PnL_after_commission_cum'].values,
        12:d0.loc[d0['Date2_y']=='2022','PnL_after_commission_cum'].values,
        13:d0.loc[d0['Date2_y']=='2023','PnL_after_commission_cum'].values}
    
    for i,H in Ws.items():
        plt.subplot(5,3,i).set_title("Year "+str(i+2010)) #fist two argument is the dimension, the three argument is the number for each plot
        plt.tight_layout() # Or equivalently,  "plt.tight_layout()"
        plt.plot(range(0,len(H)),H,'*', color='r')
        plt.xlabel('No.of.Days')
        plt.ylabel('Cum.PnL')    
    
    
    file_name_plot=os.path.join(main_dir,'yearly_plot.png')
    
    plt.savefig(file_name_plot,bbox_inches="tight")   
    
    
    #monthly_summary_downside_asas
    for i in year_distinct:
        temp=d0_monthly.loc[d0_monthly['year']==i,'downside_as_as']
        
        if temp.values.shape[0]!=12:
            out1=np.concatenate((temp.values,np.zeros(12-temp.values.shape[0])))
        else:
            out1=temp.values
        
        monthly_summary_downside_asas[i]=out1
     
    temp_matrix=monthly_summary_downside_asas.iloc[:,1:].values>0
     
    monthly_summary_downside_asas['count_positive']=temp_matrix.sum(axis=1)
    monthly_summary_downside_asas['sum']=monthly_summary_downside_asas.iloc[:,1:-1].values.sum(axis=1)
     
    #monthly_summary_pnl_asas
    for i in year_distinct:
        temp=d0_monthly.loc[d0_monthly['year']==i,'pnl_as_as']
        if temp.values.shape[0]!=12:
            out1=np.concatenate((temp.values,np.zeros(12-temp.values.shape[0])))
        else:
            out1=temp.values
        monthly_summary_pnl_asas[i]=out1
     
    temp_matrix=monthly_summary_pnl_asas.iloc[:,1:].values>0
     
    monthly_summary_pnl_asas['count_positive']=temp_matrix.sum(axis=1)
    monthly_summary_pnl_asas['sum_pnl']=monthly_summary_pnl_asas.iloc[:,1:-1].values.sum(axis=1)
     
     
    
    
    
    #sharpe ratio and accuracy
    #xx=d0.loc[d0['Date2_y']=="2020",:]
    #pnl_col_name='PnL_after_commission'
    def sharpe_ratio(xx,pnl_col_name='PnL_after_commission_adjusted_6min_mean'):
        xx['margin']=56000
        xx['return']=xx[pnl_col_name]/xx['margin']
        risk_free_rate=0
     
        year_output=xx['Date2_y'].values[0]
        SR=((xx['return'].mean()-risk_free_rate)/xx['return'].std())*np.sqrt(252)
        
        #Cum_pnl
        cum_pnl=sum(xx[pnl_col_name])
        
        #accuracy
        acc=sum(xx[pnl_col_name]>0)/xx.shape[0]
        
        #max cum loss
        xx['cum_pnl']=xx[pnl_col_name].cumsum()
        max_cum_loss=min(xx['cum_pnl'].values)
        
        #find number stop trigered
        stop_count=999#sum(xx['stop_indicate']!=0)
    
        #find number of trade
        trade_count=xx.shape[0]
        #stop ratio
        stop_ratio=stop_count/trade_count
        
        #average gain per trade/average loss per trade
        ave_gain=np.mean(xx.loc[xx[pnl_col_name]>0,pnl_col_name].values)
        ave_loss=abs(np.mean(xx.loc[xx[pnl_col_name]<0,pnl_col_name].values))
        ave_gain_over_ave_loss=ave_gain/ave_loss
        
        #drawdown
        mdd=max(np.maximum.accumulate(xx['cum_pnl'])-xx['cum_pnl'])
        
        return pd.Series([year_output,SR,acc,max_cum_loss,ave_gain,ave_loss,ave_gain_over_ave_loss,cum_pnl,stop_count,trade_count,stop_ratio,mdd])
    
    #PnL_after_commission    PnL_after_commission_adjusted_6min_mean
    d0_SR=d0.groupby(["Date2_y"]).apply(lambda x:sharpe_ratio(x.reset_index(drop=True),pnl_look_at))
    d0_SR=d0_SR.rename(columns={0:'year',1:'SR',2:'accuracy',3:'max_cum_loss',4:'ave_gain',5:'ave_loss',6:'gain/loss',7:'cum_pnl',8:'stop_count',9:'trade_count',10:'stop_ratio',11:'mdd'})
    
    d0_SR['P&L/MaxCumLoss']=abs(d0_SR['cum_pnl']/d0_SR['max_cum_loss'])
    d0_SR['capital']=80000
    d0_SR['return']=d0_SR['cum_pnl']/d0_SR['capital']
    
    cols = d0_SR.columns.tolist()
    cols.insert(1, cols.pop(cols.index('cum_pnl')))
    cols.insert(2, cols.pop(cols.index('max_cum_loss')))
    cols.insert(3, cols.pop(cols.index('P&L/MaxCumLoss')))
    cols.insert(4, cols.pop(cols.index('gain/loss')))
    cols.insert(5, cols.pop(cols.index('accuracy')))
    cols.insert(6, cols.pop(cols.index('capital')))
    cols.insert(7, cols.pop(cols.index('return')))
    
    d0_SR = d0_SR.reindex(columns= cols)
    
    d0_SR.loc['Mean',:]= d0_SR.mean(axis=0)
    
    #check monday effect
    d0['DateNum_lag1']=d0['DateNum'].shift(1)
    d0['DateNum_diff']=d0['DateNum']-d0['DateNum_lag1']
    d0['DateNum_diff_greater_one']=d0['DateNum_diff']>5
    
    sum(d0.loc[d0['DateNum_diff_greater_one']==True,'PnL_after_commission'])
    
    d0_SR_old=d0_SR.copy()
    return d0_SR,monthly_summary,monthly_summary_pnl_asas,monthly_summary_downside_asas




d0_SR,monthly_summary,monthly_summary_pnl_asas,monthly_summary_downside_asas=gen_pnl(d0)




























#investigate stop for hong kong 
a=read_excel('HSI_with_tidy.xlsx',sheet='Sheet1')
a=a.reset_index(drop=True)
a['high_open']=a['High_HSI']-a['Open_HSI']
a['low_open']=a['Open_HSI']-a['Low_HSI']
a['s_level']=(a['high_open']+a['low_open'])/2
a['s_level%']=a['s_level']/a['Open_HSI']
a['year']=a['Date2'].str[0:4]

def find_stop_investigate(data_temp):
    a1=np.percentile(data_temp.s_level,0)
    a2=np.percentile(data_temp.s_level,25)
    a3=np.percentile(data_temp.s_level,50)
    a4=np.percentile(data_temp.s_level,80)
    a5=np.percentile(data_temp.s_level,100)
    
    b1=np.percentile(data_temp['s_level%'],0)
    b2=np.percentile(data_temp['s_level%'],25)
    b3=np.percentile(data_temp['s_level%'],50)
    b4=np.percentile(data_temp['s_level%'],80)
    b5=np.percentile(data_temp['s_level%'],100)
    output=pd.DataFrame({'min':[a1],'25%':[a2],'50%':[a3],'80%':[a4],'100%':[a5],'min%':[b1],'25%%':[b2],'50%%':[b3],'80%%':[b4],'100%%':[b5]})
    return output

a_stop=a.groupby(['year']).apply(lambda x:find_stop_investigate(x.reset_index(drop=True)))



#investigate stop for japan  open to 10am
a=read_excel('n225_10am_with_tidy.xlsx',sheet='Sheet1')
a=a.reset_index(drop=True)
a['high_open']=a['High_n225_10am']-a['Open_n225_10am']
a['low_open']=a['Open_n225_10am']-a['Low_n225_10am']
a['s_level']=(a['high_open']+a['low_open'])/2
a['s_level%']=a['s_level']/a['Open_n225_10am']
a['year']=a['Date2'].str[0:4]

def find_stop_investigate(data_temp):
    a1=np.percentile(data_temp.s_level,0)
    a2=np.percentile(data_temp.s_level,25)
    a3=np.percentile(data_temp.s_level,50)
    a4=np.percentile(data_temp.s_level,80)
    a5=np.percentile(data_temp.s_level,100)
    
    b1=np.percentile(data_temp['s_level%'],0)
    b2=np.percentile(data_temp['s_level%'],25)
    b3=np.percentile(data_temp['s_level%'],50)
    b4=np.percentile(data_temp['s_level%'],80)
    b5=np.percentile(data_temp['s_level%'],100)
    output=pd.DataFrame({'min':[a1],'25%':[a2],'50%':[a3],'80%':[a4],'100%':[a5],'min%':[b1],'25%%':[b2],'50%%':[b3],'80%%':[b4],'100%%':[b5]})
    return output

b_stop=a.groupby(['year']).apply(lambda x:find_stop_investigate(x.reset_index(drop=True)))



#investigate stop for japan
a=read_excel('n225_with_tidy.xlsx',sheet='Sheet1')
a=a.reset_index(drop=True)
a['high_open']=a['High_n225']-a['Open_n225']
a['low_open']=a['Open_n225']-a['Low_n225']
a['s_level']=(a['high_open']+a['low_open'])/2
a['s_level%']=a['s_level']/a['Open_n225']
a['year']=a['Date2'].str[0:4]

def find_stop_investigate(data_temp):
    a1=np.percentile(data_temp.s_level,0)
    a2=np.percentile(data_temp.s_level,25)
    a3=np.percentile(data_temp.s_level,50)
    a4=np.percentile(data_temp.s_level,80)
    a5=np.percentile(data_temp.s_level,100)
    
    b1=np.percentile(data_temp['s_level%'],0)
    b2=np.percentile(data_temp['s_level%'],25)
    b3=np.percentile(data_temp['s_level%'],50)
    b4=np.percentile(data_temp['s_level%'],80)
    b5=np.percentile(data_temp['s_level%'],100)
    output=pd.DataFrame({'min':[a1],'25%':[a2],'50%':[a3],'80%':[a4],'100%':[a5],'min%':[b1],'25%%':[b2],'50%%':[b3],'80%%':[b4],'100%%':[b5]})
    return output

c_stop=a.groupby(['year']).apply(lambda x:find_stop_investigate(x.reset_index(drop=True)))



#d0=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))
#
#
#original_guess=d0[['Date2','Y_up_predict']].copy()
#original_guess=original_guess.rename(columns={'Y_up_predict':'prediction'})
#original_guess=original_guess.reset_index(drop=True)
#
#
#all_in_data=data.Date2.unique().tolist()
#
#
#original_guess['have_data']=original_guess['Date2'].apply(lambda x: x in all_in_data)
#
#original_guess=original_guess.loc[original_guess['have_data']==True,:]
#
##original_guess=original_guess.loc[original_guess['Date2']<='2013-12-31',:]
#
#original_guess=original_guess.reset_index(drop=True)
#
#
#
#
#
#
#from random import *
# 
#from datetime import datetime as dt
#import datetime
#from collections import OrderedDict
#import pandas as pd
#import numpy as np
# 
#
#morning_signal=0
#profit_target=20000
#stop_level=200
#after_stop_target=20000
#after_stop_stop=20000
#date_use="2011-01-04"
#date_ymd_col_name='Date2'
#date_ymd_hms_col_name='Date1'
#second_stage_trade=True
#start_row=0 
#end_row=-1 
#
# 
#start_row=0 #9:15 Open
#start_row=5 #9:20 Open
#end_row=15 #0929 close
#end_row=-1 # 1629 close
#end_row=-2 # 1628 close
#
#
# 
#def strategy1(data,date_use,date_ymd_col_name,date_ymd_hms_col_name,morning_signal,profit_target,stop_level,after_stop_target,after_stop_stop,second_stage_trade,start_row=0,end_row=-1):
#    data_use=data.loc[data[date_ymd_col_name]==date_use,:].copy()
#    data_use=data_use.reset_index(drop=True)
#    if end_row>=0:
#        data_use=data_use[(start_row):(end_row)]
#    else:
#        data_use=data_use[(start_row):(data_use.shape[0]+1+end_row)]
# 
#    data_use=data_use.reset_index(drop=True)
# 
#    entry_price=data_use[0:1]['Open'][0]
#    exit_price=data_use[0:1]['Open'][0]
#    second_entry_price=999999
#    second_exit_price=999999
#    trigger_first_stop=False
#    trigger_second_stop=False
##    date_use_dt=dt.strptime(date_use,"%Y-%m-%d")
##    exit_time=dt(int(date_use_dt.strftime("%Y")),int(date_use_dt.strftime("%m")),int(date_use_dt.strftime("%d")),16,30,0)
#    achieve_profit=999999
#    achieve_stop=999999
#    achieve_profit2=999999
#    achieve_stop2=999999    
# 
#    if morning_signal==1:
#        #find when achieve profit target
#        data_use.loc[data_use['High']>=entry_price+profit_target,'indicate_profit']=1
#        data_use['indicate_profit']=data_use['indicate_profit'].fillna(0)
#        if sum(data_use['indicate_profit']==1)>0:
#            achieve_profit=data_use.index[data_use['indicate_profit']==1][0]
#        else:
#            achieve_profit=999999
# 
#        #find when achieve stop target        
#        data_use.loc[data_use['Low']<=entry_price-stop_level,'indicate_stop']=1
#        data_use['indicate_stop']=data_use['indicate_stop'].fillna(0)
#        if sum(data_use['indicate_stop']==1)>0:
#            achieve_stop=data_use.index[data_use['indicate_stop']==1][0]
#        else:
#            achieve_stop=999999
# 
#        #case1: achieve_profit=999999, achieve_stop=999999, leave at close
#        if (achieve_profit==999999)&(achieve_stop==999999):
#            exit_price=data_use.loc[data_use['Date1']==max(data_use['Date1']),'Close'].values[0]
# 
# 
#        #case2 or case 5, second trade
#        if ((achieve_profit==999999)&(achieve_stop!=999999))|((achieve_profit!=999999)&(achieve_stop!=999999)&(achieve_profit>achieve_stop)):
#            trigger_first_stop=True
#            exit_price=entry_price-stop_level
# 
#        #case3 or case 4, exit at profit target
#        if ((achieve_profit!=999999)&(achieve_stop==999999))|((achieve_profit!=999999)&(achieve_stop!=999999)&(achieve_profit<achieve_stop)):
#            exit_price=entry_price+profit_target
# 
#        #case6, second trade
#        if (achieve_profit!=999999)&(achieve_stop!=999999)&(achieve_profit==achieve_stop):
#            trigger_first_stop=True
#            exit_price=entry_price-stop_level
# 
#        if (trigger_first_stop==True)&(second_stage_trade==True):
#            data_use2=data_use[achieve_stop:].copy()  
#            data_use2=data_use2.reset_index(drop=True)
#            second_entry_price=entry_price-stop_level-1
# 
#            #find when achieve profit target
#            data_use2.loc[data_use2['Low']<=second_entry_price-after_stop_target,'indicate_profit2']=1
#            data_use2['indicate_profit2']=data_use2['indicate_profit2'].fillna(0)
#            if sum(data_use2['indicate_profit2']==1)>0:
#                achieve_profit2=data_use2.index[data_use2['indicate_profit2']==1][0]
#            else:
#                achieve_profit2=999999
# 
#            #find when achieve stop target        
#            data_use2.loc[data_use2['High']>=(second_entry_price+after_stop_stop),'indicate_stop2']=1
#            data_use2['indicate_stop2']=data_use2['indicate_stop2'].fillna(0)
#            if sum(data_use2['indicate_stop2']==1)>0:
#                achieve_stop2=data_use2.index[data_use2['indicate_stop2']==1][0]
#            else:
#                achieve_stop2=999999
# 
#            #case1: achieve_profit=999999, achieve_stop=999999, leave at close
#            if (achieve_profit2==999999)&(achieve_stop2==999999):
#                second_exit_price=data_use2.loc[data_use2['Date1']==max(data_use2['Date1']),'Close'].values[0]
# 
#            #case2 or case 5, second trade
#            if ((achieve_profit2==999999)&(achieve_stop2!=999999))|((achieve_profit2!=999999)&(achieve_stop2!=999999)&(achieve_profit2>achieve_stop2)):
#                trigger_second_stop=True
#                second_exit_price=second_entry_price+after_stop_stop
# 
#            #case3 or case 4, exit at profit target
#            if ((achieve_profit2!=999999)&(achieve_stop2==999999))|((achieve_profit2!=999999)&(achieve_stop2!=999999)&(achieve_profit2<achieve_stop2)):
#                second_exit_price=second_entry_price-after_stop_target
# 
#            #case6, achieve_profit2==achieve_stop2, second trade
#            if (achieve_profit2!=999999)&(achieve_stop2!=999999)&(achieve_profit2==achieve_stop2):
#                trigger_second_stop=True
#                second_exit_price=second_entry_price+after_stop_stop
# 
#    if morning_signal==0:
#        #find when achieve profit target
#        data_use.loc[data_use['Low']<=entry_price-profit_target,'indicate_profit']=1
#        data_use['indicate_profit']=data_use['indicate_profit'].fillna(0)
#        if sum(data_use['indicate_profit']==1)>0:
#            achieve_profit=data_use.index[data_use['indicate_profit']==1][0]
#        else:
#            achieve_profit=999999
# 
#        #find when achieve stop target        
#        data_use.loc[data_use['High']>=entry_price+stop_level,'indicate_stop']=1
#        data_use['indicate_stop']=data_use['indicate_stop'].fillna(0)
#        if sum(data_use['indicate_stop']==1)>0:
#            achieve_stop=data_use.index[data_use['indicate_stop']==1][0]
#        else:
#            achieve_stop=999999
# 
#        #case1: achieve_profit=999999, achieve_stop=999999, leave at close
#        if (achieve_profit==999999)&(achieve_stop==999999):
#            exit_price=data_use.loc[data_use['Date1']==max(data_use['Date1']),'Close'].values[0]
# 
#        #case2 or case 5, second trade
#        if ((achieve_profit==999999)&(achieve_stop!=999999))|((achieve_profit!=999999)&(achieve_stop!=999999)&(achieve_profit>achieve_stop)):
#            trigger_first_stop=True
#            exit_price=entry_price+stop_level
# 
#        #case3 or case 4, exit at profit target
#        if ((achieve_profit!=999999)&(achieve_stop==999999))|((achieve_profit!=999999)&(achieve_stop!=999999)&(achieve_profit<achieve_stop)):
#            exit_price=entry_price-profit_target
# 
#        #case6, second trade
#        if (achieve_profit!=999999)&(achieve_stop!=999999)&(achieve_profit==achieve_stop):
#            trigger_first_stop=True
#            exit_price=entry_price+stop_level
# 
#        if (trigger_first_stop==True)&(second_stage_trade==True):
#            data_use2=data_use[achieve_stop:].copy()
#            data_use2=data_use2.reset_index(drop=True)
#            second_entry_price=entry_price+stop_level+1
# 
#            #find when achieve profit target
#            data_use2.loc[data_use2['High']>=second_entry_price+after_stop_target,'indicate_profit2']=1
#            data_use2['indicate_profit2']=data_use2['indicate_profit2'].fillna(0)
#            if sum(data_use2['indicate_profit2']==1)>0:
#                achieve_profit2=data_use2.index[data_use2['indicate_profit2']==1][0]
#            else:
#                achieve_profit2=999999
# 
#            #find when achieve stop target        
#            data_use2.loc[data_use2['Low']<=(second_entry_price-after_stop_stop),'indicate_stop2']=1
#            data_use2['indicate_stop2']=data_use2['indicate_stop2'].fillna(0)
#            if sum(data_use2['indicate_stop2']==1)>0:
#                achieve_stop2=data_use2.index[data_use2['indicate_stop2']==1][0]
#            else:
#                achieve_stop2=999999
# 
#            #case1: achieve_profit=999999, achieve_stop=999999, leave at close
#            if (achieve_profit2==999999)&(achieve_stop2==999999):
#                second_exit_price=data_use2.loc[data_use2['Date1']==max(data_use2['Date1']),'Close'].values[0]
# 
# 
#            #case2 or case 5, second trade
#            if ((achieve_profit2==999999)&(achieve_stop2!=999999))|((achieve_profit2!=999999)&(achieve_stop2!=999999)&(achieve_profit2>achieve_stop2)):
#                trigger_second_stop=True
#                second_exit_price=second_entry_price-after_stop_stop
# 
#            #case3 or case 4, exit at profit target
#            if ((achieve_profit2!=999999)&(achieve_stop2==999999))|((achieve_profit2!=999999)&(achieve_stop2!=999999)&(achieve_profit2<achieve_stop2)):
#                second_exit_price=second_entry_price+after_stop_target
# 
#            #case6, achieve_profit2==achieve_stop2, second trade
#            if (achieve_profit2!=999999)&(achieve_stop2!=999999)&(achieve_profit2==achieve_stop2):
#                trigger_second_stop=True
#                second_exit_price=second_entry_price-after_stop_stop
# 
#    output=pd.Series([date_use,morning_signal,entry_price,exit_price,trigger_first_stop,second_entry_price,second_exit_price,trigger_second_stop,
#                      profit_target,stop_level,after_stop_target,after_stop_stop,second_stage_trade,achieve_profit,achieve_stop,achieve_profit2,achieve_stop2,start_row,end_row])
#    return output
# 
# 
# 
# 
# 
#import time
#import os
##parameter_df=pd.DataFrame(OrderedDict({'profit_target':     [20000,100,150,200,250,300,350,150,200,250,300,350,200,250,300,350],
##                                       'stop_level'   :     [200,75,75,75,75,75,75,100,100,100,100,100,150,150,150,150],
##                                       'after_stop_target': [10000,75,75,75,75,75,75,100,100,100,100,100,150,150,150,150],
##                                       'after_stop_stop':   [10000,75,75,75,75,75,75,100,100,100,100,100,150,150,150,150],
##                                       'second_stage_trade':[False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]}))
#
#parameter_df = read_excel(r'C:\Users\jonathanjames\aws\notebooks\index_analysis\mis\parameter_df.xlsx','Sheet1')
#    
#    
#    
#    
#    
#    
#    
#summary=pd.DataFrame()
# 
# 
#start_time=dt.now()
#i=30
#j=0
#for j in range(0,parameter_df.shape[0]):
#    parameter_df_use=parameter_df[j:j+1]
#    pt1=parameter_df_use['profit_target'].values[0]
#    st1=parameter_df_use['stop_level'].values[0]
#    pt2=parameter_df_use['after_stop_target'].values[0]
#    st2=parameter_df_use['after_stop_stop'].values[0]
#    second_stage_trade=parameter_df_use['second_stage_trade'].values[0]
#    start_row=parameter_df_use['start_row'].values[0]
#    end_row=parameter_df_use['end_row'].values[0]
# 
#    store_result=pd.DataFrame(columns=["Date","Prediction","entry_price","exit_price","trigger_first_stop",
#                                       "second_entry_price","second_exit_price","trigger_second_stop",
#                                       "profit_target","stop_level","after_stop_target","after_stop_stop","second_stage_trade",'achieve_profit','achieve_stop','achieve_profit2','achieve_stop2','start_row','end_row'])    
#    for i in range(0,original_guess.shape[0]):
#        row_use=original_guess[i:i+1]
#        temp=strategy1(data,row_use['Date2'].values[0],'Date2','Date1',row_use['prediction'].values[0],pt1,st1,pt2,st2,second_stage_trade,start_row,end_row)
#        temp=temp.values.reshape(1,temp.shape[0])
#        temp=pd.DataFrame(temp)
#        temp.columns=("Date","Prediction","entry_price","exit_price","trigger_first_stop","second_entry_price","second_exit_price",
#                        "trigger_second_stop","profit_target","stop_level","after_stop_target","after_stop_stop","second_stage_trade",'achieve_profit','achieve_stop','achieve_profit2','achieve_stop2','start_row','end_row')
#        store_result=store_result.append(temp)
#        print("finished ",row_use['Date2'].values[0])
# 
# 
#    store_result['year']=store_result['Date'].str[0:4]    
#    store_result['first_commission']=12
#    store_result.loc[store_result['second_entry_price']!=999999,'second_commission']=12
#    store_result.loc[store_result['second_entry_price']==999999,'second_commission']=0
#    store_result.loc[store_result['Prediction']==0,'Prediction']=-1
#    store_result['Prediction_second']=store_result['Prediction']*-1
#    store_result['pnl_first_trade']=(store_result['exit_price']-store_result['entry_price'])*store_result['Prediction']*10-store_result['first_commission']
#    store_result['pnl_second_trade']=(store_result['second_exit_price']-store_result['second_entry_price'])*store_result['Prediction_second']*10-store_result['second_commission']
#    store_result['pnl']=store_result['pnl_first_trade']+store_result['pnl_second_trade']
# 
#    file_name="hsi_investigate2_"+str(pt1)+"_"+str(st1)+"_"+str(pt2)+"_"+str(st2)+"_"+str(start_row)+"_"+str(end_row)+'_'+time.strftime("%Y%m%d")+'_'+time.strftime("%H%M%S")+".csv"
#    save_path=os.path.join(main_dir,'plot2',file_name)
#    store_result.to_csv(save_path,index=False)
# 
#    def pnl_function(x):
#        year_name=x['year'].values[0]
#        x['Cum_pnl_peryear']=x['pnl'].cumsum()
#        MDD=max(np.maximum.accumulate(x['Cum_pnl_peryear']) - x['Cum_pnl_peryear'])
#        max_downside=min(x['Cum_pnl_peryear'])
#        final_cum_pnl=x['Cum_pnl_peryear'].values[-1]
#        accuracy=sum(x['pnl']>0)/x.shape[0]
#        return pd.Series([year_name,final_cum_pnl,MDD,max_downside,accuracy])
# 
#    temp=store_result.groupby(["year"]).apply(lambda x:pnl_function(x.reset_index(drop=True)))
#    temp.columns = ('year',"FinalCumPnl","MDD","MaxDownside","accuracy")
# 
#    temp['profit_target']=pt1
#    temp['stop_level']=st1
#    temp['after_stop_target']=pt2
#    temp['after_stop_stop']=st2
#    temp['second_stage_trade']=second_stage_trade
#    temp['start_row']=start_row
#    temp['end_row']=end_row
# 
#    summary=summary.append(temp)
# 
#save_path=os.path.join(main_dir,'plot2','summary_pnl'+'_'+time.strftime("%Y%m%d")+'_'+time.strftime("%H%M%S")+'.csv')
#summary.to_csv(save_path,index=False)
# 
# 
#end_time=dt.now()
#total_time=(end_time-start_time).total_seconds()
#total_time
# 
# 
#
#
#
#
#
#
#
##manually made hsi_y and HSI_with_tidy
#start_row=15
#end_row=-1
#x=data.loc[data['Date2']=='2005-12-01',:]
#def extract_price(x,start_row=0,end_row=-1):
#    if end_row>=0:
#        data_use=x[(start_row):(end_row)]
#    else:
#        data_use=x[(start_row):(x.shape[0]+1+end_row)]
# 
#    data_use=data_use.reset_index(drop=True)
# 
#    open_price=data_use['Open'].values[0]
#    close_price=data_use['Close'].values[-1]
#    high_price=max(data_use['High'])
#    low_price=min(data_use['Low'])
#    date_target=data_use['Date2'].values[0]
#    datenum=(dt.strptime(date_target,"%Y-%m-%d")-dt(1970,1,1)).days
#    percentage_diff=(close_price-open_price)/open_price
#    return pd.Series([date_target,open_price,high_price,low_price,close_price,percentage_diff,datenum])
# 
#data_extracted=data.groupby('Date2').apply(lambda x:extract_price(x.reset_index(drop=True),15,-1))
#data_extracted=data_extracted.rename(columns={0:'Date2',1:'Open_HSI',2:'High_HSI',3:'Low_HSI',4:'Close_HSI',5:'HSI_change',6:'DateNum'}) 
#data_extracted=data_extracted.reset_index(drop=True)
# 
#check=data[79950:79960].copy()
#
#writer = pd.ExcelWriter(r'C:\Users\jonathanjames\aws\notebooks\index_analysis\HSI_with_tidy.xlsx', engine='xlsxwriter')
#data_extracted.to_excel(writer, sheet_name='Sheet1')
# 
# 
##create dependent variable Y
#hsi_y=data_extracted.loc[:,['Date2','DateNum','Open_HSI','High_HSI','Low_HSI','Close_HSI']]
#hsi_y['Y_up']=hsi_y.apply(lambda row: (row.Close_HSI>=row.Open_HSI)*1,axis=1)
#hsi_y['Y_down']=hsi_y.apply(lambda row: (row.Close_HSI<row.Open_HSI)*1,axis=1)
#
#writer = pd.ExcelWriter(r'C:\Users\jonathanjames\aws\notebooks\index_analysis\hsi_y.xlsx', engine='xlsxwriter')
#hsi_y.to_excel(writer, sheet_name='Sheet1')
#writer.save()
# 
# 
# 
# 
# 
# 
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
# 
# 
# 
# 
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib import dates, ticker
#import matplotlib as mpl
#import sys
#sys.path.append(r'C:\Users\jonathanjames\Desktop\python\mpl_finance\dist\mpl_finance-0.10.0')
#from mpl_finance import candlestick_ohlc
# 
#mpl.style.use('default')
# 
# 
#data['Date1_string']=data['Date1'].apply(lambda x:x.strftime("%Y-%m-%d %H:%M:%S"))
#data_for_plot=data.loc[data['Date2']=='2005-12-01',['Date1_string','Open','High','Low','Close']].copy()
#data_for_plot['Open']=data_for_plot['Open'].astype(str)
#data_for_plot['High']=data_for_plot['High'].astype(str)
#data_for_plot['Low']=data_for_plot['Low'].astype(str)
#data_for_plot['Close']=data_for_plot['Close'].astype(str)
#data_for_plot=[tuple(r) for r in data_for_plot.values]
# 
#ohlc_data = []
# 
#for line in data_for_plot:
#    ohlc_data.append((dates.datestr2num(line[0]), np.float64(line[1]), np.float64(line[2]), np.float64(line[3]), np.float64(line[4])))
# 
#fig, ax1 = plt.subplots()
#candlestick_ohlc(ax1, ohlc_data, width = 0.5/(24*60), colorup = 'g', colordown = 'r', alpha = 0.8)
# 
#ax1.xaxis.set_major_formatter(dates.DateFormatter('%d/%m/%Y %H:%M'))
#ax1.xaxis.set_major_locator(ticker.MaxNLocator(10))
# 
#plt.xticks(rotation = 30)
#plt.grid()
#plt.xlabel('Date')
#plt.ylabel('Price')
#plt.title('Historical Data')
#plt.tight_layout()
#plt.show()
# 
# 
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
##investigate close position impact
##read FHSI_minute_20051201to20190326.hdf5
#import os
#import numpy as np
#from pandas import HDFStore,DataFrame
#import pandas as pd
#from datetime import datetime as dt
#import datetime
#
#folder_path=r"C:\Users\jonathanjames\aws\notebooks\index_analysis\mis"
#
#
#fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
#store = pd.HDFStore(fn)
#print(store)
#data_all_final= store.select('FHSI_minute')
# 
#store.close()
#
#
#data_all_final_check=data_all_final.head(10)
#data=data_all_final[['date_ymd_hms','date_ymd','Open','High','Low','Close','TotalVolume']].copy()
#data=data.rename(columns={'date_ymd_hms':'Date1','date_ymd':'Date2'})
#
#data_check=data.tail(10000)
#
#
#data_1=data.groupby('Date2').apply(lambda x:x.tail(1))
#data_2=data_1.loc[data_1['Date2']>='2011-01-01',:]
#data_2['close_minor_open_abs']=abs(data_2['High'].values-data_2['Low'].values)
#
#(data_2['close_minor_open_abs'].mean()/data_2['TotalVolume'].mean())*300
#
#data_2['TotalVolume'].mean()/data_2['close_minor_open_abs'].mean()








aggregate_us_stock_performance_v2.py


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:32:33 2021

@author: root
"""





##copy to copied_from_backtest_linux
#import os
#import numpy as np
#from pandas import HDFStore,DataFrame
#from pandas import read_excel
#import pandas as pd
#import shutil
#
#
#main_dir='/home/jonathanjames/aws/notebooks/index_analysis'
#plot_path=os.path.join(main_dir,'backtest_linux','plot')
#copy_to=os.path.join(main_dir,'plot_us','copied_from_backtest_linux')
#
#train_test_Setting = read_excel(os.path.join(main_dir,'index_table_v2_for_test_backtest.xlsx'),'Sheet2')
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='us_bet_final',:]
##train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='us_bet_final_13',:]
#
#ass_use=train_test_Setting[['asset','Number']].groupby(['asset']).head(1).reset_index(drop=True)
#
#ass=list(train_test_Setting['asset'].unique())
#increment=int(train_test_Setting.shape[0]/len(ass))
#
#alls=[]
#a=0
#for row in range(0,ass_use.shape[0]):
#    a=ass_use.iloc[row,:]
#    temp1=[list(range(int(a['Number']),int(a['Number']+increment))),a['asset']]
#    alls.append(temp1)
#
##x=[list(range(30000,30013)),'MSFT']
#for x in alls:
#    s1=x[0]
#    asset_name=x[1]
#    #read prediction
#    train_test_Setting = read_excel(os.path.join(main_dir,'index_table_v2_for_test_backtest.xlsx'),'Sheet2')
#    train_test_Setting['use']=train_test_Setting['Number'].apply(lambda x:x in s1)
#    train_test_Setting=train_test_Setting.loc[train_test_Setting['use']==True,:].copy()
#    train_test_Setting=train_test_Setting.reset_index(drop=True)
#    
#    d0=pd.DataFrame([])
#    all_number=train_test_Setting['Number'].values.tolist()
#    i=6
#    for i in range(0,train_test_Setting.shape[0]):
#        file_name=str(int(train_test_Setting['Number'][i]))+'_test_'+str(train_test_Setting['Test_start'][i].strftime("%Y"))+'.xlsx'
#        sourcepath=os.path.join(plot_path,file_name)
#        destpath=os.path.join(copy_to,file_name)
#
##        sourcepath=os.path.join(copy_to,file_name)
##        destpath=os.path.join(plot_path,file_name)
#
#        
#        if os.path.exists(destpath):
#            os.remove(destpath) 
#        shutil.copy(sourcepath,destpath)
#
#                
#
#
#
#
#
#def change_permissions_recursive(temp_folder1, mode):
#    for root, dirs, files in os.walk(temp_folder1, topdown=False):
#        for dir in [os.path.join(root,d) for d in dirs]:
#            os.chmod(dir, mode)
#        for file in [os.path.join(root, f) for f in files]:
#            os.chmod(file, mode)
#
#
#
#change_permissions_recursive('/home/jonathanjames/aws/notebooks/index_analysis/plot_us/copied_from_backtest_linux', 0o777)


















































#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:32:33 2021

@author: root
"""



import os
import numpy as np
from pandas import HDFStore,DataFrame
import pandas as pd
from datetime import datetime as dt
import datetime
from pandas import read_excel
import pandas as pd
from datetime import datetime as dt
import os



#main_dir=r'C:\Users\jonathanjames\aws\notebooks\index_analysis'
#plot_path=os.path.join(main_dir,'plot_us','copied_from_backtest_linux')
##calendar_path=os.path.join(main_dir,'daily_prediction_production')



main_dir_original='/home/jonathanjames/aws/notebooks/index_analysis'
main_dir='/home/jonathanjames/my_storage/tradelog/index_analysis_cumulative'
#plot_path=os.path.join(main_dir,'plot_us','version_parameter')
plot_path=os.path.join(main_dir,'backtest_linux','plot')
#calendar_path=os.path.join(main_dir,'daily_prediction_production')

#s1=list(range(15100,15113));asset_name='BAC'
#s1=list(range(15200,15213));asset_name='AAPL'
#alls=[[list(range(15100,15113)),'MSFT'],
#      [list(range(15200,15213)),'AAPL'],
#      [list(range(15313,15326)),'NVDA'],
#      #[list(range(15400,15413)),'VALE'],
#      [list(range(15500,15513)),'V'],
#      [list(range(15600,15613)),'MA']
#      #[list(range(16700,16713)),'CMCSA']
#      ]




train_test_Setting = read_excel(os.path.join(main_dir_original,'index_table_v2_for_test_backtest.xlsx'),'Sheet2')




tname='snp'
tname='us_stock'
key_word='yes'
key_word='us_bet_final'
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='us_bet_final',:]

train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']==key_word,:]
#train_test_Setting=train_test_Setting.loc[train_test_Setting['run_yes']=='us_bet_final_13',:]


ass_use=train_test_Setting[['asset','Number']].groupby(['asset']).head(1).reset_index(drop=True)


ass=list(train_test_Setting['asset'].unique())
increment=int(train_test_Setting.shape[0]/len(ass))

alls=[]
a=0
for row in range(0,ass_use.shape[0]):
    a=ass_use.iloc[row,:]
    temp1=[list(range(int(a['Number']),int(a['Number']+increment))),a['asset']]
    alls.append(temp1)





#set a cut off date for latest year, because last row trade may will be removed
#cutoff='2021-07-30'




#x=[list(range(19500,19513)),'MSFT']
#x=[list(range(30000,30013)),'MSFT']
#x=[list(range(19860,19874)),'IP']
#x=[list(range(19530,19545)),'UNH']
for x in alls:
    s1=x[0]
    asset_name=x[1]
    #read prediction
    train_test_Setting = read_excel(os.path.join(main_dir_original,'index_table_v2_for_test_backtest.xlsx'),'Sheet2')
    train_test_Setting['use']=train_test_Setting['Number'].apply(lambda x:x in s1)
    train_test_Setting=train_test_Setting.loc[(train_test_Setting['use']==True)&(train_test_Setting['run_yes']==key_word),:].copy()
    train_test_Setting=train_test_Setting.reset_index(drop=True)
    
    d0=pd.DataFrame([])
    all_number=train_test_Setting['Number'].values.tolist()
    i=14
    for i in range(0,train_test_Setting.shape[0]):
        print('doing',asset_name)
        print(i)
        file_name=str(int(train_test_Setting['Number'][i]))+'_test_'+str(train_test_Setting['Test_start'][i].strftime("%Y"))+'.xlsx'
        d1 = read_excel(os.path.join(plot_path,file_name),'daily_detail_summary')
    
        d1=d1[['Date2','Open_HSI','High_HSI','Low_HSI','Close_HSI','DateNum','close_open_diff','bet','islast']].copy()
        d1=d1.loc[~((d1['Open_HSI']==100)&(d1['High_HSI']==100)&(d1['Low_HSI']==100)),:].copy()
        
        d1_temp = read_excel(os.path.join(plot_path,file_name),'daily_detail_summary_aggregate')
        if d1_temp.shape[0]>0:
            d1_temp['PnL_after_commission']=d1_temp['PnL_original']-0.0035*2*2-0.015*2*0  #PnL_original  or PnL
            d1_temp['cum_pnl']=d1_temp['PnL_after_commission'].cumsum()
            no_trades=d1_temp.shape[0]
            up_trades_percent=d1_temp.loc[d1_temp['bet']==1,:].shape[0]/d1_temp.shape[0]
            
            #if not remove last row, in below second merge, may have duplicated record
            d1_temp=d1_temp.loc[pd.isnull(d1_temp['islast']),:].copy()
    
    
            #find avergae holding days
            d1_temp['holding_days']=d1_temp.apply(lambda x: (dt.strptime(x['exit_time'],"%Y-%m-%d")-dt.strptime(x['entry_time'],"%Y-%m-%d")).days,axis=1)
    
            
            #if short posiiton, deduct short interest rate assume 0.27% each day
            d1_temp.loc[d1_temp['bet']==-1,['short_interest_cost']]=d1_temp['entry_price']*d1_temp['holding_days']*0.0027/365
            d1_temp['short_interest_cost']=d1_temp['short_interest_cost'].fillna(0)
            d1_temp['PnL_after_commission']=d1_temp['PnL_after_commission']-d1_temp['short_interest_cost']
    
            
            d1=pd.merge(d1,d1_temp[['entry_time','entry_price','exit_time','exit_price','PnL_after_commission']].copy(),how='left',left_on=['Date2'],right_on=['entry_time'])
            #using exit_time to merge, so cum_pnl will appear in exit date only
            d1=pd.merge(d1,d1_temp[['exit_time','cum_pnl']].copy(),how='left',left_on=['Date2'],right_on=['exit_time'],suffixes=('','_remove'))
            
            d1=d1[['Date2','Open_HSI','High_HSI','Low_HSI','Close_HSI','DateNum','close_open_diff','bet','islast','entry_time','entry_price','exit_price','exit_time','PnL_after_commission','cum_pnl']].copy()
            d1['no_of_trades']=no_trades
            d1['up_trades_percent']=up_trades_percent
            d1['holding_days_mean']=round(d1_temp['holding_days'].mean())
    
    
            #find p&l portion contributed by long
            d1['long_pnl_portion']=sum(d1_temp.loc[d1_temp['bet']==-1,'PnL_after_commission'].values)/d1_temp['cum_pnl'].values[-1]
            
            
            d0=d0.append(d1)
            
            print('finished ',i,' out of ',train_test_Setting.shape[0])
    
    d0=d0.reset_index(drop=True)
    
    d0['year']=d0['Date2'].str[0:4]
    
    cutoff=d0.loc[~pd.isnull(d0['exit_time']),'exit_time'].values[-1]
    d0=d0.loc[d0['Date2']<=cutoff,:].copy()
    
    
    d0_temp=d0.loc[d0['year']=='2015',:].copy()
    d0_temp=d0_temp.reset_index(drop=True)
    
    def accurate_stat(d0_temp):
        print('doing ',d0_temp['Date2'].values[0])
        d0_temp['entry_price']=d0_temp['entry_price'].fillna(method='ffill')
        d0_temp.loc[d0_temp['bet']==0,'entry_price']=0
        d0_temp['cum_pnl']=d0_temp['cum_pnl'].fillna(method='ffill')
        d0_temp['face_pnl']=(d0_temp['Close_HSI']-d0_temp['entry_price'])*d0_temp['bet']
        
#        #if islast=1, it is year end, so in backtest, i force close position, so must no open position
#        d0_temp.loc[(d0_temp['islast']==1)|(d0_temp['islast']==0),'face_pnl']=0

        d0_temp.loc[max(d0_temp.index),'face_pnl']=0
        
        d0_temp['cum_pnl_openpos']=d0_temp['cum_pnl']+d0_temp['face_pnl']
        d0_temp['cum_pnl_openpos']=d0_temp['cum_pnl_openpos'].fillna(0)
        d0_temp['cum_pnl_openpos_lag1']=d0_temp['cum_pnl_openpos'].shift(1)
        d0_temp['cum_pnl_openpos_lag1']=d0_temp['cum_pnl_openpos_lag1'].fillna(0)
        d0_temp['pnl_net']=d0_temp['cum_pnl_openpos']-d0_temp['cum_pnl_openpos_lag1']
        #d0_temp.loc[~pd.isnull(d0_temp['entry_time']),'capital_per_bet']=d0_temp['entry_price']-d0_temp['cum_pnl_openpos_lag1']
    
        
        #find when max stock price occur
        max_stock_price=max(d0_temp['High_HSI'].values)
        max_stock_happen=np.argmax(d0_temp['High_HSI'].values)
        d0_temp['max_stock_price']=max_stock_price
        d0_temp['max_stock_price_happen']=0
        d0_temp.loc[d0_temp['Open_HSI']==max_stock_price,'max_stock_price_happen']=1
        

        mdd=max(np.maximum.accumulate(d0_temp['cum_pnl_openpos'])-d0_temp['cum_pnl_openpos'])
        d0_temp['mdd']=mdd
        d0_temp['capital_prudent']=max_stock_price+mdd
        d0_temp['return']=d0_temp['cum_pnl_openpos'].values[-1]/d0_temp['capital_prudent']
        d0_temp['cumpnl']=d0_temp['cum_pnl_openpos'].values[-1]
        d0_temp['initial_S']=d0_temp['Open_HSI'].values[0]
        d0_temp['ending_S']=d0_temp['Close_HSI'].values[-1]
        d0_temp['ytd_close']=d0_temp['Close_HSI'].shift(1)
        d0_temp.loc[pd.isnull(d0_temp['ytd_close']),'ytd_close']=d0_temp['Open_HSI']  #for first year in backtest, first row no last close, so use open to replace
        d0_temp['asset_name']=asset_name
        d0_temp['no_of_trades']=d0_temp['no_of_trades'].values[0]
        d0_temp['up_trades_percent']=d0_temp['up_trades_percent'].values[0]
        d0_temp['holding_days_mean']=d0_temp['holding_days_mean'].values[0]
        d0_temp['long_pnl_portion']=d0_temp['long_pnl_portion'].values[0]
        
        return d0_temp
        
    
    d0_stat=d0.groupby(['year']).apply(lambda x:accurate_stat(x.reset_index(drop=True)))
    d0_stat=d0_stat.reset_index(drop=True)
    
    d0_stat_year=d0_stat.groupby('year').head(1)
    d0_stat_year=d0_stat_year[['year','asset_name','initial_S','ending_S','mdd','max_stock_price','capital_prudent',
                               'cumpnl','return','no_of_trades','up_trades_percent',
                               'holding_days_mean','long_pnl_portion']].copy()
    d0_stat_year['mdd/capital']=d0_stat_year['mdd']/d0_stat_year['capital_prudent']
    
    #replace initial S by last year last day price
    d0_stat_year['initial_S'][1:]=d0_stat_year['ending_S'].shift(1)[1:].copy()
    
    d0_stat_year=d0_stat_year.reset_index(drop=True)
    
    d0_stat_year.loc['Mean',:]= d0_stat_year[-5000:].mean(axis=0)
    
    vars()['d0_temp_'+asset_name]=d0_stat.copy()
    vars()['d0_stat_year_'+asset_name]=d0_stat_year.copy()
















#d0_temp['cum_pnl']+d0_temp['face_pnl']



#all assets grouped

initial_S_0=vars()['d0_stat_year_'+alls[0][1]][['year','initial_S']].copy()
initial_S_0=initial_S_0.rename(columns={'initial_S':'initial_S'+'_'+alls[0][1]})

d0_temp_0=vars()['d0_temp_'+alls[0][1]][['Date2','pnl_net']].copy()
d0_temp_0=d0_temp_0.rename(columns={'pnl_net':'pnl_net'+'_'+alls[0][1]})

cum_pnl_0=vars()['d0_temp_'+alls[0][1]][['Date2','cum_pnl']].copy()
cum_pnl_0=cum_pnl_0.rename(columns={'cum_pnl':'cum_pnl'+'_'+alls[0][1]})

face_pnl_0=vars()['d0_temp_'+alls[0][1]][['Date2','face_pnl']].copy()
face_pnl_0=face_pnl_0.rename(columns={'face_pnl':'face_pnl'+'_'+alls[0][1]})


ytd_close_0=vars()['d0_temp_'+alls[0][1]][['Date2','ytd_close']].copy()
ytd_close_0=ytd_close_0.rename(columns={'ytd_close':'ytd_close'+'_'+alls[0][1]})

d0_bet_0=vars()['d0_temp_'+alls[0][1]][['Date2','bet']].copy()
d0_bet_0=d0_bet_0.rename(columns={'bet':'bet'+'_'+alls[0][1]})

capital_0=vars()['d0_stat_year_'+alls[0][1]][['year','max_stock_price']].copy()
capital_0=capital_0.rename(columns={'max_stock_price':'max_stock_price'+'_'+alls[0][1]})

no_of_trade_0=vars()['d0_stat_year_'+alls[0][1]][['year','no_of_trades']].copy()
no_of_trade_0=no_of_trade_0.rename(columns={'no_of_trades':'no_of_trades'+'_'+alls[0][1]})

up_trades_percent_0=vars()['d0_stat_year_'+alls[0][1]][['year','up_trades_percent']].copy()
up_trades_percent_0=up_trades_percent_0.rename(columns={'up_trades_percent':'up_trades_percent'+'_'+alls[0][1]})










#bet_0=vars()['d0_temp_'+alls[0][1]][['Date2','bet']].copy()
#bet_0=bet_0.rename(columns={'bet':'bet'+'_'+alls[0][1]})

#x=alls[1]
for x in alls[1:]:
    asset_name=x[1]
    
    #merge all initial S
    initial_S_0_temp=vars()['d0_stat_year_'+asset_name][['initial_S']].copy()
    initial_S_0_temp=initial_S_0_temp.rename(columns={'initial_S':'initial_S'+'_'+asset_name})
    initial_S_0=pd.concat([initial_S_0,initial_S_0_temp],axis=1)
    
    #merge all capital required
    capital_0_temp=vars()['d0_stat_year_'+asset_name][['max_stock_price']].copy()
    capital_0_temp=capital_0_temp.rename(columns={'max_stock_price':'max_stock_price'+'_'+asset_name})
    capital_0=pd.concat([capital_0,capital_0_temp],axis=1)
    
    #merge all pnl_net
    d0_temp_0_temp=vars()['d0_temp_'+asset_name][['Date2','pnl_net']].copy()
    d0_temp_0_temp=d0_temp_0_temp.rename(columns={'pnl_net':'pnl_net'+'_'+asset_name})
    d0_temp_0=pd.merge(d0_temp_0,d0_temp_0_temp,how='outer',on=['Date2'])


    #merge all cum_pnl
    cum_pnl_temp=vars()['d0_temp_'+asset_name][['Date2','cum_pnl']].copy()
    cum_pnl_temp=cum_pnl_temp.rename(columns={'cum_pnl':'cum_pnl'+'_'+asset_name})
    cum_pnl_0=pd.merge(cum_pnl_0,cum_pnl_temp,how='outer',on=['Date2'])

    #merge all face_pnl
    face_pnl_temp=vars()['d0_temp_'+asset_name][['Date2','face_pnl']].copy()
    face_pnl_temp=face_pnl_temp.rename(columns={'face_pnl':'face_pnl'+'_'+asset_name})
    face_pnl_0=pd.merge(face_pnl_0,face_pnl_temp,how='outer',on=['Date2'])

    #merge all ytd_close
    ytd_close_temp=vars()['d0_temp_'+asset_name][['Date2','ytd_close']].copy()
    ytd_close_temp=ytd_close_temp.rename(columns={'ytd_close':'ytd_close'+'_'+asset_name})
    ytd_close_0=pd.merge(ytd_close_0,ytd_close_temp,how='outer',on=['Date2'])

    #merge all bet
    d0_bet_0_temp=vars()['d0_temp_'+asset_name][['Date2','bet']].copy()
    d0_bet_0_temp=d0_bet_0_temp.rename(columns={'bet':'bet'+'_'+asset_name})
    d0_bet_0=pd.merge(d0_bet_0,d0_bet_0_temp,how='outer',on=['Date2'])

    #merge all no of trade
    no_of_trade_0_temp=vars()['d0_stat_year_'+asset_name][['no_of_trades']].copy()
    no_of_trade_0_temp=no_of_trade_0_temp.rename(columns={'no_of_trades':'no_of_trades'+'_'+asset_name})
    no_of_trade_0=pd.concat([no_of_trade_0,no_of_trade_0_temp],axis=1)

    #merge all up trade percent
    up_trades_percent_0_temp=vars()['d0_stat_year_'+asset_name][['up_trades_percent']].copy()
    up_trades_percent_0_temp=up_trades_percent_0_temp.rename(columns={'up_trades_percent':'up_trades_percent'+'_'+asset_name})
    up_trades_percent_0=pd.concat([up_trades_percent_0,up_trades_percent_0_temp],axis=1)




no_of_trade_0['sum']=no_of_trade_0.iloc[:,1:].values.sum(axis=1)










##in 2011-4-28, VRTX no value,
#if 'ytd_close_VRTX' in ytd_close_0.columns.tolist():
#    ytd_close_0.loc[ytd_close_0['Date2']=='2011-04-28','ytd_close_VRTX']=52.92
#    ytd_close_0.loc[ytd_close_0['Date2']=='2015-05-12','ytd_close_VRTX']=127.41
                                                                                




initial_capital=500000#500000#350000
number_asset=len(alls)
max_invest_per_asset=initial_capital/number_asset
margin_rate=1/5#1/5


##find stock weight
#ytd_close_0['check_zero']=np.sum(ytd_close_0.iloc[:,1:].values==0,axis=1)
#ytd_close_0['check']=ytd_close_0.isnull().any(axis=1)

##if use drop row of one nan in columns
##each assert need to have same date 
#ytd_close_0=ytd_close_0.dropna()     #drop all rows that have any NaN values
#ytd_close_0.shape[0]
#
#final_date_overall=ytd_close_0.Date2.values[-1]

#so better to manually check
final_date_overall='2023-02-07'


ytd_close_0=ytd_close_0.loc[ytd_close_0['Date2']<=final_date_overall,:].copy()
ytd_close_0=ytd_close_0.reset_index(drop=True)


#for VRTX no 2011-04-28 and 2015-05-12
#so need to replace nan by previous value
ytd_close_0=ytd_close_0.fillna(method='ffill')



ytd_close_0_temp=ytd_close_0.values[:,1:]



buy_more_less=0.6 #0.6  #i use 0.7, client use 0.55, larger the number , buy more.
ytd_close_0_temp=ytd_close_0_temp*(margin_rate/buy_more_less) 

nn2=max_invest_per_asset/ytd_close_0_temp  # it is for example, max invet in stock priced 50 is 1000, then (1000/(50*margin))*buy_more_less

nn2=nn2.astype(float)


stock_weight=np.multiply(np.round(nn2,-1),nn2>5)+np.multiply(np.round(nn2),nn2<=5)
#stock_weight=np.round(nn2,-1) #round to nearest 10
stock_weight
stock_weight=pd.DataFrame(stock_weight)

stock_weight.columns= ['weight_'+x[1] for x in alls]

stock_weight['Date2']=ytd_close_0['Date2'].copy()


#a_check=stock_weight['weight_UK_DGE_wsj']




new_pnl=d0_temp_0.loc[d0_temp_0['Date2']<=final_date_overall,:].copy()
new_pnl['year']=new_pnl.Date2.str[0:4]
new_pnl['pnl_all']=0
new_pnl['max_margin_requirement']=0

#x=alls[0]
for x in alls:
    asset_name=x[1]
    #asset_name='STT'
    #asset_name='UK_DGE_wsj'
    df_temp=vars()['d0_temp_'+asset_name][vars()['d0_temp_'+asset_name]['Date2']<=final_date_overall].copy()
    df_temp=df_temp.iloc[:,0:22].copy()
    df_temp=pd.merge(df_temp,stock_weight[['Date2','weight_'+asset_name]].copy(),how='left',on='Date2')
    df_temp_trade=df_temp.loc[~pd.isnull(df_temp['exit_time']),:].copy()
    df_temp_trade['PnL_after_commission']=df_temp_trade['PnL_after_commission']*df_temp_trade['weight_'+asset_name]

    df_temp=pd.merge(df_temp,df_temp_trade[['exit_time','PnL_after_commission']].copy(),
                     how='left',left_on='Date2',right_on='exit_time',suffixes=('','_2'))
    df_temp['entry_time_temp']=df_temp['entry_time'].fillna(method='ffill')
    df_temp.loc[df_temp['bet']==0,'entry_time_temp']=0

    df_temp=pd.merge(df_temp,df_temp_trade[['entry_time','weight_'+asset_name]].copy(),
                     how='left',left_on='entry_time_temp',right_on='entry_time',suffixes=('','_2'))
    df_temp['weight_'+asset_name+'_2']=df_temp['weight_'+asset_name+'_2'].fillna(0)
    df_temp['face_pnl2']=df_temp['face_pnl']*df_temp['weight_'+asset_name+'_2']
    df_temp['face_pnl2']=df_temp['face_pnl2'].fillna(0)
    
    df_temp['PnL_after_commission_2']=df_temp['PnL_after_commission_2'].fillna(0)
    df_temp['cum_pnl2']=df_temp['PnL_after_commission_2'].cumsum()
    
    df_temp['cum_pnl_openpos2']=df_temp['cum_pnl2']+df_temp['face_pnl2']
    df_temp['cum_pnl_openpos2_lag1']=df_temp['cum_pnl_openpos2'].shift(1)
    df_temp['cum_pnl_openpos2_lag1']=df_temp['cum_pnl_openpos2_lag1'].fillna(0)
    df_temp['pnl_net2']=df_temp['cum_pnl_openpos2']-df_temp['cum_pnl_openpos2_lag1']    
    

    #print(sum((df_temp['PnL_after_commission_2'])))
    
    #print(sum((df_temp['pnl_net2'])))
    
    df_temp['max_margin_requirement_'+asset_name]=df_temp['High_HSI']*df_temp['weight_'+asset_name+'_2']*margin_rate*abs(df_temp['bet'])
    df_temp['bet_'+asset_name]=df_temp['bet'].copy()
    df_temp_merge=df_temp[['Date2','bet_'+asset_name,'weight_'+asset_name+'_2','pnl_net2','max_margin_requirement_'+asset_name]].copy()
    
    new_pnl=pd.merge(new_pnl,df_temp_merge,how='left',on=['Date2'])
    new_pnl=new_pnl.fillna(0)

    new_pnl['pnl_all']=new_pnl['pnl_all']+new_pnl['pnl_net2']
    new_pnl['pnl_'+asset_name]=new_pnl['pnl_net2'].copy()
    del new_pnl['pnl_net2']
    new_pnl['max_margin_requirement']=new_pnl['max_margin_requirement']+new_pnl['max_margin_requirement_'+asset_name]   
    del new_pnl['max_margin_requirement_'+asset_name]   
    
    new_pnl['size_'+asset_name]=new_pnl['weight_'+asset_name+'_2']*abs(new_pnl['bet_'+asset_name])






# find individual cum pnl for a specific year 2022
import matplotlib.pyplot as plt
new_pnl_check=new_pnl.loc[new_pnl['year']>='2015',:].copy()
for x in alls:
    asset_name=x[1]
    new_pnl_check['pnl_'+asset_name+'_cum']=new_pnl_check['pnl_'+asset_name].cumsum()
    

#plot on cum of all stock in a specific year
plt.figure(figsize=(8,8))
plt.plot(range(0,new_pnl_check.shape[0]),new_pnl_check['pnl_all'].cumsum())
plt.legend(loc='best')
plt.xlabel('all stocks')
plt.ylabel('Cum.PnL')


#new_pnl_check2=new_pnl.loc[new_pnl['year']=='2020','pnl_'+'UK_DGE_wsj'].copy()



#multiple cum pnl plot  in a specific year
import matplotlib.pyplot as plt
plt.figure(figsize=(10,30), dpi=80, facecolor='w', edgecolor='k')

Ws={}
i=1
for x in alls:
    asset_name=x[1]
    Ws.update({i:new_pnl_check['pnl_'+asset_name+'_cum'].values})
    i=i+1

for i,H in Ws.items():
    plt.subplot(10,3,i).set_title("Stock "+str(i)) #fist two argument is the dimension, the three argument is the number for each plot
    plt.tight_layout() # Or equivalently,  "plt.tight_layout()"
    plt.plot(range(0,len(H)),H,'*', color='r')
    plt.xlabel(alls[i-1][1])
    plt.ylabel('Cum.PnL')    


 













##check correlation
#col_use=['pnl_net_'+x[1] for x in alls]
#col_use2=col_use+['Date2']
#
#new_pnl_check=new_pnl.loc[new_pnl['Date2']<='2014-12-31',col_use2].copy()
#
#new_pnl_check_cor_table=new_pnl_check[col_use].corr()
#new_pnl_check_cor_table=new_pnl_check_cor_table.sort_values(by='pnl_net_VRTX',ascending=False)
#new_pnl_check_cor_table['index']=new_pnl_check_cor_table.index

    
    


new_pnl['pnl_all_cum']=new_pnl['pnl_all'].cumsum()
new_pnl.to_csv(os.path.join(main_dir_original,'IB_live_trade',"new_pnl.csv"),index=False)


#investigaet positive and negative pnl
use_list=['pnl_net_'+x[1] for x in alls]
pos_neg_pnl=new_pnl[use_list].copy()
pos_neg_pnl=(pos_neg_pnl>0)*1
pos_neg_pnl=pd.DataFrame(np.sum(pos_neg_pnl,axis=1))
pos_neg_pnl=pos_neg_pnl.rename(columns={0:'count_pn'})
pos_neg_pnl['year']=new_pnl['year'].copy()

p_temp1=pos_neg_pnl.groupby(['year'])['count_pn'].value_counts(normalize=True)*100
p_temp1




#investigaet number of buy and sell
use_list=['bet_'+x[1] for x in alls]
pos_neg_pnl=new_pnl[use_list].copy()
pos_neg_pnl=(pos_neg_pnl>0)*1
pos_neg_pnl=pd.DataFrame(np.sum(pos_neg_pnl,axis=1))
pos_neg_pnl=pos_neg_pnl.rename(columns={0:'buy_count'})
pos_neg_pnl['year']=new_pnl['year'].copy()
pos_neg_pnl['Date2']=new_pnl['Date2'].copy()

p_temp2=pos_neg_pnl.groupby(['year'])['buy_count'].value_counts(normalize=True)*100
p_temp2

pos_neg_pnl3=new_pnl[use_list].copy()
pos_neg_pnl3['count']=pos_neg_pnl['buy_count'].values
pos_neg_pnl3['year']=new_pnl['year'].copy()
pos_neg_pnl3['Date2']=new_pnl['Date2'].copy()
pos_neg_pnl3['pnl_all']=new_pnl['pnl_all'].copy()






d0=new_pnl.copy()
#sharpe ratio and accuracy
xx=d0.loc[d0['year']=="2021",:]
pnl_col_name='pnl_all'
def sharpe_ratio(xx,pnl_col_name='PnL_after_commission_adjusted_6min_mean',initial_capital=50):
    #Cum_pnl
    cum_pnl=sum(xx[pnl_col_name])
    
    #accuracy
    acc=sum(xx[pnl_col_name]>0)/sum(xx[pnl_col_name]!=0)
    
    #max cum loss
    xx['cum_pnl']=xx[pnl_col_name].cumsum()
    max_cum_loss=min(xx['cum_pnl'].values)
    
    #average gain per trade/average loss per trade
    ave_gain=np.mean(xx.loc[xx[pnl_col_name]>0,pnl_col_name].values)
    ave_loss=abs(np.mean(xx.loc[xx[pnl_col_name]<0,pnl_col_name].values))
    ave_gain_over_ave_loss=ave_gain/ave_loss
    
    #drawdown
    mdd=max(np.maximum.accumulate(xx['cum_pnl'])-xx['cum_pnl'])
    max_margin=max(xx['max_margin_requirement'].values)
    risk_free_rate=0
    #capital=max_margin+mdd
    capital=initial_capital
    xx['capital']=capital
    #xx['capital']=max_margin+mdd
    xx['return']=xx[pnl_col_name]/xx['capital']

    year_output=xx['year'].values[0]
    SR=((xx['return'].mean()-risk_free_rate)/xx['return'].std())*np.sqrt(252)
    return pd.Series([year_output,SR,acc,max_cum_loss,ave_gain,ave_loss,ave_gain_over_ave_loss,cum_pnl,mdd,capital,max_margin])

#PnL_after_commission    PnL_after_commission_adjusted_6min_mean
d0_SR=d0.groupby(["year"]).apply(lambda x:sharpe_ratio(x.reset_index(drop=True),'pnl_all',initial_capital))
d0_SR=d0_SR.rename(columns={0:'year',1:'SR',2:'accuracy',3:'max_cum_loss',4:'ave_gain',5:'ave_loss',6:'gain/loss',7:'cum_pnl',8:'mdd',9:'capital',10:'max_margin'})

d0_SR['mdd/capital']=d0_SR['mdd']/d0_SR['capital']
d0_SR['return']=d0_SR['cum_pnl']/d0_SR['capital']

#d0_SR=pd.merge(d0_SR,initial_S_0,how='left',on=['year'])
#d0_SR=pd.concat([d0_SR,pd.DataFrame(stock_weight)],axis=1)



#cols = d0_SR.columns.tolist()
#cols.insert(1, cols.pop(cols.index('cum_pnl')))
#cols.insert(2, cols.pop(cols.index('max_cum_loss')))
#cols.insert(3, cols.pop(cols.index('P&L/MaxCumLoss')))
#cols.insert(4, cols.pop(cols.index('gain/loss')))
#cols.insert(5, cols.pop(cols.index('accuracy')))
#cols.insert(6, cols.pop(cols.index('margin')))
#cols.insert(7, cols.pop(cols.index('return')))
#
#d0_SR = d0_SR.reindex(columns= cols)

#d0_SR=d0_SR.loc[d0_SR['year']<'2009',:].copy()


#d0_SR.loc['Mean (1999-2008)',:]= d0_SR.mean(axis=0) 

d0_SR.loc['Mean (2018-2022)',:]= d0_SR[-5:].mean(axis=0)  #LAST FIVE YEAR MEAN
d0_SR.loc['Mean (all years)',:]= d0_SR[:].mean(axis=0)  

d0_SR.dtypes


tname='us_bet'
d0_use=d0.loc[d0['Date2']>='2008-01-01',['Date2','pnl_all']].copy()
d0_use.to_csv(os.path.join('/home/jonathanjames/my_storage/tradelog/index_analysis_cumulative/backtest_linux/check','d0_'+tname+'.csv'))
d0_SR.to_csv(os.path.join('/home/jonathanjames/my_storage/tradelog/index_analysis_cumulative/backtest_linux/check','d0_SR_'+tname+'.csv'))


  



d0_SR2=d0_SR[['year','max_margin','accuracy','mdd','mdd/capital','cum_pnl','return']].copy()   

d0_SR2[0:-2].to_csv(os.path.join(main_dir_original,'IB_live_trade',"d0_SR2.csv"),index=False)


d0_SR2.style.highlight_max(axis=0)






#look at number of trade, up portion and average holding days
stat2=pd.DataFrame([])

x=[list(range(19860,19874)),'IP']
for x in alls:
    asset_name=x[1]
    temp=vars()['d0_stat_year_'+asset_name].copy()
    temp=temp.loc[~pd.isnull(temp['asset_name']),:].copy()
    temp.dtypes
    
    
    temp2=pd.DataFrame({'Asset':[asset_name],
                        'Average_No_of_Trade':[round(np.mean(temp['no_of_trades'].values))],
                        'Average_Holding_Days':[round(np.mean(temp['holding_days_mean'].values))],
                        'Average_Long%':[round(np.mean(temp['up_trades_percent'].values),3)]
                        })
    stat2=stat2.append(temp2)

stat2=stat2.sort_values(by=['Average_Holding_Days'],ascending=['True'])
stat2.to_csv(os.path.join(main_dir_original,'IB_live_trade',"stat2.csv"),index=False)




#look at pnl contribution by each ticker
pnl_by_ticker=pd.DataFrame([])

x=[list(range(19860,19874)),'IP']
for x in alls:
    asset_name=x[1]
    temp=sum(new_pnl['pnl_'+asset_name].values)/sum(new_pnl['pnl_all'])
    temp=pd.DataFrame({'Asset':[asset_name],'P&L %':[temp]
                        })
    pnl_by_ticker=pnl_by_ticker.append(temp)    

import plotly.express as px
df = pnl_by_ticker.copy()
fig = px.pie(df, values='P&L %', names='Asset', title='P&L Contribution by Each Asset',width=1600, height=1000)

fig.update_layout(font=dict(size=22),legend_font_size=25)  #font is the text size in the pie chart

fig.update_traces(textposition='inside', textinfo='percent+label')
                            
fig.write_image(os.path.join(main_dir_original,'IB_live_trade',"pnl_by_tickers.jpeg"))

pnl_by_ticker.to_csv(os.path.join(main_dir_original,'IB_live_trade',"pnl_by_ticker.csv"),index=False)













#look at bench mark
spx=pd.read_excel(os.path.join(main_dir_original,"index_SPX_wsj_with_tidy.xlsx"),"Sheet1")
djia=pd.read_excel(os.path.join(main_dir_original,"index_DJIA_wsj_with_tidy.xlsx"),"Sheet1")
spx=pd.merge(spx,djia[['Date2','Open_index_DJIA_wsj','Close_index_DJIA_wsj']].copy(),how='left',on=['Date2'])

d0_benchmark=pd.merge(d0[['Date2','pnl_all','year']].copy(),spx[['Date2','Close_index_SPX_wsj','Close_index_DJIA_wsj']].copy(),how='left',on=['Date2'])
d0_benchmark=d0_benchmark.fillna(method='ffill')
d0_benchmark['pnl_all'][0]=0
d0_benchmark['pnl_all']=d0_benchmark['pnl_all'].cumsum()
d0_benchmark['account_value']=d0_benchmark['pnl_all']+500000
d0_benchmark['model_return']=d0_benchmark['account_value']/500000

d0_benchmark['spx_return']=d0_benchmark['Close_index_SPX_wsj']/d0_benchmark['Close_index_SPX_wsj'][0]
d0_benchmark['DJIA_return']=d0_benchmark['Close_index_DJIA_wsj']/d0_benchmark['Close_index_DJIA_wsj'][0]

d0_benchmark.to_csv(os.path.join(main_dir_original,'IB_live_trade',"d0_benchmark.csv"),index=False)


from plotly.offline import download_plotlyjs, init_notebook_mode,  plot
from plotly import graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff





x =d0_benchmark['Date2'].values
y1 = d0_benchmark['model_return'].values
y2 = d0_benchmark['spx_return'].values
y3 = d0_benchmark['DJIA_return'].values

layout = go.Layout(autosize=False,width=1300,height=700,
                   title='<span style="font-size: 30px;">Model VS Benchmarks</span>',
                   xaxis_title='<b>Date</b>',#"Date",
                   yaxis_title='<b>Account Value</b>',#"Cumulative P&L",
                   legend_title='')
                   #legend_title='<span style="font-size: 15px;">Legend Description</span>')
fig = go.Figure(layout=layout)
obj1 = go.Scatter(x = x,y = y1,mode = 'lines',marker=dict(color='#0000FF'))
fig.add_trace(obj1)
fig['data'][0]['name'] = 'Model'   #change legend first color description name

obj2 = go.Scatter(x = x,y = y2,mode = 'lines',marker=dict(color='#FF7F50'))
fig.add_trace(obj2)
fig['data'][1]['name'] = 'S&P Index'   #change legend first color description name

obj3 = go.Scatter(x = x,y = y3,mode = 'lines',marker=dict(color='#CDAA7D'))
fig.add_trace(obj3)
fig['data'][2]['name'] = 'Dow Jones Index'   #change legend first color description name


#add horizontal line
fig.add_hline(y=1, line_dash="dot",annotation_text='<span style="font-size: 19px;">Initial Balance</span>',annotation_position="bottom")


fig.update_yaxes(title_font=dict(size=20),tickfont = dict(size=16))
fig.update_xaxes(title_font=dict(size=20), tickfont = dict(size=16))


fig.update_layout(legend=dict(yanchor="top", y=1, xanchor="left", x=0.02,bgcolor="rgba(0,0,0,0)"),legend_font_size=17)


plot(fig)

fig.write_image(os.path.join(main_dir_original,'IB_live_trade',"plotly_temp_benchmark.jpeg"))





























#yearly performance
year_list=list(range(2009,2023,1))
subplot_titletext=tuple(['<span style="font-size: 25px;">Model VS Benchmarks - Year '+str(x)+' '+'</span>' for x in year_list])


dimx=5
dimy=3
res = np.full((dimx,dimy), np.nan)  
res.flat[:len(year_list)]=np.array(year_list) 
year_matrix=np.reshape(np.array(res),(dimx,dimy))
# plotly fig setup
fig = make_subplots(rows=dimx,cols=dimy,subplot_titles=subplot_titletext,horizontal_spacing = 0.05,vertical_spacing = 0.05) 

benchmark_yearly=pd.DataFrame([])

i='2013'
for i in year_list: 
    i=str(i)
    d_temp=d0.loc[d0['year']==i,['Date2','pnl_all']].copy()
    d_temp2=pd.merge(d_temp,spx[['Date2','Close_index_SPX_wsj','Close_index_DJIA_wsj']].copy(),how='left',on=['Date2'])
    d_temp2=d_temp2.fillna(method='ffill')
    d_temp2['pnl_all'][0]=0
    d_temp2['pnl_all']=d_temp2['pnl_all'].cumsum()
    d_temp2['account_value']=d_temp2['pnl_all']+500000
    d_temp2['model_return']=d_temp2['account_value']/500000
    
    d_temp2['spx_return']=d_temp2['Close_index_SPX_wsj']/d_temp2['Close_index_SPX_wsj'][0]
    d_temp2['DJIA_return']=d_temp2['Close_index_DJIA_wsj']/d_temp2['Close_index_DJIA_wsj'][0]
    
    benchmark_yearly=benchmark_yearly.append(d_temp2)
    vars()['d0_benchmark_'+i]=d_temp2.copy()
    
    x =vars()['d0_benchmark_'+i]['Date2'].values
    y1 = vars()['d0_benchmark_'+i]['model_return'].values
    y2 = vars()['d0_benchmark_'+i]['spx_return'].values
    y3 = vars()['d0_benchmark_'+i]['DJIA_return'].values
    
    locate1=np.where(year_matrix==int(i))[0][0]+1
    locate2=np.where(year_matrix==int(i))[1][0]+1
    show_leg=True if i=='2009' else False   #only show legend for first plot otherwise will hv many same legend
    print(show_leg)
    
    #name is legend name
    obj1 = go.Scatter(x = x,y = y1,mode = 'lines',marker=dict(color='#0000FF'),name='Model',showlegend=show_leg)
    fig.append_trace(obj1,locate1,locate2)
    #fig['data'][0]['name'] = 'Model'   #change legend first color description name
    
    obj2 = go.Scatter(x = x,y = y2,mode = 'lines',marker=dict(color='#FF7F50'),name="S&P Index",showlegend=show_leg)
    fig.append_trace(obj2,locate1,locate2)
    #fig['data'][1]['name'] = 'S&P Index'   #change legend first color description name
    
    obj3 = go.Scatter(x = x,y = y3,mode = 'lines',marker=dict(color='#CDAA7D'),name='Dow Jones Index',showlegend=show_leg)
    fig.append_trace(obj3,locate1,locate2)
    #fig['data'][2]['name'] = 'Dow Jones Index'   #change legend first color description name
    
    #add horizontal line
    obj4 = go.Scatter(x = [x.min(), x.max()],y = [1, 1],mode = 'lines',line=dict(color="#000000"),name='Initial Balance',showlegend=show_leg,line_dash="dot",text="Initial balance")
    fig.append_trace(obj4,locate1,locate2)
    #fig['data'][4]['name'] = 'Initial Balance'
    
fig.for_each_xaxis(lambda axis: axis.update(tickfont=dict(size=16)))
fig.for_each_xaxis(lambda axis: axis.title.update(font=dict(size=20)))
fig.for_each_xaxis(lambda axis: axis.title.update(text='Date'))
fig.for_each_yaxis(lambda axis: axis.update(tickfont=dict(size=16)))
fig.for_each_yaxis(lambda axis: axis.title.update(font=dict(size=20)))
fig.for_each_yaxis(lambda axis: axis.title.update(text='Account Value'))

fig.update_layout(height=3000, width=1800,legend_font_size=19)


# plot it
plot(fig)
fig.write_image(os.path.join(main_dir_original,'IB_live_trade',"plotly_temp_benchmark_per_year.jpeg"))
fig.write_image(os.path.join(main_dir_original,'IB_live_trade',"US_Model_Yearly_Plot.pdf"))

fig.write_html(os.path.join(main_dir_original,'IB_live_trade',"plotly_temp_benchmark_per_year.html"))


benchmark_yearly.to_csv(os.path.join(main_dir_original,'IB_live_trade',"benchmark_yearly.csv"),index=False)







#split into 4 groups
    
    
from plotly.offline import download_plotlyjs, init_notebook_mode,  plot
from plotly import graph_objects as go
from plotly.subplots import make_subplots

g1=['JPM','IP','MCD','V','AMT']   #for corporate
g2=['MNST','BAC','LIN','TXN','CMCSA']   #for corporate
g3=['NFLX','DE','EA','VRTX','UNH']   #for corporate
g4=['SWKS','WFC','MSFT','GILD','BA']   #for corporate

#r1=['BAC','MCD','TXN','GILD']  #for retail


r1=['MCD','EA','GILD']  #for retail


all_group=[g1,g2,g3,g4,r1]


capital_single_combo=(initial_capital/len(alls))

d0['g1_pnl']=0
d0['g2_pnl']=0
d0['g3_pnl']=0
d0['g4_pnl']=0
d0['r1_pnl']=0

for x in g1:
    d0['g1_pnl']=d0['g1_pnl']+d0['pnl_'+x]
for x in g2:
    d0['g2_pnl']=d0['g2_pnl']+d0['pnl_'+x]
for x in g3:
    d0['g3_pnl']=d0['g3_pnl']+d0['pnl_'+x]
for x in g4:
    d0['g4_pnl']=d0['g4_pnl']+d0['pnl_'+x]

for x in r1:
    d0['r1_pnl']=d0['r1_pnl']+d0['pnl_'+x]

for target in ['g1','g2','g3','g4','r1']:
    #target='g1'
    display_name='Combo '+target.replace('g','')
    display_name=display_name.replace('r1','R1')
    spx=pd.read_excel(os.path.join(main_dir_original,"index_SPX_wsj_with_tidy.xlsx"),"Sheet1")
    djia=pd.read_excel(os.path.join(main_dir_original,"index_DJIA_wsj_with_tidy.xlsx"),"Sheet1")
    spx=pd.merge(spx,djia[['Date2','Open_index_DJIA_wsj','Close_index_DJIA_wsj']].copy(),how='left',on=['Date2'])
    
    d0_benchmark=pd.merge(d0[['Date2',target+'_pnl']].copy(),spx[['Date2','Close_index_SPX_wsj','Close_index_DJIA_wsj']].copy(),how='left',on=['Date2'])
    d0_benchmark=d0_benchmark.fillna(method='ffill')
    d0_benchmark[target+'_pnl'][0]=0
    d0_benchmark[target+'_pnl']=d0_benchmark[target+'_pnl'].cumsum()
    d0_benchmark['account_value']=d0_benchmark[target+'_pnl']+(capital_single_combo*len(vars()[target]))
    d0_benchmark['model_return']=d0_benchmark['account_value']/(capital_single_combo*len(vars()[target]))
    
    d0_benchmark['spx_return']=d0_benchmark['Close_index_SPX_wsj']/d0_benchmark['Close_index_SPX_wsj'][0]
    d0_benchmark['DJIA_return']=d0_benchmark['Close_index_DJIA_wsj']/d0_benchmark['Close_index_DJIA_wsj'][0]

    x =d0_benchmark['Date2'].values
    y1 = d0_benchmark['model_return'].values
    y2 = d0_benchmark['spx_return'].values
    y3 = d0_benchmark['DJIA_return'].values
    
    layout = go.Layout(autosize=False,width=1300,height=700,
                       title='<span style="font-size: 30px;">'+display_name+' VS Benchmarks</span>',
                       xaxis_title='<b>Date</b>',#"Date",
                       yaxis_title='<b>Account Value</b>',#"Cumulative P&L",
                       legend_title='')
                       #legend_title='<span style="font-size: 15px;">Legend Description</span>')
    fig = go.Figure(layout=layout)
    obj1 = go.Scatter(x = x,y = y1,mode = 'lines',marker=dict(color='#0000FF'))
    fig.add_trace(obj1)
    fig['data'][0]['name'] = display_name   #change legend first color description name
    
    obj2 = go.Scatter(x = x,y = y2,mode = 'lines',marker=dict(color='#FF7F50'))
    fig.add_trace(obj2)
    fig['data'][1]['name'] = 'S&P Index'   #change legend first color description name
    
    obj3 = go.Scatter(x = x,y = y3,mode = 'lines',marker=dict(color='#CDAA7D'))
    fig.add_trace(obj3)
    fig['data'][2]['name'] = 'Dow Jones Index'   #change legend first color description name
    
    #add horizontal line
    fig.add_hline(y=1, line_dash="dot",annotation_text='<span style="font-size: 19px;">Initial Balance</span>',annotation_position="bottom")
    
    fig.update_yaxes(title_font=dict(size=20),tickfont = dict(size=16))
    fig.update_xaxes(title_font=dict(size=20), tickfont = dict(size=16))
    fig.update_layout(legend=dict(yanchor="top", y=1, xanchor="left", x=0.02,bgcolor="rgba(0,0,0,0)"),legend_font_size=17)
    
    plot(fig)
    fig.write_image(os.path.join(main_dir_original,'IB_live_trade',"plotly_temp_benchmark_"+target+".jpeg"))
    
    c_temp=capital_single_combo*len(vars()[target])
    vars()['d0_'+target]=d0.groupby(["year"]).apply(lambda x:sharpe_ratio(x.reset_index(drop=True),target+'_pnl',c_temp))
    vars()['d0_'+target]=vars()['d0_'+target].rename(columns={0:'year',1:'SR',2:'accuracy',3:'max_cum_loss',4:'ave_gain',5:'ave_loss',6:'gain/loss',7:'cum_pnl',8:'mdd',9:'capital',10:'max_margin'})
    vars()['d0_'+target]['return']=vars()['d0_'+target]['cum_pnl']/c_temp
    vars()['d0_'+target]['mdd/capital']=vars()['d0_'+target]['mdd']/c_temp
    vars()['d0_'+target].loc['Mean (all years)',:]= vars()['d0_'+target][:].mean(axis=0)  

#c_temp=capital_single_combo*len(vars()['g1'])
#d0_g1=d0.groupby(["year"]).apply(lambda x:sharpe_ratio(x.reset_index(drop=True),'g1_pnl',c_temp))
#d0_g1=d0_g1.rename(columns={0:'year',1:'SR',2:'accuracy',3:'max_cum_loss',4:'ave_gain',5:'ave_loss',6:'gain/loss',7:'cum_pnl',8:'mdd',9:'capital',10:'max_margin'})
#d0_g1['return']=d0_g1['cum_pnl']/c_temp
#d0_g1['mdd/capital']=d0_g1['mdd']/c_temp
#d0_g1.loc['Mean (all years)',:]= d0_g1[:].mean(axis=0)  
#
#c_temp=capital_single_combo*len(vars()['g2'])
#d0_g2=d0.groupby(["year"]).apply(lambda x:sharpe_ratio(x.reset_index(drop=True),'g2_pnl',c_temp))
#d0_g2=d0_g2.rename(columns={0:'year',1:'SR',2:'accuracy',3:'max_cum_loss',4:'ave_gain',5:'ave_loss',6:'gain/loss',7:'cum_pnl',8:'mdd',9:'capital',10:'max_margin'})
#d0_g2['return']=d0_g2['cum_pnl']/c_temp
#d0_g2['mdd/capital']=d0_g2['mdd']/c_temp
#d0_g2.loc['Mean (all years)',:]= d0_g2[:].mean(axis=0)  
#
#c_temp=capital_single_combo*len(vars()['g3'])
#d0_g3=d0.groupby(["year"]).apply(lambda x:sharpe_ratio(x.reset_index(drop=True),'g3_pnl',c_temp))
#d0_g3=d0_g3.rename(columns={0:'year',1:'SR',2:'accuracy',3:'max_cum_loss',4:'ave_gain',5:'ave_loss',6:'gain/loss',7:'cum_pnl',8:'mdd',9:'capital',10:'max_margin'})
#d0_g3['return']=d0_g3['cum_pnl']/c_temp
#d0_g3['mdd/capital']=d0_g3['mdd']/c_temp
#d0_g3.loc['Mean (all years)',:]= d0_g3[:].mean(axis=0)  
#
#c_temp=capital_single_combo*len(vars()['g4'])
#d0_g4=d0.groupby(["year"]).apply(lambda x:sharpe_ratio(x.reset_index(drop=True),'g4_pnl',c_temp))
#d0_g4=d0_g4.rename(columns={0:'year',1:'SR',2:'accuracy',3:'max_cum_loss',4:'ave_gain',5:'ave_loss',6:'gain/loss',7:'cum_pnl',8:'mdd',9:'capital',10:'max_margin'})
#d0_g4['return']=d0_g4['cum_pnl']/c_temp
#d0_g4['mdd/capital']=d0_g4['mdd']/c_temp
#d0_g4.loc['Mean (all years)',:]= d0_g4[:].mean(axis=0)  
#
#c_temp=capital_single_combo*len(vars()['r1'])
#d0_r1=d0.groupby(["year"]).apply(lambda x:sharpe_ratio(x.reset_index(drop=True),'r1_pnl',c_temp))
#d0_r1=d0_r1.rename(columns={0:'year',1:'SR',2:'accuracy',3:'max_cum_loss',4:'ave_gain',5:'ave_loss',6:'gain/loss',7:'cum_pnl',8:'mdd',9:'capital',10:'max_margin'})
#d0_r1['return']=d0_r1['cum_pnl']/c_temp
#d0_r1['mdd/capital']=d0_r1['mdd']/c_temp
#d0_r1.loc['Mean (all years)',:]= d0_r1[:].mean(axis=0) 



#all plot from 2009
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
plt.plot(range(0,d0.shape[0]), d0['pnl_all'].cumsum().values)
plt.legend(loc='best')
plt.xlabel('No.of.Trading Days Since Year 2009')
plt.ylabel('Cum.PnL')
output_path=os.path.join(main_dir_original,'IB_live_trade','pnl_plot_since_2009.png')
plt.savefig(output_path)


##plot return
#d0_use=d0.loc[d0['Date2']>='2008-01-01',['Date2','pnl_all']].copy()
#d0_use['return']=d0_use['pnl_all'].shift(1)/d0_use['pnl_all']










d0_SR2=d0_SR[['year','capital','accuracy','mdd','mdd/capital','cum_pnl','return']].copy() 
d0_SR2=d0_SR2.reset_index(drop=True)

d0_SR2.iloc[d0_SR2.shape[0]-1,d0_SR2.columns.get_loc('year')]='Mean'

d0_SR2=d0_SR2.rename(columns={'year':'Year','capital':'Capital','accuracy':'Accuracy','mdd':'Max Draw Down','mdd/capital':'Max Draw Down/Capital','cum_pnl':'Cumulative P&L','return':'Return'})

d0_SR2['Capital']=d0_SR2['Capital'].apply(lambda x:round(x))
d0_SR2['Accuracy']=d0_SR2['Accuracy'].apply(lambda x:round(x,2))
d0_SR2['Max Draw Down']=d0_SR2['Max Draw Down'].apply(lambda x:round(x))
d0_SR2['Max Draw Down/Capital']=d0_SR2['Max Draw Down/Capital'].apply(lambda x:round(x,2))
d0_SR2['Cumulative P&L']=d0_SR2['Cumulative P&L'].apply(lambda x:round(x))
d0_SR2['Return']=d0_SR2['Return'].apply(lambda x:round(x,2))

output_path=os.path.join(main_dir_original,'IB_live_trade','US_yearly_summary.csv')
d0_SR2.to_csv(output_path,index=None)




#output to monthly summary
d0['cum_pnl']=d0['pnl_all'].cumsum()
d0['cum_return']=d0['cum_pnl']/500000

d0=d0.reset_index(drop=True)

pnl_csv=d0[['Date2','cum_return']].copy()
pnl_csv=pnl_csv.rename(columns={'Date2':'Date','cum_return':'Return'})





#plot  white background
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
fig = plt.figure(figsize=(20,6))
ax = fig.add_subplot(121)

#ax.set_facecolor('black')

ax.set_xlabel('Number of Trading Days (2009-2021)')
ax.set_ylabel('Cumulative Return')

ax.text(.2,.9,'US Stock Picks Return',horizontalalignment='center',transform=ax.transAxes,color='white')


ax.xaxis.label.set_color('white')        #setting up X-axis label color to yellow
ax.yaxis.label.set_color('white')          #setting up Y-axis label color to blue

ax.tick_params(axis='x', colors='lightcyan')    #setting up X-axis tick color to red
ax.tick_params(axis='y', colors='lightcyan')  #setting up Y-axis tick color to black

ax.spines['left'].set_color('None')        # setting up Y-axis tick color to red
ax.spines['right'].set_color('None')        # setting up Y-axis tick color to red
ax.spines['top'].set_color('None')         #setting up above X-axis tick color to red
ax.spines['bottom'].set_color('springgreen')         #setting up above X-axis tick color to red

ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 

plt.rcParams.update({'font.size': 12,"font.weight":"bold","axes.labelweight":"bold"})
#plt.rcParams["font.weight"] = "bold"
#plt.rcParams["axes.labelweight"] = "bold"
plt.plot(range(0,d0.shape[0]), pnl_csv['Return'].values,'cyan')
#plt.show()
plt.savefig(os.path.join(main_dir_original,'IB_live_trade',"us_plot_facebook.png"), transparent=True,bbox_inches="tight")







#pnl_csv['Date']=pnl_csv['Date'].apply(lambda x: x.strftime("%Y-%m-%d")) #dt to string

temp=pd.DataFrame({'Date':['string'],'Return':['number']})

pnl_csv=temp.append(pnl_csv)
pnl_csv=pnl_csv.reset_index(drop=True)
output_path=os.path.join(main_dir_original,'IB_live_trade','cum_pnl_all_us_stocks.csv')
pnl_csv.to_csv(output_path,index=None)























def change_permissions_recursive(temp_folder1, mode):
    for root, dirs, files in os.walk(temp_folder1, topdown=False):
        for dir in [os.path.join(root,d) for d in dirs]:
            os.chmod(dir, mode)
        for file in [os.path.join(root, f) for f in files]:
            os.chmod(file, mode)

change_permissions_recursive(os.path.join(main_dir_original,'IB_live_trade'), 0o777)








minute_data_preparation.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-x
"""
Created on Sat Feb 20 22:13:48 2021

@author: root
"""





###############split hsi to 5 mins interval#########################
import os
import numpy as np
import requests
import zipfile
import io




target_dir=r'C:\Users\jonathanjames\aws\notebooks\index_analysis'



target_dir='/home/jonathanjames/aws/notebooks/index_analysis'

os.chdir(target_dir)



from pandas import read_excel
from datetime import datetime as dt
from datetime import timedelta
import datetime
import pandas as pd
from time import sleep
import sys
import time

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import talib
from talib import abstract


interval=15
#seperate data into morning and afternoon session
#folder_path=r"C:\Users\jonathanjames\aws\notebooks\index_analysis\mis"
folder_path=os.path.join(target_dir,"mis")

fn = os.path.join(folder_path,"FHSI_minute_20051201to_cum.hdf5")

#fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
store = pd.HDFStore(fn)
print(store)
data= store.select('FHSI_minute')
 
store.close()



##starting from 2017-07-31, IB open may not be the same as HKEX. so revise the number from IB
##15_to_30
#hsi_y = read_excel('hsi_y.xlsx','Sheet1')
#hsi_y_temp=hsi_y[['Date2','Open_HSI','Close_HSI']].copy()
#hsi_y_temp=hsi_y_temp.loc[hsi_y_temp['Open_HSI']!=100,:].copy()
#hsi_y_temp=hsi_y_temp.reset_index(drop=True)
#
#data_use=data.loc[data['Date2']=='2023-04-03',:]
#def revise_open(data_use):
#    data_use2=data_use.sort_values(by=['date_ymd_hms'],ascending=True)
#    data_use2=data_use2.reset_index(drop=True)
#
#    data_use2=data_use2[0:1].copy()
#    date=data_use2['Date2'].values[0]    
#    if date>='2017-07-31' and date in list(hsi_y_temp.Date2.values):
#        open1=hsi_y_temp.loc[hsi_y_temp['Date2']==date,'Open_HSI'].values[0]    
#        high1=max(data_use2['High'].values[0],open1)
#        low1=min(data_use2['Low'].values[0],open1)
#        close1=data_use2['Close'].values[-1]
#    
#        print(date)
#        
#        data_use.loc[0,'Open']=open1
#        data_use.loc[0,'High']=high1
#        data_use.loc[0,'Low']=low1
#        data_use.loc[0,'Close']=close1
#    else:
#        data_use=data_use.reset_index(drop=True)
#    
#    return data_use
#
#
#temp1=data.groupby(["Date2"]).apply(lambda x:revise_open(x.reset_index(drop=True)))
#data_all_final=temp1.reset_index(drop=True)







data_all_final=data.copy()
data_all_final_check=data_all_final.tail(4000)
data=data_all_final[['date_ymd_hms','date_ymd','Open','High','Low','Close','TotalVolume']].copy()
data['hms']=data['date_ymd_hms'].apply(lambda x: x.strftime('%H:%M:%S'))
data['minute']=data['date_ymd_hms'].apply(lambda x: x.strftime('%M'))
data['minute']=data['minute'].astype(int)

data.dtypes

def count_group(x):
    data_index=x.index
    s=np.array(range(1,x.shape[0]+1))
    out=pd.Series(s,index=data_index)
    return out

data['minute_key']=data.groupby(['date_ymd'],group_keys=False).apply(lambda x:count_group(x))

data['price_change']=(data['Close']-data['Open'])
data['price_change_percent']=(data['Close']-data['Open'])/data['Open']
data.loc[data['price_change']>=0,'price_change_indicate']=1
data['price_change_indicate']=data['price_change_indicate'].fillna(0)
data=data.rename(columns={'date_ymd_hms':'Date1','date_ymd':'Date2'})
data['Date1']=data['Date1'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))


#data_use=data.loc[data['Date2']=='2015-01-02',:]

data['data_group']=data.groupby(['Date2'])['minute'].apply(lambda x:(x % interval ==0).cumsum())
data['data_group']=data['data_group'].astype(str)
data['Date2_group']=data['Date2']+'_'+data['data_group']
data=data.reset_index(drop=True)

data_check=data.head(1000)

#remove first minute
#data=data.loc[(data['minute_key']!=1),:].copy()
#data=data.reset_index(drop=True)


data_use=data.loc[data['Date2']=='2015-01-02',:]
data_use=data.loc[data['Date2']=='2007-12-24',:]
data_use=data.loc[data['Date2']=='2020-11-25',:]
data_use=data.loc[data['Date2']=='2006-03-22',:]
data_use=data.loc[data['Date2']=='2008-06-25',:]
data_use=data_use.reset_index(drop=True)


def split_interval(data_use):
    data_use2=data_use.copy()
    
    date1=data_use2['Date1'].values[0]
    date_out=data_use2['Date2'].values[0]
    data_group=data_use2['data_group'].values[0]
    Date2_group=data_use2['Date2_group'].values[0]
    minute_key=data_use2['minute_key'].values[0]
    
        
    open1=data_use2['Open'].values[0]     
    high1=np.max(data_use2['High'].values)
    low1=np.min(data_use2['Low'].values)
    close1=data_use2['Close'].values[-1]
    TotalVolume=data_use2['TotalVolume'].values.sum()


    output=pd.DataFrame({'Date2':[date_out],'Date1':[date1],'data_group':[data_group],'Date2_group':[Date2_group],'minute_key':[minute_key],
                         'Open1':[open1],
                         'High1':[high1],
                         'Low1':[low1],
                         'Close1':[close1],
                         'TotalVolume':[TotalVolume]})

    print(date_out)
    return output



if interval>1:
    temp1=data.groupby("Date2_group").apply(lambda x:split_interval(x.reset_index(drop=True)))
    
    
    temp1=temp1.sort_values(by=['Date1'],ascending=[True])
    temp1=temp1.reset_index(drop=True)
    
    temp1['Open1']=temp1['Open1'].astype(int)
    temp1['High1']=temp1['High1'].astype(int)
    temp1['Low1']=temp1['Low1'].astype(int)
    temp1['Close1']=temp1['Close1'].astype(int)
    
    temp1=temp1.rename(columns={'Open1':'Open_HSI','High1':'High_HSI','Low1':'Low_HSI','Close1':'Close_HSI'})
    
    temp1['Y_up']=temp1.apply(lambda row: (row.Close_HSI>=row.Open_HSI)*1,axis=1)
    temp1['Y_down']=temp1.apply(lambda row: (row.Close_HSI<row.Open_HSI)*1,axis=1)
    
    temp1['Date2_group_change']=(temp1['Close_HSI']-temp1['Open_HSI'])/temp1['Open_HSI']

else:
    temp1=data.copy()
    temp1['Open']=temp1['Open'].astype(int)
    temp1['High']=temp1['High'].astype(int)
    temp1['Low']=temp1['Low'].astype(int)
    temp1['Close']=temp1['Close'].astype(int)
    
    temp1=temp1.rename(columns={'Open':'Open_HSI','High':'High_HSI','Low':'Low_HSI','Close':'Close_HSI'})
    
    temp1['Y_up']=temp1.apply(lambda row: (row.Close_HSI>=row.Open_HSI)*1,axis=1)
    temp1['Y_down']=temp1.apply(lambda row: (row.Close_HSI<row.Open_HSI)*1,axis=1)




temp3=temp1.copy()
temp3['Date2']=temp3['Date2'].astype(str)
temp3=temp3.fillna(0)


HSI_source=temp3.copy()
HSI_source['year_cohord']=HSI_source['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y")).astype(int)



HSI_source_check=HSI_source.tail(1000)


HSI_source=HSI_source.fillna(0)

out_name="hsi_y_x_"+str(interval)+"min"
import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore(out_name+".hdf5", "w", complib=str("zlib"), complevel=5)
store.put(out_name+"_dataframe",HSI_source, data_columns=HSI_source.columns)
store.close()

writer = pd.ExcelWriter(out_name+'.xlsx', engine='xlsxwriter')
HSI_source.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()




##special handle of break. create a row as the first row of the day. put 9:15am open to it and name it 9:00am
#from datetime import timedelta
#HSI_source_new=pd.DataFrame([])
#all_date=list(HSI_source.Date2.unique())
#
#x='2009-12-29'
#for x in all_date:    
#    HSI_source_temp=HSI_source.loc[HSI_source['Date2']==x,:].copy()
#    new_time=dt.strptime(HSI_source_temp.Date1.values[0],"%Y-%m-%d %H:%M:%S")-timedelta(minutes=15)
#    new_time=new_time.strftime("%Y-%m-%d %H:%M:%S")
#    new_price=HSI_source_temp.Open_HSI.values[0]
#    
#    if all_date.index(x)>0:
#        x_lag1=all_date[all_date.index(x)-1]
#        HSI_source_temp_lag1=HSI_source.loc[HSI_source['Date2']==x_lag1,:].copy()
#        price_lag1=HSI_source_temp_lag1.Close_HSI.values[-1]
#        new_price=(new_price+price_lag1)/2
#        
#    
#    new_temp=pd.DataFrame({'Date2':[x],'Date1':[new_time],'data_group':['9999'],'Date2_group':['9999'],'minute_key':[9999],
#                           'Open_HSI':[999],'High_HSI':[999],'Low_HSI':[999],'Close_HSI':[new_price],
#                           'TotalVolume':[9999],'Y_up':[0],'Y_down':[0],'Date2_group_change':[9999],'year_cohord':[9999]})
#
#    HSI_source_temp=new_temp.append(HSI_source_temp)
#    HSI_source_new=HSI_source_new.append(HSI_source_temp)
#    print(x)
#
#
#HSI_source_new=HSI_source_new.reset_index(drop=True)
#HSI_source_new_check=HSI_source_new.tail(1000)
#
#out_name="hsi_y_x_"+str(interval)+"min"
#import numpy as np
#from pandas import HDFStore,DataFrame
#store = pd.HDFStore(out_name+".hdf5", "w", complib=str("zlib"), complevel=5)
#store.put(out_name+"_dataframe",HSI_source_new, data_columns=HSI_source_new.columns)
#store.close()
#
#writer = pd.ExcelWriter(out_name+'.xlsx', engine='xlsxwriter')
#HSI_source_new.to_excel(writer, sheet_name='Sheet1')
#writer.save()
#writer.close()



#from datetime import timedelta
#
#hsi_y_temp2=hsi_y_temp.copy()
#hsi_y_temp2['break_open']=hsi_y_temp2['Open_HSI']-hsi_y_temp2['Close_HSI'].shift(1)
#hsi_y_temp2['break_open_cum']=hsi_y_temp2['break_open'].copy()#cumsum()
#HSI_source_new=pd.merge(HSI_source,hsi_y_temp2[['Date2','break_open_cum']].copy(),how='left',on=['Date2'])
#HSI_source_new['Close_adj_break']=HSI_source_new['Close_HSI']-HSI_source_new['break_open_cum']
#HSI_source_new=HSI_source_new.loc[~pd.isnull(HSI_source_new['Close_adj_break']),:].copy()
#
#
#HSI_source_new=HSI_source_new.reset_index(drop=True)
#HSI_source_new_check=HSI_source_new.tail(1000)
#
#out_name="hsi_y_x_"+str(interval)+"min"
#import numpy as np
#from pandas import HDFStore,DataFrame
#store = pd.HDFStore(out_name+".hdf5", "w", complib=str("zlib"), complevel=5)
#store.put(out_name+"_dataframe",HSI_source_new, data_columns=HSI_source_new.columns)
#store.close()
#
#writer = pd.ExcelWriter(out_name+'.xlsx', engine='xlsxwriter')
#HSI_source_new.to_excel(writer, sheet_name='Sheet1')
#writer.save()
#writer.close()



















HSI_source.to_csv('HSI_source_'+str(interval)+"min"+'.csv',index=False)


HSI_source=pd.read_csv('HSI_source_'+str(interval)+"min"+'.csv')




#create factor
HSI_source=HSI_source.rename(columns={'Open_HSI':'open','High_HSI':'high','Low_HSI':'low','Close_HSI':'close','TotalVolume':'volume'})
HSI_source['volume_lag1']=HSI_source['volume'].shift(1)
HSI_source['volume_change']=(HSI_source['volume']-HSI_source['volume_lag1'])/HSI_source['volume_lag1']
HSI_source.loc[HSI_source['volume_change']==np.inf,'volume_change']=0
HSI_source.loc[HSI_source['volume_change']==-1,'volume_change']=0

#random factor
dim=HSI_source.shape[0]
s=np.random.normal(0,1,dim)
HSI_source['random1']=s
HSI_source['random2']=s*-1


#find cum max and min
HSI_source['cum_high']=HSI_source.groupby(['Date2'])['high'].apply(lambda x: x.cummax())
HSI_source['cum_low']=HSI_source.groupby(['Date2'])['low'].apply(lambda x: x.cummin())
HSI_source_check=HSI_source.tail(5000)

#create day open column

data_temp=HSI_source.loc[HSI_source['Date2']=='2021-07-21',:].copy()
def append_open(data_temp):
    output_temp=data_temp['open'].values[0]
    output=pd.Series([output_temp]*data_temp.shape[0])
    return output

temp=HSI_source.groupby(['Date2']).apply(lambda x:append_open(x.reset_index(drop=True)))
HSI_source['day_open']=temp.values
HSI_source_check=HSI_source.tail(5000)






greater_at_least=100

#find big move and big drop
HSI_source_cc=HSI_source[['Date2','Date1','day_open','close']].copy()
data_temp=HSI_source_cc.loc[HSI_source_cc['Date2']=='2021-07-21',:].copy()
gat=100
def find_up(data_temp,gat):
    n1=len(data_temp.close)
    x1=np.tile(data_temp.close,(n1,1))
    x2=np.triu(x1,k=1)
    x3=np.reshape(data_temp.close.values,(n1,1))-x2
    x4=np.triu(x3,k=1)
    upper99999=np.tril([99999]*n1,0)
    x4=x4+upper99999
    #x2=np.array([np.roll(row, -(n1-n)) for n, row in enumerate(x1)])
    f1=(x4!=99999)&(x4<=-1*gat)*1
    output=(np.sum(f1,axis=1)>=1)*1
    return pd.Series(output)

def find_down(data_temp,gat):
    n1=len(data_temp.close)
    x1=np.tile(data_temp.close,(n1,1))
    x2=np.triu(x1,k=1)
    x3=np.reshape(data_temp.close.values,(n1,1))-x2
    x4=np.triu(x3,k=1)
    upper99999=np.tril([99999]*n1,0)
    x4=x4+upper99999
    #x2=np.array([np.roll(row, -(n1-n)) for n, row in enumerate(x1)])
    f1=(x4!=99999)&(x4>=gat)*1
    output=(np.sum(f1,axis=1)>=1)*1
    return pd.Series(output)

temp=HSI_source_cc.groupby(['Date2']).apply(lambda x:find_up(x.reset_index(drop=True),greater_at_least))
HSI_source['Y_up']=temp.values
temp=HSI_source_cc.groupby(['Date2']).apply(lambda x:find_down(x.reset_index(drop=True),greater_at_least))
HSI_source['Y_down']=temp.values
HSI_source.loc[(HSI_source['Y_up']==0)&(HSI_source['Y_down']==0),'Y_middle']=1
HSI_source.loc[(HSI_source['Y_up']==1)&(HSI_source['Y_down']==1),'Y_middle']=1
HSI_source.loc[(HSI_source['Y_middle']==1),'Y_up']=0
HSI_source.loc[(HSI_source['Y_middle']==1),'Y_down']=0
HSI_source=HSI_source.fillna(0)
HSI_source_check=HSI_source.tail(500)

HSI_source['Y_up'].values.sum()
HSI_source['Y_middle'].values.sum()
HSI_source['Y_down'].values.sum()



##find central factor
#
#target_variable_use=['Y_up','Y_middle','Y_down']
#
#for target_variable in target_variable_use:
#    distinct_year=HSI_source['year_cohord'].unique()
#    distinct_year=[i for i in distinct_year if i >=2007]
#    yy=2007
#    percentile_cum=pd.DataFrame([])
#    for yy in distinct_year:
#        data_use=HSI_source.loc[HSI_source['year_cohord']<yy,target_variable].values
#        output=sum(data_use)/len(data_use)
#        t1='central_'+target_variable
#    
#        percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
#                                                           t1:[output]}))
#    
#    HSI_source=pd.merge(HSI_source,percentile_cum,how='left',on=['year_cohord'])
#
#HSI_source.loc[HSI_source['Y_up']==1,'central_factor']=HSI_source['central_Y_up']
#HSI_source.loc[HSI_source['Y_middle']==1,'central_factor']=HSI_source['central_Y_middle']
#HSI_source.loc[HSI_source['Y_down']==1,'central_factor']=HSI_source['central_Y_down']
#HSI_source_check=HSI_source.tail(5000)

#HSI_source['high_lag1']=HSI_source['high'].shift(1)
#HSI_source['high_forward1']=HSI_source['high'].shift(-1)
#HSI_source['high_lag2']=HSI_source['high'].shift(2)
#HSI_source['high_forward2']=HSI_source['high'].shift(-2)
#HSI_source['high_lag3']=HSI_source['high'].shift(3)
#HSI_source['high_forward3']=HSI_source['high'].shift(-3)
#
#HSI_source['low_lag1']=HSI_source['low'].shift(1)
#HSI_source['low_forward1']=HSI_source['low'].shift(-1)
#HSI_source['low_lag2']=HSI_source['low'].shift(2)
#HSI_source['low_forward2']=HSI_source['low'].shift(-2)
#HSI_source['low_lag3']=HSI_source['low'].shift(3)
#HSI_source['low_forward3']=HSI_source['low'].shift(-3)
#
#HSI_source_check=HSI_source.head(10000)
#
##define new up and down trend
#greater_at_least=50
#HSI_source['Rdown']=((HSI_source.open>HSI_source.low_forward1)&
#                   (HSI_source.open>HSI_source.low_forward2)&
#                   (HSI_source.open-HSI_source.low_forward3>=greater_at_least))*1
#          
#HSI_source['Rup']=((HSI_source.open<HSI_source.high_forward1)&
#                   (HSI_source.open<HSI_source.high_forward2)&
#                   (HSI_source.high_forward3-HSI_source.open>=greater_at_least))*1
#          
#HSI_source.loc[(HSI_source['Rdown']==0)&(HSI_source['Rup']==0),'Rmiddle']=1
#          
#          
#del HSI_source['high_lag1'];del HSI_source['high_lag2'];del HSI_source['high_lag3'];
#del HSI_source['high_forward1'];del HSI_source['high_forward2'];del HSI_source['high_forward3'];
#del HSI_source['low_lag1'];del HSI_source['low_lag2'];del HSI_source['low_lag3'];
#del HSI_source['low_forward1'];del HSI_source['low_forward2'];del HSI_source['low_forward3'];
#HSI_source_check=HSI_source.tail(10000)
#
#HSI_source['Y_up']=HSI_source['Rup']
#HSI_source['Y_down']=HSI_source['Rdown']
#HSI_source['Y_middle']=HSI_source['Rmiddle']
#HSI_source['Y_middle']=HSI_source['Y_middle'].fillna(0)

HSI_source['volume_change_lag1']=HSI_source['volume_change'].shift(1)
HSI_source['volume_change_lag2']=HSI_source['volume_change'].shift(2)
HSI_source['volume_change_lag3']=HSI_source['volume_change'].shift(3)

HSI_source['hsi_change_lag1']=HSI_source['Date2_group_change'].shift(1)
HSI_source['hsi_change_lag2']=HSI_source['Date2_group_change'].shift(2)
HSI_source['hsi_change_lag3']=HSI_source['Date2_group_change'].shift(3)

HSI_source_check=HSI_source.tail(10000)


#HSI_source['Y_up'].values.sum()
#HSI_source['Y_middle'].values.sum()
#HSI_source['Y_down'].values.sum()






#find cumulative change and time step
HSI_source_cc=HSI_source[['Date2','Date1','day_open','close']].copy()
data_temp=HSI_source_cc.loc[HSI_source_cc['Date2']=='2005-12-02',:].copy()

def cum_change_jumpup(data_temp):
    filter1=data_temp.close.values-data_temp.day_open.values
    n1=len(data_temp.close)
    x1=np.tile(data_temp.close,(n1,1))
    x2=np.tril(x1,k=-1)
    x3=np.reshape(data_temp.close.values,(n1,1))-x2
    x4=np.tril(x3,k=-1)
    upper99999=np.triu([99999]*n1,0)
    x4=x4+upper99999
    #x2=np.array([np.roll(row, -(n1-n)) for n, row in enumerate(x1)])
    f1=(x4!=99999)&(x4>=0)*1
    x5=x4*f1
   
    max_jumpup=np.max(x5,axis=1)
    max_jumpup[filter1<0]=0          #only select out when close>day_open
    
    return pd.Series(max_jumpup)

def cum_change_jumpdown(data_temp):
    filter1=data_temp.close.values-data_temp.day_open.values
    n1=len(data_temp.close)
    x1=np.tile(data_temp.close,(n1,1))
    x2=np.tril(x1,k=-1)
    x3=np.reshape(data_temp.close.values,(n1,1))-x2
    x4=np.tril(x3,k=-1)
    upper99999=np.triu([99999]*n1,0)
    x4=x4+upper99999
    
    f2=(x4!=99999)&(x4<0)*1
    x6=x4*f2

    max_jumpdown=np.min(x6,axis=1)
    max_jumpdown[filter1<0]=0        #only select out when close>day_open
    
    
    return pd.Series(max_jumpdown)

temp=HSI_source_cc.groupby(['Date2']).apply(lambda x: cum_change_jumpup(x.reset_index(drop=True)))
HSI_source['jumpup']=temp.values
HSI_source['jumpup_lag1']=HSI_source['jumpup'].shift(1)
HSI_source['jumpup_lag1']=HSI_source['jumpup_lag1'].fillna(0)

HSI_source_check=HSI_source.head(200)

temp=HSI_source_cc.groupby(['Date2']).apply(lambda x: cum_change_jumpdown(x.reset_index(drop=True)))
HSI_source['jumpdown']=temp.values
HSI_source['jumpdown_lag1']=HSI_source['jumpdown'].shift(1)
HSI_source['jumpdown_lag1']=HSI_source['jumpdown_lag1'].fillna(0)
HSI_source_check=HSI_source.head(200)
HSI_source=HSI_source.reset_index(drop=True)



target_variable='jumpup_lag1'

distinct_year=HSI_source['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2007
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=HSI_source.loc[HSI_source['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    second_percentile_capture=np.nanpercentile(data_use,50)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t3:[third_percentile_capture]}))


HSI_source=pd.merge(HSI_source,percentile_cum,how='left',on=['year_cohord'])
HSI_source_check=HSI_source.tail(1000)
HSI_source.loc[HSI_source['jumpup_lag1']>HSI_source['third_percentile_jumpup_lag1'],'jumpup_lag1_percentile']=HSI_source['jumpup_lag1']
HSI_source=HSI_source.fillna(0)



target_variable='jumpdown_lag1'

distinct_year=HSI_source['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2007
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=HSI_source.loc[HSI_source['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    second_percentile_capture=np.nanpercentile(data_use,50)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t3:[third_percentile_capture]}))

HSI_source=pd.merge(HSI_source,percentile_cum,how='left',on=['year_cohord'])
HSI_source.loc[HSI_source['jumpdown_lag1']<HSI_source['first_percentile_jumpdown_lag1'],'jumpdown_lag1_percentile']=HSI_source['jumpdown_lag1']
HSI_source=HSI_source.fillna(0)
HSI_source_check=HSI_source.tail(1000)



HSI_source.loc[(HSI_source['jumpup_lag1']>HSI_source['third_percentile_jumpup_lag1'])&(HSI_source['jumpdown_lag1']>HSI_source['third_percentile_jumpdown_lag1']),'jf1']=1
HSI_source.loc[(HSI_source['jumpdown_lag1']<HSI_source['first_percentile_jumpdown_lag1'])&(HSI_source['jumpup_lag1']<HSI_source['first_percentile_jumpup_lag1']),'jf2']=1
HSI_source['jf3']=HSI_source['jf1']-HSI_source['jf2']
HSI_source=HSI_source.fillna(0)









#create drop from high, and rise from low
HSI_source['drop_from high']=HSI_source['close']-HSI_source['cum_high']
HSI_source['rise_from low']=HSI_source['close']-HSI_source['cum_low']
HSI_source['risefromlow_dropfromhigh']=HSI_source['rise_from low']+HSI_source['drop_from high']
HSI_source['risefromlow_dropfromhigh']=HSI_source['risefromlow_dropfromhigh'].shift(1)
HSI_source=HSI_source.fillna(0)

target_variable='risefromlow_dropfromhigh'

distinct_year=HSI_source['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2007
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=HSI_source.loc[HSI_source['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,16.7)
    second_percentile_capture=np.nanpercentile(data_use,33.4)
    third_percentile_capture=np.nanpercentile(data_use,50)
    fourth_percentile_capture=np.nanpercentile(data_use,66.7)
    fifth_percentile_capture=np.nanpercentile(data_use,83.4)

    
    t1='first_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    t4='fourth_percentile_'+target_variable
    t5='fifth_percentile_'+target_variable    
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t3:[third_percentile_capture],
                                                       t4:[fourth_percentile_capture],
                                                       t5:[fifth_percentile_capture]                                                       
                                                       }))

HSI_source=pd.merge(HSI_source,percentile_cum,how='left',on=['year_cohord'])

HSI_source.loc[((HSI_source['risefromlow_dropfromhigh']<HSI_source['first_percentile_risefromlow_dropfromhigh'])|
               (HSI_source['risefromlow_dropfromhigh']>=HSI_source['fifth_percentile_risefromlow_dropfromhigh'])),'risefromlow_dropfromhigh1']=HSI_source['risefromlow_dropfromhigh']

HSI_source.loc[(((HSI_source['risefromlow_dropfromhigh']>=HSI_source['first_percentile_risefromlow_dropfromhigh'])&
                 (HSI_source['risefromlow_dropfromhigh']<=HSI_source['second_percentile_risefromlow_dropfromhigh']))|
                ((HSI_source['risefromlow_dropfromhigh']>=HSI_source['fourth_percentile_risefromlow_dropfromhigh'])&
                 (HSI_source['risefromlow_dropfromhigh']<HSI_source['fifth_percentile_risefromlow_dropfromhigh']))),'risefromlow_dropfromhigh2']=HSI_source['risefromlow_dropfromhigh']

    
#del HSI_source['risefromlow_dropfromhigh1']  
#del HSI_source['risefromlow_dropfromhigh2']    
    
HSI_source=HSI_source.fillna(0)
HSI_source_check=HSI_source.tail(1000)





























##data['index']=data.index
#data2=data.copy()
#data2_check=data2.head(1000)
#data2=pd.merge(data2[['Date1','price_change']].copy(),HSI_source,how='left',on=['Date1'])
#
#data2_check=data2.head(1000)
#
#
#s = [1,np.NaN,10,12,14,12,30]
#pd.Series(s).rolling(3).mean() #if any one of nan in 3 observation, won't calculate
#pd.Series(s).rolling(3,min_periods=1).mean() # if at least 1 observation in 3 observation, calculate mean
#pd.Series(s).rolling(3,min_periods=2).mean()
#
#
#
#
#t=15
#
#data2['f1']=np.NaN
#
#data2.loc[data2['price_change']>0,'price_change_positive']=data2['price_change']
#data2.loc[data2['price_change']<0,'price_change_negative']=data2['price_change']
#
#
#data2.price_change_positive
#data2['roll_mean_15_positive']=data2.price_change_positive.rolling(t,1).mean()
#data2['roll_mean_15_negative']=data2.price_change_negative.rolling(t,1).mean()
#data2=data2.fillna(0)
#
#data2['roll_mean_15']=data2['roll_mean_15_positive']+data2['roll_mean_15_negative']
#data2['roll_mean_15_shift1']=data2['roll_mean_15'].shift(1)
#data2=data2.fillna(0)
#
#data2_check=data2.head(500)
#
#
#HSI_source=pd.merge(HSI_source,data2[['Date1','roll_mean_15','roll_mean_15_shift1']].copy(),how='left',on=['Date1'])
#
#
#HSI_source_check=HSI_source.head(1000)
#
#
#
#
##make LBW_edit2 as four group
#target_variable='roll_mean_15_shift1'
#
#
#distinct_year=HSI_source['year_cohord'].unique()
#distinct_year=[i for i in distinct_year if i >=2007]
#yy=2007
#percentile_cum=pd.DataFrame([])
#for yy in distinct_year:
#    data_use=HSI_source.loc[HSI_source['year_cohord']<yy,target_variable].values
#    first_percentile_capture=np.nanpercentile(data_use,25)
#    second_percentile_capture=np.nanpercentile(data_use,50)
#    third_percentile_capture=np.nanpercentile(data_use,75)
#    t1='first_percentile_'+target_variable
#    t2='second_percentile_'+target_variable
#    t3='third_percentile_'+target_variable
#    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
#                                                       t1:[first_percentile_capture],
#                                                       t2:[second_percentile_capture],
#                                                       t3:[third_percentile_capture]}))
#
#
#HSI_source=pd.merge(HSI_source,percentile_cum,how='left',on=['year_cohord'])
#a_check=HSI_source.tail(1000)
#
#
#HSI_source.dtypes
#percentile_cum.dtypes
#
#
#HSI_source.loc[HSI_source['roll_mean_15_shift1']<=HSI_source['first_percentile_roll_mean_15_shift1'],'f1_down']=HSI_source['roll_mean_15_shift1']
#HSI_source.loc[HSI_source['roll_mean_15_shift1']>=HSI_source['third_percentile_roll_mean_15_shift1'],'f1_up']=HSI_source['roll_mean_15_shift1']
#HSI_source=HSI_source.fillna(0)
#
#HSI_source['f1']=HSI_source['f1_up']+HSI_source['f1_down']





#short ema over long ema
shortSMA=abstract.SMA(HSI_source,9)
longSMA=abstract.SMA(HSI_source,24)
HSI_source['shortSMA'] = shortSMA
HSI_source['longSMA'] =longSMA
HSI_source['smaSell'] = ((shortSMA.shift(1) <= longSMA.shift(1)) & (shortSMA.shift(2) >= longSMA.shift(2)))
HSI_source['smaBuy'] = ((shortSMA.shift(1) >= longSMA.shift(1)) & (shortSMA.shift(2) <= longSMA.shift(2)))

HSI_source['smaSell']=HSI_source['smaSell']*1
HSI_source['smaBuy']=HSI_source['smaBuy']*1

HSI_source['sma_9_24']=HSI_source['smaBuy']-HSI_source['smaSell']

















#money flow 14   #which price up, close to 100, when down close to 0, 
moneyflow=abstract.MFI(HSI_source,14)
HSI_source['moneyflow']=moneyflow

HSI_source_check=HSI_source.head(1000)

#del HSI_source['moneyflow_shift1']
#del HSI_source['moneyflow_up']
#del HSI_source['moneyflow_down']


HSI_source['moneyflow_shift1']=HSI_source['moneyflow'].shift(1)
HSI_source.loc[(HSI_source['moneyflow_shift1']<=20),'moneyflow_down']=20-HSI_source['moneyflow_shift1']
HSI_source['moneyflow_down']=HSI_source['moneyflow_down'].fillna(0)

HSI_source.loc[(HSI_source['moneyflow_shift1']>=80),'moneyflow_up']=HSI_source['moneyflow_shift1']-80
HSI_source['moneyflow_up']=HSI_source['moneyflow_up'].fillna(0)

HSI_source['moneyflow_20_80_14_2']=HSI_source['moneyflow_up']-HSI_source['moneyflow_down']

HSI_source.loc[(HSI_source['moneyflow_shift1']>=50),'moneyflow_up_full']=HSI_source['moneyflow_shift1']-50
HSI_source['moneyflow_up_full']=HSI_source['moneyflow_up_full'].fillna(0)

HSI_source.loc[(HSI_source['moneyflow_shift1']<50),'moneyflow_down_full']=50-HSI_source['moneyflow_shift1']
HSI_source['moneyflow_down_full']=HSI_source['moneyflow_down_full'].fillna(0)

HSI_source['moneyflow_full']=HSI_source['moneyflow_up_full']-HSI_source['moneyflow_down_full']







max(moneyflow[~np.isnan(moneyflow)])

#william 14
#(HH-close)(HH-LL) and multipl -ve to it
#theorically, >-20 is over bought, <=-80 is over sold
#but reult told me is opposite


william=abstract.WILLR(HSI_source,14)
HSI_source['william']=william*-1
HSI_source['william_shift1']=HSI_source['william'].shift(1)
HSI_source.loc[(HSI_source['william_shift1']<=20),'william_down']=HSI_source['william_shift1']
HSI_source['william_down']=HSI_source['william_down'].fillna(0)

HSI_source.loc[(HSI_source['william_shift1']>=80),'william_up']=HSI_source['william_shift1']
HSI_source['william_up']=HSI_source['william_up'].fillna(0)

HSI_source['william_20_80']=HSI_source['william_up']-HSI_source['william_down']


del HSI_source['william_down'];del HSI_source['william_up']



ts = pd.Series([10, 11, 15, 18, 13, 4, 25])
k = 2
ts.rolling(k).max()


#william use my own code
t=14
hh=HSI_source.high.rolling(t).max()
ll=HSI_source.low.rolling(t).min()
william=100*(hh-HSI_source.close)/(hh-ll)

HSI_source['william']=william
HSI_source['william_shift1']=HSI_source['william'].shift(1)
HSI_source.loc[(HSI_source['william_shift1']<=20),'william_up']=20-HSI_source['william_shift1']
HSI_source['william_up']=HSI_source['william_up'].fillna(0)

HSI_source.loc[(HSI_source['william_shift1']>=80),'william_down']=HSI_source['william_shift1']-80
HSI_source['william_down']=HSI_source['william_down'].fillna(0)

HSI_source['william_20_80_14_2']=HSI_source['william_up']-HSI_source['william_down']  #this is useful


HSI_source.loc[(HSI_source['william_shift1']<=50),'william_up_full']=50-HSI_source['william_shift1']
HSI_source['william_up_full']=HSI_source['william_up_full'].fillna(0)

HSI_source.loc[(HSI_source['william_shift1']>=50),'william_down_full']=HSI_source['william_shift1']-50
HSI_source['william_down_full']=HSI_source['william_down_full'].fillna(0)

HSI_source['william_full']=HSI_source['william_up_full']-HSI_source['william_down_full']









HSI_source_check=HSI_source.loc[HSI_source['Date2']>='2006-01-05',['Date2','open','high','low','close','william_20_80','william_20_80_14_2']]


HSI_source_check['check']=HSI_source_check['william_20_80']-HSI_source_check['william_20_80_14_2']





#UltimateOscillator 14

#UltimateOscillator=abstract.ULTOSC(HSI_source, timeperiod1=7, timeperiod2=14, timeperiod3=28)
#HSI_source['UltimateOscillator']=UltimateOscillator
#HSI_source['UltimateOscillator_shift1']=HSI_source['UltimateOscillator'].shift(1)
#HSI_source.loc[(HSI_source['UltimateOscillator_shift1']<=30),'UltimateOscillator_up']=30-HSI_source['UltimateOscillator_shift1']
#HSI_source['UltimateOscillator_up']=HSI_source['UltimateOscillator_up'].fillna(0)
#
#HSI_source.loc[(HSI_source['UltimateOscillator_shift1']>=70),'UltimateOscillator_down']=HSI_source['UltimateOscillator_shift1']-70
#HSI_source['UltimateOscillator_down']=HSI_source['UltimateOscillator_down'].fillna(0)
#
#HSI_source['UltimateOscillator_30_70']=HSI_source['UltimateOscillator_up']-HSI_source['UltimateOscillator_down']
#
#HSI_source.loc[(HSI_source['UltimateOscillator_shift1']<=50),'UltimateOscillator_up_full']=50-HSI_source['UltimateOscillator_shift1']
#HSI_source['UltimateOscillator_up_full']=HSI_source['UltimateOscillator_up_full'].fillna(0)
#
#HSI_source.loc[(HSI_source['UltimateOscillator_shift1']>=50),'UltimateOscillator_down_full']=HSI_source['UltimateOscillator_shift1']-50
#HSI_source['UltimateOscillator_down_full']=HSI_source['UltimateOscillator_down_full'].fillna(0)
#
#HSI_source['UltimateOscillator_full']=HSI_source['UltimateOscillator_up_full']-HSI_source['UltimateOscillator_down_full']




#true range

truerange_plus=abstract.PLUS_DM(HSI_source,timeperiod=14)
truerange_minus=abstract.MINUS_DM(HSI_source,timeperiod=14)
HSI_source['truerange_plus']=truerange_plus
HSI_source['truerange_minus']=truerange_minus

HSI_source['truerange_plus_shift1']=HSI_source['truerange_plus'].shift(1)
HSI_source['truerange_minus_shift1']=HSI_source['truerange_minus'].shift(1)

HSI_source['truerange']=HSI_source['truerange_plus_shift1']-HSI_source['truerange_minus_shift1']


HSI_source.loc[(HSI_source['truerange']>=0),'truerange_up']=HSI_source['truerange']
HSI_source['truerange_up']=HSI_source['truerange_up'].fillna(0)

HSI_source.loc[(HSI_source['truerange']<0),'truerange_down']=HSI_source['truerange']
HSI_source['truerange_down']=HSI_source['truerange_down'].fillna(0)
HSI_source['truerange_down']=HSI_source['truerange_down']*-1



target_variable='truerange'


distinct_year=HSI_source['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2007
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=HSI_source.loc[HSI_source['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    second_percentile_capture=np.nanpercentile(data_use,50)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t3:[third_percentile_capture]}))


HSI_source=pd.merge(HSI_source,percentile_cum,how='left',on=['year_cohord'])
a_check=HSI_source.tail(1000)


HSI_source.dtypes
percentile_cum.dtypes

new_var=target_variable+'_percentile'
HSI_source.loc[(HSI_source[target_variable]<=HSI_source[t1])|(HSI_source[target_variable]>=HSI_source[t3]),new_var]=HSI_source[target_variable]

HSI_source=HSI_source.fillna(0)

a_check=HSI_source.tail(1000)















#DX
directmove=abstract.DX(HSI_source,14)
HSI_source['directmove']=directmove
HSI_source['directmove_shift1']=HSI_source['directmove'].shift(1)
HSI_source.loc[(HSI_source['directmove_shift1']>=50),'directmove_up']=HSI_source['directmove_shift1']
HSI_source['directmove_up']=HSI_source['directmove_up'].fillna(0)

HSI_source.loc[(HSI_source['directmove_shift1']<=2),'directmove_down']=HSI_source['directmove_shift1']
HSI_source['directmove_down']=HSI_source['directmove_down'].fillna(0)


#bop
balancepower=abstract.BOP(HSI_source,14)
HSI_source['balancepower']=balancepower
HSI_source['balancepower_shift1']=HSI_source['balancepower'].shift(1)
HSI_source.loc[(HSI_source['balancepower_shift1']>=0),'balancepower_up']=HSI_source['balancepower_shift1']
HSI_source['balancepower_up']=HSI_source['balancepower_up'].fillna(0)

HSI_source.loc[(HSI_source['balancepower_shift1']<0),'balancepower_down']=HSI_source['balancepower_shift1']
HSI_source['balancepower_down']=HSI_source['balancepower_down'].fillna(0)



#aroon
aroon=abstract.AROONOSC(HSI_source,14)
HSI_source['aroon']=aroon
HSI_source['aroon_shift1']=HSI_source['aroon'].shift(1)
HSI_source.loc[(HSI_source['aroon_shift1']>=0),'aroon_up']=HSI_source['aroon_shift1']
HSI_source['aroon_up']=HSI_source['aroon_up'].fillna(0)

HSI_source.loc[(HSI_source['aroon_shift1']<0),'aroon_down']=HSI_source['aroon_shift1']
HSI_source['aroon_down']=HSI_source['aroon_down'].fillna(0)



#short ema over long ema
shortSMA=abstract.SMA(HSI_source,7)
longSMA=abstract.SMA(HSI_source,200)
HSI_source['shortSMA'] = shortSMA
HSI_source['longSMA'] =longSMA
HSI_source['smaSell'] = ((shortSMA.shift(1) <= longSMA.shift(1)) & (shortSMA.shift(2) >= longSMA.shift(2)))
HSI_source['smaBuy'] = ((shortSMA.shift(1) >= longSMA.shift(1)) & (shortSMA.shift(2) <= longSMA.shift(2)))

HSI_source['smaSell']=HSI_source['smaSell']*1
HSI_source['smaBuy']=HSI_source['smaBuy']*1


A_check=HSI_source.head(1000).copy()





































out=HSI_source.copy()
out['year']=HSI_source['Date2'].str[0:4]
out.loc[(out['smaBuy']==1),'up_entry']=out['open']
out.loc[(out['smaSell']==1)&(out['smaBuy']==0),'up_exit']=out['open']

out.loc[(out['smaSell']==1),'down_entry']=out['open']
out.loc[(out['smaBuy']==1)&(out['smaSell']==0),'down_exit']=out['open']


out_temp=out.copy()
s1='down_entry'
s2='down_exit'
up_or_down=-1

def pnl_signal(out_temp,s1,s2,up_or_down):
    out_temp_up_entry=out_temp[['Date2','year',s1]].copy()
    out_temp_up_entry=out_temp_up_entry.loc[~(pd.isnull(out_temp_up_entry[s1])),:]
    out_temp_up_entry=out_temp_up_entry.reset_index(drop=True)
    
    first_entry_time=out_temp_up_entry.Date2.values[0]
    
    out_temp_up_exit=out_temp[['Date2',s2]].copy()
    out_temp_up_exit=out_temp_up_exit.loc[out_temp_up_exit['Date2']>first_entry_time,:]
    out_temp_up_exit=out_temp_up_exit.loc[~(pd.isnull(out_temp_up_exit[s2])),:]
    out_temp_up_exit=out_temp_up_exit.reset_index(drop=True)
    out_temp_up=pd.concat([out_temp_up_entry,out_temp_up_exit],axis=1)
    
    
    out_temp_up['pnl']=(out_temp_up[s2]-out_temp_up[s1])*up_or_down
    out_temp_up=out_temp_up.loc[~(pd.isnull(out_temp_up['pnl'])),:]
    return out_temp_up






p1=pnl_signal(out,'up_entry','up_exit',1)
p1=p1.groupby(['year'])['pnl'].sum()
p1

p2=pnl_signal(out,'down_entry','down_exit',-1)
p2=p2.groupby(['year'])['pnl'].sum()
p2




HSI_source_check=HSI_source.head(100)
del HSI_source_check
del data


HSI_source=HSI_source.fillna(0)





## 透過『get_function_groups』，取得分類後的技術指標清單
#all_ta_groups = talib.get_function_groups()
## 看一下這個字典
#all_ta_groups
## 有哪些大類別？
#all_ta_groups.keys()
## 查看某類別底下的技術指標清單
#all_ta_groups['Momentum Indicators']
## 查看所有類別的指標數量
#table = pd.DataFrame({
#            '技術指標類別名稱': list(all_ta_groups.keys()),
#            '該類別指標總數': list(map(lambda x: len(x), all_ta_groups.values()))
#        })
#table
#
#
#
#
#help(talib.SAR)
#
#
## Calculate parabolic sar
#HSI_source['SAR'] = abstract.SAR(HSI_source,acceleration=0.02, maximum=0.2)
#
## Plot Parabolic SAR with close price
#HSI_source[['close', 'SAR']][:500].plot(figsize=(10,5))
#plt.grid()
#plt.show()










## 確認價量資料表 df 的值都是 float 格式
#df = df.astype('float')

# 準備一份你想要計算並且併入 df 的技術指標清單

# 這裡示範全部 158 種技術指標
ta_list = talib.get_functions()


#ta_list = ['SAR','ADX']

# 迴圈執行，看看結果吧！
x='SAR'
count=0
for x in ta_list:
    try:
        # x 為技術指標的代碼，透過迴圈填入，再透過 eval 計算出 output
        
        output = eval('abstract.'+x+'(HSI_source)')
        # 如果輸出是一維資料，幫這個指標取名為 x 本身；多維資料則不需命名
        output.name = x.lower() if type(output) == pd.core.series.Series else None
        # 透過 merge 把輸出結果併入 df DataFrame
        #HSI_source=pd.concat([HSI_source,output],axis=1)
        HSI_source = pd.merge(HSI_source, pd.DataFrame(output), left_on = HSI_source.index, right_on = output.index)
        HSI_source =HSI_source.set_index('key_0') #move key_0 column as index and del key_0 column
        #del output
        count=count+1
        print('finished ',x,' ',count+1)
    except:
        print(x)




#create lag one
#ta_list = ['SAR','ADX']
for x in ta_list:
    try:
        tname= x.lower()+'_lag1'
        if tname not in list(HSI_source.columns.values):
            HSI_source[tname]=HSI_source[x.lower()].shift(1)
            del HSI_source[x.lower()]
            print(x)
    except:
        print(x)


HSI_source.to_csv('HSI_source_b2.csv',index=False)


HSI_source_col_name=list(HSI_source.columns.values)
HSI_source['HT_PHASOR']







HSI_source=pd.read_csv('HSI_source_b2.csv')
HSI_source.columns.values
HSI_source=HSI_source.fillna(0)












HSI_source_select=HSI_source.loc[HSI_source['Date2']<='2010-12-31',:].copy()


all_f=['ht_dcperiod_lag1',
 'ht_dcphase_lag1',
 'ht_trendmode_lag1',
 'add_lag1',
 'div_lag1',
 'maxindex_lag1',
 'minindex_lag1',
 'mult_lag1',
 'sub_lag1',
 'sum_lag1',
 'acos_lag1',
 'asin_lag1',
 'atan_lag1',
 'ceil_lag1',
 'cos_lag1',
 'cosh_lag1',
 'exp_lag1',
 'floor_lag1',
 'ln_lag1',
 'log10_lag1',
 'sin_lag1',
 'sinh_lag1',
 'sqrt_lag1',
 'tan_lag1',
 'tanh_lag1',
 'adx_lag1',
 'adxr_lag1',
 'apo_lag1',
 'aroonosc_lag1',
 'bop_lag1',
 'cci_lag1',
 'cmo_lag1',
 'dx_lag1',
 'macd_lag1',
 'mfi_lag1',
 'minus_di_lag1',
 'minus_dm_lag1',
 'mom_lag1',
 'plus_di_lag1',
 'plus_dm_lag1',
 'ppo_lag1',
 'roc_lag1',
 'rocp_lag1',
 'rocr_lag1',
 'rocr100_lag1',
 'rsi_lag1',
 'trix_lag1',
 'ultosc_lag1',
 'willr_lag1',
 'dema_lag1',
 'ema_lag1',
 'ht_trendline_lag1',
 'kama_lag1',
 'ma_lag1',
 'mama_lag1',
 'midpoint_lag1',
 'midprice_lag1',
 'sar_lag1',
 'sarext_lag1',
 'sma_lag1',
 't3_lag1',
 'tema_lag1',
 'trima_lag1',
 'wma_lag1',
 'cdl2crows_lag1',
 'cdl3blackcrows_lag1',
 'cdl3inside_lag1',
 'cdl3linestrike_lag1',
 'cdl3outside_lag1',
 'cdl3starsinsouth_lag1',
 'cdl3whitesoldiers_lag1',
 'cdlabandonedbaby_lag1',
 'cdladvanceblock_lag1',
 'cdlbelthold_lag1',
 'cdlbreakaway_lag1',
 'cdlclosingmarubozu_lag1',
 'cdlconcealbabyswall_lag1',
 'cdlcounterattack_lag1',
 'cdldarkcloudcover_lag1',
 'cdldoji_lag1',
 'cdldojistar_lag1',
 'cdldragonflydoji_lag1',
 'cdlengulfing_lag1',
 'cdleveningdojistar_lag1',
 'cdleveningstar_lag1',
 'cdlgapsidesidewhite_lag1',
 'cdlgravestonedoji_lag1',
 'cdlhammer_lag1',
 'cdlhangingman_lag1',
 'cdlharami_lag1',
 'cdlharamicross_lag1',
 'cdlhighwave_lag1',
 'cdlhikkake_lag1',
 'cdlhikkakemod_lag1',
 'cdlhomingpigeon_lag1',
 'cdlidentical3crows_lag1',
 'cdlinneck_lag1',
 'cdlinvertedhammer_lag1',
 'cdlkicking_lag1',
 'cdlkickingbylength_lag1',
 'cdlladderbottom_lag1',
 'cdllongleggeddoji_lag1',
 'cdllongline_lag1',
 'cdlmarubozu_lag1',
 'cdlmatchinglow_lag1',
 'cdlmathold_lag1',
 'cdlmorningdojistar_lag1',
 'cdlmorningstar_lag1',
 'cdlonneck_lag1',
 'cdlpiercing_lag1',
 'cdlrickshawman_lag1',
 'cdlrisefall3methods_lag1',
 'cdlseparatinglines_lag1',
 'cdlshootingstar_lag1',
 'cdlshortline_lag1',
 'cdlspinningtop_lag1',
 'cdlstalledpattern_lag1',
 'cdlsticksandwich_lag1',
 'cdltakuri_lag1',
 'cdltasukigap_lag1',
 'cdlthrusting_lag1',
 'cdltristar_lag1',
 'cdlunique3river_lag1',
 'cdlupsidegap2crows_lag1',
 'cdlxsidegap3methods_lag1',
 'avgprice_lag1',
 'medprice_lag1',
 'typprice_lag1',
 'wclprice_lag1',
 'beta_lag1',
 'correl_lag1',
 'linearreg_lag1',
 'linearreg_angle_lag1',
 'linearreg_intercept_lag1',
 'linearreg_slope_lag1',
 'stddev_lag1',
 'tsf_lag1',
 'var_lag1',
 'atr_lag1',
 'natr_lag1',
 'trange_lag1',
 'ad_lag1',
 'adosc_lag1',
 'obv_lag1']

x='cosh_lag1'
all_zero=[]
for x in all_f:
    if (sum(HSI_source_select[x].values)==0)|(sum(HSI_source_select[x].values)==np.inf):
        print(x)
        all_zero.append(x)



all_f=[c for c in all_f if c not in all_zero]

HSI_source_select['Y_selection']=HSI_source_select.Y_up-HSI_source_select.Y_down












# create a base classifier used to evaluate a subset of attributes
model = LogisticRegression(max_iter=3000)

# create the RFE model and select 3 attributes
rfe = RFE(model, 1)
use_factor_list_nodate=all_f.copy()
rfe = rfe.fit(HSI_source_select.loc[:,use_factor_list_nodate], HSI_source_select.Y_selection)
# summarize the selection of the attributes
print(rfe.support_)
out=rfe.ranking_
out=out.tolist()


output=pd.DataFrame({'use_factor':all_f,'rank':out})

output=output.sort_values(by=['rank'],ascending=[True])
output=output.reset_index(drop=True)

output.to_csv('technical_indicator_ranking.csv',index=False)










#only keep first 35 factor
remove_column=output.use_factor[35:].tolist()


for x in remove_column:
    if x in list(HSI_source.columns.values):
        del HSI_source[x]
















#add some new factors
import talib
from talib import abstract
HSI_source['SAR'] = abstract.SAR(HSI_source,acceleration=0.02, maximum=0.2)
HSI_source.loc[HSI_source['SAR']>=HSI_source['high'],'sar_talib_down2']=HSI_source['SAR']-HSI_source['high']
HSI_source.loc[HSI_source['SAR']<=HSI_source['low'],'sar_talib_up2']=HSI_source['low']-HSI_source['SAR']

HSI_source['sar_talib_down2_shift1']=HSI_source['sar_talib_down2'].shift(1)
HSI_source['sar_talib_up2_shift1']=HSI_source['sar_talib_up2'].shift(1)
HSI_source=HSI_source.fillna(0)

HSI_source['sar_talib_modified']=HSI_source['sar_talib_up2_shift1']-HSI_source['sar_talib_down2_shift1']

HSI_source['sar_talib_modified_original']=HSI_source['sar_talib_modified'].copy()


target_variable='sar_talib_modified_original'


distinct_year=HSI_source['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2007
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=HSI_source.loc[HSI_source['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    second_percentile_capture=np.nanpercentile(data_use,50)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t3:[third_percentile_capture]}))


HSI_source=pd.merge(HSI_source,percentile_cum,how='left',on=['year_cohord'])
a_check=HSI_source.tail(1000)


HSI_source.dtypes
percentile_cum.dtypes

new_var=target_variable+'_percentile'
HSI_source.loc[(HSI_source[target_variable]<=HSI_source[t1])|(HSI_source[target_variable]>=HSI_source[t3]),new_var]=HSI_source[target_variable]

HSI_source=HSI_source.fillna(0)

a_check=HSI_source.tail(1000)



HSI_source.loc[HSI_source[target_variable]<HSI_source[t1],'sar_group']=-2
HSI_source.loc[(HSI_source[target_variable]>=HSI_source[t1])&(HSI_source[target_variable]<HSI_source[t2]),'sar_group']=-1
HSI_source.loc[(HSI_source[target_variable]>=HSI_source[t2])&(HSI_source[target_variable]<HSI_source[t3]),'sar_group']=1
HSI_source.loc[HSI_source[target_variable]>=HSI_source[t3],'sar_group']=2
#del HSI_source['sar_group']















#add midprice
import talib
from talib import abstract
HSI_source['midprice_2'] = abstract.MIDPRICE(HSI_source,2)
HSI_source['midprice_2_change']=(HSI_source['midprice_2']-HSI_source['midprice_2'].shift(1))/HSI_source['midprice_2'].shift(1)
HSI_source['midprice_2_change_lag1']=HSI_source['midprice_2_change'].shift(1)

HSI_source['midprice_4'] = abstract.MIDPRICE(HSI_source,4)
HSI_source['midprice_4_change']=(HSI_source['midprice_4']-HSI_source['midprice_4'].shift(1))/HSI_source['midprice_4'].shift(1)
HSI_source['midprice_4_change_lag1']=HSI_source['midprice_4_change'].shift(1)


HSI_source['midprice_6'] = abstract.MIDPRICE(HSI_source,6)
HSI_source['midprice_6_change']=(HSI_source['midprice_6']-HSI_source['midprice_6'].shift(1))/HSI_source['midprice_6'].shift(1)
HSI_source['midprice_6_change_lag1']=HSI_source['midprice_6_change'].shift(1)


HSI_source['midprice_8'] = abstract.MIDPRICE(HSI_source,8)
HSI_source['midprice_8_change']=(HSI_source['midprice_8']-HSI_source['midprice_8'].shift(1))/HSI_source['midprice_8'].shift(1)
HSI_source['midprice_8_change_lag1']=HSI_source['midprice_8_change'].shift(1)

HSI_source=HSI_source.fillna(0)


HSI_source_check=HSI_source.tail(1000)


help(abstract.MIDPRICE)




#e








HSI_source=HSI_source.fillna(0)

out_name="hsi_y_x_"+str(interval)+"min"
import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore(out_name+".hdf5", "w", complib=str("zlib"), complevel=5)
store.put(out_name+"_dataframe",HSI_source, data_columns=HSI_source.columns)
store.close()

writer = pd.ExcelWriter(out_name+'.xlsx', engine='xlsxwriter')
HSI_source.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()








extract_futures_from_barchart_tradingview.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:01:44 2020

@author: root
"""
import os
import pandas as pd


#download symbol from https://www.barchart.com/futures/quotes/HA*0/historical-prices?viewName=main&page=all

set_dir="/home/jonathanjames/aws/notebooks/index_analysis/data/HHI_HKEX"
download_path_save_as=os.path.join(set_dir,"barchart_historical_data")

os.chdir(set_dir)


read_symbol=pd.read_csv("HHIF_symbol_from_barchart.csv")

read_symbol=read_symbol.loc[~pd.isnull(read_symbol['Symbol']),:]
read_symbol=read_symbol.reset_index(drop=True)

read_symbol=read_symbol.iloc[0:195,:]





#coco data confirmed no night session
#2016-09, barchart start having 1min, but each csv only has 10000 row, so not enough for full month, so need to use at least 2mins



#2013-4-8, hkex start night session  5pm to 11pm
#2014-11-03 night session extend to 1145 pm
#2017-11-06 night session till 1am
#2019-06-17 night session till 3am



import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import io
import sys
import pandas as pd
from datetime import datetime as dt

from dateutil import tz



op = webdriver.ChromeOptions()
#op.add_argument('headless')
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-shm-usage')


#add file save path using chrome to download
prefs = {"download.default_directory" : download_path_save_as}
op.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(options=op,executable_path='/home/jonathanjames/aws/notebooks/horse/chrome_driver/chromedriver_linux64/chromedriver')
#browser.execute_script("return document.cookie")  
browser.execute_script("return navigator.userAgent")  




#browser = webdriver.Chrome(executable_path=r'C:\Users\jonathan.james\.Spyder\chromedriver.exe')
browser.get("https://www.barchart.com/login")

wait = WebDriverWait(browser, 30)

#close a pop up
wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/i'))).click()

#login
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bc-main-content-wrapper"]/div/div[2]/div[2]/div/div/div/div[1]/form/div[1]/input'))).send_keys('jonathanjameslei@gmail.com')
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-page-form-password"]'))).send_keys('wjkd4685')
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bc-main-content-wrapper"]/div/div[2]/div[2]/div/div/div/div[1]/form/div[6]/button'))).click()


    










i=0
for i in range(0,read_symbol.shape[0]):
    target_symbol=read_symbol['Symbol'][i]

    bar_chart_link="https://www.barchart.com/futures/quotes/"+target_symbol+"/historical-download"


    browser.get(bar_chart_link)
    
    
    
    #download minute data
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/select'))).send_keys('Intraday')
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/input'))).clear()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/input'))).send_keys('1')

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/input'))).clear()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/input'))).send_keys('05/17/2000')
    
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/input'))).clear()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/input'))).send_keys('05/17/2030')

    #CLICK DOWNLOAD
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/a'))).click()



    #download daily data
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/select'))).send_keys('Daily')


    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/input'))).clear()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/input'))).send_keys('05/17/2000')
    
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/input'))).clear()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/input'))).send_keys('05/17/2030')

    #CLICK DOWNLOAD
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/a'))).click()











































#extract ftse futures from barchart.com
import os
import pandas as pd


#download symbol from https://www.barchart.com/futures/quotes/HA*0/historical-prices?viewName=main&page=all

set_dir="/home/jonathanjames/aws/notebooks/index_analysis/data/ftse100_futures"
download_path_save_as=os.path.join(set_dir,"barchart_historical_data")

os.chdir(set_dir)


year_list=[i for i in range(2005,2022)]

futures_list=['H','M','U','Z']

symbol_list=[]
i=2021
for i in year_list:
    for j in futures_list:
        symbol_list.append('X'+str(j)+str(i)[-2:])




import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import io
import sys
import pandas as pd






op = webdriver.ChromeOptions()
#op.add_argument('headless')
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-shm-usage')


#add file save path using chrome to download
prefs = {"download.default_directory" : download_path_save_as}
op.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(options=op,executable_path='/home/jonathanjames/aws/notebooks/horse/chrome_driver/chromedriver_linux64/chromedriver84')
#browser.execute_script("return document.cookie")  
browser.execute_script("return navigator.userAgent")  




#browser = webdriver.Chrome(executable_path=r'C:\Users\jonathan.james\.Spyder\chromedriver.exe')
browser.get("https://www.barchart.com/login")

wait = WebDriverWait(browser, 30)

#close a pop up
#wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/i'))).click()

#login
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bc-main-content-wrapper"]/div/div[2]/div[2]/div/div/div/div[1]/form/div[1]/input'))).send_keys('jonathanjameslei@gmail.com')
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-page-form-password"]'))).send_keys('wjkd4685')
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bc-main-content-wrapper"]/div/div[2]/div[2]/div/div/div/div[1]/form/div[6]/button'))).click()


    










i=symbol_list[2]
for i in symbol_list:
    target_symbol=i

    bar_chart_link="https://www.barchart.com/futures/quotes/"+target_symbol+"/historical-download"


    browser.get(bar_chart_link)
    
    
    
    #download minute data
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/select'))).send_keys('Intraday')
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/input'))).clear()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/input'))).send_keys('5')
    sleep(1)
    

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/input'))).clear()
    sleep(0.5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/input'))).clear()
    sleep(0.5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/input'))).clear()

    
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/input'))).send_keys('01/01/2000')
    

    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/input'))).clear()
    sleep(0.5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/input'))).clear()
    sleep(0.5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/input'))).clear()
    sleep(0.5)

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/input'))).send_keys('05/17/2030')

    
    #sleep(1)
    #CLICK DOWNLOAD
    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/a'))).click()
    sleep(2)




initial_date="2005-01-25"
#dt.fromtimestamp(1592583300)


i='XM05'#'HHIF2008'
data_all=pd.DataFrame([])
for i in symbol_list:
    file_name=os.path.join(download_path_save_as,i[0:2].lower()+i[-2:]+"_intraday-5min_historical-data-07-30-2021.csv")
    temp=pd.read_csv(file_name)
    temp=temp[:-1].copy()
    temp['Date']=temp['Time'].apply(lambda x :dt.strptime(x,"%m/%d/%Y %H:%M")) #string to dt
    
    
    temp['Date2']=temp['Date'].apply(lambda x:x.strftime("%Y-%m-%d")) #dt to string
    temp=temp.loc[temp['Date2']>initial_date,:]
    temp=temp.sort_values(by=['Date'],ascending=True)
    
    #find one day before last trading day
    initial_date=temp.Date2.unique()[-2]
    temp=temp.loc[temp['Date2']<=initial_date,:].copy()
    
    data_all=data_all.append(temp)

    print("finished ",i,temp['Date2'].values[0],temp['Date2'].values[-1])


data_all=data_all.reset_index(drop=True)




us_zone = tz.gettz('US/Central')
uk_zone=tz.gettz('Europe/London')
hk_zone=tz.gettz('Asia/Hong_Kong')
data_all['Date_cdt']=data_all['Date'].apply(lambda x:x.replace(tzinfo=us_zone))
data_all['Date_uk']=data_all['Date_cdt'].apply(lambda x:x.astimezone(uk_zone))
data_all['Date_hk']=data_all['Date_cdt'].apply(lambda x:x.astimezone(hk_zone))














































#extract N225 futures from barchart.com
import os
import pandas as pd


#download symbol from https://www.barchart.com/futures/quotes/HA*0/historical-prices?viewName=main&page=all

set_dir="/home/jonathanjames/aws/notebooks/index_analysis/data/n225_futures"

download_path_save_as=os.path.join(set_dir,"barchart_historical_data")

os.chdir(set_dir)


year_list=[i for i in range(2004,2022)]

futures_list=['H','M','U','Z']

symbol_list=[]
i=2021
for i in year_list:
    for j in futures_list:
        symbol_list.append('NO'+str(j)+str(i)[-2:])




import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import io
import sys
import pandas as pd

from datetime import datetime as dt
import datetime




op = webdriver.ChromeOptions()
#op.add_argument('headless')
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-shm-usage')


#add file save path using chrome to download
prefs = {"download.default_directory" : download_path_save_as}
op.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(options=op,executable_path='/home/jonathanjames/aws/notebooks/horse/chrome_driver/chromedriver_linux64/chromedriver84')


#browser.execute_script("return document.cookie")  
browser.execute_script("return navigator.userAgent")  




#browser = webdriver.Chrome(executable_path=r'C:\Users\jonathan.james\.Spyder\chromedriver.exe')
browser.get("https://www.barchart.com/login")

wait = WebDriverWait(browser, 30)

#close a pop up
#wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/i'))).click()

#login
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bc-main-content-wrapper"]/div/div[2]/div[2]/div/div/div/div[1]/form/div[1]/input'))).send_keys('jonathanjameslei@gmail.com')
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-page-form-password"]'))).send_keys('wjkd4685')
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bc-main-content-wrapper"]/div/div[2]/div[2]/div/div/div/div[1]/form/div[6]/button'))).click()


    










i=symbol_list[0]
for i in symbol_list[3:]:
    target_symbol=i

    bar_chart_link="https://www.barchart.com/futures/quotes/"+target_symbol+"/historical-download"


    browser.get(bar_chart_link)
    
    
    
    #download minute data
    #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/select'))).send_keys('Daily')
    #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/input'))).clear()
    #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/input'))).send_keys('5')
    sleep(1)
    

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/input'))).clear()
    sleep(0.5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/input'))).clear()
    sleep(0.5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/input'))).clear()

    
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/input'))).send_keys('01/01/2000')
    

    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/input'))).clear()
    sleep(0.5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/input'))).clear()
    sleep(0.5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/input'))).clear()
    sleep(0.5)

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/div[1]/form/div[3]/input'))).send_keys('05/17/2030')

    
    #sleep(1)
    #CLICK DOWNLOAD
    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content-column"]/div/div[2]/div/div[1]/div[2]/a'))).click()
    sleep(2)




initial_date="2004-01-01"
#dt.fromtimestamp(1592583300)


i='NOU21'#'HHIF2008'
data_all=pd.DataFrame([])
for i in symbol_list:
    file_name=os.path.join(download_path_save_as,i[0:3].lower()+i[-2:]+"_daily_historical-data-07-31-2021.csv")
    temp=pd.read_csv(file_name)
    temp=temp[:-1].copy()
    temp['Date']=temp['Time'].apply(lambda x :dt.strptime(x,"%m/%d/%Y")) #string to dt
    
    
    temp['Date2']=temp['Date'].apply(lambda x:x.strftime("%Y-%m-%d")) #dt to string
    temp['OI']=temp['Open Int'].shift(-1)
    temp=temp.loc[temp['Date2']>initial_date,:]
    temp=temp.sort_values(by=['Date'],ascending=True)
    
    #find two day before last trading day
    initial_date=temp.Date2.unique()[-3]
    temp=temp.loc[temp['Date2']<=initial_date,:].copy()
    temp['contract']=i
    
    data_all=data_all.append(temp)

    print("finished ",i,temp['Date2'].values[0],temp['Date2'].values[-1])


data_all=data_all.reset_index(drop=True)
del data_all['Date']



#us_zone = tz.gettz('US/Central')
#uk_zone=tz.gettz('Europe/London')
#hk_zone=tz.gettz('Asia/Hong_Kong')
#data_all['Date_cdt']=data_all['Date'].apply(lambda x:x.replace(tzinfo=us_zone))
#data_all['Date_uk']=data_all['Date_cdt'].apply(lambda x:x.astimezone(uk_zone))
#data_all['Date_hk']=data_all['Date_cdt'].apply(lambda x:x.astimezone(hk_zone))

path_out=os.path.join(set_dir,'N225_futures_from_barchart.xlsx')
writer = pd.ExcelWriter(path_out, engine='xlsxwriter')
data_all.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()





















##############################################################################
##########extract n225 from https://tw.tradingview.com/############################
##############################################################################

year_list=[i for i in range(2008,2022)]

futures_list=['H','M','U','Z']

symbol_list=[]
i=2021
for i in year_list:
    for j in futures_list:
        symbol_list.append('NK225'+str(j)+str(i))
        
        
        

        
        
import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import io
import sys
import pandas as pd

from datetime import datetime as dt
from pandas import read_excel
from dateutil import tz

#login



set_dir="/home/jonathanjames/aws/notebooks/index_analysis/data/n225_futures"
#set_dir=r"C:\Users\jonathanjames\aws\notebooks\index_analysis\data\n225_futures"

download_path_save_as=os.path.join(set_dir,"tradingview_data")





os.chdir(set_dir)


op = webdriver.ChromeOptions()
#op.add_argument('headless')
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-shm-usage')


#add file save path using chrome to download
prefs = {"download.default_directory" : download_path_save_as}
op.add_experimental_option("prefs",prefs)

op.add_experimental_option("excludeSwitches", ['enable-automation'])

browser = webdriver.Chrome(options=op,executable_path='/home/jonathanjames/aws/notebooks/horse/chrome_driver/chromedriver_linux64/chromedriver84')
#browser = webdriver.Chrome(options=op,executable_path=r'C:\Users\jonathanjames\aws\notebooks\horse\chrome_driver\chromedriver_win32\chromedriver_87.exe')

#browser.execute_script("return document.cookie")  
browser.execute_script("return navigator.userAgent")  




#browser = webdriver.Chrome(executable_path=r'C:\Users\jonathan.james\.Spyder\chromedriver.exe')
browser.get("https://tw.tradingview.com/#signin")

wait = WebDriverWait(browser, 30)


#click login





wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span'))).click()
#wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__user-name-input__e1145da9-d962-4a16-9257-c9020c9f711b"]'))).send_keys('jonathan2019trading')
#wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__password-input__e1145da9-d962-4a16-9257-c9020c9f711b"]'))).send_keys('wjkd4685')
#wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__submit-button__e1145da9-d962-4a16-9257-c9020c9f711b"]/span[1]'))).click()
#wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__user-name-input__e1145da9-d962-4a16-9257-c9020c9f711b"]'))).send_keys('po3667222@gmail.com')
#wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__password-input__e1145da9-d962-4a16-9257-c9020c9f711b"]'))).send_keys('wjkd4685')

wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__user-name-input__e1145da9-d962-4a16-9257-c9020c9f711b"]'))).send_keys('bigbigbigtaitai@gmail.com')
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__password-input__e1145da9-d962-4a16-9257-c9020c9f711b"]'))).send_keys('bigbigbig2021')


sleep(3)


browser.maximize_window()
browser.get("https://tw.tradingview.com/chart/mo6AvbRF/")



#note
#when screen show how many bars, historicakl excel template all have how many row
#so if drap browser's left and right so more bars show, then historical has more bars

i='NK225U2020'
for i in symbol_list:
    target_symbol=i

    #link='https://www.tradingview.com/chart/?symbol=OSE%3A'+target_symbol
    #browser.get(link)
    

    
    
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div'))).click()
    sleep(1)
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div[2]/div[1]/input'))).send_keys(target_symbol)
    sleep(1)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div[1]/input'))).send_keys(Keys.ENTER)
    
    
    
    #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/div[11]'))).click() #choose 15  mins
    

#    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.CONTROL,"a")
#    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.DELETE)
#    
#    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]'))).send_keys(target_symbol)
#    
#    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.ENTER)
#    sleep(2)
       
    #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "value-DWZXOdoK", " " ))]'))).click()
    #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/div[11]'))).click() #choose 15  mins
    sleep(4)
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div[5]'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/span/button'))).click()        
    sleep(1)
    






initial_date="2008-01-01"
#dt.fromtimestamp(1592583300)


i='NK225U2021'
data_all=pd.DataFrame([])
for i in symbol_list:
    file_name=os.path.join(download_path_save_as,'OSE_DLY_'+i+', 15.csv')
    temp=pd.read_csv(file_name)
    temp['Date1']=temp['time'].apply(lambda x:dt.fromtimestamp(x))
    
    temp['Date2']=temp['Date1'].apply(lambda x:x.strftime("%Y-%m-%d")) #dt to string
    temp=temp.loc[temp['Date2']>initial_date,:]
    temp=temp.sort_values(by=['Date1'],ascending=True)
    
    #find two day before last trading day
    initial_date=temp.Date2.unique()[-3]
    temp=temp.loc[temp['Date2']<=initial_date,:].copy()
    temp['contract']=i
    
    data_all=data_all.append(temp)

    print("finished ",i,temp['Date2'].values[0],temp['Date2'].values[-1])





data_all=data_all.reset_index(drop=True)
#del data_all['Date']




jp_zone=tz.gettz('Asia/Tokyo')
hk_zone=tz.gettz('Asia/Hong_Kong')
data_all['Date_hk']=data_all['Date1'].apply(lambda x:x.replace(tzinfo=hk_zone))
data_all['Date_jp']=data_all['Date_hk'].apply(lambda x:x.astimezone(jp_zone))
data_all['Date_jp_lag1']=data_all['Date_jp'].shift(1)
data_all['Date_jp_hms']=data_all['Date_jp'].apply(lambda x:x.strftime("%H:%M:%S"))

data_all['time_diff']=data_all['Date_jp_lag1']-data_all['Date_jp']
data_all['time_diff_min']=data_all['time_diff'].apply(lambda x:x.total_seconds()/60)

del data_all['Date_jp_lag1']
del data_all['time_diff']

a_check=data_all.tail(1000).copy()

a_check=data_all.loc[data_all['Date2']<='2010-01-01',:].copy()















09:00:00 open - 15:00:00 close
08:30:00 open - 15:00:00 close


data_all_temp=data_all.copy()

data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2008-03-27',:].copy()
data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2020-08-04',:].copy()
data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2011-07-23',:].copy()  #no data
data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2011-07-30',:].copy()  #no data
data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2011-08-06',:].copy()  #no data

def find_price(data_all_temp):
    t_date=data_all_temp.Date2.values[0]
    print('doing ',t_date)
    data_all_temp_use=pd.DataFrame([])
    if t_date<='2016-07-15':
        a=dt(int(t_date.split('-')[0]),int(t_date.split('-')[1]),int(t_date.split('-')[2]),9,0,0).replace(tzinfo=jp_zone)
        b=dt(int(t_date.split('-')[0]),int(t_date.split('-')[1]),int(t_date.split('-')[2]),15,0,0).replace(tzinfo=jp_zone)
        data_all_temp_use=data_all_temp.loc[(data_all_temp['Date_jp']>=a)&(data_all_temp['Date_jp']<=b),:].copy()

    if t_date>'2016-07-15':
        a=dt(int(t_date.split('-')[0]),int(t_date.split('-')[1]),int(t_date.split('-')[2]),8,30,0).replace(tzinfo=jp_zone)
        b=dt(int(t_date.split('-')[0]),int(t_date.split('-')[1]),int(t_date.split('-')[2]),15,0,0).replace(tzinfo=jp_zone)
        data_all_temp_use=data_all_temp.loc[(data_all_temp['Date_jp']>=a)&(data_all_temp['Date_jp']<=b),:].copy()
    
    if data_all_temp_use.shape[0]==0:
        output=pd.DataFrame({'Date2':[t_date],'open':[0],'high':[0],'low':[0],'close':[0],'volume':[0]})
    else:
        oprice=data_all_temp_use.open.values[0]
        hprice=max(data_all_temp_use.high)
        lprice=min(data_all_temp_use.low)
        cprice=data_all_temp_use.close.values[-1]
        volume=sum(data_all_temp_use.Volume.values)
        
        output=pd.DataFrame({'Date2':[t_date],'open':[oprice],'high':[hprice],'low':[lprice],'close':[cprice],'volume':[volume]})
    
    return output


temp=data_all.groupby(['Date2']).apply(lambda x:find_price(x))
temp=temp.loc[temp['volume']!=0,:].copy()
temp=temp.reset_index(drop=True)
temp=temp.rename(columns={'open':'Open','high':'High','low':'Low','close':'Close','volume':'Volume'})





#check with barchart
barchart_data = read_excel(os.path.join(set_dir,'N225_futures_from_barchart.xlsx'),'Sheet1')
temp2=pd.merge(temp,barchart_data[['Date2','Open','High','Low','Last','Volume']].copy(),how='left',on=['Date2'])

#find OI from barchart
temp=pd.merge(temp,barchart_data[['Date2','OI']].copy(),how='left',on=['Date2'])
temp=temp.loc[(temp['OI']!=0)&(~pd.isnull(temp['OI'])),:].copy()
temp=temp.reset_index(drop=True)


path_out=os.path.join(set_dir,'N225_futures_from_tradingview.xlsx') #rename this and save as n225_cum
writer = pd.ExcelWriter(path_out, engine='xlsxwriter')
temp.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

















##### find price within 0_to_60 japan time
data_all_temp=data_all.copy()

data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2008-03-27',:].copy()
data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2020-08-04',:].copy()
data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2011-07-23',:].copy()  #no data
data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2011-07-30',:].copy()  #no data
data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2011-08-06',:].copy()  #no data

def find_price(data_all_temp):
    t_date=data_all_temp.Date2.values[0]
    print('doing ',t_date)
    data_all_temp_use=pd.DataFrame([])
    if t_date<='2016-07-15':
        a=dt(int(t_date.split('-')[0]),int(t_date.split('-')[1]),int(t_date.split('-')[2]),9,0,0).replace(tzinfo=jp_zone)
        b=dt(int(t_date.split('-')[0]),int(t_date.split('-')[1]),int(t_date.split('-')[2]),9,45,0).replace(tzinfo=jp_zone)
        data_all_temp_use=data_all_temp.loc[(data_all_temp['Date_jp']>=a)&(data_all_temp['Date_jp']<=b),:].copy()

    if t_date>'2016-07-15':
        a=dt(int(t_date.split('-')[0]),int(t_date.split('-')[1]),int(t_date.split('-')[2]),8,45,0).replace(tzinfo=jp_zone)
        b=dt(int(t_date.split('-')[0]),int(t_date.split('-')[1]),int(t_date.split('-')[2]),9,45,0).replace(tzinfo=jp_zone)
        data_all_temp_use=data_all_temp.loc[(data_all_temp['Date_jp']>=a)&(data_all_temp['Date_jp']<=b),:].copy()
    
    if data_all_temp_use.shape[0]==0:
        output=pd.DataFrame({'Date2':[t_date],'open':[0],'high':[0],'low':[0],'close':[0],'volume':[0]})
    else:
        oprice=data_all_temp_use.open.values[0]
        hprice=max(data_all_temp_use.high)
        lprice=min(data_all_temp_use.low)
        cprice=data_all_temp_use.close.values[-1]
        volume=sum(data_all_temp_use.Volume.values)
        
        output=pd.DataFrame({'Date2':[t_date],'open':[oprice],'high':[hprice],'low':[lprice],'close':[cprice],'volume':[volume]})
    
    return output


temp=data_all.groupby(['Date2']).apply(lambda x:find_price(x))
temp=temp.loc[temp['volume']!=0,:].copy()
temp=temp.reset_index(drop=True)
temp=temp.rename(columns={'open':'Open','high':'High','low':'Low','close':'Close','volume':'Volume'})
temp=temp.reset_index(drop=True)

path_out=os.path.join(set_dir,'N225_futures_from_tradingview_0_to_60.xlsx') #rename this and save as n225_cum
writer = pd.ExcelWriter(path_out, engine='xlsxwriter')
temp.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()




















##### find price within open and first 15mins
data_all_temp=data_all.copy()

data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2008-03-27',:].copy()
data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2016-07-15',:].copy()
data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2020-08-04',:].copy()
data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2011-07-23',:].copy()  #no data
data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2011-07-30',:].copy()  #no data
data_all_temp=data_all_temp.loc[data_all_temp['Date2']=='2011-08-06',:].copy()  #no data

def find_price(data_all_temp):
    t_date=data_all_temp.Date2.values[0]
    print('doing ',t_date)
    data_all_temp_use=pd.DataFrame([])
    if t_date<='2016-07-15':
        a=dt(int(t_date.split('-')[0]),int(t_date.split('-')[1]),int(t_date.split('-')[2]),9,0,0).replace(tzinfo=jp_zone)
        b=dt(int(t_date.split('-')[0]),int(t_date.split('-')[1]),int(t_date.split('-')[2]),9,45,0).replace(tzinfo=jp_zone)
        data_all_temp_use=data_all_temp.loc[(data_all_temp['Date_jp']>=a)&(data_all_temp['Date_jp']<=b),:].copy()

    if t_date>'2016-07-15':
        a=dt(int(t_date.split('-')[0]),int(t_date.split('-')[1]),int(t_date.split('-')[2]),9,0,0).replace(tzinfo=jp_zone)
        b=dt(int(t_date.split('-')[0]),int(t_date.split('-')[1]),int(t_date.split('-')[2]),9,45,0).replace(tzinfo=jp_zone)
        data_all_temp_use=data_all_temp.loc[(data_all_temp['Date_jp']>=a)&(data_all_temp['Date_jp']<=b),:].copy()
    
    if data_all_temp_use.shape[0]==0:
        output=pd.DataFrame({'Date2':[t_date],'open':[0],'high':[0],'low':[0],'close':[0],'volume':[0]})
    else:
        oprice=data_all_temp_use.open.values[0]
        hprice=max(data_all_temp_use.high)
        lprice=min(data_all_temp_use.low)
        cprice=data_all_temp_use.close.values[-1]
        volume=sum(data_all_temp_use.Volume.values)
        
        output=pd.DataFrame({'Date2':[t_date],'open':[oprice],'high':[hprice],'low':[lprice],'close':[cprice],'volume':[volume]})
    
    return output


temp=data_all.groupby(['Date2']).apply(lambda x:find_price(x))
temp=temp.loc[temp['volume']!=0,:].copy()
temp=temp.reset_index(drop=True)
temp=temp.rename(columns={'open':'Open','high':'High','low':'Low','close':'Close','volume':'Volume'})
temp=temp.reset_index(drop=True)

path_out=os.path.join(set_dir,'N225_futures_from_tradingview_0_to_15.xlsx') #rename this and save as n225_futures_0_to_15_cum.xlsx
writer = pd.ExcelWriter(path_out, engine='xlsxwriter')
temp.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()





















#################################################################
###############KOPSI#############################################

FBK2U2021


year_list=[i for i in range(2008,2022)]

futures_list=['H','M','U','Z']

symbol_list=[]
i=2021
for i in year_list:
    for j in futures_list:
        symbol_list.append('NK225'+str(j)+str(i))
        
        
        

        
        
import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import io
import sys
import pandas as pd

from datetime import datetime as dt
from pandas import read_excel
from dateutil import tz

#login



set_dir="/home/jonathanjames/aws/notebooks/index_analysis/data/n225_futures"
#set_dir=r"C:\Users\jonathanjames\aws\notebooks\index_analysis\data\n225_futures"

download_path_save_as=os.path.join(set_dir,"tradingview_data")





os.chdir(set_dir)


op = webdriver.ChromeOptions()
#op.add_argument('headless')
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-shm-usage')


#add file save path using chrome to download
prefs = {"download.default_directory" : download_path_save_as}
op.add_experimental_option("prefs",prefs)

op.add_experimental_option("excludeSwitches", ['enable-automation'])

browser = webdriver.Chrome(options=op,executable_path='/home/jonathanjames/aws/notebooks/horse/chrome_driver/chromedriver_linux64/chromedriver84')
#browser = webdriver.Chrome(options=op,executable_path=r'C:\Users\jonathanjames\aws\notebooks\horse\chrome_driver\chromedriver_win32\chromedriver_87.exe')

#browser.execute_script("return document.cookie")  
browser.execute_script("return navigator.userAgent")  




#browser = webdriver.Chrome(executable_path=r'C:\Users\jonathan.james\.Spyder\chromedriver.exe')
browser.get("https://tw.tradingview.com/#signin")

wait = WebDriverWait(browser, 30)


#click login





wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span'))).click()
#wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__user-name-input__e1145da9-d962-4a16-9257-c9020c9f711b"]'))).send_keys('jonathan2019trading')
#wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__password-input__e1145da9-d962-4a16-9257-c9020c9f711b"]'))).send_keys('wjkd4685')
#wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__submit-button__e1145da9-d962-4a16-9257-c9020c9f711b"]/span[1]'))).click()
#wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__user-name-input__e1145da9-d962-4a16-9257-c9020c9f711b"]'))).send_keys('po3667222@gmail.com')
#wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__password-input__e1145da9-d962-4a16-9257-c9020c9f711b"]'))).send_keys('wjkd4685')

wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__user-name-input__e1145da9-d962-4a16-9257-c9020c9f711b"]'))).send_keys('bigbigbigtaitai@gmail.com')
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__password-input__e1145da9-d962-4a16-9257-c9020c9f711b"]'))).send_keys('bigbigbig2021')


sleep(3)


browser.maximize_window()
browser.get("https://tw.tradingview.com/chart/mo6AvbRF/")



#note
#when screen show how many bars, historicakl excel template all have how many row
#so if drap browser's left and right so more bars show, then historical has more bars

i='NK225U2020'
for i in symbol_list:
    target_symbol=i

    #link='https://www.tradingview.com/chart/?symbol=OSE%3A'+target_symbol
    #browser.get(link)
    

    
    
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div'))).click()
    sleep(1)
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div[2]/div[1]/input'))).send_keys(target_symbol)
    sleep(1)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div[1]/input'))).send_keys(Keys.ENTER)
    
    
    
    #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/div[11]'))).click() #choose 15  mins
    

#    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.CONTROL,"a")
#    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.DELETE)
#    
#    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]'))).send_keys(target_symbol)
#    
#    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.ENTER)
#    sleep(2)
       
    #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "value-DWZXOdoK", " " ))]'))).click()
    #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/div[11]'))).click() #choose 15  mins
    sleep(4)
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div[5]'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/span/button'))).click()        
    sleep(1)
    






initial_date="2008-01-01"
#dt.fromtimestamp(1592583300)


i='NK225U2021'
data_all=pd.DataFrame([])
for i in symbol_list:
    file_name=os.path.join(download_path_save_as,'OSE_DLY_'+i+', 15.csv')
    temp=pd.read_csv(file_name)
    temp['Date1']=temp['time'].apply(lambda x:dt.fromtimestamp(x))
    
    temp['Date2']=temp['Date1'].apply(lambda x:x.strftime("%Y-%m-%d")) #dt to string
    temp=temp.loc[temp['Date2']>initial_date,:]
    temp=temp.sort_values(by=['Date1'],ascending=True)
    
    #find two day before last trading day
    initial_date=temp.Date2.unique()[-3]
    temp=temp.loc[temp['Date2']<=initial_date,:].copy()
    temp['contract']=i
    
    data_all=data_all.append(temp)

    print("finished ",i,temp['Date2'].values[0],temp['Date2'].values[-1])





data_all=data_all.reset_index(drop=True)
#del data_all['Date']




jp_zone=tz.gettz('Asia/Tokyo')
hk_zone=tz.gettz('Asia/Hong_Kong')
data_all['Date_hk']=data_all['Date1'].apply(lambda x:x.replace(tzinfo=hk_zone))
data_all['Date_jp']=data_all['Date_hk'].apply(lambda x:x.astimezone(jp_zone))
data_all['Date_jp_lag1']=data_all['Date_jp'].shift(1)
data_all['Date_jp_hms']=data_all['Date_jp'].apply(lambda x:x.strftime("%H:%M:%S"))

data_all['time_diff']=data_all['Date_jp_lag1']-data_all['Date_jp']
data_all['time_diff_min']=data_all['time_diff'].apply(lambda x:x.total_seconds()/60)

del data_all['Date_jp_lag1']
del data_all['time_diff']

a_check=data_all.tail(1000).copy()

a_check=data_all.loc[data_all['Date2']<='2010-01-01',:].copy()












































datetime.fromtimestamp(1592583300)








##############################################################################
##########extract from https://tw.tradingview.com/############################
##############################################################################

year_list=[i for i in range(2008,2021)]

futures_list=['F','G','H','J','K','M','N','Q','U','V','X','Z']

symbol_list=[]
for i in year_list:
    for j in futures_list:
        symbol_list.append('HHI'+str(j)+str(i))
        
        
        

        
        
import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import io
import sys
import pandas as pd



#login



set_dir="/home/jonathanjames/aws/notebooks/index_analysis/data/HHI_HKEX"
download_path_save_as=os.path.join(set_dir,"tradingview_data")

os.chdir(set_dir)


op = webdriver.ChromeOptions()
#op.add_argument('headless')
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-shm-usage')


#add file save path using chrome to download
prefs = {"download.default_directory" : download_path_save_as}
op.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(options=op,executable_path='/home/jonathanjames/aws/notebooks/horse/chrome_driver/chromedriver_linux64/chromedriver')
#browser.execute_script("return document.cookie")  
browser.execute_script("return navigator.userAgent")  




#browser = webdriver.Chrome(executable_path=r'C:\Users\jonathan.james\.Spyder\chromedriver.exe')
browser.get("https://tw.tradingview.com/#signin")

wait = WebDriverWait(browser, 30)


#click login
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signin-form"]/div[1]/div[1]/input'))).send_keys('jonathan2019trading')
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signin-form"]/div[2]/div[1]/div[1]/input'))).send_keys('wjkd4685')
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signin-form"]/div[3]/div[2]/button'))).click()

sleep(3)

browser.get("https://tw.tradingview.com/chart/")
browser.maximize_window()
    
#wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).clear()
#for i in range(0,20):
#    if wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).get_attribute('value')=='AAPL':
#       wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.CONTROL,"a")
#       wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.DELETE)
#       wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys('HHIM2013')
#       wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.ENTER)
#    sleep(1)


i='HHIF2008'
for i in symbol_list:
    target_symbol=i

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.CONTROL,"a")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.DELETE)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(target_symbol)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.ENTER)
    sleep(2)
       
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "value-DWZXOdoK", " " ))]'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/div[11]'))).click() #choose 15  mins
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div[5]'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/span/button'))).click()        
    sleep(2)
    






#read downloaded file and edit it
from datetime import datetime as dt

initial_date="2007-12-30"
#dt.fromtimestamp(1592583300)


i='HHIH2013'#'HHIF2008'
data_all=pd.DataFrame([])
for i in symbol_list:
    file_name=os.path.join(set_dir,"tradingview_data","HKEX_DLY_"+i+", 15.csv")
    temp=pd.read_csv(file_name)
    temp['Date']=temp['time'].apply(lambda x :dt.fromtimestamp(x))
    
    
    temp['Date2']=temp['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))
    temp=temp.loc[temp['Date2']>initial_date,:]
    
    
    temp['day_start']=temp['Date'].apply(lambda x:dt(x.year,x.month,x.day,8,30))
    temp['day_end']=temp['Date'].apply(lambda x:dt(x.year,x.month,x.day,16,30))
    
    #only use morning and afternoon
    temp=temp.loc[(temp['Date']>=temp['day_start'])&(temp['Date']<=temp['day_end']),:]
    temp['symbol']=i
    
    temp=temp[['Date','Date2','day_start','day_end','symbol','open','high','low','close','Volume']].copy()
    
    
    data_all=data_all.append(temp)
    initial_date=temp['Date2'].values[-1]
    print("finished ",i)




data_all=data_all.reset_index(drop=True)
data_all=data_all.sort_values(by=['Date'],ascending=[True])

temp=data_all.loc[data_all['Date2']=='2020-06-19',:].reset_index(drop=True)
temp=data_all.loc[data_all['Date2']=='2013-03-28',:].reset_index(drop=True)

def custom_ohlc(temp):
    Date=temp['Date2'].values[0]
    first_row_time=temp['Date'].values[0]
    last_row_time=temp['Date'].values[-1]
    open_price=temp['open'].values[0]
    high_price=max(temp['high'].values)
    low_price=min(temp['low'].values)
    close_price=temp['close'].values[-1]
    volume=sum(temp.Volume.values)
    symbol=temp['symbol'].values[0]
    total_rows_15_mins_bar=temp.shape[0]
    output=pd.DataFrame({'Date':[Date],
                         'first_row_time':[first_row_time],
                         'last_row_time':[last_row_time],
                         'Open':[open_price],
                         'High':[high_price],
                         'Low':[low_price],
                         'Close':[close_price],
                         'Volume':[volume],
                         'symbol':[symbol],
                         'total_rows_15_mins_bar':[total_rows_15_mins_bar]})
    return output



data_all2=data_all.groupby(['Date2']).apply(lambda x:custom_ohlc(x.reset_index(drop=True)))

#for easy checking
data_all2['first_row_time_only']=data_all2['first_row_time'].apply(lambda x:x.strftime("%H:%M:%S"))
data_all2['last_row_time_only']=data_all2['last_row_time'].apply(lambda x:x.strftime("%H:%M:%S"))



data_all3=data_all2.loc[~(data_all2['total_rows_15_mins_bar']==1),:]
data_all3=data_all3.sort_values(by=['Date'],ascending=[True])

data_all3.to_csv("/home/jonathanjames/aws/notebooks/index_analysis/data/HHI_20071231_to_20200619_from_tradingview.csv")






















































##############################################################################
##########extract from https://tw.tradingview.com/############################
##############################################################################

year_list=[i for i in range(2008,2021)]

futures_list=['F','G','H','J','K','M','N','Q','U','V','X','Z']

symbol_list=[]
for i in year_list:
    for j in futures_list:
        symbol_list.append('HHI'+str(j)+str(i))
        
        
        

        
        
import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import io
import sys
import pandas as pd



#login



set_dir="/home/jonathanjames/aws/notebooks/index_analysis/data/NZ50"
download_path_save_as=os.path.join(set_dir,"tradingview_data")

os.chdir(set_dir)


op = webdriver.ChromeOptions()
#op.add_argument('headless')
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-shm-usage')


#add file save path using chrome to download
prefs = {"download.default_directory" : download_path_save_as}
op.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(options=op,executable_path='/home/jonathanjames/aws/notebooks/horse/chrome_driver/chromedriver_linux64/chromedriver84')
#browser.execute_script("return document.cookie")  
browser.execute_script("return navigator.userAgent")  




#browser = webdriver.Chrome(executable_path=r'C:\Users\jonathan.james\.Spyder\chromedriver.exe')
browser.get("https://tw.tradingview.com/#signin")

wait = WebDriverWait(browser, 30)


#click login

wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span'))).click()



//*[@id="email-signin__user-name-input__8331c182-74f5-43c1-bdf6-9c7f56bc6d27"]


wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__user-name-input__8331c182-74f5-43c1-bdf6-9c7f56bc6d27"]'))).send_keys('jonathan2019trading')
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "tv-control-material-input__control", " " ))]'))).send_keys('wjkd4685')
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-signin__submit-button__740dffa1-fceb-40ce-b112-9af405d9377b"]'))).click()
sleep(3)

browser.get("https://tw.tradingview.com/chart/")
browser.maximize_window()
    
#wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).clear()
#for i in range(0,20):
#    if wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).get_attribute('value')=='AAPL':
#       wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.CONTROL,"a")
#       wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.DELETE)
#       wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys('HHIM2013')
#       wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.ENTER)
#    sleep(1)


i='HHIF2008'
for i in symbol_list:
    target_symbol=i

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.CONTROL,"a")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.DELETE)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(target_symbol)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-toolbar-symbol-search"]/div/input'))).send_keys(Keys.ENTER)
    sleep(2)
       
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "value-DWZXOdoK", " " ))]'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/div[11]'))).click() #choose 15  mins
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div[5]'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/span/button'))).click()        
    sleep(2)
    






#read downloaded file and edit it
from datetime import datetime as dt

initial_date="2007-12-30"
#dt.fromtimestamp(1592583300)


i='HHIH2013'#'HHIF2008'
data_all=pd.DataFrame([])
for i in symbol_list:
    file_name=os.path.join(set_dir,"tradingview_data","HKEX_DLY_"+i+", 15.csv")
    temp=pd.read_csv(file_name)
    temp['Date']=temp['time'].apply(lambda x :dt.fromtimestamp(x))
    
    
    temp['Date2']=temp['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))
    temp=temp.loc[temp['Date2']>initial_date,:]
    
    
    temp['day_start']=temp['Date'].apply(lambda x:dt(x.year,x.month,x.day,8,30))
    temp['day_end']=temp['Date'].apply(lambda x:dt(x.year,x.month,x.day,16,30))
    
    #only use morning and afternoon
    temp=temp.loc[(temp['Date']>=temp['day_start'])&(temp['Date']<=temp['day_end']),:]
    temp['symbol']=i
    
    temp=temp[['Date','Date2','day_start','day_end','symbol','open','high','low','close','Volume']].copy()
    
    
    data_all=data_all.append(temp)
    initial_date=temp['Date2'].values[-1]
    print("finished ",i)




data_all=data_all.reset_index(drop=True)
data_all=data_all.sort_values(by=['Date'],ascending=[True])

temp=data_all.loc[data_all['Date2']=='2020-06-19',:].reset_index(drop=True)
temp=data_all.loc[data_all['Date2']=='2013-03-28',:].reset_index(drop=True)

def custom_ohlc(temp):
    Date=temp['Date2'].values[0]
    first_row_time=temp['Date'].values[0]
    last_row_time=temp['Date'].values[-1]
    open_price=temp['open'].values[0]
    high_price=max(temp['high'].values)
    low_price=min(temp['low'].values)
    close_price=temp['close'].values[-1]
    volume=sum(temp.Volume.values)
    symbol=temp['symbol'].values[0]
    total_rows_15_mins_bar=temp.shape[0]
    output=pd.DataFrame({'Date':[Date],
                         'first_row_time':[first_row_time],
                         'last_row_time':[last_row_time],
                         'Open':[open_price],
                         'High':[high_price],
                         'Low':[low_price],
                         'Close':[close_price],
                         'Volume':[volume],
                         'symbol':[symbol],
                         'total_rows_15_mins_bar':[total_rows_15_mins_bar]})
    return output



data_all2=data_all.groupby(['Date2']).apply(lambda x:custom_ohlc(x.reset_index(drop=True)))

#for easy checking
data_all2['first_row_time_only']=data_all2['first_row_time'].apply(lambda x:x.strftime("%H:%M:%S"))
data_all2['last_row_time_only']=data_all2['last_row_time'].apply(lambda x:x.strftime("%H:%M:%S"))



data_all3=data_all2.loc[~(data_all2['total_rows_15_mins_bar']==1),:]
data_all3=data_all3.sort_values(by=['Date'],ascending=[True])

data_all3.to_csv("/home/jonathanjames/aws/notebooks/index_analysis/data/HHI_20071231_to_20200619_from_tradingview.csv")







index_price_individual_strategy_us_stock_pick.py






#%reset -f
#654_pnl_statistic.xlsx
import os
#os.chdir(r'C:\Users\jonathanjames\aws\notebooks\tensorflow-mnist-tutorial-master')

import math
import numpy as np
import pandas as pd
import sys

import time
time_start=time.time()
import ast
import matplotlib.pyplot as plt


from datetime import datetime as dt

from pandas import read_excel





#r_path=r"C:\Program Files\R\R-3.3.3\bin\Rscript"
#index_analysis_path=r'C:\Users\jonathanjames\aws\notebooks\index_analysis'
#data=read_excel(os.path.join(index_analysis_path,'index_table_v2_for_test_backtest.xlsx'),'Sheet1')
#calendar = read_excel(os.path.join(index_analysis_path,'daily_prediction_production','calendar_us.xlsx'),'calendar')
#
##this is for log path
#log_path=os.path.join(index_analysis_path,'log')
#r_path_cook_train=os.path.join(index_analysis_path,'R_script','hsi_cook_distance.R')
#r_path_cook_test=os.path.join(index_analysis_path,'R_script','hsi_cook_distance_test.R')
#main_folder=os.path.join(index_analysis_path,'plot')





r_path="/root/anaconda3/envs/myRenv3_4/lib/R/bin/Rscript"
index_analysis_path_original='/home/jonathanjames/aws/notebooks/index_analysis'
index_analysis_path='/home/jonathanjames/aws/notebooks/index_analysis'
#index_analysis_path='/home/jonathanjames/my_storage/tradelog/index_analysis_cumulative'

#tidy_path='/home/jonathanjames/my_storage/tradelog/index_analysis_cumulative/backtest_linux/database/tidy'
tidy_path='/home/jonathanjames/aws/notebooks/index_analysis'

data=read_excel(os.path.join(index_analysis_path_original,'index_table_v2_for_test_backtest.xlsx'),'Sheet1')
calendar = read_excel(os.path.join(index_analysis_path_original,'daily_prediction_production','calendar.xlsx'),'calendar_us')

#this is for log path
#log_path=os.path.join(index_analysis_path,'backtest_linux/log')
log_path=os.path.join(index_analysis_path,'log')
r_path_cook_train=os.path.join(index_analysis_path_original,'R_script','hsi_cook_distance_linux.R')
r_path_cook_test=os.path.join(index_analysis_path_original,'R_script','hsi_cook_distance_test_linux.R')
main_folder=os.path.join('/home/jonathanjames/my_storage/tradelog/index_analysis_cumulative','backtest_linux/plot')










test_year=2022
#train_start='2005-12-01';train_end='2013-12-31'
#test_start='2014-01-01';test_end='2014-12-31'
train_start='2005-12-01';train_end=str(test_year-1)+'-12-31'
test_start=str(test_year)+'-01-01';test_end=str(test_year)+'-12-31' #'2018-04-06'#'2018-04-04'
NumberRun=19514#10000#int(sys.argv[5])
no_of_run=80000#200000#int(sys.argv[6])#200000#1000000
shuffle=False
train_pkeep=1#0.75
fixed_initial_weight=True
dropout_seed=None
batch_size_number=0.0
batch_size_percent=1.0#1.0#1.0#0.01
use_automation=True
factor_file='factor2.txt'#'factor0_dummy.txt'#'factor2.txt'
set_prob_threshold=0.5   #without any filter, set 0.5
stoploss_use=999999#999999#10000#000
cook_use=100#0.002  # if <1 it is a fixed value, if >1 it is percentile
test_mode='MSFT'#'IBM@BBY'#'WST'#'MSFT'  #UNH BA


try:
    train_start=sys.argv[1];train_end=sys.argv[2]
    test_start=sys.argv[3];test_end=sys.argv[4]
    NumberRun=int(round(float(sys.argv[5])))
    no_of_run=int(round(float(sys.argv[6])))#200000#1000000
    shuffle=ast.literal_eval(sys.argv[7])
    train_pkeep=np.float32(sys.argv[8])#1.0#0.75
    fixed_initial_weight=ast.literal_eval(sys.argv[9])
    dropout_seed=None
    batch_size_number=int(round(float(sys.argv[10])))#1#round(train_x.shape[0]*0.5)
    batch_size_percent=np.float32(sys.argv[11])
    use_automation=True
    factor_file=sys.argv[12]#factor_file='factor_base_47_interact_comm2_with_HSI_index_v2_83188_MF_japan_stock_1_high_corr_HJPNX_OTPSX_FBGKX_change_TBGVX_change_XBI_DHFCX_use_wsj.txt'
    set_prob_threshold=np.float32(sys.argv[13])
    stoploss_use=np.float32(sys.argv[14])
    cook_use=np.float32(sys.argv[15])
    test_mode=sys.argv[16]
except:
    pass









#output stand out
import sys
stan_out_log=os.path.join(log_path,'stan_out_log_'+time.strftime("%Y%m%d")+'_'+time.strftime("%H%M%S")+'_'+str(NumberRun)+'.log')
sys.stderr = open(stan_out_log, 'w')

















if test_mode!='fullday':
    HSI_source=read_excel(os.path.join(tidy_path,test_mode+'_with_tidy.xlsx'),'Sheet1')
    HSI_source.dtypes
    t1='Open_'+test_mode
    t2='High_'+test_mode
    t3='Low_'+test_mode
    t4='Close_'+test_mode
    t6=test_mode+'_change'
    HSI_source=HSI_source.rename(columns={t1:'Open_HSI',t2:'High_HSI',
                                          t3:'Low_HSI',
                                          t4:'Close_HSI',
                                          t6:'HSI_change'})
    #read data
    #fn = os.path.join(index_analysis_path_original,'hsi_y_x_'+test_mode+'.hdf5')
    fn = os.path.join(index_analysis_path,'hsi_y_x_'+test_mode+'.hdf5')
    store = pd.HDFStore(fn, 'r')
    print(store)
    hsi_y_x= store.select('hsi_y_x_'+test_mode+'_dataframe')
    list(hsi_y_x.columns.values)
    store.close()
    
    hsi_y_x=hsi_y_x.rename(columns={'Y_up_cum_final':'Y_up','Y_down_cum_final':'Y_down'})
    hsi_y_x=hsi_y_x.reset_index(drop=True)








if test_mode=='fullday':
    HSI_source=read_excel(os.path.join(index_analysis_path,'HSI_with_tidy.xlsx'),'Sheet1')
    #read data
    fn = os.path.join(index_analysis_path,'hsi_y_x.hdf5')
    store = pd.HDFStore(fn, 'r')
    print(store)
    hsi_y_x= store.select('hsi_y_x_dataframe')
    list(hsi_y_x.columns.values)
    store.close()
    
    #hsi_y_x['f1']=hsi_y_x['f1'].fillna(0)
    
    #hsi_y_x=read_excel('daily_source_data_production/hsi_y_x_20210407_073941_production.xlsx')
    #hsi_y_x=read_excel('daily_source_data_production/hsi_y_x_20211116_073941_production.xlsx')
    
    




















output_folder=os.path.join(main_folder,str(NumberRun))

import shutil
if os.path.exists(output_folder):
    shutil.rmtree(output_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_folder_nsample=os.path.join(main_folder,str(NumberRun),'nsample')
if not os.path.exists(output_folder_nsample):
    os.makedirs(output_folder_nsample)
















#below factor list is up to train 20101231 using python lofistic regression including stock financial 30 variable
#factor_file='factor_base_47_interact_comm2_with_HSI_index_v2_83188_MF_japan_stock_1_high_corr_HJPNX_OTPSX_FBGKX_change_TBGVX_change_XBI_DHFCX_1605.T_change_no_fund.txt'
#factor_file='factor1.txt'
if use_automation==True:
    factor_path=os.path.join(index_analysis_path_original,'plot_us','factor',factor_file)
    #factor_path=os.path.join(index_analysis_path,'factor_hhi.txt')
    import ast
    with open(factor_path, 'r') as f:
        use_factor_list = ast.literal_eval(f.read())
else:
    use_factor_list=['Date2','balancepower_up','balancepower_down']








x_all_temp=hsi_y_x.loc[:,use_factor_list] #select columns
x_all=x_all_temp.reset_index(drop=True)



year_test=test_start[0:4]
test_x_with_date=pd.DataFrame(x_all.loc[(x_all['Date2']>=test_start)&(x_all['Date2']<=test_end),:].copy())
#test_x_with_date=pd.DataFrame(x_all.loc[(x_all['Date2']>=test_start)&(x_all['Date2']<='2018-12-22'),'Date2'].copy())
test_x_with_date=test_x_with_date.reset_index(drop=True)


HSI=HSI_source.copy()
test_x_with_date=pd.merge(left=test_x_with_date,right=HSI,how='left',on='Date2')


test_x_with_date['close_open_diff']=test_x_with_date['Close_HSI']-test_x_with_date['Open_HSI']













if len(use_factor_list)==2:
    one_use=use_factor_list[1]
    test_x_with_date['bet']=test_x_with_date[one_use].copy()


if len(use_factor_list)==3:
    one_use=test_x_with_date[use_factor_list[1]].values
    second_use=test_x_with_date[use_factor_list[2]].values
    test_x_with_date['bet']=one_use+second_use
    



if sum(test_x_with_date['bet'].values==0)==test_x_with_date.shape[0]:
    test_x_with_date.loc[0,'bet']=1
    test_x_with_date.loc[1,'bet']=-1












##try to use price - ema indicator
#import talib
#from talib import abstract
#HSI_source_temp=HSI_source.copy()
#HSI_source_temp=HSI_source_temp.rename(columns={"Close_HSI":'close'})
#HSI_source_temp['ema_10']=abstract.EMA(HSI_source_temp,7)
##HSI_source_temp=HSI_source_temp.rename(columns={"kl_spread":'close'})
##HSI_source_temp['ema_10']=abstract.EMA(HSI_source_temp,7)#normal use 7
#
#HSI_source_temp['RSI']=abstract.RSI(HSI_source_temp,14)
#HSI_source_temp['price_ema10']=100*(HSI_source_temp['close']-HSI_source_temp['ema_10'])/HSI_source_temp['ema_10']
#HSI_source_temp['year_cohord']=HSI_source_temp['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y")).astype(int)
#
#
#
#
#HSI_source_temp['f1']=(HSI_source_temp['close']-HSI_source_temp['ema_10'])/HSI_source_temp['ema_10']
#
##HSI_source_temp['f1']=HSI_source_temp['close'].copy()
#
#
#
#target_variable='f1'
#distinct_year=HSI_source_temp['year_cohord'].unique()
#distinct_year=[i for i in distinct_year if i >=2009]
#yy=2009
#percentile_cum=pd.DataFrame([])
#for yy in distinct_year:
#    data_use=HSI_source_temp.loc[HSI_source_temp['year_cohord']<yy,target_variable].values
#    data_use=data_use[~np.isnan(data_use)]
#    data_use_mean=np.mean(data_use);data_use_std=np.std(data_use)
#    t1='mean';t2='std'
#    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],t1:[data_use_mean],t2:[data_use_std]}))
#
#
#HSI_source_temp=pd.merge(HSI_source_temp,percentile_cum,how='left',on=['year_cohord'])
#
#
#
#HSI_source_temp['f1_temp']=(HSI_source_temp['f1']-HSI_source_temp['mean'])/HSI_source_temp['std']
#HSI_source_temp['f2']=100*(1/(1+np.exp(-1*HSI_source_temp['f1_temp'])))
#
#
##use emprical distribution
#target_variable='f1'
#new_variable='f3'
#
#distinct_year=[int(year_test)-1,int(year_test)] 
#yy=2009
#output=pd.DataFrame([])
#for yy in distinct_year:
#    data_use=HSI_source_temp.loc[(HSI_source_temp['year_cohord']>=yy-100)&(HSI_source_temp['year_cohord']<yy),target_variable].values
#    data_use=data_use[~np.isnan(data_use)] 
#    data_use=pd.DataFrame(data_use)
#
#HSI_source_temp=pd.merge(HSI_source_temp,output[['Date2',new_variable]].copy(),how='left',on=['Date2'])
#HSI_source_temp['f1_temp']-HSI_source_temp['f1_temp'].shift(1)
#HSI_source_temp['f2']=HSI_source_temp['f2'].shift(1)
#HSI_source_temp['f3']=HSI_source_temp['f3'].shift(1)
#HSI_source_temp['RSI']=HSI_source_temp['RSI'].shift(1)
#
#test_x_with_date=pd.merge(test_x_with_date,HSI_source_temp[['Date2','f1_temp','f2','f3','RSI']].copy(),how='left',on=['Date2'])
#
#
#test_x_with_date.loc[(test_x_with_date['f3']>=70),'bet1']=-1
#test_x_with_date.loc[(test_x_with_date['f3']<=30),'bet1']=1
#
#test_x_with_date['bet1']=test_x_with_date['bet1'].fillna(method='ffill')
##test_x_with_date['bet1']=test_x_with_date['bet1'].fillna(0)
#test_x_with_date['bet']=test_x_with_date['bet1'].copy()
#
#del test_x_with_date['bet1']





##version 1 -  e.g. less than 20, then long, higher than 80 short
#test_x_with_date.loc[(test_x_with_date['f3']>=80),'bet1']=-1
#test_x_with_date.loc[(test_x_with_date['f3']<=20),'bet1']=1
#
#test_x_with_date['bet1']=test_x_with_date['bet1'].fillna(method='ffill')
#test_x_with_date['bet']=test_x_with_date['bet1'].copy()
#del test_x_with_date['bet1']


#test_x_with_date.loc[(test_x_with_date['f1_temp']>=0.8),'bet1']=-1
#test_x_with_date.loc[(test_x_with_date['f1_temp']<=-0.8),'bet1']=1
#
#test_x_with_date['bet1']=test_x_with_date['bet1'].fillna(method='ffill')
#test_x_with_date['bet']=test_x_with_date['bet1'].copy()
#del test_x_with_date['bet1']




##version 2 -  e.g. less than 20, then long, higher than 20, it is 0 then close
#test_x_with_date.loc[(test_x_with_date['f3']>=80),'bet1']=-1
#test_x_with_date.loc[(test_x_with_date['f3']<=20),'bet1']=1
#
##test_x_with_date['bet1']=test_x_with_date['bet1'].fillna(method='ffill')
#test_x_with_date['bet1']=test_x_with_date['bet1'].fillna(0)
#test_x_with_date['bet']=test_x_with_date['bet1'].copy()
#
#del test_x_with_date['bet1']




##version 3  when arrive 50, flat position
#upper_t=80
#lower_t=20
#target='f3'
#test_x_with_date['bet1']=0
#
#i=1
#for i in np.arange(0,test_x_with_date.shape[0]):
#    indicator_now=test_x_with_date.loc[i,target]
#    if i == 0:
#        if indicator_now>=upper_t:
#            test_x_with_date.loc[i,'bet1']=-1
#        if indicator_now<=lower_t:
#            test_x_with_date.loc[i,'bet1']=1
#        current_signal=test_x_with_date.loc[i,'bet1']
#    if i >= 1:
#        indicator_last=test_x_with_date.loc[i-1,target]
#        if current_signal==0:
#            if indicator_now>=upper_t:
#                test_x_with_date.loc[i,'bet1']=-1
#            elif indicator_now<=lower_t:
#                test_x_with_date.loc[i,'bet1']=1
#            else:
#                test_x_with_date.loc[i,'bet1']=0
#            
#        if (current_signal==1):
#            if (indicator_now>=50)&(indicator_now<upper_t)&(indicator_last<50):
#                test_x_with_date.loc[i,'bet1']=0
#            elif (indicator_now>=upper_t):
#                test_x_with_date.loc[i,'bet1']=-1
#            else:
#                test_x_with_date.loc[i,'bet1']=1
#        if (current_signal==-1):
#            if (indicator_now<=50)&(indicator_now>lower_t)&(indicator_last>50):
#                test_x_with_date.loc[i,'bet1']=0
#            elif (indicator_now<=lower_t):
#                test_x_with_date.loc[i,'bet1']=1
#            else:
#                test_x_with_date.loc[i,'bet1']=-1
#                
#    current_signal=test_x_with_date.loc[i,'bet1']
#            
#
#test_x_with_date['bet']=test_x_with_date['bet1'].copy()
#
#del test_x_with_date['bet1']





##version 2, with stop loss
#test_x_with_date.loc[(test_x_with_date['f3']>=80),'bet1']=-1
#test_x_with_date.loc[(test_x_with_date['f3']<=20),'bet1']=1
#
#test_x_with_date['bet1']=test_x_with_date['bet1'].fillna(method='ffill')
#test_x_with_date['bet1']=test_x_with_date['bet1'].fillna(0)
#
#
#test_x_with_date['bet_change']=(test_x_with_date['bet1'].shift(1)!=test_x_with_date['bet1'])*1
#test_x_with_date.loc[test_x_with_date['bet_change']==0,'bet_change']=np.nan
#test_x_with_date['bet_stop']=np.nan
#
#side=0
#i=2
#for i in np.arange(0,test_x_with_date.shape[0]):
#    if (test_x_with_date.loc[i,'bet_change']==1)&(test_x_with_date.loc[i,'bet1']==1):
#        side=1
#        entry=test_x_with_date.loc[i,'Open_HSI']
#    if (test_x_with_date.loc[i,'bet_change']==1)&(test_x_with_date.loc[i,'bet1']==-1):
#        side=-1
#        entry=test_x_with_date.loc[i,'Open_HSI']
#    if side != 0:
#        profit=(test_x_with_date.loc[i,'Close_HSI']-entry)*side
#        if profit/entry<-0.05:
#            test_x_with_date.loc[i,'bet_stop']='yes'
#            side=0
#            
#
#test_x_with_date.loc[test_x_with_date['bet_change']==1,'bet_stop']=test_x_with_date['bet_change']
#test_x_with_date['bet_stop']=test_x_with_date['bet_stop'].fillna(method='ffill')
#test_x_with_date['bet_stop_shift1']=test_x_with_date['bet_stop'].shift(1)
#test_x_with_date.loc[(test_x_with_date['bet_stop']=='yes')&(test_x_with_date['bet_stop_shift1']=='yes'),'bet_stop_final']='yes'
#test_x_with_date.loc[test_x_with_date['bet_stop_final']=='yes','bet1']=0
#
#
#test_x_with_date['bet']=test_x_with_date['bet1'].copy()
#
#del test_x_with_date['bet1']



##version 3, normal with stop loss
#test_x_with_date['bet0']=test_x_with_date['bet'].copy()
#test_x_with_date['bet1']=test_x_with_date['bet'].copy()
#
#
#test_x_with_date['bet_change']=(test_x_with_date['bet1'].shift(1)!=test_x_with_date['bet1'])*1
#test_x_with_date.loc[test_x_with_date['bet_change']==0,'bet_change']=np.nan
#test_x_with_date['bet_stop']=np.nan
#
#side=0
#i=2
#for i in np.arange(0,test_x_with_date.shape[0]):
#    if (test_x_with_date.loc[i,'bet_change']==1)&(test_x_with_date.loc[i,'bet1']==1):
#        side=1
#        entry=test_x_with_date.loc[i,'Open_HSI']
#    if (test_x_with_date.loc[i,'bet_change']==1)&(test_x_with_date.loc[i,'bet1']==-1):
#        side=-1
#        entry=test_x_with_date.loc[i,'Open_HSI']
#    if side != 0:
#        profit=(test_x_with_date.loc[i,'Close_HSI']-entry)*side
#        if profit/entry<-0.01:
#            test_x_with_date.loc[i,'bet_stop']='yes'
#            side=0
#            
#
#test_x_with_date.loc[test_x_with_date['bet_change']==1,'bet_stop']=test_x_with_date['bet_change']
#test_x_with_date['bet_stop']=test_x_with_date['bet_stop'].fillna(method='ffill')
#test_x_with_date['bet_stop_shift1']=test_x_with_date['bet_stop'].shift(1)
#test_x_with_date.loc[(test_x_with_date['bet_stop']=='yes')&(test_x_with_date['bet_stop_shift1']=='yes'),'bet_stop_final']='yes'
#test_x_with_date.loc[test_x_with_date['bet_stop_final']=='yes','bet1']=0
#
#
#test_x_with_date['bet']=test_x_with_date['bet1'].copy()
#
#del test_x_with_date['bet1']











#find last row day in testing
test_x_with_date_last=test_x_with_date.tail(1)
test_x_with_date_last_date=test_x_with_date_last.Date2.values[0]

#find last trading date in calendar by year
calendar['Date2']=calendar['Date'].astype(str)
calendar=calendar.loc[calendar['trading_date']==1,:]
calendar['year']=calendar['Date2'].str[0:4]
calendar=calendar.reset_index(drop=True)
all_last_trading_date=list(calendar.groupby(['year']).tail(1).Date2.values)


if int(test_start[0:4])<2021:
    test_x_with_date_last['islast']=1
else:
    if test_x_with_date_last_date in all_last_trading_date:
        test_x_with_date_last['islast']=1
    else:
        test_x_with_date_last['islast']=0
        
    
test_x_with_date=pd.merge(test_x_with_date,test_x_with_date_last[['Date2','islast']].copy(),how='left',on=['Date2'])


test_x_with_date_temp=test_x_with_date.copy()

i=0

test_x_with_date_temp['up_entry']=np.NaN
test_x_with_date_temp['up_exit']=np.NaN
test_x_with_date_temp['down_entry']=np.NaN
test_x_with_date_temp['down_exit']=np.NaN
have_position=0

for i in range(0,test_x_with_date_temp.shape[0]):
    if have_position==0:
        if (test_x_with_date['bet'][i]==1):
            test_x_with_date_temp.iloc[i,test_x_with_date_temp.columns.get_loc('up_entry')]=test_x_with_date_temp['Open_HSI'].values[i]
            have_position=1                
        if (test_x_with_date['bet'][i]==-1):
            test_x_with_date_temp.iloc[i,test_x_with_date_temp.columns.get_loc('down_entry')]=test_x_with_date_temp['Open_HSI'].values[i]
            have_position=-1                
            
    if have_position==1:
        if (test_x_with_date['bet'][i]==0):
            test_x_with_date_temp.iloc[i,test_x_with_date_temp.columns.get_loc('up_exit')]=test_x_with_date_temp['Open_HSI'].values[i]
            have_position=0
        if (test_x_with_date['bet'][i]==-1):
            test_x_with_date_temp.iloc[i,test_x_with_date_temp.columns.get_loc('up_exit')]=test_x_with_date_temp['Open_HSI'].values[i]
            test_x_with_date_temp.iloc[i,test_x_with_date_temp.columns.get_loc('down_entry')]=test_x_with_date_temp['Open_HSI'].values[i]
            have_position=-1
            
    if have_position==-1:
        if (test_x_with_date['bet'][i]==0):
            test_x_with_date_temp.iloc[i,test_x_with_date_temp.columns.get_loc('down_exit')]=test_x_with_date_temp['Open_HSI'].values[i]
            have_position=0
        if (test_x_with_date['bet'][i]==1):
            test_x_with_date_temp.iloc[i,test_x_with_date_temp.columns.get_loc('down_exit')]=test_x_with_date_temp['Open_HSI'].values[i]
            test_x_with_date_temp.iloc[i,test_x_with_date_temp.columns.get_loc('up_entry')]=test_x_with_date_temp['Open_HSI'].values[i]
            have_position=1 
            

    if (test_x_with_date_temp.islast.values[i]==1)|(test_x_with_date_temp.islast.values[i]==0):
        if have_position==1:
            test_x_with_date_temp.iloc[i,test_x_with_date_temp.columns.get_loc('up_exit')]=test_x_with_date_temp['Close_HSI'].values[i]
        if have_position==-1:
            test_x_with_date_temp.iloc[i,test_x_with_date_temp.columns.get_loc('down_exit')]=test_x_with_date_temp['Close_HSI'].values[i]
        have_position=0
    



out_temp=test_x_with_date_temp.copy()
s1='down_entry'
s2='down_exit'
up_or_down=1


def convert_signal(out_temp,s1,s2,up_or_down):
    today_close=out_temp.Close_HSI.values[-1]   #exit at last's row's close
    today_close_time=out_temp.Date2.values[-1]
    out_temp_up_entry=out_temp[['Date2',s1]].copy()
    out_temp_up_entry=out_temp_up_entry.rename(columns={'Date2':'entry_time',s1:'entry_price'})
    out_temp_up_entry=out_temp_up_entry.loc[~(pd.isnull(out_temp_up_entry['entry_price'])),:]
    out_temp_up_entry=out_temp_up_entry.reset_index(drop=True)
    
    if out_temp_up_entry.shape[0]!=0:

        out_temp_up_exit=out_temp[['Date2',s2]].copy()
        out_temp_up_exit=out_temp_up_exit.rename(columns={'Date2':'exit_time',s2:'exit_price'})
        out_temp_up_exit=out_temp_up_exit.loc[~(pd.isnull(out_temp_up_exit['exit_price'])),:]
        out_temp_up_exit=out_temp_up_exit.reset_index(drop=True)
        out_temp_up=pd.concat([out_temp_up_entry,out_temp_up_exit],axis=1) #concat colume
            
        out_temp_up['bet']=up_or_down
        print('finished ',today_close_time )        
    else:
        out_temp_up=pd.DataFrame([])
    return out_temp_up




test_x_with_date_temp1=convert_signal(test_x_with_date_temp,'up_entry','up_exit',1)
test_x_with_date_temp2=convert_signal(test_x_with_date_temp,'down_entry','down_exit',-1)

test_x_with_date_converted=test_x_with_date_temp1.append(test_x_with_date_temp2)
test_x_with_date_converted=test_x_with_date_converted.reset_index(drop=True)

#if islast=0 (so it is for any date not the last trading day as last row record) 
#and appear in exit time, but bet equal to previous one record, remove it in test_x_with_date_converted
if sum(test_x_with_date['islast']==0)==1:
    dd=test_x_with_date[test_x_with_date['islast']==0]['Date2'].values[0]
    target_index=test_x_with_date[test_x_with_date.Date2==dd].index[0]
    if target_index > 0:
        if test_x_with_date.bet.values[target_index]==test_x_with_date.bet.values[target_index-1]:
            test_x_with_date_converted=test_x_with_date_converted.loc[test_x_with_date_converted['exit_time']!=dd,:].copy()





#create used factor table
use_factor=[i.replace('_change','') for i in use_factor_list]
use_factor=[i.replace('EMA_','') for i in use_factor]
use_factor.remove('Date2')
#i='GSPC_interact_GDAXI'
#use_factor_type=[data.loc[data['Name_use_python']==i,'Type'].reset_index(drop=True)[0] for i in use_factor]
use_factor='balancepower_up'

use_factor_type=[]
for i in use_factor:
    try:
        use_factor_type.append(data.loc[data['Name_use_python']==i,'Type'].reset_index(drop=True)[0])
    except:
        use_factor_type.append('MayBeInteraction')


use_factor_df=pd.DataFrame({'type':use_factor_type,'factor':use_factor})
use_factor_df=use_factor_df.sort_values(by='type',ascending=True).reset_index(drop=True)
use_factor_df.insert(0,'Type',use_factor_df.type)
del use_factor_df['type']





stat_output=pd.DataFrame([])    
if test_x_with_date_converted.shape[0]!=0:

    #if have new signal at last row of testing data remove it, coz hard to handle
    test_x_with_date_converted=pd.merge(test_x_with_date_converted,test_x_with_date_temp[['Date2','islast']].copy(),how='left',left_on=['entry_time'],right_on=['Date2'])
    #test_x_with_date_converted=test_x_with_date_converted.loc[pd.isnull(test_x_with_date_converted['islast']),:].copy()
    
    d_temp=test_x_with_date[['Date2','High_HSI','Low_HSI']].copy()

    
    #find high and low between entry and exit
    data3=test_x_with_date_converted.loc[(test_x_with_date_converted['entry_time']=='2022-02-21'),:].copy()
    
    d='2022-02-21'

    def find_max_min(data3):
        data_index=data3.index
        d=data3.entry_time.values[0]
        t1=data3.entry_time.values[0]
        t2=data3.exit_time.values[0]
        
        if pd.isnull(data3['islast'].values[0]):
            d_temp_use=d_temp.loc[(d_temp['Date2']>=t1)&(d_temp['Date2']<t2),:].copy()
        else:
            d_temp_use=d_temp.loc[d_temp['Date2']==t1,:].copy()
        
        High_group=d_temp_use.High_HSI.max()
        Low_group=d_temp_use.Low_HSI.min()
        output=pd.DataFrame({'High_group':[High_group],'Low_group':[Low_group]},index=data_index)
        print(d,' ',t1,' ',t2)
        return output
    
    temp=test_x_with_date_converted.groupby(['entry_time']).apply(lambda x:find_max_min(x))
    
    test_x_with_date_converted=pd.concat([test_x_with_date_converted,temp],axis=1)
    
    test_x_with_date_converted=test_x_with_date_converted.sort_values(by=['entry_time'],ascending=[True])
    test_x_with_date_converted=test_x_with_date_converted.reset_index(drop=True)
    
    

    
    #create bet indicator to indicator betting or not
    
    commission=0  #divide by 10
    
    test_x_with_date_converted['open_low_diff']=test_x_with_date_converted['entry_price']-test_x_with_date_converted['Low_group']
    test_x_with_date_converted['high_open_diff']=test_x_with_date_converted['High_group']-test_x_with_date_converted['entry_price']
    
    
    test_x_with_date_converted['close_open_diff']=test_x_with_date_converted['exit_price']-test_x_with_date_converted['entry_price']
    
    
    test_x_with_date_converted['PnL_original']=test_x_with_date_converted['bet']*test_x_with_date_converted['close_open_diff']
    test_x_with_date_converted['Cum.Sum_original']=test_x_with_date_converted['PnL_original'].cumsum()
    
    

    test_x_with_date_converted['PnL']=test_x_with_date_converted['PnL_original'].copy()
    test_x_with_date_converted['stop_level']=test_x_with_date_converted['entry_price']*stoploss_use
    
    if test_mode=='n225':
        test_x_with_date['stop_level']=test_x_with_date['stop_level'].apply(lambda x: round(x,-1))
    


    if stoploss_use>1:
        cap_loss=stoploss_use
        test_x_with_date_converted.loc[(test_x_with_date_converted['open_low_diff']>=cap_loss)&(test_x_with_date_converted['bet']==1),'PnL']=-1*cap_loss
        test_x_with_date_converted.loc[(test_x_with_date_converted['high_open_diff']>=cap_loss)&(test_x_with_date_converted['bet']==-1),'PnL']=-1*cap_loss
    else:
        test_x_with_date_converted.loc[(test_x_with_date_converted['open_low_diff']>=test_x_with_date_converted['stop_level'])&(test_x_with_date_converted['bet']==1),'PnL']=-1*test_x_with_date_converted['stop_level']
        test_x_with_date_converted.loc[(test_x_with_date_converted['high_open_diff']>=test_x_with_date_converted['stop_level'])&(test_x_with_date_converted['bet']==-1),'PnL']=-1*test_x_with_date_converted['stop_level']      
    
    
    test_x_with_date_converted.loc[test_x_with_date_converted['bet']==0,'PnL']=0
    
    test_x_with_date_converted['Cum.Sum']=test_x_with_date_converted['PnL'].cumsum()
    
    #pnl long side and short side
    pnl_long=10*sum(test_x_with_date_converted.loc[test_x_with_date_converted['bet']==1,'PnL'].values)
    pnl_short=10*sum(test_x_with_date_converted.loc[test_x_with_date_converted['bet']==-1,'PnL'].values)
    



    
    total_bets=test_x_with_date_converted.shape[0]
    total_up_bets=sum(test_x_with_date_converted['bet']==1)
    total_up_bets_ratio=total_up_bets/total_bets
    real_accuracy=test_x_with_date_converted[test_x_with_date_converted['PnL']>=0].shape[0]/total_bets
    

    #find drawdown
    drawdown=max(np.maximum.accumulate(test_x_with_date_converted['Cum.Sum']*10)-test_x_with_date_converted['Cum.Sum']*10)
    
    if "@" in test_mode:
        test_x_with_date_converted=pd.merge(test_x_with_date_converted,hsi_y_x[['Date2','cost_pair_trade']].copy(),how='left',left_on=['entry_time'],right_on=['Date2'])        
        capital_assumption=max(test_x_with_date_converted.cost_pair_trade.values)*10/3+drawdown*1.3  #margin is 6, but here just use 4
    else:
        try:
            test_x_with_date_converted=pd.merge(test_x_with_date_converted,hsi_y_x[['Date2','open']].copy(),how='left',left_on=['entry_time'],right_on=['Date2'])
            capital_assumption=max(test_x_with_date_converted.open.values)*10*0.7+drawdown*1.5
        except:
            hsi_y_x=pd.merge(hsi_y_x,HSI_source[['Date2','Open_HSI']].copy(),how='left')
            test_x_with_date_converted=pd.merge(test_x_with_date_converted,hsi_y_x[['Date2','Open_HSI']].copy(),how='left',left_on=['entry_time'],right_on=['Date2'])
            capital_assumption=max(test_x_with_date_converted.Open_HSI.values)*10*0.7+drawdown*1.5
            
        

    del test_x_with_date_converted['Date2_y']
    test_x_with_date_converted=test_x_with_date_converted.rename(columns={'Date2_x':'Date2'})
    
    print('Real accuracy '+str("{:.2%}".format(real_accuracy))+'\n')
    print('PnL is '+str(int(sum(test_x_with_date_converted['PnL'])))+'points <=> HKD'+str(int(sum(test_x_with_date_converted['PnL']))*10)+'\n')
    #'Assume buy 1 small FHSI with deposit HKD19000, return is '+str("{:.2%}".format(sum(test_x_with_date_converted['PnL'])*10/19000))+'\n'
    print('Max cumulative loss is '+str(int(min(test_x_with_date_converted['Cum.Sum'])))+'points <=> HKD '+str(int(min(test_x_with_date_converted['Cum.Sum'])*10))+'\n')
    print('drawdown is '+str(drawdown))
    print('count_number_sample_selected '+str('xxxx')+ ' train_down_ratio '+str('xxx'))
                    
    
    

    
    
    
    from pylab import *
    plt.figure(figsize=(10,4), dpi=80, facecolor='w', edgecolor='k')
    
    plt.plot(range(0,test_x_with_date_converted.shape[0]),test_x_with_date_converted['Cum.Sum']*10,'*', color='r')
    plt.legend(loc='best')
    plt.xlabel('time')
    plt.ylabel('cumulative pnl')
    plt.title('Cum.pnl')
    
    
    figtext(.02, -0.5,'run number '+str(NumberRun)+'. Asset is '+test_mode+'\n'+  
            'Test Start:'+test_start+' Test End: '+test_end+'\n'+
            'Train Start:'+train_start+' Train End: '+train_end+'\n'+
            'Total PnL is HKD '+str(int(sum(test_x_with_date_converted['PnL']))*10)+'\n'+
            'drawdown is '+str(drawdown)+'\n'+
            'Max cum loss is '+str(int(min(test_x_with_date_converted['Cum.Sum'])*10))+'\n'+
            'real_accuracy '+str(real_accuracy)+'\n'+
            'total_bets '+str(total_bets)+'\n'+
            'count_number_sample_selected (last valid run only)'+str(99999999)+'\n'+
            'run_message: '+'Tried to run xxx'+'\n'+
            'in training sample, train_up_ratio '+str(99999999)+' train_down_ratio '+str(9999)+'\n'+
            'model point up prob '+str(99999999)+' count_total_sample '+str(9999999)+'\n'+
            'test fitted up '+str(total_up_bets_ratio)+' test fitted down '+str(1-total_up_bets_ratio),
            fontsize='large')
    
    
    
    
    
    file_name_plot=os.path.join(main_folder,str(NumberRun)+'_test_pnl_'+year_test+'_plot_aggregate.png')
    #file_name_plot=os.path.join(r'C:\Users\jonathanjames\aws\notebooks\index_analysis\check_diff',str(NumberRun)+'_test_'+year_test+'_plot.png')
    
    plt.savefig(file_name_plot,bbox_inches="tight")
    
    
    
    
    

    
    
    
    #summary statistics
    from collections import OrderedDict
    stat_output=pd.DataFrame(OrderedDict({'NumberRun':NumberRun,
                              'Test_Year':test_start[0:4],
                              'PnL':int(sum(test_x_with_date_converted['PnL'])*10),
                              'Return':float(sum(test_x_with_date_converted['PnL'])*10/capital_assumption),
                              'Real accuracy':float(real_accuracy),
                              'Max cumulative loss':str(int(min(test_x_with_date_converted['Cum.Sum'])*10)),
                              'drawdown':str(drawdown),
                              '% of up (fitted) in training sample':str("{:.2%}".format(99999)),
                              '% of down (fitted) in training sample':str("{:.2%}".format(99999)),
                              '% of up in training sample':str("{:.2%}".format(99999)),
                              '% of down in training sample':str("{:.2%}".format(99999)),
                              '% of up (fitted) in testing sample':str("{:.2%}".format(99999)),
                              '% of down (fitted) in testing sample':str("{:.2%}".format(99999)),
                              '% of up in testing sample':str("{:.2%}".format(99999)),
                              '% of down in testing sample':str("{:.2%}".format(99999)),
                              'real_accuracy_after_using_prob_filter':float(9999),
                              'long pnl':float(pnl_long),
                              'short pnl':float(pnl_short),
                              'total_bets':int(total_bets),
                              'total_up_bets_ratio':float(total_up_bets_ratio),
                              'train_up_ratio':float(999999),
                              'model_point_up_prob':float(9999999),
                              'run_message':'Tried to run '+str(9999999),
                              'test_mode':test_mode
                              },index=[0]))
    del stat_output['index']
    

    
    
file_name=os.path.join(main_folder,str(NumberRun)+'_test_'+year_test+'.xlsx')
writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
use_factor_df.to_excel(writer, sheet_name='factor')
stat_output.to_excel(writer, sheet_name='pnl_summary_aggregate')
stat_output.to_excel(writer, sheet_name='pnl_summary')
test_x_with_date_converted.to_excel(writer, sheet_name='daily_detail_summary_aggregate')
test_x_with_date.to_excel(writer, sheet_name='daily_detail_summary')    

writer.save()
writer.close()
    
    
print('total_running time is '+str(round(time.time()-time_start,2))+' seconds')













sys.stderr.close()
sys.stderr = sys.__stderr__










dash_example_data_processing_window.py









#example 4
from dash import Dash, dcc, html, Input, Output,dash_table
import plotly.express as px
import dash_bootstrap_components as dbc


from dash.dash_table.Format import Format, Padding
from dash.dash_table.Format import Format, Scheme, Trim

import subprocess
import os
import time

notebook_path=r'C:\Users\jonathanjames\aws\notebooks'
#notebook_path='/home/jonathanjames/aws/notebooks'

#redirect or copy log to this file
#text_file='/home/jonathanjames/aws/notebooks/materials-python-dash/dash_example/target_log/temp_log.log'
#text_file=os.path.join(notebook_path,'materials-python-dash','dash_example','target_log','temp_log.log')
text_file=os.path.join(notebook_path,'index_analysis','log','stan_out_mindata_temp.log') #hsi min production log


#check encoding of txt file
from bs4 import UnicodeDammit
with open(text_file, 'rb') as file:
   content = file.read()

suggestion = UnicodeDammit(content)
txt_encoding=suggestion.original_encoding




s_path=os.path.join(notebook_path,'materials-python-dash','dash_example','assets2')

#if want dbc.col placed horizontally, need to use a bootstrap sheet like dbc.themes.BOOTSTRAP, otherwise everything place vertically
#but if use external_stylesheets, margin may have predefined, so it would be different from original so need to recalibrate margin of some items.
app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],assets_folder=s_path)
#app = Dash(__name__,assets_folder=s_path)



app.layout = dbc.Container(
    [
        html.Div([html.P(children="🥑 🐎", style={"font-size": "30px","margin": "0 auto","text-align": "center","color":"Lime"}),
                      html.H1(children="Avocado Analytics",style={"fontSize": "40px", "color": "white","font-weight": "bold",
                                                                  "text-align": "center","margin": "0px auto"}),
                      html.P(children="Analyze the behavior of avocado prices and the number of avocados sold in the US between 2015 and 2018",
                             style={"fontSize": "17px", "color": "white","text-align": "center","max-width": "384px","margin": "1px auto"}
                       ),
                     ],
            #"margin": "auto" is to center this div box
            style={"background-color": "#222222","height": "170px","width": "1088px","padding": "0px 0 0 0",
                   "margin-top":"20px","margin-left":"120px"},  #margin-top is to move down div box a bit
        ),
        html.Br(),
        dbc.Row([
                dbc.Col([
#                        html.Div([html.Button('Main', id='apply-button1', n_clicks=0,
#                                              style={'font-size': '15px', 'width': '110px',
#                                                     'display': 'inline-block', 'margin-bottom': '0px',
#                                                     'margin-right': '0px', 'height':'37px', 'verticalAlign': 'top'}
#                                              ),html.Div(id='output-container-button1',style={"color": "yellow"})]),#id='output-container-button1' return the output after clicking this button
#                        html.Br(),
#                        html.Div([html.Button('Back Up', id='apply-button2', n_clicks=0,
#                                              style={'font-size': '15px', 'width': '110px',
#                                                     'display': 'inline-block', 'margin-bottom': '0px',
#                                                     'margin-right': '0px', 'height':'37px', 'verticalAlign': 'top'}
#                                              ),html.Div(id='output-container-button2',style={"color": "yellow"})]),
#                        html.Br(),
#                        html.Div([html.Button('Kill aws', id='apply-button3', n_clicks=0,
#                                              style={'font-size': '15px', 'width': '110px',
#                                                     'display': 'inline-block', 'margin-bottom': '0px',
#                                                     'margin-right': '0px', 'height':'37px', 'verticalAlign': 'top'}
#                                              ),html.Div(id='output-container-button3',style={"color": "yellow"})]),
                        ],
                        width={"size": 1, "order": 1, "offset": 0},
                        style={'margin-right': '10px', 'margin-left': '0px'}
                        ),
                dbc.Col([html.Div([html.Div(id="live-update-text"),
                                   dcc.Interval(id='interval-component',interval=2*1000,n_intervals=0), # 2 is refresh per 2s
                                   ],
                                   style={"color":"black","background-color": "#F5F9F9",
                                          "height": "600px","width": "1088px",
                                          "margin": "auto","box-shadow": "0 4px 6px 0 rgba(248, 245, 246, 0.8)",
                                          "overflow-y": "scroll",'overflow-x':'scroll'},
                                   #id="scroll-div",
                                 )
                        ], 
                         width={"size": 1, "order": 2, "offset": 0},
                         ), 
        
            ]
        ),

    ]
)








@app.callback(Output('live-update-text', 'children'),
              Input('interval-component', 'n_intervals'))
def update_metrics(n):
    #ok if txt is in window
    with open(text_file,'r',encoding=txt_encoding) as f:
        lines = f.readlines()      
        
    line2=[]
    if len(lines)>0:
        for x in lines:
            line2.append(x)
            line2.append(html.Br())  #this is line break

    
    return [html.P(line2)]        

    
#output will be stored in output-container-button1 
@app.callback(Output('output-container-button1', 'children'),
              Input('apply-button1', 'n_clicks'))
def run_script_onClick1(n_clicks):
    #print('[DEBUG] n_clicks:', n_clicks)
    if not n_clicks:                        #when first time run this script, n_clicks=0, so need to perform no action
        #raise dash.exceptions.PreventUpdate
        return dash.no_update
    # without `shell` it needs list ['/full/path/python', 'script.py']           
    #result = subprocess.check_output( ['/usr/bin/python', 'script.py'] )  
    # with `shell` it needs string 'python script.py'
    result = subprocess.check_output('/root/anaconda3/envs/old1/bin/python /home/jonathanjames/aws/notebooks/index_analysis/main.py > /home/jonathanjames/aws/notebooks/materials-python-dash/dash_example/target_log/temp_log.log 2>&1 &', shell=True)  
    # convert bytes to string
    #result = result.decode()  
    result='Executed'
    return result
    
    
@app.callback(Output('output-container-button2', 'children'),
              Input('apply-button2', 'n_clicks'))
def run_script_onClick2(n_clicks):
    if not n_clicks:
        return dash.no_update
    result = subprocess.check_output("(sh /home/jonathanjames/aws/notebooks/linux/backup_importance.sh 2>&1 &)|tee /home/jonathanjames/aws/notebooks/linux/log/backup_importance_$(date +'%Y%m%d'_'%H%M%S').log /home/jonathanjames/aws/notebooks/materials-python-dash/dash_example/target_log/temp_log.log > /dev/null", shell=True)
    result='Executed'
    return result
    
@app.callback(Output('output-container-button3', 'children'),
              Input('apply-button3', 'n_clicks'))
def run_script_onClick3(n_clicks):
    if not n_clicks:
        return dash.no_update
    result = subprocess.check_output("kill $(ps -u jonathanjames | grep 'aws' | awk '{print $1}')", shell=True)  
    result='Executed'
    return result


from pandas import read_excel
today_day=time.strftime("%Y-%m-%d")
calendar = read_excel(r'C:\Users\jonathanjames\aws\notebooks\index_analysis\daily_prediction_production\calendar.xlsx','calendar')
calendar['Date2']=calendar['Date'].astype(str)
calendar=calendar.loc[calendar['trading_date']==1,:]
calendar=calendar.reset_index(drop=True)



if sum(calendar['Date2'].isin([today_day]))==0:
    exit()


if __name__ == "__main__":
    app.run_server()






#if __name__ == "__main__":
#    if sum(calendar['Date2'].isin([today_day]))==1:
#        app.run_server()
#    else:
#        print(today_day+' is not trading date',flush=True)

#if __name__ == "__main__":
#    app.run_server(use_reloader=False)








app.py


"""

import dash
from dash import Dash,html,dcc, Input, Output, callback, dash_table


dash.__version__


import pandas as pd
import numpy as np
import os

import datetime 
from datetime import datetime as dt

#https://realpython.com/python-dash/


###########################################################install dash#############################################################
#./pip3 install dash==2.8.1
#./pip3 install dash_bootstrap_components
# /root/anaconda3/bin/python /home/jonathanjames/aws/notebooks/dash_example.py



os.chdir("/home/jonathanjames/aws/notebooks/materials-python-dash/apps/app_4")

#specify css file folder
assets_path = os.getcwd() +'/assets_original'





# mother_path='/home/jonathanjames/aws/notebooks/materials-python-dash/apps/app_4'
# file_path=os.path.join(mother_path,"avocado.csv")

data = pd.read_csv("avocado.csv")


#data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data["Date"]=data["Date"].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
data.sort_values("Date", inplace=True)


#this is only for a new font style
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=external_stylesheets,assets_folder=assets_path)
#app = Dash(__name__,assets_folder=assets_path)




server = app.server
app.title = "Avocado Analytics: Understand Your Avocados!"

#this is the icon use in the left of the page tag in the browser
app._favicon = ("1f004.png")


app.layout = html.Div(
    children=[
        #this div is header block division with black color specify in css file className="header"
        html.Div(
            children=[html.P(children="🥑 🐎", className="header-emoji"),  #paragraph
                      html.H1(children="Avocado Analytics", className="header-title"),
                      html.P(children="Analyze the behavior of avocado prices and the number of avocados sold in the US between 2015 and 2018",
                       className="header-description",
                       ),
                     ],
            className="header",
        ),
        #this block contain 3 dropdown menu (region, type, date)
        html.Div(
            children=[
                        html.Div(
                            children=[
                                html.Div(children="Region", className="menu-title"),
                                dcc.Dropdown(
                                    id="region-filter",
                                    options=[
                                        {"label": region, "value": region}  #after user picking, value is stored at variable 'value'
                                        for region in np.sort(data.region.unique())
                                    ],
                                    value="Albany",
                                    clearable=False,
                                    className="dropdown",
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Div(children="Type", className="menu-title"),
                                dcc.Dropdown(
                                    id="type-filter",
                                    options=[
                                        {"label": avocado_type, "value": avocado_type}
                                        for avocado_type in data.type.unique()
                                    ],
                                    value="organic",
                                    clearable=False,
                                    searchable=False,
                                    className="dropdown",
                                ),
                            ],
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data.Date.min().date(),
                                    max_date_allowed=data.Date.max().date(),
                                    start_date=data.Date.min().date(),
                                    end_date=data.Date.max().date(),
                                ),
                            ]
                        ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                        html.Div(
                            children=dcc.Graph(
                                id="price-chart",
                                config={"displayModeBar": False},
                            ),
                            className="card",
                        ),
                        html.Div(
                            children=dcc.Graph(
                                id="volume-chart",
                                config={"displayModeBar": False},
                            ),
                            className="card",
                        ),
            ],
            className="wrapper",
        ),
    ]
)


@app.callback(
    [Output("price-chart", "figure"), Output("volume-chart", "figure")],
    [Input("region-filter", "value"),
     Input("type-filter", "value"),
     Input("date-range", "start_date"),
     Input("date-range", "end_date"),
    ],
)

def update_charts(region, avocado_type, start_date, end_date):
    region=region.replace('999','')
    mask = (
        (data.region == region)
        & (data.type == avocado_type)
        & (data.Date >= start_date)
        & (data.Date <= end_date)
    )
    filtered_data = data.loc[mask, :]
    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["AveragePrice"],
                "type": "lines",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {"text": '<span style="font-size: 18px;font-weight: bold;">Average Price of Avocados</span>',
                      "x": 0.05, #text position from left
                      "xanchor": "left",
                     },
            "xaxis": {"fixedrange": True, "tickfont":dict(size=15)},
            "yaxis": {"tickprefix": "$", "fixedrange": True, "tickfont":dict(size=15)},
            "colorway": ["#17B897"],
        },
    }

    volume_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Total Volume"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {"text": '<span style="font-size: 18px;font-weight: bold;">Avocados Sold</span>',
                      "x": 0.05,
                      "xanchor": "left"
                      },
            "xaxis": {"fixedrange": True, "tickfont":dict(size=15)},
            "yaxis": {"fixedrange": True, "tickfont":dict(size=15),"tickformat":".0%"},  #use %
            "colorway": ["#E12D39"],
        },
    }
    return price_chart_figure, volume_chart_figure


if __name__ == "__main__":
    #app.run_server(debug=True)  #access in local computer
    app.run_server(host='0.0.0.0',debug=True)  #also access by LAN computer http://192.168.3.216:8050/
    
    
    

    
    
    
#for deployment install heroku
#curl https://cli-assets.heroku.com/install.sh | sh
    
#/home/jonathanjames/aws/notebooks/materials-python-dash/apps/app_4
    
    

"""
    
    





    
    
    
    
    
    
    
    
    
    
    

    
import dash
from dash import Dash,html,dcc, Input, Output, callback, dash_table


dash.__version__


import pandas as pd
import numpy as np
import os

import datetime 
from datetime import datetime as dt



import dash_bootstrap_components as dbc
import plotly.express as px


#https://realpython.com/python-dash/


###########################################################install dash#############################################################
#./pip3 install dash==1.20.0
# /root/anaconda3/bin/python /home/jonathanjames/aws/notebooks/dash_example.py



os.chdir("/home/jonathanjames/aws/notebooks/materials-python-dash/apps/app_4")

#specify css file folder
assets_path = os.getcwd() +'/assets_use'





# mother_path='/home/jonathanjames/aws/notebooks/materials-python-dash/apps/app_4'
# file_path=os.path.join(mother_path,"avocado.csv")

data = pd.read_csv("avocado.csv")


#data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data["Date"]=data["Date"].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
data.sort_values("Date", inplace=True)


#this is only for a new font style
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=external_stylesheets,assets_folder=assets_path)
#app = Dash(__name__,assets_folder=assets_path)




server = app.server
app.title = "Avocado Analytics: Understand Your Avocados!"

#this is the icon use in the left of the page tag in the browser
app._favicon = ("1f004.png")


vv='all'
def make_figures(vv):
    use_data=data.copy() if vv=='all' else data[data['type']==vv].copy()
    fig=px.scatter(
            use_data,
            x="Date",
            y="AveragePrice",
            size="Total Volume",
            color="type",
            hover_name="region",
            animation_frame="year",
            #animation_group="type",
            log_x=False,
            size_max=10,
            title="xxx name",
            #template='plotly',
        )
    #when year 2016, switch x axis to [dt(2016,1,1),dt(2016,1,1)]
    xranges = {}
    for i in list(data.year.unique()):
        xranges.update({i:[dt(i,1,1),dt(i,12,31)]})
    
    for f in fig.frames:
        if int(f.name) in xranges.keys():
            f.layout.update(xaxis_range = xranges[int(f.name)])    
    
    graph2 = dcc.Graph(figure=fig)

    return [dbc.Row([dbc.Col(graph2, lg=6)])]





app.layout = html.Div(
    children=[
        #this div is header block division with black color specify in css file className="header"
        html.Div(
            children=[html.P(children="🥑 🐎", className="header-emoji"),  #paragraph
                      html.H1(children="Avocado Analytics", className="header-title"),
                      html.P(children="Analyze the behavior of avocado prices and the number of avocados sold in the US between 2015 and 2018",
                       className="header-description",
                       ),
                     ],
            className="header",
        ),

        html.Div(
            children=[
                        html.Div(
                            children=[
                                html.Div(children="abc", className="menu-title0"),
                                dcc.Dropdown(
                                    id="type-filter0",
                                    options=[{"label": 'all', "value": 'all'}]+[{"label": tt, "value": tt} for tt in np.sort(data.type.unique())],
                                    value="all",
                                    clearable=False,
                                    className="dropdown",
                                ),
                            ]
                        ),
            ],
            className="menu0",
        ),
        html.Br(),
        html.Br(),
        html.Div(id="px-chart"),
        
        #this block contain 3 dropdown menu (region, type, date)
        html.Div(
            children=[
                        html.Div(
                            children=[
                                html.Div(children="Region", className="menu-title"),
                                dcc.Dropdown(
                                    id="region-filter",
                                    options=[
                                        {"label": region, "value": region}  #after user picking, value is stored at variable 'value'
                                        for region in np.sort(data.region.unique())
                                    ],
                                    value="Albany",
                                    clearable=False,
                                    className="dropdown",
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Div(children="Type", className="menu-title"),
                                dcc.Dropdown(
                                    id="type-filter",
                                    options=[
                                        {"label": avocado_type, "value": avocado_type}
                                        for avocado_type in data.type.unique()
                                    ],
                                    value="organic",
                                    clearable=False,
                                    searchable=False,
                                    className="dropdown",
                                ),
                            ],
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    children="Date Range", className="menu-title"
                                ),
                                dcc.DatePickerRange(
                                    id="date-range",
                                    min_date_allowed=data.Date.min().date(),
                                    max_date_allowed=data.Date.max().date(),
                                    start_date=data.Date.min().date(),
                                    end_date=data.Date.max().date(),
                                ),
                            ]
                        ),
            ],
            className="menu2",
        ),
        html.Div(
            children=[
                        html.Div(
                            children=dcc.Graph(
                                id="price-chart",
                                config={"displayModeBar": False},
                            ),
                            className="card",
                        ),
                        html.Div(
                            children=dcc.Graph(
                                id="volume-chart",
                                config={"displayModeBar": False},
                            ),
                            className="card",
                        ),
            ],
            className="wrapper",
        ),
    ]
)











@app.callback(
    [Output("price-chart", "figure"), Output("volume-chart", "figure"), Output("px-chart", "children")],
    [Input("region-filter", "value"),
     Input("type-filter", "value"),
     Input("date-range", "start_date"),
     Input("date-range", "end_date"),
     Input("type-filter0", "value"),
    ],
)

def update_charts(region, avocado_type, start_date, end_date,vv):
    region=region.replace('999','')
    mask = (
        (data.region == region)
        & (data.type == avocado_type)
        & (data.Date >= start_date)
        & (data.Date <= end_date)
    )
    filtered_data = data.loc[mask, :]
    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["AveragePrice"],
                "type": "lines",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {"text": '<span style="font-size: 18px;font-weight: bold;">Average Price of Avocados</span>',
                      "x": 0.05, #text position from left
                      "xanchor": "left",
                     },
            "xaxis": {"fixedrange": True, "tickfont":dict(size=15)},
            "yaxis": {"tickprefix": "$", "fixedrange": True, "tickfont":dict(size=15)},
            "colorway": ["#17B897"],
        },
    }

    volume_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Total Volume"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {"text": '<span style="font-size: 18px;font-weight: bold;">Avocados Sold</span>',
                      "x": 0.05,
                      "xanchor": "left"
                      },
            "xaxis": {"fixedrange": True, "tickfont":dict(size=15)},
            "yaxis": {"fixedrange": True, "tickfont":dict(size=15),"tickformat":".0%"},  #use %
            "colorway": ["#E12D39"],
        },
    }
    return price_chart_figure, volume_chart_figure, make_figures(vv)


if __name__ == "__main__":
    #app.run_server(debug=True)  #access in local computer
    app.run_server(host='0.0.0.0',debug=True)  #also access by LAN computer http://192.168.3.216:8050/
    


















#read a txt file and refresh it per 2s
import dash_core_components as dcc 
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output,dash_table


text_file='/home/jonathanjames/aws/notebooks/materials-python-dash/dash_example/stan_out_post.log'

app = Dash(__name__) 

app.layout = html.Div([dbc.Row(dbc.Col(html.Div(id="live-update-text"))),
                       dcc.Interval(id='interval-component',
                                    interval=2*1000, # 2 is refresh per 2s
                                    n_intervals=0)
                      ])

@app.callback(Output('live-update-text', 'children'),
              Input('interval-component', 'n_intervals'))
def update_metrics(n):
    # from this file, like this: 
    with open(text_file) as f:
        lines = f.readlines()
    line2=[]
    if len(lines)>0:
        for x in lines:
            line2.append(x)
            line2.append(html.Br())  #this is line break

    
    return [html.P(line2,
                   style={"color":"black",
                          "background-color": "#F5F9F9",
                          "height": "800px","width": "1100px","overflow-y": "scroll",
                          "margin": "auto","box-shadow": "0 4px 6px 0 rgba(248, 245, 246, 0.8)"})]       
            
if __name__=='__main__':
    app.run_server()





#click a button to execute a script
import dash_core_components as dcc 
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output,dash_table
import subprocess

app =Dash(__name__)

app.layout = html.Div([html.Button('Apply', id='apply-button', n_clicks=0),
                       html.Div(id='output-container-button', children='Hit the button to update.')
                      ])
                                     
                
@app.callback(Output('output-container-button', 'children'),
              Input('apply-button', 'n_clicks'))
def run_script_onClick(n_clicks):
    #print('[DEBUG] n_clicks:', n_clicks)
    if not n_clicks:
        #raise dash.exceptions.PreventUpdate
        return dash.no_update
    # without `shell` it needs list ['/full/path/python', 'script.py']           
    #result = subprocess.check_output( ['/usr/bin/python', 'script.py'] )  
    # with `shell` it needs string 'python script.py'
    result = subprocess.check_output('/root/anaconda3/envs/old1/bin/python /home/jonathanjames/aws/notebooks/index_analysis/main.py > /home/jonathanjames/aws/notebooks/materials-python-dash/dash_example/stan_out_post.log 2>&1 &', shell=True)  
    # convert bytes to string
    result = result.decode()  
    
    return result
            
if __name__ == "__main__":
    app.run_server()











#click button to execute script and show log
import dash_core_components as dcc 
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output,dash_table
import subprocess

app =Dash(__name__)





app.layout = dbc.Container([html.Div([html.Button('Apply', id='apply-button', n_clicks=0),html.Div(id='output-container-button', children='Hit the button to update.')]),
                            html.Div([dbc.Row(dbc.Col(html.Div(id="live-update-text"))),dcc.Interval(id='interval-component',interval=2*1000,n_intervals=0)]) # 2 is refresh per 2s
                            ])
    

text_file='/home/jonathanjames/aws/notebooks/materials-python-dash/dash_example/stan_out_post.log'

@app.callback(Output('live-update-text', 'children'),
              Input('interval-component', 'n_intervals'))
def update_metrics(n):
    # from this file, like this: 
    with open(text_file) as f:
        lines = f.readlines()
    line2=[]
    if len(lines)>0:
        for x in lines:
            line2.append(x)
            line2.append(html.Br())  #this is line break

    
    return [html.P(line2,
                   style={"color":"black",
                          "background-color": "#F5F9F9",
                          "height": "800px","width": "1100px",
                          "margin": "auto","box-shadow": "0 4px 6px 0 rgba(248, 245, 246, 0.8)",
                          "overflow-y": "scroll"})]        
    
    
@app.callback(Output('output-container-button', 'children'),
              Input('apply-button', 'n_clicks'))
def run_script_onClick(n_clicks):
    #print('[DEBUG] n_clicks:', n_clicks)
    if not n_clicks:
        #raise dash.exceptions.PreventUpdate
        return dash.no_update
    # without `shell` it needs list ['/full/path/python', 'script.py']           
    #result = subprocess.check_output( ['/usr/bin/python', 'script.py'] )  
    # with `shell` it needs string 'python script.py'
    result = subprocess.check_output('/root/anaconda3/envs/old1/bin/python /home/jonathanjames/aws/notebooks/index_analysis/main.py > /home/jonathanjames/aws/notebooks/materials-python-dash/dash_example/stan_out_post.log 2>&1 &', shell=True)  
    # convert bytes to string
    result = result.decode()  
    
    return result


if __name__ == "__main__":
    app.run_server()












#scroll to bottom when default, need to use java script
from dash import Dash, dcc, html, Input, Output,dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_core_components as dcc

#redirect or copy log to this file
text_file='/home/jonathanjames/aws/notebooks/materials-python-dash/dash_example/target_log/temp_log.log'

s_path='/home/jonathanjames/aws/notebooks/materials-python-dash/dash_example/assets2'

#if want dbc.col placed horizontally, need to use a bootstrap sheet like dbc.themes.BOOTSTRAP, otherwise everything place vertically
#but if use external_stylesheets, margin may have predefined, so it would be different from original so need to recalibrate margin of some items.
app = Dash(__name__,assets_folder=s_path)
app.layout =html.Div([
        html.Div(dcc.Slider(
            min=0,
            max=100,
            value=65,
            tooltip={'always_visible':True, 'placement':'bottom'}
        ),
        style=dict(height=100))
    ]*5,
    style=dict(maxHeight=300, overflowX='scroll'), id="scroll-div")


if __name__ == '__main__':
    app.run_server(use_reloader=False)
    

    
    
    
#for deployment install heroku
#curl https://cli-assets.heroku.com/install.sh | sh
    
#/home/jonathanjames/aws/notebooks/materials-python-dash/apps/app_4  

    
    








dash_example.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 13:37:04 2023

@author: root
"""

#   https://www.the-analytics.club/plotly-dashboards-in-python
###########################################################install dash#############################################################
#./pip3 install dash==2.8.1
#./pip3 install dash_bootstrap_components
# /root/anaconda3/bin/python /home/jonathanjames/aws/notebooks/dash_example.py






#example 1


"""


import dash
from dash import Dash,html,dcc, Input, Output, callback, dash_table
from pandas.io.formats import style
import plotly.express as px
import pandas as pd
import os

index_analysis_path='/home/jonathanjames/aws/notebooks/materials-python-dash/dash_example'

os.chdir(index_analysis_path)


#specify css file folder
assets_path = os.getcwd() +'/assets'



file_path=os.path.join(index_analysis_path,'life_expectancy.csv')
df = pd.read_csv(file_path)

app = Dash(__name__,assets_folder=assets_path)



# # Alternative way
# app.css.append_css({
#     "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
# })



colors = {"background": "#011833", "text": "#7FDBFF"} #color used in the graph

app.layout = html.Div(
    [   #To create a heading, you can use html.H1 and html.P to create a paragrap
        html.H1(
            "My Dazzling Dashboard",
        ),
        html.Div(
            [     # Dropdown to filter developing/developed country.
                html.Div(
                    [
                        html.Label("Developing Status of the Country"),
                        dcc.Dropdown(
                            id="status-dropdown",
                            options=[
                                {"label": s, "value": s} for s in df.Status.unique()
                            ],
                            className="dropdown",
                        ),
                    ]
                ),
                # Dropdown to filter countries with average schooling years.
                html.Div(
                    [
                        html.Label("Average schooling years grater than"),
                        dcc.Dropdown(
                            id="schooling-dropdown",
                            options=[
                                {"label": y, "value": y}
                                for y in range(
                                    int(df.Schooling.min()), int(df.Schooling.max()) + 1
                                )
                            ],
                            className="dropdown",
                        ),
                    ]
                ),
            ],
            className="row",
        ),
        # Placeholder to render teh chart.
        html.Div(dcc.Graph(id="life-exp-vs-gdp"), className="chart"),
        
         # Slider to select year.
        dcc.Slider(
            id="year-slider",
            min=df.Year.min(),
            max=df.Year.max(),
            step=None,
            marks={year: str(year) for year in range(df.Year.min(), df.Year.max() + 1)},
            value=df.Year.min(),
        ),
        
    ],
    className="container",
)


@app.callback(
    Output("life-exp-vs-gdp", "figure"),
    Input("year-slider", "value"),
    Input("status-dropdown", "value"),
    Input("schooling-dropdown", "value"),
)
def update_figure(selected_year, country_status, schooling):
    filtered_dataset = df[(df.Year == selected_year)]

    if schooling:
        filtered_dataset = filtered_dataset[filtered_dataset.Schooling <= schooling]

    if country_status:
        filtered_dataset = filtered_dataset[filtered_dataset.Status == country_status]

    fig = px.scatter(
        filtered_dataset,
        x="GDP",
        y="Life expectancy",
        size="Population",
        color="continent",
        hover_name="Country",
        log_x=True,
        size_max=60,
    )

    fig.update_layout(
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"],
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)


"""












#example 3

# -*- coding: utf-8 -*-



#https://hellodash.pythonanywhere.com/adding-themes/figure-templates





"""

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
)

app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO, dbc_css])

iris = px.data.iris()
gapminder = px.data.gapminder()
tips = px.data.tips()
carshare = px.data.carshare()

figure_templates = [
    "bootstrap_theme",
    "plotly",
    "ggplot2",
    "seaborn",
    "simple_white",
    "plotly_white",
    "plotly_dark",
    "presentation",
    "xgridoff",
    "ygridoff",
    "gridon",
    "none",
]

change_theme = ThemeChangerAIO(
    aio_id="theme",
    radio_props={"value": dbc.themes.SUPERHERO},
    button_props={
        "size": "lg",
        "outline": False,
        "style": {"marginTop": ".5rem"},
        "color": "success",
    },
)

change_figure_template = html.Div(
    [
        html.Div("Change Figure Template"),
        dcc.Dropdown(figure_templates, "bootstrap_theme", id="template"),
    ],
    className="pb-4",
)

sources = html.Div(
    [

        html.Label(
            [
                "Sources: ",
                html.A(
                    "Dash Bootstrap Templates| ",
                    href="https://pypi.org/project/dash-bootstrap-templates/0.1.1/",
                    target="_blank",
                ),
                html.A(
                    "Plotly Templates| ",
                    href="https://plotly.com/python/templates/",
                    target="_blank",
                ),
                html.A(
                    "Plotly Express",
                    href="https://plotly.com/python/plotly-express/",
                    target="_blank",
                ),
            ]
        ),
    ]
)


def make_figures(template):
    graph1 = dcc.Graph(
        figure=px.scatter(
            iris,
            x="sepal_width",
            y="sepal_length",
            color="species",
            title=f"Iris <br>{template} figure template",
            template=template,
        ),
        className="border",
    )
    graph2 = dcc.Graph(
        figure=px.scatter(
            gapminder,
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            hover_name="country",
            animation_frame="year",
            animation_group="country",
            log_x=True,
            size_max=60,
            title=f"Gapminder <br>{template} figure template",
            template=template,
        ),
        className="border",
    )
    graph3 = dcc.Graph(
        figure=px.violin(
            tips,
            y="tip",
            x="smoker",
            color="sex",
            box=True,
            points="all",
            hover_data=tips.columns,
            title=f"Tips <br>{template} figure template",
            template=template,
        ),
        className="border",
    )
    graph4 = dcc.Graph(
        figure=px.scatter_mapbox(
            carshare,
            lat="centroid_lat",
            lon="centroid_lon",
            color="peak_hour",
            size="car_hours",
            size_max=15,
            zoom=10,
            mapbox_style="carto-positron",
            title=f"Carshare <br> {template} figure template",
            template=template,
        ),
        className="border",
    )

    return [
        dbc.Row([dbc.Col(graph1, lg=6), dbc.Col(graph2, lg=6)]),
        dbc.Row([dbc.Col(graph3, lg=6), dbc.Col(graph4, lg=6)], className="mt-4"),
    ]


app.layout = dbc.Container(
    [
        dbc.Row(
            [
                ###################################
                #  Uncomment this line when running this app locally
                dbc.Col(change_theme, lg=2),
                ###################################

                dbc.Col(change_figure_template, lg=4),
            ],
        ),
        dbc.Row(dbc.Col(html.Div(id="graphs"))),
        dbc.Row(dbc.Col(sources)),
    ],
    className="dbc p-4",
    fluid=True,
)


@app.callback(
    Output("graphs", "children"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
    Input("template", "value"),
)
def update_graph_theme(theme, template):
    template = template_from_url(theme) if template == "bootstrap_theme" else template
    return make_figures(template)


if __name__ == "__main__":
    app.run_server(host='0.0.0.0',debug=True)  #also access by LAN computer http://192.168.3.216:8050/



"""




#example 4
from dash import Dash, dcc, html, Input, Output,dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
#from dash_bootstrap_templates import ThemeChangerAIO
from dash_bootstrap_templates import load_figure_template

from dash.dash_table.Format import Format, Padding
from dash.dash_table.Format import Format, Scheme, Trim
#template_from_url - bootstrap,cosmo,superhero

# dbc_css = (
#     "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
# )


#style path
s_path='/home/jonathanjames/aws/notebooks/materials-python-dash/dash_example/assets'

#note that body backdround color is set at base.css in s_path
#this superhero theme color/style only for the graph in plotly called in "make_figures"
app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO],assets_folder=s_path)
#app = Dash(__name__)


gapminder = px.data.gapminder()


load_figure_template(["superhero","sketchy", "cyborg", "minty"])  #becasue in px.scatter, it  use template='superhero'



use_dropdown = html.Div(
    [html.Div("Places"),
     dcc.Dropdown(options=[{"label": 'all', "value": 'all'}]+[{"label": c, "value": c}for c in gapminder.continent.unique()],
                     value="all",
                     id="template",
                     className="custom-dropdown",
                     style={"background-color":"","color":"#07090C"},
                     ),
    ],
)

use_dropdown2 = html.Div(
    [html.Div("Places"),
     dcc.Dropdown(options=[{"label": 'all', "value": 'all'}]+[{"label": c, "value": c}for c in gapminder.continent.unique()],
                     value="all",
                     id="template2",
                     style={"background-color":"","color":"#07090C"},
                     ),
    ],
    #className="pb-4",
)

vv='Asia'
def make_figures(vv):
    use_data=gapminder.copy() if vv=='all' else gapminder[gapminder['continent']==vv].copy()
    
    template='superhero'        
    figure=px.scatter(
            use_data,
            x="gdpPercap",
            y="lifeExp",
            size="pop",   #bubble size
            color="continent",
            hover_name="country",
            animation_frame="year",
            #animation_group="country",
            log_x=True,
            size_max=60,  #bubble size
            title="<span style='font-size:24px;color:white;'>set a title</span>",
            #title=f"Gapminder <br>{template} figure template",
            template='superhero',
            width=1200, height=700)   #control size
    figure.update_xaxes(showline = True, linecolor = 'white', linewidth = 2, mirror = True) #set border
    figure.update_yaxes(showline = True, linecolor = 'white', linewidth = 2, mirror = True) #set border
    figure.update_layout(
                        margin=dict(l=60, r=20, t=60, b=20),  #left,right,top,bottom
                        legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.98,font=dict(size=16)),
                        #paper_bgcolor="LightSteelBlue",
                        )
    figure.update_yaxes(title_text="Life Expectency",title_font=dict(size=20),tickfont = dict(size=16))
    figure.update_xaxes(title_text="GDP (%)",title_font=dict(size=20), tickfont = dict(size=16))
    graph2 = dcc.Graph(figure=figure)#className="border",#style={'width': '200vh', 'height': '85vh'},
    

    return [dbc.Row([dbc.Col(graph2)])]


#dash table exaplme
table_temp=gapminder.head(50)
table_temp=table_temp.reset_index(drop=True)
#https://dash.plotly.com/datatable/width
#https://dash.plotly.com/datatable/reference

#https://dash.plotly.com/datatable/data-formatting    

#dict(id='a', name='Rounded Percentage', type='numeric', format=Format(precision=2, scheme=Scheme.percentage_rounded))
col_define=[{"name": i, "id": i} for i in table_temp.columns]
col_define[3]=dict(name='lifeExp',id='lifeExp',type='numeric',format=Format(precision=2, scheme=Scheme.fixed))#2 decimal places
col_define[5]=dict(name='gdpPercap',id='gdpPercap',type='numeric',format=Format(precision=0, scheme=Scheme.fixed))#0 decimal places
money = dash_table.FormatTemplate.money(1) #use $ sign and comma
col_define[4]=dict(name='pop',id='pop',type='numeric',format=money)#money

table_out = html.Div(
    dash_table.DataTable(
        columns=col_define,
        data=table_temp.to_dict("records"),
        row_selectable=False,
        row_deletable=False,
        editable=False,
        filter_action="none",
        sort_action="none",
        style_table={'height': '300px', 'overflowY': 'auto','width': '900px', 'overflowX': 'auto'}, #control size with scroll bar
        fixed_rows={'headers': True},
        style_cell={'textAlign': 'center'},
        style_as_list_view=True,#without verticla grid line
        style_header={
            'backgroundColor': 'black',
            'fontWeight': 'bold'
        },
        style_data={
            'color': 'black',
            'backgroundColor': 'white'
        },
        style_data_conditional=[
        {'if': {'row_index': 'oddoddoddodd'},'backgroundColor': 'rgb(220, 220, 220)'},
        {'if': {'filter_query': '{gdpPercap} > 800 && {gdpPercap} < 2000','column_id': 'gdpPercap'},'color': 'tomato','fontWeight': 'bold'},
        {'if': {'filter_query': '{gdpPercap} <=800','column_id': 'gdpPercap'},'color': 'green','fontWeight': 'bold'},
        ],
        #adjust col width
        style_cell_conditional=[{'if': {'column_id': 'country'},'width': '10%'},
                                {'if': {'column_id': 'continent'},'width': '10%'},
                                {'if': {'column_id': 'year'},'width': '10%'},
                                {'if': {'column_id': 'lifeExp'},'width': '10%'},
                                {'if': {'column_id': 'pop'},'width': '10%'},
                                {'if': {'column_id': 'gdpPercap'},'width': '10%'},
                                {'if': {'column_id': 'iso_alpha'},'width': '10%'},
                                {'if': {'column_id': 'iso_num'},'width': '10%'},
                                ],
        #page_size=10,

    ),
)

dict(a='ww',b='ee')



app.layout = dbc.Container(
    [
        html.Div([html.P(children="🥑 🐎", style={"font-size": "48px","margin": "0 auto","text-align": "center","color":"Lime"}),
                      html.H1(children="Avocado Analytics",style={"fontSize": "50px", "color": "white","font-weight": "bold",
                                                                  "text-align": "center","margin": "0px auto"}),
                      html.P(children="Analyze the behavior of avocado prices and the number of avocados sold in the US between 2015 and 2018",
                             style={"fontSize": "17px", "color": "white","text-align": "center","max-width": "384px","margin": "1px auto"}
                       ),
                     ],
            #"margin": "auto" is to center this div box
            style={"background-color": "#222222","height": "230px","width": "1088px","margin": "auto","padding": "0px 0 0 0",
                   "margin-top":"20px"},  #margin-top is to move down div box a bit
        ),
        dbc.Row([dbc.Col(use_dropdown, lg=3)],style={'height': '75px'}),   #lg control the horizontal length of the dropdown menu
        dbc.Row(dbc.Col(html.Div(id="graphs"))),
        html.Br(),
        html.Div([html.P("HELLO",style={"color":"black","background-color": "#F5F9F9","height": "188px","width": "588px","margin": "auto","box-shadow": "0 4px 6px 0 rgba(248, 245, 246, 0.8)"})]),       
        html.Br(),
        dbc.Row([dbc.Col(use_dropdown2, lg=3)],style={'height': '75px'}),   #lg control the horizontal length of the dropdown menu
        dbc.Row(dbc.Col(html.Div(id="graphs2"))),
        html.Br(),
        html.Div([html.H5("DataTable with Bootstrap theme"),table_out]),#data table
        html.Br(),
    ],
    #className="dbc p-4",
    fluid=True,
)

# #single callbacks
# @app.callback(
#     [Output("graphs", "children"),Output("graphs2", "children")],  #define output name called graphs" then call it in layout
#     [Input("template", "value"),Input("template2", "value")],
# )
# def update_graph_theme(v1,v2):
#     return make_figures(v1),make_figures(v2)


@app.callback(
    [Output("graphs", "children")],  #define output name called graphs" then call it in layout
    [Input("template", "value")],
)
def update_graph_theme(v1):
    return make_figures(v1)



@app.callback(
    [Output("graphs2", "children")],  #define output name called graphs" then call it in layout
    [Input("template2", "value")],
)
def update_graph_theme(v2):
    return make_figures(v2)





if __name__ == "__main__":
    app.run_server(use_reloader=False)










index_price_hsi_minutedata_production.py


#import ib_insync
#ib_insync.__version__

#%reset -f
#654_pnl_statistic.xlsx
import os
#os.chdir(r'C:\Users\jonathanjames\aws\notebooks\tensorflow-mnist-tutorial-master')
import math
import numpy as np
import pandas as pd
import sys
import time
time_start=time.time()
import ast
import matplotlib.pyplot as plt
from datetime import datetime as dt
from pandas import read_excel
from ib_insync import *
import re
from dateutil import tz
from datetime import timedelta

import pytz

#*args is to unpack the input list
def eprint(*args):
    print(*args,flush = True)  #print to log
    #print(*args,flush = True)                             #print to command prompt









index_analysis_path_original=r'C:/Users/jonathanjames/aws/notebooks/index_analysis'
index_analysis_path=r'C:/Users/jonathanjames/aws/notebooks/index_analysis/hsi_min_trade_production'



#this is for log path
#log_path=os.path.join(index_analysis_path,'log')

#main_folder=os.path.join(index_analysis_path,'plot')


#today_day='2023-04-17'
today_day=time.strftime("%Y-%m-%d")
current_year=int(today_day[0:4])


#create folder for temp output
today_path=os.path.join(index_analysis_path,'production',today_day)
if not os.path.exists(today_path):
    os.makedirs(today_path)

##create folder for log
#today_path=os.path.join(index_analysis_path,'log',today_day)
#if not os.path.exists(today_path):
#    os.makedirs(today_path)

#output stand out
import sys
#stan_out_log=os.path.join(log_path,today_day,'stan_out_log_'+time.strftime("%Y%m%d")+'_'+time.strftime("%H%M%S")+'.log')
#sys.stderr = open(stan_out_log, 'w')

eprint('Today is ',today_day)

reference_account='U4684739' 
reference_client_id=53#54  
reference_port=7497
         
account_use='DU3984794'
client_id=52#50
port_use=7490  #7497 is live. 7490 is simulation
trading_asset='MHI'
contract_size=1
stop_loss=30
define_time='15:10:00'
time_offset=2



eprint("Start reading arguments")
try:
    reference_account=sys.argv[1]
    reference_client_id=sys.argv[2]
    reference_port=int(sys.argv[3])
         
    account_use=sys.argv[4]
    client_id=int(sys.argv[5])
    port_use=int(sys.argv[6])  #7497 is live. 7490 is simulation
    trading_asset=sys.argv[7]
    contract_size=int(sys.argv[8])
    stop_loss=int(sys.argv[9])
    define_time=sys.argv[10]
    time_offset=int(sys.argv[11])

except:
    eprint("Oops!",sys.exc_info()[0],'error details is ',sys.exc_info()[1],"occured when reading arguments",'\n')
    
    
    



eprint("------------------------------------------Start------------------------------------------------")
eprint(today_day+' '+define_time)

#connect IB
# util.startLoop()  # uncomment this line when in a notebook
util.patchAsyncio()
ib = IB()
#this is live bet account
ib.connect('127.0.0.1', port_use, clientId=client_id)
#ib.connect('127.0.0.1', port_use, clientId=client_id) 
eprint('IB connected (trading account) with port ',port_use,' client_id is ',client_id)
ib.isConnected()

#this is reference account
ib2=IB()
ib2.connect('127.0.0.1', reference_port, clientId=reference_client_id)
eprint('IB connected (reference account) with port ',reference_port,' client_id is ',reference_client_id,'\n')
ib2.isConnected()




pred_dictionary={'1':'BUY','0':'SELL'}

output_sentence='' #email header show MKT/MTL order detail
email_content=''   #email content, show STP order detail


hk_zone=pytz.timezone("Asia/Hong_Kong")



entry_time_year=int(dt.now(hk_zone).strftime('%Y'))
entry_time_month=int(dt.now(hk_zone).strftime('%m'))
entry_time_day=int(dt.now(hk_zone).strftime('%d'))


temp=dt(entry_time_year,entry_time_month,entry_time_day,
        int(define_time.split(':')[0]),
        int(define_time.split(':')[1]),
        int(define_time.split(':')[2]))-timedelta(seconds=time_offset)
temp=temp.replace(tzinfo=tz.gettz("Asia/Hong_Kong")) #this time is for comparing with IB so better specify time zone
define_time=temp

entry_time_is=dt(entry_time_year,entry_time_month,entry_time_day,9,15,0)
entry_time_is_hk=entry_time_is.replace(tzinfo=tz.gettz("Asia/Hong_Kong")) #this time is for comparing with IB so better specify time zone
trade_time_is=dt(entry_time_year,entry_time_month,entry_time_day,9,25,0)
trade_time_is_hk=trade_time_is.replace(tzinfo=tz.gettz("Asia/Hong_Kong"))
exit_time_is=dt(entry_time_year,entry_time_month,entry_time_day,16,25,0)
exit_time_is_hk=exit_time_is.replace(tzinfo=tz.gettz("Asia/Hong_Kong"))





#find time in hong kong zone
#input_feed=str(fills_current[7])
def find_hk_time(input_feed):
    find_Execution=re.findall(r'execution=Execution\((.*?), tzinfo',input_feed)
    time_is=re.findall(r'time=datetime.datetime\((.*)',find_Execution[0])[0]
    time_is=time_is.split(',')
    time_is=[int(i.strip()) for i in time_is]
    
    #find time zone
    find_Execution=re.findall(r'execution=Execution\((.*?)acctNumber',input_feed)
    zone_temp=re.findall(r'tzinfo=datetime.timezone.(.*)\)',find_Execution[0])[0]
    
    if len(time_is)==5:
        execution_time_is=dt(time_is[0],time_is[1],time_is[2],time_is[3],time_is[4],0)
    else:
        execution_time_is=dt(time_is[0],time_is[1],time_is[2],time_is[3],time_is[4],time_is[5])
    
    #datatime default is 'naive, so assign UTC to it'
    execution_time_is_utc = execution_time_is.replace(tzinfo=tz.gettz(zone_temp))
    
    #convert time hong kong
    to_zone = tz.gettz('Asia/Hong_Kong')
    execution_time_is_hk=execution_time_is_utc.astimezone(to_zone)
    execution_time_is_hk_date=dt.strptime(execution_time_is_hk.strftime("%Y-%m-%d"),"%Y-%m-%d")

    execution_time_is_hk_hms=dt.strptime(execution_time_is_hk.strftime("%H:%M:%S"),"%H:%M:%S")
    return execution_time_is_hk, execution_time_is_hk_date, execution_time_is_hk_hms


def request_TWS_time():
    x=ib.reqCurrentTime()
    to_zone = tz.gettz('Asia/Hong_Kong')
    y = x.astimezone(to_zone)
    #y=y.replace(tzinfo=None)
    return y


#read calendar
calendar = read_excel(os.path.join(index_analysis_path_original,'daily_prediction_production','calendar.xlsx'),'calendar')
calendar['Date2']=calendar['Date'].astype(str)
calendar['Date2_ym']=calendar['Date2'].apply(lambda x:x.split('-')[0]+x.split('-')[1])
calendar_today=calendar.loc[calendar['Date2']==today_day,:].copy()


calendar=calendar.loc[calendar['Settlement_date']==1,:]
download_df=calendar.loc[(calendar['Date2']>=today_day),:]
trading_contract_without_format=download_df.Date2.values[0]
trading_contract_without_format=trading_contract_without_format.replace('-','')


#read from paquet minute data
fn = os.path.join(index_analysis_path,"historical_indicator_data.parquet")
historical_indicator=pd.read_parquet(fn, engine='pyarrow')
historical_indicator.columns.values

#only select up to and not include this year
his_big=historical_indicator.loc[historical_indicator['year_cohord']<current_year,['Date1','year_cohord','f1']].copy()
eprint('Finished reading historical indicator. his_big last row is ',his_big.Date1.values[-1])

#use 500 is enough to do ema
#becasue only need nearly 100 rows is already enough to find ema
his_small=historical_indicator.loc[historical_indicator['Date2']<today_day,['Date1','close']].copy()
his_small=his_small[['Date1','close']][-500:].copy()
eprint('Finished reading historical indicator. his_small last row is ',his_small.Date1.values[-1],'\n')

#read today data

def do_prediction():
    contract=Future(symbol='HSI',lastTradeDateOrContractMonth=trading_contract_without_format, exchange='HKFE',includeExpired=True)
    bars = ib.reqHistoricalData(contract,endDateTime=today_day.replace("-","")+' 20:00:00', durationStr='1 D',
                                    barSizeSetting='15 mins', whatToShow='TRADES', useRTH=True)
#    bars = ib.reqHistoricalData(contract,endDateTime=dt(2023,4,20,20,0,0), durationStr='1 D',
#                                    barSizeSetting='15 mins', whatToShow='TRADES', useRTH=True)
    temp=util.df(bars)
    #temp=None
    #temp.close.values[-1]
    #before market open, temp is none. 
    if temp is None:
        temp=pd.DataFrame([])
        extract_time=request_TWS_time()
        price_use='pre market'
    else:
        temp['Date1']=temp['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S")) #dt to string
        temp=temp.sort_values(by=['Date1'],ascending=True)
        temp=temp[['Date1','close']].copy()
        #us reqHistoricalData may have 1 to 2 seconds delay, so use ib.reqMktData(contract, '', False, False)
        for i in range(1,10):
            extract_time=request_TWS_time()
            abc=ib.reqMktData(contract, '', False, False)
            ib.sleep(0.1) #initially abc has no value, need to sleep 0.1 second for value filling
            #print(x)
            extract_time=abc.time
            price_use=abc.last
            if not pd.isnull(price_use):
                break
        eprint("live data extracted ",i,' times')

        temp.loc[temp.shape[0]-1,'close']=price_use

    if not pd.isnull(price_use):
        temp=his_small.append(temp)
        temp=temp.drop_duplicates(subset='Date1',keep='last')
        
        
        #calculate ema
        #temp=his_small.copy()

        temp=temp.append(pd.DataFrame({'Date1':['NextTime'],'close':[np.NaN],'ema_10':[np.NaN],'f1':[np.NaN],'f3':[np.NaN]}))
        temp['f3']=temp['f3'].shift(1)
        
    
        temp=temp.loc[(temp['Date1']>=today_day)|(temp['Date1']=='NextTime'),:].copy()
        #temp=temp.loc[(temp['Date1']=='NextTime'),:].copy()
        temp=temp.reset_index(drop=True)
        
        #create bet logic
        test_x_with_date=temp.copy()
        test_x_with_date.loc[(test_x_with_date['f3']>=70),'bet']=-1
        test_x_with_date.loc[(test_x_with_date['f3']<=30),'bet']=1
        
        test_x_with_date['bet']=test_x_with_date['bet'].fillna(method='ffill')
        test_x_with_date['bet_lag1']=test_x_with_date['bet'].shift(1)
        
        current_bet=test_x_with_date.loc[test_x_with_date['Date1']=='NextTime','bet'].values[0]
        
        last_bet=test_x_with_date.loc[test_x_with_date['Date1']=='NextTime','bet_lag1'].values[0]
        
        prediction_BUY_SELL=''
        if ((current_bet==1)&(pd.isnull(last_bet)))|((current_bet==1)&(last_bet==-1)):
            prediction_BUY_SELL='BUY'
        if ((current_bet==-1)&(pd.isnull(last_bet)))|((current_bet==-1)&(last_bet==1)):
            prediction_BUY_SELL='SELL'

        eprint('prediction_BUY_SELL is ',prediction_BUY_SELL)
        eprint('extract_time is',extract_time,' with price ', price_use,'\ntest_x_with_date is :\n',test_x_with_date,'\n')
            
    else:
        prediction_BUY_SELL=''
        test_x_with_date=pd.DataFrame([])
        
    
    return prediction_BUY_SELL,test_x_with_date,price_use,extract_time


#run once to see if it work
#eprint('*****Start checking on do_prediction() function*****')
#prediction_BUY_SELL,test_x_with_date,last_close,extract_time=do_prediction()
#eprint('*****End checking on do_prediction() function*****','\n')

#prediction_BUY_SELL=''
#test_x_with_date=pd.DataFrame([])
#extract_time=request_TWS_time()

#prediction_BUY_SELL_number=0
#prediction_BUY_SELL='BUY'
if (dt.now(hk_zone)<entry_time_is_hk):
    eprint('Entered < 0915')
    prediction_BUY_SELL,test_x_with_date,last_close,extract_time=do_prediction()
    #prediction_BUY_SELL='SELL'
    
    if prediction_BUY_SELL!='':
        prediction_BUY_SELL_number=1 if prediction_BUY_SELL=='BUY' else 0 
        #all_open_order=ib2.reqAllOpenOrders() #this only get order
        
        #need to use reqAllOpenOrders() first before using
        #ib2.openTrades() or ib2.openOrders() if login with different clientID to look for other clients, otherwise it is blank
        #https://groups.io/g/insync/topic/32303346#4997
        ib2.client.reqAllOpenOrders()
        #openTrades() get all details including order, contract
        all_open_order=ib2.openTrades()
        eprint(all_open_order)
        


        #account_number='U6489376'
        target_side=pred_dictionary[str(1-prediction_BUY_SELL_number)]   #this is opposite of prediction_BUY_SELL
        #if reference account is doing opposite side, need to place market order in account_use
        open_order_use=[w for w in all_open_order if (w.order.account==reference_account)&\
                                                     (w.order.action==target_side)&\
                                                     (w.order.orderType=='MTL')&\
                                                     (w.contract.lastTradeDateOrContractMonth==trading_contract_without_format)&\
                                                     (w.contract.symbol==trading_asset)]
        if len(open_order_use)>0:
            eprint("Have opposite order in reference account, use MKT order")
            contract=Future(trading_asset, trading_contract_without_format, 'HKFE')
            ib.qualifyContracts(contract)
            order = Order()
            order.account=account_use
            order.action = prediction_BUY_SELL  #BUY SELL
            order.orderType = "MKT"
            order.totalQuantity =contract_size
            order.outsideRth = True
            
            for i in range(0,1000):
                if request_TWS_time()>=entry_time_is_hk:
                    trade = ib.placeOrder(contract, order)
                    eprint('MKT order placed at '+time.strftime("%Y-%m-%d %H:%M:%S"))
                    break
                ib.sleep(0.5)

            eprint('MKT order status ',trade.orderStatus.status)
            
            while not trade.isDone():
                ib.waitOnUpdate()
                
        
        else:
            # if same side in reference account, ok to place MTL order
            #account_use='U4684739'
            eprint("No opposite order in reference account, use MTL order")
            contract=Future(trading_asset, trading_contract_without_format, 'HKFE')
            ib.qualifyContracts(contract)
            order = Order()
            order.account=account_use
            order.action = prediction_BUY_SELL
            order.orderType = "MTL"
            order.totalQuantity = contract_size
            order.tif='AUC'
            trade = ib.placeOrder(contract, order)
            eprint('MTL order status ',trade.orderStatus.status)

            while not trade.isDone():
                ib.waitOnUpdate()
 
            
        #IB colleage said pre market MKT order after filling will show 'Sumbitted'        
        if (trade.orderStatus.status=='Filled')|(trade.orderStatus.status=='Submitted'):
            #find order id
            order_id_use=trade.order.permId  #find unique order id, under this id, there may be multiple fills records
            eprint('order id ',order_id_use)
            #eprint(trade)
            #not neessary to use permId to find all fills, can use orderStatus
            fill_price_morning=trade.orderStatus.avgFillPrice
            shares_morning=trade.orderStatus.filled
            side_morning=trade.order.action
                
            #find stoploss level
            #floor is round down, ceil is round up
            #if sell, then round down. if long then round up because when large contract, overall price may be decimal
            stop_loss_level=math.floor(fill_price_morning-stop_loss) if prediction_BUY_SELL=='BUY' else math.ceil(fill_price_morning+stop_loss)
            prediction_BUY_SELL_opposite=pred_dictionary[str(1-prediction_BUY_SELL_number)]
                
            #STP order GTD
            #note that in stoporder, need to specify which account, even already used port and clientID
            contract=Future(trading_asset, trading_contract_without_format, 'HKFE')
            order = StopOrder(account=account_use,action = prediction_BUY_SELL_opposite, totalQuantity = shares_morning,stopPrice=stop_loss_level)
            trade = ib.placeOrder(contract, order)
                
            ib.sleep(2)
            #find open order on this trade
            order_id_stop_use=trade.order.permId
            all_open_order=ib.openOrders()
            open_order_use=[w for w in all_open_order if (w.account==account_use)&(w.permId==order_id_stop_use)][0]
                
            if open_order_use.orderType=='STP':
                stop_order_status='STP order status is '+open_order_use.action+' lots '+\
                                   str(open_order_use.totalQuantity)+' at price '+str(round(open_order_use.auxPrice))
                email_content=stop_order_status
                    
            output_sentence=account_use+'_'+str(side_morning)+" "+str(shares_morning)+"@"+str(fill_price_morning)+'_'+\
                                trading_asset+'_'+'client ID '+str(client_id)
            eprint(output_sentence)
            eprint(email_content,'\n')




if (dt.now(hk_zone)>trade_time_is_hk)&(dt.now(hk_zone)<exit_time_is_hk):
    eprint("Entered between 0925 and 1625")
    for i in range(0,1000):
        if request_TWS_time()>=define_time:
            prediction_BUY_SELL,test_x_with_date,last_close,extract_time=do_prediction()
            if prediction_BUY_SELL!='':
                prediction_BUY_SELL_number=1 if prediction_BUY_SELL=='BUY' else 0 
                #find open order on this account
                all_open_order=ib.openOrders()
                open_order_use=[w for w in all_open_order if w.account==account_use]
                
                #cancel the STP order
                if len(open_order_use)>0:
                    for order_x in open_order_use:                
                        eprint('open order is ',order_x,'\n')
                        if order_x.orderType=='STP':
                            ib.cancelOrder(order_x)
                            eprint('STP order cancelled ','\n')
    
                #flat position and reverse enter
                old_position=0
                if len(ib.positions(account=account_use))!=0:
                    for p_x in ib.positions(account=account_use):
                        order_old ='BUY' if p_x.position>0 else 'SELL' 
                        cond=(p_x.contract.tradingClass==trading_asset)&\
                             (p_x.contract.lastTradeDateOrContractMonth==trading_contract_without_format)&\
                             (order_old!=prediction_BUY_SELL)
                             
                        if cond:
                            old_position=abs(int(p_x.position))
                            break
    
                contract=Future(trading_asset,trading_contract_without_format, 'HKFE')
                ib.qualifyContracts(contract)
                order = Order()
                order.account=account_use
                order.action = prediction_BUY_SELL  #BUY SELL
                order.orderType = "MKT"
                order.totalQuantity =old_position+contract_size
                order.outsideRth = True
                            
                trade = ib.placeOrder(contract, order)
                eprint('MKT order placed at '+time.strftime("%Y-%m-%d %H:%M:%S"))
                ib.sleep(0.5)
                while not trade.isDone():
                    ib.waitOnUpdate()
    
                #IB colleage said pre market MKT order after filling will show 'Sumbitted'        
                if (trade.orderStatus.status=='Filled')|(trade.orderStatus.status=='Submitted'):
                    #find order id
                    order_id_use=trade.order.permId  #find unique order id, under this id, there may be multiple fills records
                    eprint('order id ',order_id_use)
                    #eprint(trade)
                    #not neessary to use permId to find all fills, can use orderStatus
                    fill_price_morning=trade.orderStatus.avgFillPrice
                    shares_morning=trade.orderStatus.filled
                    side_morning=trade.order.action
                        
                    #find stoploss level
                    #floor is round down, ceil is round up
                    #if sell, then round down. if long then round up because when large contract, overall price may be decimal
                    stop_loss_level=math.floor(fill_price_morning-stop_loss) if prediction_BUY_SELL=='BUY' \
                                                                                else math.ceil(fill_price_morning+stop_loss)
                    prediction_BUY_SELL_opposite=pred_dictionary[str(1-prediction_BUY_SELL_number)]
                                
                    #STP order GTD
                    #note that in stoporder, need to specify which account, even already used port and clientID
                    contract=Future(trading_asset,trading_contract_without_format, 'HKFE')
                    order = StopOrder(account=account_use,action = prediction_BUY_SELL_opposite,
                                      totalQuantity = contract_size,stopPrice=stop_loss_level)
                    trade = ib.placeOrder(contract, order)
                    
                    ib.sleep(2)
                    #find open order on this trade
                    order_id_stop_use=trade.order.permId
                    all_open_order=ib.openOrders()
                    open_order_use=[w for w in all_open_order if (w.account==account_use)&(w.permId==order_id_stop_use)][0]
                                
                    if open_order_use.orderType=='STP':
                        stop_order_status='STP order status is '+open_order_use.action+' lots '+str(open_order_use.totalQuantity)+\
                                          ' at price '+str(round(open_order_use.auxPrice))
                        email_content=stop_order_status
                                    
                    output_sentence=account_use+'_'+str(side_morning)+" "+str(shares_morning)+"@"+str(fill_price_morning)+'_'+\
                                    trading_asset+'_'+'client ID '+str(client_id)
                    eprint(output_sentence)
                    eprint(email_content,'\n')
    
            break
        ib.sleep(0.5)






#close position at market close
if (dt.now(hk_zone)>exit_time_is_hk):
    eprint("Entered > 1625")
    for i in range(0,1000):
        if request_TWS_time()>=define_time:        
            #find open order on this account
            all_open_order=ib.openOrders()
            open_order_use=[w for w in all_open_order if w.account==account_use]
            
            #cancel the STP order
            if len(open_order_use)>0:
                for order_x in open_order_use:                
                    eprint('open order is ',order_x,'\n')
                    if order_x.orderType=='STP':
                        ib.cancelOrder(order_x)

            #flat position
            if len(ib.positions(account=account_use))!=0:
                for p_x in ib.positions(account=account_use):
                    if p_x.contract.tradingClass==trading_asset:
                        #print(p_x.contract.conId);print(p_x.account);print(p_x.position)
                        contract=Future(p_x.contract.tradingClass,p_x.contract.lastTradeDateOrContractMonth,'HKFE')
                        ib.qualifyContracts(contract)
                        order_action ='SELL' if p_x.position>0 else 'BUY'                     
                        order = MarketOrder(action = order_action,totalQuantity = abs(int(p_x.position)),tif = 'DAY')
                        order.account=p_x.account
                        order.outsideRth = True

                        trade = ib.placeOrder(contract, order)
                        eprint('MKT order placed at '+time.strftime("%Y-%m-%d %H:%M:%S"))
                        while not trade.isDone():
                            ib.waitOnUpdate()

                        #find order id
                        order_id_use=trade.order.permId  #find unique order id, under this id, there may be multiple fills records
                        eprint('order id',order_id_use)
                        #eprint(trade)

                        fill_price_morning=trade.orderStatus.avgFillPrice
                        shares_morning=trade.orderStatus.filled
                        side_morning=trade.order.action
                        output_sentence='Flat '+account_use+'_'+str(side_morning)+" "+str(shares_morning)+"@"+\
                                         str(fill_price_morning)+'_'+trading_asset+'_'+'client ID '+str(client_id)
                        eprint(output_sentence,'\n')
            break
        ib.sleep(0.5)




if ib.isConnected()==True:
    ib.disconnect()
    eprint('IB API disconnected')

if ib2.isConnected()==True:
    ib2.disconnect()
    eprint('IB API 2 disconnected','\n')




#save IB data as refeence, note that test_x_with_date only store today data/factor
#if test_x_with_date.shape[0]!=0:
try:
    extract_time=extract_time.strftime("%Y-%m-%d_%H-%M-%S") # dt to string
    out_path=os.path.join(index_analysis_path,'production',today_day,'test_x_with_date_IBtime_'+extract_time+'.csv')
    test_x_with_date.to_csv(out_path, header=True, index=True, sep=',', mode='a')
except:
    pass







if output_sentence != '':
    #python send email
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    mail_content = email_content
    #The mail addresses and password
    sender_address = 'jonathan2019trading@gmail.com'
    sender_pass = 'vhfrnlisxofeajsy'
    receiver_address = 'jonathan2019trading@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = output_sentence
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content+'\n'))
    #The body and the attachments for the mail
    try:
        html = """\
        <html>
          <head></head>
          <body>
            {0}
          </body>
        </html>
        """.format(test_x_with_date.to_html())
        
        part1 = MIMEText(html, 'html')
        message.attach(part1)
    except:
        pass

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')








#sys.stderr.close()
#sys.stderr = sys.__stderr__









api_morning_mindata_production.main.py




#use below function to print to stan out
from __future__ import print_function
import sys

#def eprint(*args, **kwargs):
#    print(*args, file=sys.stderr, **kwargs,flush = True) #print to log
#    print(*args,flush = True)   #print to cmd


    
import os
import numpy as np
#os.chdir(r'C:\Users\jonathanjames\Desktop\python\WinPython-64bit-3.6.2.0Qt5\notebooks\index_analysis')
target_dir=r'C:\Users\jonathanjames\aws\notebooks\index_analysis'

use_hsi_future_price=True

os.chdir(target_dir)
from pandas import read_excel

import pandas_datareader as pdr
from datetime import timedelta
from datetime import datetime as dt
import pandas as pd
from time import sleep
import subprocess
import pytz

import threading



#output stan out
import sys
import time
#stan_out_log=os.path.join('log','stan_out_higher_level_'+time.strftime("%Y%m%d")+'_'+time.strftime("%H%M%S")+'_mindata_production'+'.log')
#sys.stderr = open(stan_out_log, 'w')


#current_date=dt.now().strftime('%Y')+dt.now().strftime('%m')+dt.now().strftime('%d')

today_day=time.strftime("%Y-%m-%d")
#today_day='2018-12-27'
#read trading calendar
calendar = read_excel(r'C:\Users\jonathanjames\aws\notebooks\index_analysis\daily_prediction_production\calendar.xlsx','calendar')
calendar['Date2']=calendar['Date'].astype(str)
calendar=calendar.loc[calendar['trading_date']==1,:]
calendar=calendar.reset_index(drop=True)






hk_zone=pytz.timezone("Asia/Hong_Kong")







sleep(5)

#if this reference_account and reference_clientid has opposite side contract, then don't place at MTL, use MKT after open
#below is MTL order sample, no asset symbol name, so use clientid to identify it
#    [Order(orderId=3623, clientId=21, permId=295475302, action='SELL', totalQuantity=1.0,
#           orderType='MTL', lmtPrice=20353.0, auxPrice=0.0, tif='AUC', ocaType=3, trailStopPrice=20352.0,
#           eTradeOnly=False, firmQuoteOnly=False, volatilityType=0, deltaNeutralOrderType='None',
#           referencePriceType=0, account='U4684739', clearingIntent='IB', adjustedOrderType='None',
#           cashQty=0.0, dontUseAutoPriceForHedge=True)]

#reference_account='U4684739' 
#reference_client_id=54#55  
#reference_port=7497
         
#account_use='DU3984794'
#client_id=50#51
#port_use=7490  #7497 is live. 7490 is simulation
#trading_asset='MHI'
#contract_size=1
#stop_loss=30
#define_time='15:10:45'
#time_offset=2


#i=0
#for i in range(0,50):
#    time.sleep(5)
#    print("waiting..."+str(i),flush=True)




all_accounts=[{'reference_account':'U4684739',
               'reference_client_id':54,
               'reference_port':7497,
               'account_use':'DU3984794',
               'client_id':50,
               'port_use':7490,
               'trading_asset':'MHI',
               'contract_size':1,
               'stop_loss':30,
               'time_offset':2}]


#this program will find all time defined in define_time0 whicch is greater than current one
#for example, time is now 9:28am, so the next target time is 9:30:0 specify in define_time0
#time_offset_big =20 means this program will sleep until 9:29:40, then enter into script index_price_hsi_mindata_production.py
#time_offset=2 means it will wait until 9:29:58 then execute order if any in script index_price_hsi_mindata_production.py
    
define_time0=['9:09:50','9:30:0','9:45:0',
             '10:0:0','10:15:0','10:30:0','10:45:0',
             '11:0:0','11:15:0','11:30:0','11:45:0',
             '13:0:0','13:15:0','13:30:0','13:45:0',
             '14:0:0','14:15:0','14:30:0','14:45:0',
             '15:0:0','15:15:0','15:30:0','15:45:0',
             '16:0:0','16:15:0','16:29:57']

time_offset_big=20

entry_time_year=int(dt.now(hk_zone).strftime('%Y'))
entry_time_month=int(dt.now(hk_zone).strftime('%m'))
entry_time_day=int(dt.now(hk_zone).strftime('%d'))

define_time0_use=[]
for x in define_time0:
    temp=dt(entry_time_year,entry_time_month,entry_time_day,int(x.split(':')[0]),int(x.split(':')[1]),int(x.split(':')[2]))-\
         timedelta(seconds=time_offset_big)
    temp=temp.astimezone(hk_zone)
    define_time0_use.append(temp)

#find all times that greater than now
define_time0_use=[x for x in define_time0_use if dt.now(hk_zone)<x]

#eprint("hello")
#print("simon")
#1/0

print('Start Main',flush=True)


if sum(calendar['Date2'].isin([today_day]))==1:
    #next_time=dt(2023,5,2,18,50,0);next_time=next_time.astimezone(hk_zone)
    for next_time in define_time0_use:
        define_time=(next_time+timedelta(seconds=time_offset_big)).strftime("%H:%M:%S")
        time_now=dt.now(hk_zone)
        wait_time=(next_time-time_now).seconds
        print("Time now is ",time_now)
        print('waiting for ',next_time,' waiting time is ',wait_time,' seconds',flush=True)
        sleep(wait_time)  # wait until next target time
        
        api_script=os.path.join(target_dir,'IB_live_trade','index_price_hsi_mindata_production.py')
        cmds_list = [r"C:\Users\jonathanjames\Desktop\python\WPy-3670\python-3.6.7.amd64\python.exe"+\
                     ' '+api_script+\
                     ' '+k['reference_account']+' '+str(k['reference_client_id'])+' '+str(k['reference_port'])+\
                     ' '+k['account_use']+' '+str(k['client_id'])+' '+str(k['port_use'])+\
                     ' '+k['trading_asset']+' '+str(k['contract_size'])+' '+str(k['stop_loss'])+\
                     ' '+define_time+\
                     ' '+str(k['time_offset']) for k in all_accounts]

        print('All arguments are',cmds_list[0],flush=True)
        

        time_now_save=time.strftime("%Y%m%d")+'_'+time.strftime("%H%M%S")
        name = cmds_list[0].split()[5]+'_'+time_now_save
        #if in children script, already output a std error/std out log file, below out and err won't hv any outputs
        #out = open(os.path.join('hsi_min_trade_production\log_temp',"%s_log.txt" % name), 'w')
        #err = open(os.path.join('hsi_min_trade_production\log_temp',"%s_error_log.txt" % name), 'w')#open('/dev/null', 'w')
        p = subprocess.Popen(cmds_list[0].split())#, stdout=out, stderr=err)
        p.wait()
        print (name + " completed, return code: " + str(p.returncode),flush=True)
        print ("Done!",flush=True)
        #except:
        #    print("Oops!",sys.exc_info()[0],'error details is ',sys.exc_info()[1],"occured",'\n',flush=True)
#        #cmd=cmds_list[0]
#        def run(cmd):
#            name = cmd.split()[5]+'_'+time_now_save
#            #out = open(os.path.join('log',"%s_log.txt" % name), 'w')
#            #err = open(os.path.join('log',"%s_error_log.txt" % name), 'w')#open('/dev/null', 'w')
#            p = subprocess.Popen(cmd.split())#, stdout=out, stderr=err)
#            #p = subprocess.Popen(cmd.split(), stdout=out, stderr=err)
#        
#            p.wait()
#            eprint (name + " completed, return code: " + str(p.returncode))
#
#        proc = [threading.Thread(target=run,args=(cmd,)) for cmd in cmds_list]
#        a=[p.start() for p in proc]  ## 執行該子執行緒
#        #等待該執行緒執行結束，也就是說放在 join 之後的程式碼就會等到子執行緒執行完成後，才會接著執行
#        b=[p.join() for p in proc]  ### 等待 t 這個子執行緒結束
#        eprint ("Done!")


else:
    print(today_day+' is not trading date',flush=True)





#sys.stderr.close()
#sys.stderr = sys.__stderr__




























    
    
    


















api_morning_mindata_production_runas_admin.bat


for /f "delims=" %%# in ('powershell get-date -format "{yyyyMMddHHmmss}"') do @set mytimestamp=%%#
echo %mytimestamp%




::  *> mean redirect all stream including output, error, warning
:: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_redirection?view=powershell-5.1
:: & is the call operator (ampersand) which allows you to execute a command, a script, or a function.
:: if use &, it won't show output to screen


set log1=C:\Users\jonathanjames\aws\notebooks\index_analysis\log\stan_out_mindata_admin_%mytimestamp%_batlog.log
powershell -command "& C:\Users\jonathanjames\aws\notebooks\index_analysis\IB_live_trade\api_morning_mindata_production.bat *> %log1% -Verb runas"





    
    
    





































api_morning_mindata_production.bat


@echo off

for /f "delims=" %%# in ('powershell get-date -format "{yyyyMMddHHmmss}"') do @set mytimestamp=%%#
echo %mytimestamp%


set a1=C:\Users\jonathanjames\Desktop\python\WPy-3670\python-3.6.7.amd64\python.exe
set a2=C:\Users\jonathanjames\aws\notebooks\materials-python-dash\dash_example\dash_example_data_processing_window.py
set log0=C:\Users\jonathanjames\aws\notebooks\index_analysis\log\stan_out_dash.log
::echo jamesnch dash
:: jamesnch python dash
:: Start-Process is to trigger this process and without waiting for it to end, and immediately do next step. but don't know how to output log explore later
:: if no -NoNewWindow, it will open a new cmd window to run this process
:: if add -NoNewWindow, it won't have new window.
::powershell -command "Start-Process -NoNewWindow %a1% %a2%"
::powershell -command "Start-Process %a1% %a2%"

::echo jamesnched dash at http://127.0.0.1:8050/

::can directly run this command in power shell
::C:\Users\jonathanjames\Desktop\python\WPy-3670\python-3.6.7.amd64\python.exe C:\Users\jonathanjames\aws\notebooks\index_analysis\IB_live_trade\api_morning_mindata_production_main.py 2>&1 | tee C:\Users\jonathanjames\aws\notebooks\index_analysis\log\stan_out_mindata_temp2.log > C:\Users\jonathanjames\aws\notebooks\index_analysis\log\stan_out_mindata_temp.log

set a=C:\Users\jonathanjames\Desktop\python\WPy-3670\python-3.6.7.amd64\python.exe
set b=C:\Users\jonathanjames\aws\notebooks\index_analysis\IB_live_trade\api_morning_mindata_production_main.py
set log1=C:\Users\jonathanjames\aws\notebooks\index_analysis\log\stan_out_mindata_%mytimestamp%_batlog.log
set log2=C:\Users\jonathanjames\aws\notebooks\index_analysis\log\stan_out_mindata_temp.log
::set log1=C:\Users\jonathanjames\Desktop\try\stan_out_mindata_temp.log

:: this is normally ouput 1 log
::powershell -command "%a% %b% 2>&1 > %log1%" 

:: output 2 logs
powershell -command "%a% %b% 2>&1 | tee %log1% > %log2%"


::timeout /t 60 /nobreak






run_python_dash.bat

set a1=C:\Users\jonathanjames\Desktop\python\WPy-3670\python-3.6.7.amd64\python.exe
set a2=C:\Users\jonathanjames\aws\notebooks\materials-python-dash\dash_example\dash_example_data_processing_window.py
echo jamesnch dash
powershell -command "Start-Process %a1% %a2%"
echo jamesnched dash at http://127.0.0.1:8050/












us_stock_factor.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 10:45:19 2021

@author: root
"""


#############################
#######create factors########
#############################

import os
import datetime
import numpy as np
from numpy import inf
import time
import pandas as pd
from datetime import datetime as dt
from pandas import read_excel
#os.chdir(r'C:\Users\jonathanjames\aws\notebooks\index_analysis')
os.chdir('/home/jonathanjames/aws/notebooks/index_analysis')
os.chdir("/home/jonathanjames/my_storage/tradelog/index_analysis_cumulative")


hsi_y_path='backtest_linux/database/hkex/hsi_y.xlsx'
tidy_path='backtest_linux/database/tidy'












import numpy as np
import talib
from talib import abstract
import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt

def psar(barsdata,d_name,o_name,h_name,l_name,c_name, iaf = 0.02, maxaf = 0.2):
    length = len(barsdata)
    dates = list(barsdata[d_name])
    open_price=list(barsdata[o_name])
    high = list(barsdata[h_name])
    low = list(barsdata[l_name])
    close = list(barsdata[c_name])
    psar = close[0:len(close)]
    psarbull = [None] * length
    psarbear = [None] * length
    bull = True
    af = iaf
    ep = low[0]
    hp = high[0]
    lp = low[0]
    
    for i in range(2,length):
        if bull:
            psar[i] = psar[i - 1] + af * (hp - psar[i - 1])
        else:
            psar[i] = psar[i - 1] + af * (lp - psar[i - 1])
        
        reverse = False
        
        if bull:
            if low[i] < psar[i]:
                bull = False
                reverse = True
                psar[i] = hp
                lp = low[i]
                af = iaf
        else:
            if high[i] > psar[i]:
                bull = True
                reverse = True
                psar[i] = lp
                hp = high[i]
                af = iaf
    
        if not reverse:
            if bull:
                if high[i] > hp:
                    hp = high[i]
                    af = min(af + iaf, maxaf)
                if low[i - 1] < psar[i]:
                    psar[i] = low[i - 1]
                if low[i - 2] < psar[i]:
                    psar[i] = low[i - 2]
            else:
                if low[i] < lp:
                    lp = low[i]
                    af = min(af + iaf, maxaf)
                if high[i - 1] > psar[i]:
                    psar[i] = high[i - 1]
                if high[i - 2] > psar[i]:
                    psar[i] = high[i - 2]
                    
        if bull:
            psarbull[i] = psar[i]
        else:
            psarbear[i] = psar[i]

    return {"dates":dates, "open":open_price,"high":high, "low":low, "close":close, "psar":psar, "psarbear":psarbear, "psarbull":psarbull}



#data=HSI_source.copy()
#datenum_field='DateNum'
#target_field='smaBuy_original'
#decay=5
    
#datenum is in decending order


data1=pd.DataFrame({'Datenum':[17010,17000,16990],'nfp': [0,5,8]}) 
ema_custom_v2(data1,'Datenum','nfp',5)











import sys
import os





#find symbol data start date
train_test_Setting = read_excel(os.path.join('index_table_v2_for_test_backtest.xlsx'),'note')

alls=list(train_test_Setting.loc[~pd.isnull(train_test_Setting['Symbol']),'Symbol'].values)
#alls=list(train_test_Setting.loc[~pd.isnull(train_test_Setting['Symbol_nasdaq100']),'Symbol_nasdaq100'].values)

i='AAPL'
alld=[]
for i in alls:
    vars()[i] = read_excel(os.path.join(tidy_path,i+'_with_tidy.xlsx'),'Sheet1')
    alld.append(vars()[i]['Date2'].values[0])

alldf=pd.DataFrame({'name':alld})


selection_target_all=['AAPL','MSFT','NVDA','BRK.B','JPM','JNJ']
#selection_target_all=['V','PG','HD','DIS','ADBE','MA']


#selection_target_all=['CMCSA','NFLX','CRM','ABT']


selection_target_all=['AAPL','MSFT','NVDA','BRK.B','JPM','JNJ',
                      'UNH','V','PG','HD','DIS','ADBE',
                      'BAC','MA','CMCSA','NFLX','CRM','ABT',
                      'XOM','VZ']


selection_target_all=['TMO','KO','PEP','ACN',
'INTC',
'DHR',
'COST',
'NKE',
'LLY',
'WMT']

selection_target_all=['T',
'MRK',
'CVX',
'MDT',
'WFC',
'MCD']




selection_target_all=['TXN',
'NEE',
'ORCL',
'LIN',
'QCOM',
'HON',
'INTU',
'MS',
'BMY',
'C'
]


selection_target_all=['LOW',
'UNP',
'UPS',
'SBUX',
'AMT',
'GS',
'BLK',
'AMD',
'ISRG',
'AMGN']










selection_target_all=[
'RTX',
'IBM',
'AMAT',
'TGT',
'BA',
'DE',
'CVS',
'CAT',
'GE',
'MMM']

selection_target_all=[
'SPGI',
'SCHW',
'AXP',
'PLD',
'BKNG',
'MO',
'SYK',
'ANTM',
'GILD',
'ADI']

selection_target_all=['ADP',
'LMT',
'MDLZ',
'CCI',
'TJX',
'LRCX',
'CB',
'PNC',
'MU',
'DUK']


selection_target_all=['MMC',
'FIS',
'EQIX',
'EL',
'EW',
'BDX',
'USB',
'TFC',
'COP',
'CI']


selection_target_all=['CSX',
'SHW',
'SO',
'REGN',
'COF',
'FISV',
'CME',
'ILMN']



#final 20 fo s&p
selection_target_all=[
'MSFT',
'JPM',
'UNH',
'V',
'BAC',
'CMCSA',
'NFLX',
'WFC',
'MCD',
'TXN',
'LIN',
'AMT',
'BA',
'DE',
'GILD',
'MNST','VRTX','EA','SWKS','IP']



selection_target_all=[
"ADSK",
"ATVI",
"ASML",
"MRVL",
"IDXX"

]

selection_target_all=[
"MAR",
"ALGN",
"KLAC",
"KDP",
"LULU"

]


selection_target_all=[
"EBAY",
"EXC",
"MNST",
"VRTX",
"SNPS"]



selection_target_all=[
"PAYX",
"BIIB",
"ORLY",
"AEP",
"CDNS"]



selection_target_all=[
"CTAS",
"WBA",
"BIDU",
"MCHP",
"EA"]


selection_target_all=[
"CTSH",
"XLNX",
"ROST",
"XEL",
"CPRT"]

selection_target_all=[
"FAST",
"ANSS",
"SGEN",
"PCAR",
"NTES"]





selection_target_all=[
"SWKS",
"SIRI",
"VRSN",
"DLTR",
"CERN"]



selection_target_all=[
"TCOM",
"CHKP",
"INCY"]

selection_target_all=[
"TGT",
"AXP",
"CVS",
"CAT",
"SPGI"]




selection_target_all=[
"ICE",
"AON",
"NSC",
"CL",
"BSX"]



selection_target_all=[
"ITW",
"ETN",
"D",
"WM",
"MCO"]


selection_target_all=[
"F",
"APD",
"EMR",
"NOC",
"FDX"]


selection_target_all=[
"ECL",
"PGR",
"CMG",
"HUM",
"FCX"]




selection_target_all=[
"MSCI",
"EOG",
"JCI",
"AIG",
"TEL"]




selection_target_all=[
"ROP",
"A",
"MET",
"GPN",
"GD"]


selection_target_all=[
'LHX',
'PSA',
'APH',
'KMB',
'TROW']




selection_target_all=[
'TT',
'PRU',
'PXD',
'DLR',
'BAX']

selection_target_all=[
'IP',
'TRMB',
'HAL',
'CRL',
'ETR']


selection_target_all=[
'NTRS',
'VMC',
'TSN',
'EXR',
'HES',
'DOV',
'NDAQ',
'TSCO',
'MLM',
'DTE']




A_all=pd.DataFrame([])
for k in selection_target_all:
    pp=pd.DataFrame(np.array([k]*7*21))
    A_all=A_all.append(pp)



selection_target='V'
for selection_target in selection_target_all:
    HSI_source=pd.read_excel(os.path.join('backtest_linux/database/tidy',selection_target+'_with_tidy.xlsx'),'Sheet1')
    #HSI_source=pd.read_excel(selection_target+'_with_tidy.xlsx','Sheet1')
    t1='Open_'+selection_target
    t2='High_'+selection_target
    t3='Low_'+selection_target
    t4='Close_'+selection_target
    t5='Volume_'+selection_target
    t6=selection_target+'_change'
    HSI_source=HSI_source.rename(columns={t1:'open',t2:'high',t3:'low',t4:'close',t5:'volume',t6:'HSI_change'})
    
    HSI_source=HSI_source.loc[HSI_source['Date2']>='1997-01-01',['Date2','open','high','low','close','volume','HSI_change','DateNum']].copy()
    
    

    
    
    #or use normal response
    HSI_source['Y_up_cum_final']=HSI_source.apply(lambda row: (row.close>=row.open)*1,axis=1)
    HSI_source['Y_down_cum_final']=HSI_source.apply(lambda row: (row.close<row.open)*1,axis=1)
    
    
    
    
    #date need to be ascending order
    result = psar(HSI_source,d_name='Date2',o_name='open',h_name='high',l_name='low',c_name='close',iaf = 0.02, maxaf = 0.2) #iaf 0.02
    
    out=pd.DataFrame({'Date2':result['dates'], "open":result['open'],"high":result['high'], "low":result['low'],'close':result['close'],'psar':result['psar'],'psarbear':result['psarbear'],'psarbull':result['psarbull']})
    out['DateNum']=out['Date2'].apply(lambda x :(dt.strptime(x,"%Y-%m-%d")-dt(1970,1,1)).days)
    
    
    out['psarbear_high_diff']=out['psarbear']-out['high']
    out['psarbull_low_diff']=out['low']-out['psarbull']
    out['Date3'] = [dt.strptime(x, '%Y-%m-%d') for x in out['Date2']]
    #out=out[0:-1]
    
    
#    plt.plot(out['Date3'], out['close'])
#    plt.plot(out['Date3'], out['psarbull'])
#    plt.plot(out['Date3'], out['psarbear'])
#    plt.grid()
#    plt.show()
    
    
    
    
    out['sar_up']=out['psarbull'].shift(1)
    out['sar_down']=out['psarbear'].shift(1)
    out.loc[~(pd.isnull(out['sar_up'])),'sar_up_indicator']=1
    out.loc[~(pd.isnull(out['sar_down'])),'sar_down_indicator']=1
    out['sar_up_indicator']=out['sar_up_indicator'].fillna(0)
    out['sar_down_indicator']=out['sar_down_indicator'].fillna(0)
    out['sar_indicator']=out['sar_up_indicator']-out['sar_down_indicator']
    
    out['sar_up']=out['sar_up'].fillna(0)
    out['sar_down']=out['sar_down'].fillna(0)
    out['sar_value_indicator']=out['sar_up']-out['sar_down']
    
    
    
    out['sar_up2']=out['psarbull_low_diff'].shift(1)
    out['sar_down2']=out['psarbear_high_diff'].shift(1)
    out['sar_up2']=out['sar_up2'].fillna(0)
    out['sar_down2']=out['sar_down2'].fillna(0)
    out['sar_value2_indicator']=out['sar_up2']-out['sar_down2']
    
    #out.loc[out['sar_up2']<=1000,'sar_up2']=0
    #out.loc[out['sar_down2']<=1000,'sar_down2']=0
    
    
    
    
    
    HSI_source=pd.merge(HSI_source,out[['Date2','sar_up','sar_down',
                                    'sar_up_indicator', 'sar_down_indicator',
                                    'sar_indicator',
                                    'sar_value_indicator',
                                    'sar_up2', 'sar_down2',
                                    'sar_value2_indicator']],how='left',left_on=['Date2'],right_on=['Date2'])

    #for making -1 0 1
    HSI_source['sar_down_indicator']=HSI_source['sar_down_indicator'].copy()
    HSI_source['sar_up_indicator']=HSI_source['sar_up_indicator']*-1    
    
    
    #hsi_y_x_temp2=hsi_y_x.copy()
    
    #hsi_y_x=hsi_y_x_temp2.copy()
    
    
    import numpy as np
    import pandas as pd
    import talib
    from talib import abstract
    #date need to be arranged in ascending order using ta-lib
    
    
    
    
    # Calculate parabolic sar
    HSI_source['SAR'] = abstract.SAR(HSI_source,acceleration=0.02, maximum=0.2)
    HSI_source['SAREXT'] = abstract.SAREXT(HSI_source)
    
    
    
#    # Plot Parabolic SAR with close price
#    HSI_source[['close', 'SAR']][:500].plot(figsize=(10,5))
#    plt.grid()
#    plt.show()
    
    
    
    
    #sar use percentile
    HSI_source.loc[HSI_source['SAR']>=HSI_source['high'],'sar_talib_down2']=HSI_source['SAR']-HSI_source['high']
    HSI_source.loc[HSI_source['SAR']<=HSI_source['low'],'sar_talib_up2']=HSI_source['low']-HSI_source['SAR']
    
    HSI_source['sar_talib_down2_shift1']=HSI_source['sar_talib_down2'].shift(1)
    HSI_source['sar_talib_down2_shift1']=HSI_source['sar_talib_down2_shift1'].fillna(0)
    HSI_source['sar_talib_up2_shift1']=HSI_source['sar_talib_up2'].shift(1)
    HSI_source['sar_talib_up2_shift1']=HSI_source['sar_talib_up2_shift1'].fillna(0)
    
    HSI_source['year_cohord']=HSI_source['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y")).astype(int)
    HSI_source['sar_talib_modified']=HSI_source['sar_talib_up2_shift1']-HSI_source['sar_talib_down2_shift1']
    
    HSI_source['sar_talib_modified_original']=HSI_source['sar_talib_modified'].copy()
    
    
    target_variable='sar_talib_modified_original'
    
    
    distinct_year=HSI_source['year_cohord'].unique()
    distinct_year=[i for i in distinct_year if i >=1999]
    yy=2010
    percentile_cum=pd.DataFrame([])
    for yy in distinct_year:
        data_use=HSI_source.loc[HSI_source['year_cohord']<yy,target_variable].values
        first_percentile_capture=np.nanpercentile(data_use,25)
        second_percentile_capture=np.nanpercentile(data_use,50)
        third_percentile_capture=np.nanpercentile(data_use,75)
        t1='first_percentile_'+target_variable
        t2='second_percentile_'+target_variable
        t3='third_percentile_'+target_variable
        percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                           t1:[first_percentile_capture],
                                                           t2:[second_percentile_capture],
                                                           t3:[third_percentile_capture]}))
    
    
    HSI_source=pd.merge(HSI_source,percentile_cum,how='left',on=['year_cohord'])
    a_check=HSI_source.tail(1000)
    
    new_var=target_variable+'_percentile'
    HSI_source.loc[(HSI_source[target_variable]<=HSI_source[t1])|(HSI_source[target_variable]>=HSI_source[t3]),new_var]=HSI_source[target_variable]
    HSI_source.loc[HSI_source[target_variable]<=HSI_source[t1],new_var+'lower']=HSI_source[target_variable]*-1
    HSI_source.loc[HSI_source[target_variable]>=HSI_source[t3],new_var+'upper']=HSI_source[target_variable]
    HSI_source[new_var+'lower']=HSI_source[new_var+'lower'].fillna(0)
    HSI_source[new_var+'upper']=HSI_source[new_var+'upper'].fillna(0)
    
    #for making -1 0 1
    HSI_source.loc[HSI_source[new_var+'lower']>0,new_var+'lower']=1
    HSI_source.loc[HSI_source[new_var+'upper']>0,new_var+'upper']=-1
    
    
    HSI_source[new_var]=HSI_source[new_var].fillna(0)
    
    
    
    #muli 
    vector_arith_multi=abstract.MULT(HSI_source)
    HSI_source['vector_arith_multi']=vector_arith_multi
    HSI_source['vector_arith_multi_shift1']=HSI_source['vector_arith_multi'].shift(1)
    
    
    #help(abstract.MULT)
    
    
    #linear
    linint=abstract.LINEARREG_INTERCEPT(HSI_source)
    HSI_source['linint']=linint
    HSI_source['linint_shift1']=HSI_source['linint'].shift(1)
    HSI_source['linint_change']=(HSI_source['linint']-HSI_source['linint_shift1'])/HSI_source['linint_shift1']
    HSI_source['linint_shift1_change']=HSI_source['linint_change'].shift(1)
    
    
    
    #ad  Chaikin A/D Line
    ad=abstract.AD(HSI_source)
    HSI_source['ad']=ad
    HSI_source['ad_shift1']=HSI_source['ad'].shift(1)
    HSI_source['ad_change']=(HSI_source['ad']-HSI_source['ad_shift1'])/HSI_source['ad_shift1']
    HSI_source['ad_change_shift1']=HSI_source['ad_change'].shift(1)
    
    #for making -1 0 1
    HSI_source['ad_change_shift1_temp']=HSI_source['ad_change_shift1'].copy()
    del HSI_source['ad_change_shift1']
    HSI_source.loc[HSI_source['ad_change_shift1_temp']>0,'ad_change_shift1']=-1
    HSI_source.loc[HSI_source['ad_change_shift1_temp']<0,'ad_change_shift1']=1
    
    HSI_source.loc[(HSI_source['HSI_change']>=0)&(HSI_source['ad_change']<0),'ad1']=HSI_source['ad_change']
    HSI_source.loc[(HSI_source['HSI_change']<0)&(HSI_source['ad_change']>=0),'ad2']=HSI_source['ad_change']   
    HSI_source.loc[(HSI_source['HSI_change']>=0)&(HSI_source['ad_change']>=0),'ad3']=HSI_source['ad_change']
    HSI_source.loc[(HSI_source['HSI_change']<0)&(HSI_source['ad_change']<0),'ad4']=HSI_source['ad_change']
    
    #for making -1 0 1
    HSI_source.loc[HSI_source['ad1']<0,'ad1']=1
    HSI_source.loc[HSI_source['ad2']>0,'ad2']=-1    
    HSI_source.loc[HSI_source['ad3']>0,'ad3']=-1
    HSI_source.loc[HSI_source['ad4']<0,'ad4']=1     
    
    
    HSI_source['ad1_shift1']=HSI_source['ad1'].shift(1)
    HSI_source['ad2_shift1']=HSI_source['ad2'].shift(1)
    HSI_source['ad3_shift1']=HSI_source['ad3'].shift(1)
    HSI_source['ad4_shift1']=HSI_source['ad4'].shift(1)
    
    
    
    
    
    
    
    HSI_source=HSI_source.fillna(0)
    
    
    
    
    
    
    
    
    
    
    
    
    
    #OBV  On-Balance Volume  https://www.fmlabs.com/reference/default.htm?url=OBV.htm
    obv=abstract.OBV(HSI_source)
    HSI_source['obv']=obv
    HSI_source['obv_shift1']=HSI_source['obv'].shift(1)
    HSI_source['obv_change']=(HSI_source['obv']-HSI_source['obv_shift1'])
    
    
    HSI_source.loc[(HSI_source['HSI_change']>=0)&(HSI_source['obv_change']<0),'obv1']=HSI_source['obv_change']
    HSI_source.loc[(HSI_source['HSI_change']<0)&(HSI_source['obv_change']>=0),'obv2']=HSI_source['obv_change']
    HSI_source.loc[(HSI_source['HSI_change']>=0)&(HSI_source['obv_change']>=0),'obv3']=HSI_source['obv_change']
    HSI_source.loc[(HSI_source['HSI_change']<0)&(HSI_source['obv_change']<0),'obv4']=HSI_source['obv_change']


    
    #for making -1 0 1
    HSI_source.loc[HSI_source['obv3']>0,'obv3']=-1
    HSI_source.loc[HSI_source['obv4']<0,'obv4']=1 
    
    
    HSI_source['obv1_shift1']=HSI_source['obv1'].shift(1)
    HSI_source['obv2_shift1']=HSI_source['obv2'].shift(1)
    HSI_source['obv3_shift1']=HSI_source['obv3'].shift(1)
    HSI_source['obv4_shift1']=HSI_source['obv4'].shift(1)
    HSI_source=HSI_source.fillna(0)
    
    
    
    
    
    
    
    #money flow 14
    moneyflow=abstract.MFI(HSI_source,14)
    HSI_source['moneyflow']=moneyflow
    HSI_source['moneyflow_shift1']=HSI_source['moneyflow'].shift(1)
    HSI_source.loc[(HSI_source['moneyflow_shift1']<=20),'moneyflow_up']=HSI_source['moneyflow_shift1']
    HSI_source['moneyflow_up']=HSI_source['moneyflow_up'].fillna(0)
    
    HSI_source.loc[(HSI_source['moneyflow_shift1']>=80),'moneyflow_down']=HSI_source['moneyflow_shift1']
    HSI_source['moneyflow_down']=HSI_source['moneyflow_down'].fillna(0)
    
    
    
    
    
    
    
    
    #william 14
    william=abstract.WILLR(HSI_source,14)
    HSI_source['william']=william*-1
    HSI_source['william_shift1']=HSI_source['william'].shift(1)
    HSI_source.loc[(HSI_source['william_shift1']<=20),'william_up']=HSI_source['william_shift1']
    HSI_source['william_up']=HSI_source['william_up'].fillna(0)
    
    HSI_source.loc[(HSI_source['william_shift1']>=80),'william_down']=HSI_source['william_shift1']
    HSI_source['william_down']=HSI_source['william_down'].fillna(0)
    
    
    #for making -1 0 1
    HSI_source.loc[HSI_source['william_up']>0,'william_up']=-1
    HSI_source.loc[HSI_source['william_down']>0,'william_down']=1 
    
    
    
    
    
    
    #UltimateOscillator 14
    
    UltimateOscillator=abstract.ULTOSC(HSI_source, timeperiod1=7, timeperiod2=14, timeperiod3=28)
    HSI_source['UltimateOscillator']=UltimateOscillator
    HSI_source['UltimateOscillator_shift1']=HSI_source['UltimateOscillator'].shift(1)
    HSI_source.loc[(HSI_source['UltimateOscillator_shift1']<=30),'UltimateOscillator_up']=HSI_source['UltimateOscillator_shift1']
    HSI_source['UltimateOscillator_up']=HSI_source['UltimateOscillator_up'].fillna(0)
    
    HSI_source.loc[(HSI_source['UltimateOscillator_shift1']>=70),'UltimateOscillator_down']=HSI_source['UltimateOscillator_shift1']
    HSI_source['UltimateOscillator_down']=HSI_source['UltimateOscillator_down'].fillna(0)
    
    
    
    
    
    
    
    #true range
    
    truerange_plus=abstract.PLUS_DM(HSI_source,timeperiod=14)
    truerange_minus=abstract.MINUS_DM(HSI_source,timeperiod=14)
    HSI_source['truerange_plus']=truerange_plus
    HSI_source['truerange_minus']=truerange_minus
    
    HSI_source['truerange_plus_shift1']=HSI_source['truerange_plus'].shift(1)
    HSI_source['truerange_minus_shift1']=HSI_source['truerange_minus'].shift(1)
    
    HSI_source['truerange']=HSI_source['truerange_plus_shift1']-HSI_source['truerange_minus_shift1']
    
    
    HSI_source.loc[(HSI_source['truerange']>=0),'truerange_up']=HSI_source['truerange']
    HSI_source['truerange_up']=HSI_source['truerange_up'].fillna(0)
    
    HSI_source.loc[(HSI_source['truerange']<0),'truerange_down']=HSI_source['truerange']
    HSI_source['truerange_down']=HSI_source['truerange_down'].fillna(0)
    HSI_source['truerange_down']=HSI_source['truerange_down']*-1
    
    #for making -1 0 1
    HSI_source.loc[HSI_source['truerange_up']>0,'truerange_up']=-1
    HSI_source.loc[HSI_source['truerange_down']>0,'truerange_down']=1
    
    
    
    
    
    #DX
    directmove=abstract.DX(HSI_source,14)
    HSI_source['directmove']=directmove
    HSI_source['directmove_shift1']=HSI_source['directmove'].shift(1)
    HSI_source.loc[(HSI_source['directmove_shift1']>=50),'directmove_up']=HSI_source['directmove_shift1']
    HSI_source['directmove_up']=HSI_source['directmove_up'].fillna(0)
    
    HSI_source.loc[(HSI_source['directmove_shift1']<=2),'directmove_down']=HSI_source['directmove_shift1']
    HSI_source['directmove_down']=HSI_source['directmove_down'].fillna(0)
    
    #for making -1 0 1
    HSI_source.loc[HSI_source['directmove_up']>0,'directmove_up']=-1
    HSI_source.loc[HSI_source['directmove_down']>0,'directmove_down']=1
    
    
    
    #bop
    balancepower=abstract.BOP(HSI_source,14)
    HSI_source['balancepower']=balancepower
    HSI_source['balancepower_shift1']=HSI_source['balancepower'].shift(1)
    HSI_source.loc[(HSI_source['balancepower_shift1']>=0),'balancepower_up']=HSI_source['balancepower_shift1']
    HSI_source['balancepower_up']=HSI_source['balancepower_up'].fillna(0)
    
    HSI_source.loc[(HSI_source['balancepower_shift1']<0),'balancepower_down']=HSI_source['balancepower_shift1']
    HSI_source['balancepower_down']=HSI_source['balancepower_down'].fillna(0)
    
    
    
    #for making -1 0 1
    HSI_source.loc[HSI_source['balancepower_up']>0,'balancepower_up']=-1
    HSI_source.loc[HSI_source['balancepower_down']<0,'balancepower_down']=1 
    
    
    
    
    #aroon OSC  (up-down)
    aroon=abstract.AROONOSC(HSI_source,14)
    HSI_source['aroon']=aroon
    HSI_source['aroon_shift1']=HSI_source['aroon'].shift(1)
    HSI_source.loc[(HSI_source['aroon_shift1']>=0),'aroon_up']=HSI_source['aroon_shift1']
    HSI_source['aroon_up']=HSI_source['aroon_up'].fillna(0)
    
    HSI_source.loc[(HSI_source['aroon_shift1']<0),'aroon_down']=HSI_source['aroon_shift1']
    HSI_source['aroon_down']=HSI_source['aroon_down'].fillna(0)
    
    #for making -1 0 1
    HSI_source.loc[HSI_source['aroon_up']>0,'aroon_up']=-1
    HSI_source.loc[HSI_source['aroon_down']<0,'aroon_down']=1 
    
    
    
    
    HSI_source.loc[(HSI_source['aroon_shift1']>=70),'aroon_up_70']=HSI_source['aroon_shift1']
    HSI_source['aroon_up_70']=HSI_source['aroon_up_70'].fillna(0)
    HSI_source.loc[(HSI_source['aroon_shift1']<=-70),'aroon_down_70']=HSI_source['aroon_shift1']
    HSI_source['aroon_down_70']=HSI_source['aroon_down_70'].fillna(0)
    
    
    #for making -1 0 1
    HSI_source.loc[HSI_source['aroon_up_70']>0,'aroon_up_70']=-1
    HSI_source.loc[HSI_source['aroon_down_70']<0,'aroon_down_70']=1 
    
    
    
    target_variable='aroon_shift1'
    distinct_year=HSI_source['year_cohord'].unique()
    distinct_year=[i for i in distinct_year if i >=1999]
    yy=2010
    percentile_cum=pd.DataFrame([])
    for yy in distinct_year:
        data_use=HSI_source.loc[HSI_source['year_cohord']<yy,target_variable].values
        first_percentile_capture=np.nanpercentile(data_use,25)
        second_percentile_capture=np.nanpercentile(data_use,50)
        third_percentile_capture=np.nanpercentile(data_use,75)
        t1='first_percentile_'+target_variable
        t2='second_percentile_'+target_variable
        t3='third_percentile_'+target_variable
        percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                           t1:[first_percentile_capture],
                                                           t2:[second_percentile_capture],
                                                           t3:[third_percentile_capture]}))
    
    
    HSI_source=pd.merge(HSI_source,percentile_cum,how='left',on=['year_cohord'])
    a_check=HSI_source.tail(1000)
    
    new_var=target_variable+'_percentile'
    HSI_source.loc[(HSI_source[target_variable]<=HSI_source[t1])|(HSI_source[target_variable]>=HSI_source[t3]),new_var]=HSI_source[target_variable]
    HSI_source.loc[HSI_source[target_variable]<=HSI_source[t1],new_var+'lower']=HSI_source[target_variable]*-1
    HSI_source.loc[HSI_source[target_variable]>=HSI_source[t3],new_var+'upper']=HSI_source[target_variable]
    HSI_source[new_var+'lower']=HSI_source[new_var+'lower'].fillna(0)
    HSI_source[new_var+'upper']=HSI_source[new_var+'upper'].fillna(0)


    #for making -1 0 1
    HSI_source.loc[HSI_source[new_var+'lower']>0,new_var+'lower']=1
    HSI_source.loc[HSI_source[new_var+'upper']>0,new_var+'upper']=-1


    HSI_source[new_var]=HSI_source[new_var].fillna(0)
    
    
    
    
    
    
    #short ema over long ema
    shortSMA=abstract.SMA(HSI_source,7)
    longSMA=abstract.SMA(HSI_source,200)
    HSI_source['shortSMA'] = shortSMA
    HSI_source['longSMA'] =longSMA
    HSI_source['smaSell'] = ((shortSMA.shift(1) <= longSMA.shift(1)) & (shortSMA.shift(2) >= longSMA.shift(2)))
    HSI_source['smaBuy'] = ((shortSMA.shift(1) >= longSMA.shift(1)) & (shortSMA.shift(2) <= longSMA.shift(2)))
    
    HSI_source['smaSell']=HSI_source['smaSell']*1
    HSI_source['smaBuy']=HSI_source['smaBuy']*1
    
    
    #for making -1 0 1
    HSI_source.loc[HSI_source['smaSell']>0,'smaSell']=-1



    
    HSI_source['smaSell_original']=HSI_source['smaSell'].shift(-1)
    HSI_source['smaBuy_original']=HSI_source['smaBuy'].shift(-1)
    
#    HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=False)
#    HSI_source=ema_custom_v2(HSI_source,'DateNum','smaSell_original',5)
#    HSI_source=ema_custom_v2(HSI_source,'DateNum','smaBuy_original',5)
#    HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=True)
    
    
    
    #short ema over long ema
    shortSMA=abstract.SMA(HSI_source,3)
    longSMA=abstract.SMA(HSI_source,10)
    HSI_source['shortSMA'] = shortSMA
    HSI_source['longSMA'] =longSMA
    HSI_source['smaSell'] = ((shortSMA.shift(1) <= longSMA.shift(1)) & (shortSMA.shift(2) >= longSMA.shift(2)))
    HSI_source['smaBuy'] = ((shortSMA.shift(1) >= longSMA.shift(1)) & (shortSMA.shift(2) <= longSMA.shift(2)))
    
    HSI_source['smaSell']=HSI_source['smaSell']*1
    HSI_source['smaBuy']=HSI_source['smaBuy']*1
    
    HSI_source['smaSell_original2']=HSI_source['smaSell'].shift(-1)
    HSI_source['smaBuy_original2']=HSI_source['smaBuy'].shift(-1)
    
#    HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=False)
#    HSI_source=ema_custom_v2(HSI_source,'DateNum','smaSell_original2',5)
#    HSI_source=ema_custom_v2(HSI_source,'DateNum','smaBuy_original2',5)
#    HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=True)
    
    
    
    #CDL3OUTSIDE - Three Outside Up/Down
    pattern1 = abstract.CDL3OUTSIDE(HSI_source)
    HSI_source['pattern1']=pattern1
    HSI_source['pattern1']=HSI_source['pattern1'].shift(1)
    HSI_source.loc[(HSI_source['pattern1']>0),'pattern1_positive']=HSI_source['pattern1']
    HSI_source['pattern1_positive']=HSI_source['pattern1_positive'].fillna(0)
    
    HSI_source.loc[(HSI_source['pattern1']<0),'pattern1_negative']=HSI_source['pattern1']
    HSI_source['pattern1_negative']=HSI_source['pattern1_negative'].fillna(0)
    
    
    
    #cci
    cci = abstract.CCI(HSI_source)
    HSI_source['cci']=cci
    HSI_source['cci']=HSI_source['cci'].shift(1)
    HSI_source.loc[(HSI_source['cci']>100),'cci_down']=HSI_source['cci']
    HSI_source.loc[(HSI_source['cci']<-100),'cci_up']=HSI_source['cci']*-1
    
    #for making -1 0 1
    HSI_source.loc[HSI_source['cci_down']>0,'cci_down']=-1
    HSI_source.loc[HSI_source['cci_up']>0,'cci_up']=1    
    

    HSI_source=HSI_source.fillna(0)
    
    
    
    
    #CMO - Chande Momentum Oscillator
    t_var='cmo'
    vars()[t_var] = abstract.CMO(HSI_source, timeperiod=14)
    HSI_source[t_var]=vars()[t_var]
    HSI_source[t_var]=HSI_source[t_var].shift(1)
    HSI_source.loc[(HSI_source[t_var]>50),t_var+'_down']=HSI_source[t_var]
    HSI_source.loc[(HSI_source[t_var]<-50),t_var+'_up']=HSI_source[t_var]
    
    
    #for making -1 0 1
    HSI_source.loc[HSI_source[t_var+'_up']<0,t_var+'_up']=1
    HSI_source.loc[HSI_source[t_var+'_down']>0,t_var+'_down']=-1 
    
    
    HSI_source=HSI_source.fillna(0)
    
    
    
    #MOM - Momentum
    t_var='mom'
    vars()[t_var] = abstract.MOM(HSI_source, timeperiod=10)
    HSI_source[t_var]=vars()[t_var]
    HSI_source[t_var]=HSI_source[t_var].shift(1)
    
    #for making -1 0 1
    HSI_source[t_var+'_temp']=HSI_source[t_var].copy()
    del HSI_source[t_var]
    HSI_source.loc[HSI_source[t_var+'_temp']>0,t_var]=-1
    HSI_source.loc[HSI_source[t_var+'_temp']<0,t_var]=1 
    
    HSI_source=HSI_source.fillna(0)



    
    
    
    #PPO - Percentage Price Oscillator
    t_var='ppo'
    vars()[t_var] = abstract.PPO(HSI_source,fastperiod=12, slowperiod=26, matype=0)
    HSI_source[t_var]=vars()[t_var]
    HSI_source[t_var]=HSI_source[t_var].shift(1)
    HSI_source.loc[(HSI_source[t_var]>0),t_var+'_up']=HSI_source[t_var]
    HSI_source.loc[(HSI_source[t_var]<0),t_var+'_down']=HSI_source[t_var]*-1
    
    
    #for making -1 0 1
    HSI_source.loc[HSI_source[t_var+'_up']>0,t_var+'_up']=1
    HSI_source.loc[HSI_source[t_var+'_down']>0,t_var+'_down']=-1 
    
    
    HSI_source=HSI_source.fillna(0)
    
    
    
    
    
    
    
    
    #BBANDS - Bollinger Bands
    bb = abstract.BBANDS(HSI_source, timeperiod=5, nbdevup=2.0, nbdevdn=2.0, matype=0)
    HSI_source['bb_down']=(bb['upperband']-HSI_source.close).shift(1)
    HSI_source['bb_up']=(HSI_source.close-bb['lowerband']).shift(1)
    
    
    #https://phemex.com/academy/what-is-mesa-adaptive-moving-average#:~:text=The%20MESA%20Adaptive%20Moving%20Average,value%20and%20signals%20market%20trends.
    #MAMA - MESA Adaptive Moving Average
    #If the MAMA crosses the FAMA line from below and moves higher, the market tends to be bullish, 
    #and traders frequently consider this as a buy signal. On the other hand, when the MAMA line crosses
    # the FAMA from above and shifts underneath, the market is considered to be undergoing a bearish trend
    #, which is generally a strong signal for investors to enter short positions.
    mama = abstract.MAMA(HSI_source, fastlimit=0.5, slowlimit=0.5)
    shortSMA= mama.mama
    longSMA=mama.fama
    HSI_source['mamaSell'] = ((shortSMA.shift(1) <= longSMA.shift(1)) & (shortSMA.shift(2) >= longSMA.shift(2)))
    HSI_source['mamaBuy'] = ((shortSMA.shift(1) >= longSMA.shift(1)) & (shortSMA.shift(2) <= longSMA.shift(2)))
    
    HSI_source['mamaSell']=HSI_source['mamaSell']*1
    HSI_source['mamaBuy']=HSI_source['mamaBuy']*1
    
    
    #for making -1 0 1
    HSI_source.loc[HSI_source['mamaSell']>0,'mamaSell']=-1
    HSI_source.loc[HSI_source['mamaBuy']>0,'mamaBuy']=1 
    
    
    
    
    HSI_source['mamaSell_original']=HSI_source['mamaSell'].shift(-1)
    HSI_source['mamaBuy_original']=HSI_source['mamaBuy'].shift(-1)
    
#    HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=False)
#    HSI_source=ema_custom_v2(HSI_source,'DateNum','mamaSell_original',5)
#    HSI_source=ema_custom_v2(HSI_source,'DateNum','mamaBuy_original',5)
#    HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=True)
    
    
    
    
    #APO - Absolute Price Oscillator
    t_var='apo'
    vars()[t_var] = abstract.APO(HSI_source, fastperiod=12, slowperiod=26, matype=0)
    HSI_source[t_var]=vars()[t_var]
    HSI_source[t_var]=HSI_source[t_var].shift(1)
    HSI_source.loc[(HSI_source[t_var]>0),t_var+'_up']=HSI_source[t_var]
    HSI_source.loc[(HSI_source[t_var]<0),t_var+'_down']=HSI_source[t_var]*-1
    HSI_source=HSI_source.fillna(0)


    #for making -1 0 1
    HSI_source.loc[HSI_source[t_var]>0,t_var]=1
    HSI_source.loc[HSI_source[t_var]<0,t_var]=-1 

    
    
    
    
    
    
    #rsi
    t_var='rsi'
    vars()[t_var] = abstract.RSI(HSI_source, timeperiod=14)
    HSI_source[t_var]=vars()[t_var]
    HSI_source[t_var]=HSI_source[t_var].shift(1)
    HSI_source.loc[(HSI_source[t_var]>70),t_var+'_up']=HSI_source[t_var]
    HSI_source.loc[(HSI_source[t_var]<30),t_var+'_down']=HSI_source[t_var]
    HSI_source=HSI_source.fillna(0)
    
    
    
    #Stochastic Oscillator
    #%D values over 75 indicate an overbought condition; values under 25 indicate an oversold condition. 
    #When the Fast %D crosses above the Slow %D, it is a buy signal; when it crosses below, it is a sell signal.
    stock_o = abstract.STOCH(HSI_source, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    slowk=stock_o.slowk
    slowd=stock_o.slowd
    
    t_var='slowd'
    HSI_source[t_var]=slowd
    HSI_source[t_var]=HSI_source[t_var].shift(1)
    HSI_source.loc[(HSI_source[t_var]>75),t_var+'_down']=HSI_source[t_var]
    HSI_source.loc[(HSI_source[t_var]<25),t_var+'_up']=HSI_source[t_var]
    HSI_source=HSI_source.fillna(0)
    
    
    #for making -1 0 1
    HSI_source.loc[HSI_source[t_var+'_up']>0,t_var+'_up']=1
    HSI_source.loc[HSI_source[t_var+'_down']>0,t_var+'_down']=-1 
    
    
    
    
    
    shortSMA= slowd
    longSMA=slowk
    HSI_source['stock_oSell'] = ((shortSMA.shift(1) <= longSMA.shift(1)) & (shortSMA.shift(2) >= longSMA.shift(2)))
    HSI_source['stock_oBuy'] = ((shortSMA.shift(1) >= longSMA.shift(1)) & (shortSMA.shift(2) <= longSMA.shift(2)))
    
    HSI_source['stock_oSell']=HSI_source['stock_oSell']*1
    HSI_source['stock_oBuy']=HSI_source['stock_oBuy']*1
    
    HSI_source['stock_oSell_original']=HSI_source['stock_oSell'].shift(-1)
    HSI_source['stock_oBuy_original']=HSI_source['stock_oBuy'].shift(-1)
    
#    HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=False)
#    HSI_source=ema_custom_v2(HSI_source,'DateNum','stock_oSell_original',5)
#    HSI_source=ema_custom_v2(HSI_source,'DateNum','stock_oBuy_original',5)
#    HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=True)
    
    
    
    
    
    
    
    
    
    
    
    var_temp=[['sar_up_indicator','sar_down_indicator'],
    #['sar_value_indicator'],
    #['sar_up2', 'sar_down2'],
    #['sar_value2_indicator'],
    ['sar_talib_modified_original_percentilelower','sar_talib_modified_original_percentileupper'],
    #['sar_talib_modified_original_percentile'],
    ['ad_change_shift1'],
    ['ad3_shift1','ad4_shift1'],
    ['ad1_shift1','ad2_shift1'],
    ['obv3_shift1','obv4_shift1'],   #on balance volume
    #['moneyflow_up','moneyflow_down'],
    ['william_up','william_down'],
    #['UltimateOscillator_up','UltimateOscillator_down'],
    ['truerange_up','truerange_down'],
    ['directmove_up','directmove_down'],
    ['balancepower_up','balancepower_down'],
    #['aroon_shift1'],
    ['aroon_up','aroon_down'],
    ['aroon_up_70','aroon_down_70'],
    ['aroon_shift1_percentilelower','aroon_shift1_percentileupper'],
    ['smaBuy','smaSell'],
    #['EMA_smaSell_original','EMA_smaBuy_original'],
    #['EMA_smaSell_original2','EMA_smaBuy_original2'],
    #['pattern1_positive','pattern1_negative'],
    ['cci_up','cci_down'],
    ['cmo_up','cmo_down'],
    ['mom'],
    ['ppo_up','ppo_down'],
    #['bb_up','bb_down'],
    ['mamaSell','mamaBuy'],
    #['EMA_mamaSell_original','EMA_mamaBuy_original'],
    ['apo'],
    #['rsi_up','rsi_down'],
    ['slowd_down','slowd_up']]
    #['stock_oSell','stock_oBuy']
    #['EMA_stock_oBuy_original','EMA_stock_oSell_original']
    
    checklist=pd.DataFrame([])
    n1=0
    for ii in var_temp:  
        f2=['Date2']+ii
        #j=['MCDFX_change', 'MICDX_change']
        base_folder='/home/jonathanjames/aws/notebooks/index_analysis'
        
        
        
        use_factor_list3=f2.copy()
        out=''
        for i in use_factor_list3:
            out=out+"'"+i+"',"
        out="["+out[0:(len(out)-1)]+"]"
        
        
        n1=n1+1
        name='factor'+str(n1)+'.txt'
        target_file=os.path.join('factor',name)
        textfile = open(target_file, 'w')
        textfile.write(out)
        textfile.close()
        
        checklist=checklist.append(pd.DataFrame({'new_factor':[ii],'factor':[out],'filename':[name]}))
    
    #a_check=hsi_y_x[['sar_up_indicator','sar_down_indicator','sar_value_indicator','sar_up2', 'sar_down2','sar_value2_indicator']].copy()
    
    
    

    def change_permissions_recursive(temp_folder1, mode):
        for root, dirs, files in os.walk(temp_folder1, topdown=False):
            for dir in [os.path.join(root,d) for d in dirs]:
                os.chmod(dir, mode)
            for file in [os.path.join(root, f) for f in files]:
                os.chmod(file, mode)

    change_permissions_recursive('/home/jonathanjames/aws/notebooks/index_analysis/factor', 0o777)


    
    
    
    
    #random factor
    dim=HSI_source.shape[0]
    s=np.random.normal(0,1,dim)
    HSI_source['random1']=s
    HSI_source['random2']=s*-1
    
    s=np.random.normal(0,1,dim)
    HSI_source['random3']=s
    HSI_source['random4']=s*-1
    
    s=np.random.normal(0,1,dim)
    HSI_source['random5']=s
    HSI_source['random6']=s*-1
    
    s=np.random.normal(0,1,dim)
    HSI_source['random7']=s
    HSI_source['random8']=s*-1
    
    
    HSI_source['constant_factor']=1
    
    #save HSI_source as hsi_y_x
    out_name='hsi_y_x'+'_'+selection_target
    
    import numpy as np
    from pandas import HDFStore,DataFrame
    store = pd.HDFStore(out_name+'.hdf5', "w", complib=str("zlib"), complevel=5)
    store.put(out_name+'_dataframe',HSI_source, data_columns=HSI_source.columns)
    store.close()
    
#    writer = pd.ExcelWriter(out_name+'.xlsx', engine='xlsxwriter')
#    HSI_source.to_excel(writer, sheet_name='Sheet1')
#    writer.save()
#    writer.close()


















full_data_ticker=[]

selection_target='GSPC'
for selection_target in selection_target_all:
    HSI_source=pd.read_excel(os.path.join('backtest_linux/database/tidy',selection_target+'_with_tidy.xlsx'),'Sheet1')
    #HSI_source=pd.read_excel(selection_target+'_with_tidy.xlsx','Sheet1')
    t1='Open_'+selection_target
    t2='High_'+selection_target
    t3='Low_'+selection_target
    t4='Close_'+selection_target
    t6=selection_target+'_change'
    HSI_source=HSI_source.rename(columns={t1:'open',t2:'high',t3:'low',t4:'close',t6:'HSI_change'})
    
    HSI_source=HSI_source.loc[HSI_source['Date2']>='1990-01-01',['Date2','open','high','low','close','HSI_change','DateNum']].copy()

    #make usre the ticker has data at least from 1996
    if HSI_source.Date2.values[0]<='1996-01-01':
        full_data_ticker.append(selection_target)
        HSI_source['useless_factor']=1
        
        #save HSI_source as hsi_y_x
        out_name='hsi_y_x'+'_'+selection_target
        store = pd.HDFStore(out_name+'.hdf5', "w", complib=str("zlib"), complevel=5)
        store.put(out_name+'_dataframe',HSI_source, data_columns=HSI_source.columns)
        store.close()


A_all=pd.DataFrame([])
for k in full_data_ticker[0:100]:
    pp=pd.DataFrame(np.array([k]*25))
    A_all=A_all.append(pp)
















##create pair trade
#
#
#
#
#
##create hdf5 for sample indicator but use a useless_factor here
#import numpy as np
#from pandas import HDFStore,DataFrame
#from sklearn.linear_model import LinearRegression
#
##selection_target_all=s_temp.Code.values.tolist()[0:]
#
#selection_target_all=['V@MA']
#
#
#full_data_ticker=[]
#
#selection_target='BBY@AAPL'
#for selection_target in selection_target_all:
#    s1=selection_target.split('@')[0]
#    s2=selection_target.split('@')[1]
#    HSI_source=pd.read_excel(os.path.join('backtest_linux/database/tidy',s1+'_with_tidy.xlsx'),'Sheet1')
#    t1='Open_'+s1
#    t2='High_'+s1
#    t3='Low_'+s1
#    t4='Close_'+s1
#    t6=s1+'_change'
#    HSI_source=HSI_source.rename(columns={t1:'open',t2:'high',t3:'low',t4:'close',t6:'HSI_change'})    
#    HSI_source=HSI_source.loc[HSI_source['Date2']>='1998-01-01',['Date2','open','high','low','close','HSI_change','DateNum']].copy()
#    
#    HSI_source2=pd.read_excel(os.path.join('backtest_linux/database/tidy',s2+'_with_tidy.xlsx'),'Sheet1')
#    t1='Open_'+s2
#    t2='High_'+s2
#    t3='Low_'+s2
#    t4='Close_'+s2
#    t6=s2+'_change'
#    HSI_source2=HSI_source2.rename(columns={t1:'open',t2:'high',t3:'low',t4:'close',t6:'HSI_change'})    
#    HSI_source2=HSI_source2.loc[HSI_source2['Date2']>='1998-01-01',['Date2','open','high','low','close','HSI_change','DateNum']].copy()
#    
#    
#    new_name=s1+'_'+s2+'_pair'
#    HSI_source=pd.merge(HSI_source,HSI_source2[['Date2','open','close']].copy(),how='left',on=['Date2'],suffixes=('','_s2'))
#    
#    HSI_source['year_month']=HSI_source['Date2'].apply(lambda x:int(x.split('-')[0]+x.split('-')[1]))
#    
#    HSI_source_use=HSI_source.copy()
#    HSI_source_use['reg_coef']=np.nan
#    HSI_source_use['reg_intercept']=np.nan
#    
#    freq=6 #unit is month
#    
#    all_month=list(HSI_source['year_month'].unique())
#    all_month_use=all_month[freq:]
#    all_month=np.array(all_month)
#    
#    y=199902
#    for y in all_month_use:
#        start1=all_month[np.where(all_month==y)[0][0]-freq]
#        end1=all_month[np.where(all_month==y)[0][0]-1]
#        data_use=HSI_source.loc[(HSI_source['year_month']>=start1)&(HSI_source['year_month']<=end1),:].copy()
#        
#        y_use=data_use['close'].values
#        x_use=data_use['close_s2'].values.reshape((-1,1)) #x must be 2 dim
#        
#        reg = LinearRegression().fit(x_use, y_use)
#        reg_coef=reg.coef_[0]
#        reg_intercept=reg.intercept_
#        
#        HSI_source_use.loc[HSI_source_use['year_month']==y,'reg_coef']=reg_coef
#        HSI_source_use.loc[HSI_source_use['year_month']==y,'reg_intercept']=reg_intercept
#        print('finished ',str(y))       
#        
#
#        
#    
#    #determine weight
#    HSI_source_use=HSI_source_use.loc[~pd.isnull(HSI_source_use['reg_coef']),:].copy()
#    
#    HSI_source_use['s1_weight']=1
#    HSI_source_use['s2_weight']=1
#    
#    HSI_source_use.loc[HSI_source_use['reg_coef']>1,'s2_weight']=HSI_source_use['reg_coef']
#    HSI_source_use.loc[(HSI_source_use['reg_coef']<1)&(HSI_source_use['reg_coef']>0),'s1_weight']=1/HSI_source_use['reg_coef']
#    HSI_source_use.loc[(HSI_source_use['reg_coef']<0)&(HSI_source_use['reg_coef']>-1),'s1_weight']=-1*1/HSI_source_use['reg_coef']    
#    HSI_source_use.loc[HSI_source_use['reg_coef']<-1,'s2_weight']=-1*HSI_source_use['reg_coef']
#    
#    HSI_source_use['s1_weight_round']=round(HSI_source_use['s1_weight'])
#    HSI_source_use['s2_weight_round']=round(HSI_source_use['s2_weight'])    
#    
#    HSI_source_use['close_s1_s2']=HSI_source_use['close']*HSI_source_use['s1_weight_round']-HSI_source_use['close_s2']*HSI_source_use['s2_weight_round']
#
#    #make usre the ticker has data at least from 1996
#    if HSI_source.Date2.values[0]<='1996-01-01':
#        full_data_ticker.append(selection_target)
#        HSI_source['useless_factor']=1
#        
#        #save HSI_source as hsi_y_x
#        out_name='hsi_y_x'+'_'+selection_target
#        store = pd.HDFStore(out_name+'.hdf5', "w", complib=str("zlib"), complevel=5)
#        store.put(out_name+'_dataframe',HSI_source, data_columns=HSI_source.columns)
#        store.close()







monthly_update_us.py

# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:14:49 2021

@author: jonathanjames
"""



import os
import numpy as np
from pandas import HDFStore,DataFrame
import pandas as pd
from datetime import datetime as dt
import datetime
from pandas import read_excel



from pandas import read_excel
import pandas as pd
from datetime import datetime as dt
import os


main_dir='/home/jonathanjames/aws/notebooks/index_analysis'
folder_path='mis'
plot_path=os.path.join('/home/jonathanjames/my_storage/tradelog/index_analysis_cumulative','backtest_linux','plot')
calendar_path=os.path.join(main_dir,'daily_prediction_production')






all_asset=[['BAC',list(range(19560,19574))],['V',list(range(19545,19559))],['BA',list(range(19680,19694))]]

all_asset=[['JPM',list(range(19515,19529))],['WFC',list(range(19605,19619))],['VRTX',list(range(19740,19754))]]

#ll=['BA',list(range(19680,19693))]
for ll in all_asset:
    asset_name=ll[0]
    s1=ll[1]
    #read prediction
    train_test_Setting = read_excel(os.path.join(main_dir,'index_table_v2_for_test_backtest.xlsx'),'Sheet2')
    train_test_Setting['use']=train_test_Setting['Number'].apply(lambda x:x in s1)
    train_test_Setting=train_test_Setting.loc[train_test_Setting['use']==True,:].copy()
    train_test_Setting=train_test_Setting.reset_index(drop=True)
    
    d0=pd.DataFrame([])
    all_number=train_test_Setting['Number'].values.tolist()
    i=0
    for i in range(0,train_test_Setting.shape[0]):
        file_name=str(int(train_test_Setting['Number'][i]))+'_test_'+str(train_test_Setting['Test_start'][i].strftime("%Y"))+'.xlsx'
        d1 = read_excel(os.path.join(plot_path,file_name),'daily_detail_summary_aggregate')
        d0=d0.append(d1)
        #d0=d0[['Date2','Open_HSI','High_HSI','Low_HSI','Close_HSI','DateNum','close_open_diff','bet']]
        print('finished ',i,' out of ',train_test_Setting.shape[0])
    
    
    
    d0['cum_pnl']=d0['PnL'].cumsum()
    
    mdd=max(np.maximum.accumulate(d0['cum_pnl'])-d0['cum_pnl'])
    
    mean_entry=np.mean(d0['entry_price'].values)
    
    upper_entry=np.percentile(d0['entry_price'].values,75)
    
    capital=mean_entry 
    #capital=upper_entry
    if asset_name=='BAC':
        capital=mean_entry*0.7
        
    if asset_name=='V':
        capital=mean_entry*0.55

    if asset_name=='BA':
        capital=mean_entry*0.25
    
    d0['cum_return']=d0['cum_pnl']/capital
    
    if d0['exit_price'].values[-1]==101:
        d0=d0[0:-1].copy()
    if d0['exit_price'].values[-1]==100:
        d0=d0[0:-1].copy()

    
    d0=d0.reset_index(drop=True)
    
    pnl_csv=d0[['entry_time','cum_return']].copy()
    pnl_csv=pnl_csv.rename(columns={'entry_time':'Date','cum_return':'Return'})
    
    #pnl_csv['Date']=pnl_csv['Date'].apply(lambda x: x.strftime("%Y-%m-%d")) #dt to string
    
    temp=pd.DataFrame({'Date':['string'],'Return':['number']})
    
    pnl_csv=temp.append(pnl_csv)
    pnl_csv=pnl_csv.reset_index(drop=True)
    output_path=os.path.join(main_dir,'IB_live_trade','cum_pnl_'+asset_name+'.csv')
    pnl_csv.to_csv(output_path,index=None)




















#
import os
import numpy as np

import requests
import zipfile
import io
import pandas as pd
import yfinance as yf
from pandas import read_excel
import talib
from talib import abstract
from datetime import datetime as dt
target_dir='/home/jonathanjames/aws/notebooks/index_analysis'

target_dir_new='/home/jonathanjames/my_storage/tradelog/index_analysis_cumulative'
tidy_path=os.path.join(target_dir_new,'backtest_linux/database/tidy')
target_dir_out=os.path.join(target_dir_new,'backtest_linux/database/indicator_sample')



os.chdir(target_dir)


use_yahoo=False
use_normal=True

if use_yahoo==True:
    index_list=['^GSPC','^DJI','^IXIC','^HSI','^NYA','^RUT','^VIX','^FTSE','^GDAXI','^FCHI','^STOXX50E','^N100','^BFX',
                '^N225','000001.SS','^STI','^AXJO','^AORD','^BSESN','^JKSE','^KLSE','^NZ50','^KS11','^TWII']
    
    stock_list=['AAPL','MSFT','TGT','TXN','INTU','IBM','JPM','JNJ','UNH','BA','PG','NFLX',
                 'HD','DIS','ORCL','ADBE','BAC','GE','AMD','PFE','CSCO']
    
    cur_list=['EURUSD=X','GBPUSD=X','AUDUSD=X','EURJPY=X','EURGBP=X','GBPJPY=X','EURCAD=X','EURJPY=X',]
    
    
    sample_list=cur_list+index_list+stock_list



if use_normal==True:
    data = read_excel(os.path.join(target_dir,'index_table_v2_for_test_backtest.xlsx'),'Sheet1')
    data_select=data.loc[data['Extract']=='Yes',['Source', 'Type','Company','Name_use_python']].copy()
    data_select['Name_use_python_clean']=data_select['Name_use_python'].apply(lambda x: x.replace('_wsj',''))
    data_select=data_select.reset_index(drop=True)
    
#    use=[0,1,31,32,133,134,384,385,457,458,557,558,782,783,812,813,818]
#    data_select=data_select.iloc[use].copy()
#    data_select=data_select.reset_index(drop=True)

    sample_list=data_select.Name_use_python.values.tolist()






ticker='MICEXINDEXCF.ME'
ticker='fx_BTCUSD_wsj'
ticker='EURHKD'
ticker='IVW'
ticker='^HSI'
ticker='000001.SS'
for ticker in sample_list[811:]:
    if use_yahoo==True:
        raw = yf.download(ticker,start='1995-01-03',end='2040-06-30',progress=False)
        ticker=ticker.replace("=X","")
        ticker=ticker.replace("^","")
        raw=raw.reset_index(drop=False)
        raw=raw.rename(columns={'Close':'Close'+'_'+ticker})
        raw['Date2']=raw['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))
        raw=raw.sort_values(by=['Date2'],ascending=[True])
        vars()['raw_'+ticker]=raw[['Date2','Close'+'_'+ticker]].copy()
    if use_normal==True:
        file_exist=os.path.exists(os.path.join(tidy_path,ticker+'_with_tidy.xlsx'))
        if file_exist==True:
            raw= read_excel(os.path.join(tidy_path,ticker+'_with_tidy.xlsx'),'Sheet1')
            raw=raw.sort_values(by=['Date2'],ascending=[True])
            vars()['raw_'+ticker]=raw[['Date2','Close'+'_'+ticker]].copy()      
            if ticker=='fx_BTCUSD_wsj':
                vars()['raw_'+ticker]=vars()['raw_'+ticker].loc[vars()['raw_'+ticker]['Date2']>='2013-04-01',:].copy()  #btc before 2013 data has problem


    if file_exist==True:        
        vars()['raw_'+ticker]['year_cohord']=vars()['raw_'+ticker]['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y")).astype(int)
        vars()['raw_'+ticker]=vars()['raw_'+ticker].rename(columns={'Close'+'_'+ticker:'close'})
        vars()['raw_'+ticker]['ema_10']=abstract.EMA(vars()['raw_'+ticker],7)
        
        
        year_min=vars()['raw_'+ticker]['year_cohord'].unique()
        year_min=min(year_min)
        year_min_plus=year_min+2 #make sure use at least 2 year historical data
        
        
        #use emprical distribution
        target_variable='f2'
        new_variable='Indicator'+'_'+ticker     #new variable name
        distinct_year=vars()['raw_'+ticker]['year_cohord'].unique()
        distinct_year=[i for i in distinct_year if i >=year_min_plus] 
        yy=2020
        output=pd.DataFrame([])
        for yy in distinct_year:
            data_use=vars()['raw_'+ticker].loc[(vars()['raw_'+ticker]['year_cohord']>=yy-100)&(vars()['raw_'+ticker]['year_cohord']<yy),target_variable].values
            data_use=data_use[~np.isnan(data_use)]
            data_use=pd.DataFrame(data_use)
            data_use.columns=['historical_indicator']
            data_use['key']='k'
            data_use_count=data_use.shape[0]

    
        if output.shape[0]>0:
            vars()['raw_'+ticker]=pd.merge(vars()['raw_'+ticker],output[['Date2',new_variable]].copy(),how='left',on=['Date2'])
            
            #only export data >year_min_plus
            vars()['raw_'+ticker]=vars()['raw_'+ticker].loc[vars()['raw_'+ticker]['year_cohord']>=year_min_plus,:].copy()
            vars()['raw_'+ticker]=vars()['raw_'+ticker].reset_index(drop=True)
            
            #save raw file
            out_file='raw_'+ticker+'.csv'
            vars()['raw_'+ticker].to_csv(os.path.join(target_dir_out,out_file))
        
            #save file with only two columns
            vars()['raw_'+ticker]=vars()['raw_'+ticker].rename(columns={'Date2':'Date'})
            out_file='Indicator_'+ticker+'.csv'
            vars()['raw_'+ticker][['Date',new_variable]].to_csv(os.path.join(target_dir_out,out_file),index=False)    
            
            print('finished ',ticker, ' ',str(sample_list.index(ticker)),' out of ',str(len(sample_list)))




#append tgh and output as sample for client


all_type=list(data_select.Type.unique())

tt='index'
tt='n225'
tt='Currency'
for tt in all_type:
    data_select2=data_select.loc[data_select['Type']==tt,:].copy()
    data_select2=data_select2.reset_index(drop=True)

    output_client=pd.DataFrame([])
    i=0
    for i in np.arange(0,data_select2.shape[0]):
    
        ticker=data_select2.loc[i,'Name_use_python']
        
        input_file=os.path.join(target_dir_out,'Indicator_'+ticker+'.csv')
        if os.path.exists(input_file):
            temp1=pd.read_csv(input_file)
            temp1.columns=['Date','Indicator']
            temp1['Type']=data_select2.loc[i,'Type']
            temp1['Asset/Company']=data_select2.loc[i,'Company']
            temp1['Code']=data_select2.loc[i,'Name_use_python_clean']
            temp1=temp1[0:-1].copy()  #remove last row becasue the price may not be correct
            output_client=output_client.append(temp1)
            print('finished ',ticker)
        
    output_client=output_client[['Date','Type','Asset/Company','Code','Indicator']].copy()
    output_client['Indicator']=output_client['Indicator'].apply(lambda x:round(x,1))  #round to 1 decimal place
    
    tt=tt.replace("_wsj","")
    
    output_client_index=output_client[['Type','Asset/Company','Code']].copy()
    output_client_index=output_client_index.drop_duplicates()
    output_client_index=output_client_index.reset_index(drop=True)

    
    file_name=os.path.join(target_dir_out,_'+tt+'.xlsx')
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    output_client_index.to_excel(writer, sheet_name='Ticker',index=False)
    writer.save()
    writer.close()
    
    file_name=os.path.join(target_dir_out,''+tt+'.csv')
    output_client.to_csv(file_name,index=False)

    print("finished ",tt)







a_check=vars()['raw_'+ticker].copy()


#check density
import matplotlib.pyplot as plt
ticker='fx_BTCUSD_wsj'#'EURGBP'#'EURUSD'#'HSI'#'TXN'#'MSFT'#'AAPL'
ticker='MSFT'

input_file='raw_'+ticker+'.csv'
temp1=pd.read_csv(os.path.join(target_dir_out,input_file))
distinct_year=temp1['year_cohord'].unique()

i=0
plt.figure(figsize=(10,80), dpi=80, facecolor='w', edgecolor='k') 
year=2001
for year in distinct_year:
    i=i+1
    v1=temp1.loc[temp1['year_cohord']==year,'Indicator'+'_'+ticker].values
    
    #find when indicator = 20 or 80, the f2 value
    threshold1=round(max(temp1.loc[(temp1['year_cohord']==year)&(temp1['Indicator'+'_'+ticker]<=20),'f2'].values),5)
    threshold2=round(max(temp1.loc[(temp1['year_cohord']==year)&(temp1['Indicator'+'_'+ticker]<=80),'f2'].values),5)
       
    plt.subplot(20,2,i).set_title(year) #fist two argument is the dimension, the three argument is the number for each plot
    plt.text(23, 0.01,str(threshold1)+'  '+str(threshold2), fontsize = 10)
    plt.tight_layout() # Or equivalently,  "plt.tight_layout()"
    plt.hist(v1,normed=True,bins=30)#,range=(0,1))  #ravel=flatten
    plt.axvline(x = 20, color = 'r', linestyle = '-')
    plt.axvline(x = 80, color = 'r', linestyle = '-')
    plt.xlabel('indicator')
    plt.ylabel('density') 






#indicator on differenct asset example
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode,  plot
from plotly import graph_objects as go
from plotly.subplots import make_subplots


ticker2='AAPL'
input_file='raw_'+ticker2+'.csv'
temp2=pd.read_csv(os.path.join(target_dir_out,input_file))
temp2=temp2.rename(columns={'Date2':'Date'})
temp2=temp2.loc[(temp2['Date']>='2021-07-01')&(temp2['Date']<='2022-06-30'),:].copy()




b1 =temp2['Date'].values
b2 = temp2['close'].values
b3=temp2['Indicator_'+ticker2].values


#make indicator example
fig = make_subplots(rows=2, cols=1, shared_xaxes=True,vertical_spacing=0.01,row_heights=[0.6,0.4])

fig.update_yaxes(title_text="AAPL Stock Price",title_font=dict(size=20), row=1, col=1,tickfont = dict(size=16))
fig.update_yaxes(title_text="Indicator",title_font=dict(size=20), row=2, col=1,tickfont = dict(size=16))
fig.update_xaxes(title_text="Date",row=2,title_font=dict(size=20), tickfont = dict(size=16))

fig.add_trace(go.Scatter(x = b1,y = b2,mode = 'lines',marker=dict(color='blue')),row=1,col=1)
fig.add_trace(go.Scatter(x = b1,y = b3,mode = 'lines',marker=dict(color='#8B3626')),row=2,col=1)

##add horizontal line
fig.add_hline(y=80, line_dash="dot",annotation_text="",annotation_position="bottom left",line_color="green",line_width=2,row=2)
fig.add_hline(y=20, line_dash="dot",annotation_text="",annotation_position="bottom left",line_color="red",line_width=2,row=2)
#fig.layout.yaxis.tickformat = ',.0%'  #display in percentage
fig['data'][0]['name'] = "AAPL Stock Price"   #change legend first color description name
fig['data'][1]['name'] = 'Indicator'   #change legend first color description name

plot(fig)



fig.write_image(os.path.join(target_dir_out,"indicator_multiple_example.jpeg"))





#make strategy 1 example
ticker2='fx_BTCUSD_wsj'
input_file='raw_'+ticker2+'.csv'
temp2=pd.read_csv(os.path.join(target_dir_out,input_file))
temp2=temp2.rename(columns={'Date2':'Date'})
temp2=temp2.loc[(temp2['Date']>='2020-11-24')&(temp2['Date']<='2020-12-05'),:].copy()

b1 =temp2['Date'].values
b2 = temp2['close'].values
b3=temp2['Indicator_'+ticker2].values




fig = make_subplots(rows=2, cols=1, shared_xaxes=True,vertical_spacing=0.05,row_heights=[0.6,0.4],subplot_titles=("Method 1", ""))

fig.update_yaxes(title_text="Bitcoin Price (USD)",title_font=dict(size=20), row=1, col=1,tickfont = dict(size=16))
fig.update_yaxes(title_text="Indicator",title_font=dict(size=20), row=2, col=1,tickfont = dict(size=16))
fig.update_xaxes(title_text="Date",row=2,title_font=dict(size=20), tickfont = dict(size=16))

#add two plots
fig.add_trace(go.Scatter(x = b1,y = b2,mode = 'lines',marker=dict(color='blue')),row=1,col=1)
fig.add_trace(go.Scatter(x = b1,y = b3,mode = 'lines',marker=dict(color='#8B3626')),row=2,col=1)

##add horizontal line
fig.add_hline(y=80, line_dash="dot",annotation_text="",annotation_position="bottom left",line_color="green",line_width=2,row=2)
fig.add_hline(y=20, line_dash="dot",annotation_text="",annotation_position="bottom left",line_color="red",line_width=2,row=2)

#add the short vertical line
fig.add_trace(go.Scatter(
    x=["2020-11-26","2020-11-26"],
    y=[17000,17250],
    mode="lines+text",
    name="Lines and Text",
    text=["2020-11-26 Price = 17122", ""],line_color="black",line_width=3, line_dash="dot",textfont=dict(size=16),
    textposition="bottom right"),row=1,col=1)

fig.add_trace(go.Scatter(
    x=["2020-11-30","2020-11-30"],
    y=[19250,19520],
    mode="lines+text",
    name="Lines and Text",  #this is legend name
    text=["", "2020-11-30 Price = 19376"],line_color="black",line_width=3, line_dash="dot",textfont=dict(size=16),
    textposition="middle right"),row=1,col=1)

fig.add_trace(go.Scatter(
    x=["2020-11-26","2020-11-26"],
    y=[5,15],
    mode="lines+text",
    name="Lines and Text",
    text=["2020-11-26 Indicator = 9.6", ""],line_color="black",line_width=3, line_dash="dot",textfont=dict(size=16),
    textposition="bottom right"),row=2,col=1)

fig.add_trace(go.Scatter(
    x=["2020-11-30","2020-11-30"],
    y=[85,95],
    mode="lines+text",
    name="Lines and Text",  #this is legend name
    text=["", "2020-11-30 Indicator = 88.6"],line_color="black",line_width=3, line_dash="dot",textfont=dict(size=16),
    textposition="middle right"),row=2,col=1)

#fig.layout.yaxis.tickformat = ',.0%'  #display in percentage
fig['data'][0]['name'] = "Bitcoin Price (USD)"   #change legend first color description name
fig['data'][1]['name'] = 'Indicator'   #change legend first color description name

fig.update_layout(
    autosize=False,#font=dict(family="Courier New, monospace",size=18,color="RebeccaPurple"),
    width=600,
    height=800,
    showlegend=False,
    margin = go.layout.Margin(l=0,r=30,t=30,b=0))

plot(fig)

fig.write_image(os.path.join(target_dir_out,"indicator_method1.jpeg"))







#make strategy 2 example
ticker2='fx_BTCUSD_wsj'
input_file='raw_'+ticker2+'.csv'
temp2=pd.read_csv(os.path.join(target_dir_out,input_file))
temp2=temp2.rename(columns={'Date2':'Date'})
temp2=temp2.loc[(temp2['Date']>='2019-06-01')&(temp2['Date']<='2019-06-10'),:].copy()

b1 =temp2['Date'].values
b2 = temp2['close'].values
b3=temp2['Indicator_'+ticker2].values




fig = make_subplots(rows=2, cols=1, shared_xaxes=True,vertical_spacing=0.05,row_heights=[0.6,0.4],subplot_titles=("Method 2", ""))

fig.update_yaxes(title_text="Bitcoin Price (USD)",title_font=dict(size=20), row=1, col=1,tickfont = dict(size=16))
fig.update_yaxes(title_text="Indicator",title_font=dict(size=20), row=2, col=1,tickfont = dict(size=16))
fig.update_xaxes(title_text="Date",row=2,title_font=dict(size=20), tickfont = dict(size=16))

#add two plots
fig.add_trace(go.Scatter(x = b1,y = b2,mode = 'lines',marker=dict(color='blue')),row=1,col=1)
fig.add_trace(go.Scatter(x = b1,y = b3,mode = 'lines',marker=dict(color='#8B3626')),row=2,col=1)

##add horizontal line
fig.add_hline(y=80, line_dash="dot",annotation_text="",annotation_position="bottom left",line_color="green",line_width=2,row=2)
fig.add_hline(y=20, line_dash="dot",annotation_text="",annotation_position="bottom left",line_color="red",line_width=2,row=2)

#add the short vertical line
fig.add_trace(go.Scatter(
    x=["2019-06-04","2019-06-04"],
    y=[7620,7720],
    mode="lines+text",
    name="Lines and Text",
    text=["2019-06-04 Indicator = 7663", ""],line_color="black",line_width=3, line_dash="dot",textfont=dict(size=16),
    textposition="bottom center"),row=1,col=1)

fig.add_trace(go.Scatter(
    x=["2019-06-07","2019-06-07"],
    y=[7850,7970],
    mode="lines+text",
    name="Lines and Text",  #this is legend name
    text=["", "2019-06-07 Indicator = 7920"],line_color="black",line_width=3, line_dash="dot",textfont=dict(size=16),
    textposition="middle center"),row=1,col=1)

fig.add_trace(go.Scatter(
    x=["2019-06-04","2019-06-04"],
    y=[0,10],
    mode="lines+text",
    name="Lines and Text",
    text=["2019-06-04 Indicator = 5.4", ""],line_color="black",line_width=3, line_dash="dot",textfont=dict(size=16),
    textposition="bottom center"),row=2,col=1)

fig.add_trace(go.Scatter(
    x=["2019-06-07","2019-06-07"],
    y=[25,38],
    mode="lines+text",
    name="Lines and Text",  #this is legend name
    text=["", "2019-06-07 Indicator = 31.1"],line_color="black",line_width=3, line_dash="dot",textfont=dict(size=16),
    textposition="middle center"),row=2,col=1)

#fig.layout.yaxis.tickformat = ',.0%'  #display in percentage
fig['data'][0]['name'] = "Bitcoin Price (USD)"   #change legend first color description name
fig['data'][1]['name'] = 'Indicator'   #change legend first color description name

fig.update_layout(
    autosize=False,#font=dict(family="Courier New, monospace",size=18,color="RebeccaPurple"),
    width=600,
    height=800,
    showlegend=False,
    margin = go.layout.Margin(l=0,r=30,t=30,b=0))

plot(fig)

fig.write_image(os.path.join(target_dir_out,"indicator_method2.jpeg"))














#plot  for illustraction
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode,  plot
from plotly import graph_objects as go
from plotly.subplots import make_subplots
ticker='DJIA'

input_file='raw_'+ticker+'.csv'
temp1=pd.read_csv(os.path.join(target_dir_out,input_file))
temp1=temp1.rename(columns={'Date2':'Date'})

temp1['RSI']=abstract.RSI(temp1,7)

temp1=temp1.loc[(temp1['Date']>='2022-01-01')&(temp1['Date']<='2022-06-30'),:].copy()


x =temp1['Date'].values
y1 = temp1['close'].values


indicator=temp1['Indicator_'+ticker].values
rsi=temp1['RSI'].values

fig = make_subplots(rows=3, cols=1, shared_xaxes=True,vertical_spacing=0.03,row_heights=[0.6,0.2,0.2])

fig.update_yaxes(title_text=ticker +" Price", row=1, col=1)
fig.update_yaxes(title_text="Indicator", row=2, col=1)
fig.update_yaxes(title_text="RSI", row=3, col=1)

fig.add_trace(go.Scatter(x = x,y = y1,mode = 'lines',marker=dict(color='blue')),row=1,col=1)

# Plot OHLC on 1st subplot (using the codes from before)
# Plot volume trace on 2nd row 
fig.add_trace(go.Scatter(x=x, y=indicator,mode='lines'), row=2, col=1)
fig.add_trace(go.Scatter(x=x, y=rsi,mode='lines'), row=3, col=1)


##add horizontal line
fig.add_hline(y=80, line_dash="dot",annotation_text="hello",annotation_position="bottom left",row=2)
fig.add_hline(y=20, line_dash="dot",annotation_text="hello",annotation_position="bottom left",row=2)
#fig.layout.yaxis.tickformat = ',.0%'  #display in percentage

fig['data'][0]['name'] = ticker +" Price"   #change legend first color description name
fig['data'][1]['name'] = 'Indicator'   #change legend first color description name
fig['data'][2]['name'] = 'RSI'
plot(fig)

fig.write_image(os.path.join(target_dir_out,"plotly_temp.jpeg"))























#apply indicator to index components and plot
#indicator on differenct asset example
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode,  plot
from plotly import graph_objects as go
from plotly.subplots import make_subplots

target_path='/home/jonathanjames/my_storage/tradelog/index_analysis_cumulative'



name1={'snp':'GSPC','dow':'DJI','hsi':'HSI_index','ftse':'FTSE','n225':'N225'}
name1_for_output={'snp':'S&P Index','dow':'Dow Jone Index' ,'hsi':'Hang Seng Index','ftse':'FTSE Index','n225':'N225 Index'}


name1={'snp_index':'GSPC'}
name1_for_output={'snp_index':'S&P Index'}

name1={'snp_AON':'AON'}
name1_for_output={'snp_AON':'AON'}

name1={'us_bet':['GSPC','US Trading Model','S&P Index']}


reference_start='2009-01-01'

x='snp_AON'
for x in list(name1):
    #read result
    result=pd.read_csv(os.path.join('backtest_linux/check','d0_'+x+'.csv'))
    result=result.sort_values(by=['Date2'],ascending=['True'])
    capital=500000
    result['account_value']=(result['pnl_all'].cumsum()+capital)
    result['daily_return']=(result['account_value']-capital)/capital
    
    
    result['daily_return_cum_product']=result['daily_return'].copy()
    result=result.reset_index(drop=True)
    

    
    #read index
    selection_target=name1[x][0]
    HSI_source=pd.read_excel(os.path.join('backtest_linux/database/tidy',selection_target+'_with_tidy.xlsx'),'Sheet1')
    #HSI_source=pd.read_excel(selection_target+'_with_tidy.xlsx','Sheet1')
    t1='Open_'+selection_target
    t2='High_'+selection_target
    t3='Low_'+selection_target
    t4='Close_'+selection_target
    t6=selection_target+'_change'
    HSI_source=HSI_source.rename(columns={t1:'open',t2:'high',t3:'low',t4:'close',t6:'HSI_change'})
    HSI_source=HSI_source.loc[:,['Date2','open','high','low','close','HSI_change','DateNum']].copy()
    
    HSI_source=HSI_source.sort_values(by=['Date2'],ascending=['True'])


    
    HSI_source=HSI_source.loc[HSI_source['Date2']>=reference_start,['Date2','open','high','low','close','DateNum']].copy()
    HSI_source['daily_return']=(HSI_source['close']-HSI_source['close'].values[0])/HSI_source['close'].values[0]
    
    HSI_source['HSI_change_cum_product']=HSI_source['daily_return'].copy()
    HSI_source=HSI_source.reset_index(drop=True)
    
    result=pd.merge(result,HSI_source[['Date2','HSI_change_cum_product']].copy(),how='left',on=['Date2'])


    temp2=result.copy()
    
    #find yearly return
    result['year']=result['Date2'].str[0:4]
    HSI_source['year']=HSI_source['Date2'].str[0:4]
    
#    temp2.columns
#    temp2a=temp2.groupby(['year']).head(1)
#    temp2b=temp2.groupby(['year']).tail(1)
#    temp2a=temp2a.reset_index(drop=True)
#    temp2b=temp2b.reset_index(drop=True)
#    
#    temp2a['daily_return_cum_product_end']=temp2b['daily_return_cum_product'].copy()
#    temp2a['indicator_yearly_return']=(temp2a['daily_return_cum_product_end']-temp2a['daily_return_cum_product'])/temp2a['daily_return_cum_product']
#    temp2a['HSI_change_cum_product_end']=temp2b['HSI_change_cum_product'].copy()
#    temp2a['index_yearly_return']=(temp2a['HSI_change_cum_product_end']-temp2a['HSI_change_cum_product'])/temp2a['HSI_change_cum_product']
    
    def find_yearly_return(data_temp,field):
        temp=(data_temp[field].values[-1]-data_temp[field].values[0])/data_temp[field].values[0]
        return pd.DataFrame({'year':[data_temp['year'].values[0]],'return':temp})
    
    temp2a=result.groupby(['year']).apply(lambda x: find_yearly_return(x,'account_value'))
    temp2a=temp2a.rename(columns={'return':'indicator_yearly_return'})
    
    
    
    temp2b=HSI_source.groupby(['year']).apply(lambda x: find_yearly_return(x,'close'))
    temp2b=temp2b.rename(columns={'return':'index_yearly_return'})

    temp2a=temp2a.reset_index(drop=True)
    temp2b=temp2b.reset_index(drop=True)
    temp2a=pd.merge(temp2a,temp2b,how='left',on=['year'])

    temp2a=temp2a[['year','indicator_yearly_return','index_yearly_return']].copy()
    
    temp2.columns.values
    temp2a_last=pd.DataFrame({'year':['Total'],'indicator_yearly_return':[temp2['daily_return_cum_product'].values[-1]],'index_yearly_return':[temp2['HSI_change_cum_product'].values[-1]]})
    temp2a.columns.values
    
    temp2a=temp2a.append(temp2a_last)

    temp2a['indicator_yearly_return']=round(temp2a['indicator_yearly_return']*100,1)
    temp2a['index_yearly_return']=round(temp2a['index_yearly_return']*100,1)   
    temp2a['indicator_yearly_return_str']=temp2a['indicator_yearly_return'].apply(lambda x:str(x)+'%')
    temp2a['index_yearly_return_str']=temp2a['index_yearly_return'].apply(lambda x:str(x)+'%')    

    temp2a=temp2a.reset_index(drop=True)

    ## add bold html to the last row  
    temp2a.loc[temp2a.shape[0]-1,'year']='<b>' +'Total'+ '</b>'
    temp2a.loc[temp2a.shape[0]-1,'indicator_yearly_return_str']='<b>' +temp2a['indicator_yearly_return_str'].values[-1]+ '</b>'
    temp2a.loc[temp2a.shape[0]-1,'index_yearly_return_str']='<b>' +temp2a['index_yearly_return_str'].values[-1]+ '</b>'


    x1 =temp2['Date2'].values
    y1 = temp2['daily_return_cum_product'].values
    y2=temp2['HSI_change_cum_product'].values



    fig = make_subplots(
        rows=1, cols=2,
        shared_xaxes=True,
        horizontal_spacing=0.01,
        column_widths = [0.7, 0.33],
        row_heights = [0.1],
        specs=[[{"type": "scatter"},{"type": "table"}]])
    
    
    obj1 = go.Scatter(x = x1,y = y1,mode = 'lines')
    fig.add_trace(obj1,row=1,col=1)
    obj2 = go.Scatter(x = x1,y = y2,mode = 'lines',marker=dict(color='#CDAA7D'))
    fig.add_trace(obj2,row=1,col=1)
    
    fig['data'][0]['name'] = 'Cumulative Return - '+name1[x][1]   #change legend first color description name
    fig['data'][1]['name'] = 'Cumulative Return - '+name1[x][2] #change legend first color description name
    
    fig.add_trace(
        go.Table(
            header=dict(
                values=['<br>Year', name1[x][1]+"<br>Return", name1[x][2]+'<br>Return'],
                font=dict(size=14),
                align="center"
            ),
            cells=dict(
                values=[temp2a[k].tolist() for k in ['year','indicator_yearly_return_str','index_yearly_return_str']],
                font=dict(size=14),
                align = "center")
        ),
        row=1, col=2
        )

    
    fig.update_layout(
        autosize=False,#font=dict(family="Courier New, monospace",size=18,color="RebeccaPurple"),
        width=1300,
        height=700,
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01,font=dict(size=13)),
        yaxis=dict(tickformat=".0%"),
        showlegend=True)
    fig.update_yaxes(title_text="Return",title_font=dict(size=20), row=1, col=1,tickfont = dict(size=16))
    fig.update_xaxes(title_text="Date",row=1,col=1,title_font=dict(size=20), tickfont = dict(size=16))
    plot(fig)
    
    fig.write_image(os.path.join(target_path,'backtest_linux','check',x+".jpeg"))







krow_summary


#python data type
http://chris.friedline.net/2015-12-15-rutgers/lessons/python2/03-data-types-and-format.html
#python NaN and null
https://stackoverflow.com/questions/17534106/what-is-the-difference-between-nan-and-none#17534682
################################
############new_type############
################################

import math
#normalize
X=np.array([[9,33,20,33,44],[6,26,15,22,17],[16,19,32,54,32]])
X_center=X - np.mean(X, axis = 0)
X_normal=X_center/np.std(X, axis = 0)

#check if a dataframe column every row contain a specific string 
data_div_first=data_div_tt[~data_div_tt['winning_combination'].str.contains("Any combination")].reset_index(drop=True)
#find if the column contain ">"
data_div_first.loc[data_div_first['winning_combination'].str.contains(">"),'more']=1
#if nan, replace by 0
data_div_first.loc[np.isnan(data_div_first['more']),'more']=0
trackwork.loc[np.isnan(trackwork.TW_P),'TW_P']=0

#split win combination into three columns by /                   
data_div_first[['race_tt1','race_tt2','race_tt3']]=data_div_first['winning_combination'].str.split('/',expand=True)
data_div_first['Date']=data_div_first['meeting_date'].astype(str).str[:10]  

#select 2 element within 4 for all the combination
import itertools
import copy
list(itertools.combinations(['a','d','e','s'], 2))


test='9>1,3,4,5'
test.count('>')!=0
bag=test.split('>')
bag[0].count(",")==1
bag0_all=[int(x) for x in bag[0].split(',')] #bag[0]='2,5' is a list element, bag[0].split(',') is a list ['2', '5']
bag1_all=[int(x) for x in bag[1].split(',')]

new=copy.deepcopy(bag0_all) #deepcopy a list

new=['jame','apple','banana']
new.sort() #sort a list
new=[str(x) for x in new] #convert all list element to string

allanswer=[]
allanswer.append(','.join(new)) #using append by ',' new must be all string inside

#join all element of a list by |
output='|'.join(allanswer)

all_comb=['(jonathan)','(123)','(ee','w3)']
all_comb=[str(x) for x in all_comb]
all_comb=[x.replace('(','') for x in all_comb]  #replace ( by ''

#apply to every element of a column
data_div_first['race_tt1_all']=data_div_first['race_tt1'].apply(lambda x:split_tt(x))

#check if a column row value contained in another column row
data_div_first['tt1_contain']=data_div_first.apply(lambda row: row.bet_tt1 in row.race_tt1_all, axis=1)

#convert object to string
racerunner_withw_use['Date'] = racerunner_withw_use['Date'].astype(str)
racerunner_withw_use=racerunner_withw_use.loc[racerunner_withw_use['Date']>'2013-09-01',:].reset_index(drop=True)

data_div_first['bet_tt1']=data_div_first.apply(lambda row: read_bet1(row['Date'],row['race_no'],lag=2),axis=1)





x=np.array([[0.1,0.2],
            [0.4,0.6]])
y=np.array([[0.5,0.6],
            [0.4,0.8]])
w1=np.array([[0.1,0.2],
            [0.15,0.25]])
theta1=np.array([[0.3,0.4],
                 [0.5,0.25]])    
#matrix multiplication
a=np.dot(x,w1)
def sm(x):
    return 1/(1+np.exp(-x))
a1=sm(a)
Y=np.dot(a1,theta1)
Y2=sm(Y)
def dloss(x):
    return 2*(x-y)
dLdY2=dloss(Y2)

dLda1=np.dot(dLdY2,theta1.T)
dLdtheta1=np.dot(a1.T,dLdY2)

dLdw1=np.dot(x.T,dLda1)


import math
#normalize
X=np.array([[9,33,20,33,44],[6,26,15,22,17],[16,19,32,54,32]])

X_normal=X_center/np.std(X, axis = 0)


#PCA and Whitening
# Assume input data matrix X of size [N x D]
X_center=X - np.mean(X, axis = 0) # zero-center the data (important)
cov = np.dot(X_center.T, X_center) / X_center.shape[0] # get the data covariance matrix

#variance
np.var(X_center, axis = 0)
#sd
np.square(np.std(X, axis = 0))

U,S,V = np.linalg.svd(cov)
Xrot = np.dot(X_center, U) # decorrelate the data
#cov is diagonal
cov = np.dot(Xrot.T, Xrot) / Xrot.shape[0]

Xrot_reduced = np.dot(X, U[:,:3]) # Xrot_reduced becomes [N x 100]
             
             
# whiten the data:
# divide by the eigenvalues (which are square roots of the singular values)
Xwhite = Xrot / np.sqrt(S + 1e-5) 


################################
############video_issue#########
################################


#convert dataframe column to numeric
video_check['AT_C_x'] = video_check['AT_C_x'].convert_objects(convert_numeric=True)


def sum_horse_no(x,col_race,col_hr_no):
    race_key=x[col_race][0]
    hr_no_sum=sum(x[col_hr_no])
    return [race_key,hr_no_sum]



import pandas as pd

newcol=racerunner_withw_use_temp.groupby(['Season_']).apply(lambda x:sum_horse_no(x.reset_index(drop=True),'Season_','No_')).reset_index(drop=True)

lst1 = [item[0] for item in newcol]
lst2 = [item[1] for item in newcol]

newcol2=pd.DataFrame({'racekey_racerunner':lst1,'sum_hr_racerunner':lst2})


################################
#####HKDBLiveWithDB12_3#########
################################


RawData['DateNum'] = (RawData.Date-datetime.date(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
RawData['Date'] = RawData['Date'].astype(str)
RawData= RawData.sort_values(by =['RaceIndex','HorseNo'],ascending=[False, True] )

#insert a column to dataframe
TempA1_check.insert(0,'RaceKey2',TempA1_check['RaceIndex'].astype(str)+'-'+TempA1_check['HorseNo'].astype(str))



#group by raceindex and calculate mean
trackwork_use['nfp_mean'] = trackwork_use['NFP'].groupby(trackwork_use['RaceIndex']).transform('mean')


#fill na by 0 of the whole table
VideoTable_M=VideoTable_M.fillna(0)

#count the number of data in ATB_M
sum(VideoTable_M.ATB_M.apply(lambda x: x>0))

#convert column to string
VideoTable_merge['Date']=VideoTable_merge['Date'].astype(str)

VideoTable_merge['IR_M']=VideoTable_merge['IR_M'].astype(float)

#find the max of two columns row by row
VideoTable_merge['max_IR']=VideoTable_merge[['IR_C','IR_M']].max(axis=1)


hkdb_v10=hkdb_v9.sort_values(['racekey','horse_no'], ascending=[True, True])            
hkdb_v10.to_csv("C:\\Users\\jonathan.james\\Desktop\\setting\\hkdb_new.csv", index=False)

#rename columns
hkdb=hkdb.rename(columns={'TW_P':'TW_P_direct'})


################################
########Check_hkdb_test#########
################################


#read hkdb left main columns
main_columns=list(file1.columns.values)[2:19]
main_columns=[x.encode('UTF8') for x in main_columns]

#read factors
factors = open(r'C:\Users\jonathan.james\Desktop\zip\20170916\20170916_testcsv\factors.txt' )
lines = factors.readlines()
factors=lines[1:len(lines)]
factors=[x.strip() for x in factors]  #remove left and right space of a string


################################
##hk_analysis_trackwwork_v2#####
################################

#check data structure type
type(racerunner_withw_use_oddoddoddodd['Win_oddoddoddsddo_ult1']) #pandas.core.series.Series
#check type of data
racerunner_withw_use_oddoddoddodd['Win_oddoddoddsddo_ult1'].dtype #dtype('O') #'O' just stands for "object",in Pandas' world is string (characters).

#view the data type for each column in a DataFrame (all at once).
racerunner_withw_use.dtypes




#convert object(string) to numeric (float64)
racerunner_withw_use_oddoddoddodd['Win_oddoddoddsddo_ult1']=pd.to_numeric(racerunner_withw_use_oddoddoddodd['Win_oddoddoddsddo_ult1'],errors='coerce')
sum(np.reciprocal(racerunner_withw_use_oddoddoddodd['Win_oddoddoddsddo_ult1']))

#create a column with mean group by raceindex
video_use['nfp_mean'] = video_use['nfp'].groupby(video_use['RaceIndex']).transform('mean')

key=pd.to_datetime(dataset_copy['Date']) #convert to datetime


t1.fill(8) #fill a numpy array with a number


#use joblib
import os
os.getcwd()
os.chdir("C:\\Users\\jonathan.james\\.Spyder\\notebook")
from joblib import Parallel, delayed
from Factors_test_function import DBA
import datetime
import numpy as np
n=len(hkdb_with_track_work)
i=0
out=Parallel(n_jobs=7,verbose=5)(delayed(DBA)(hkdb_with_track_work[i:(i+1)].reset_index(drop=True),trackwork_use) for i in np.arange(n))

hkdb_with_track_work['revised_tony_paul']=out
                    
%timeit Parallel(n_jobs=7,verbose=5)(delayed(DBA)(hkdb_with_track_work[i:(i+1)].reset_index(drop=True),trackwork_use) for i in np.arange(10))                    
            
x=hkdb_with_track_work.tail(1).reset_index(drop=True)
%timeit DBA(x)


#using mp pool

import os
import multiprocessing as mp

os.getcwd()
os.chdir("C:\\Users\\jonathan.james\\.Spyder\\notebook")
from joblib import Parallel, delayed
from Factors_test_function import wrap
import datetime
import numpy as np
n=len(hkdb_with_track_work)


setup=[]
for i in np.arange(n):
    setup.append((hkdb_with_track_work[i:(i+1)].reset_index(drop=True),trackwork_use))
out=mp.Pool(processes=7).map(wrap,setup)

#%timeit mp.Pool(processes=8).map(wrap,setup)


################################
######old_factor_analysis#######
################################



#ema, exponential moving avergae calculation
import pandas as pd
import numpy as np
data=pd.DataFrame({'Datenum': [100,95,85,75,50],'nfp': [0,9,5,1,3]}) 
data=pd.DataFrame({'Datenum': [100,95,85,75,50],'nfp': [0,9,5,0,0]}) 
datenum_field='Datenum'
target_field='nfp'
decay=90
#def ema_custom(data,datenum_field,target_field,decay):
#    datenum_vector=np.array(data[datenum_field],dtype=pd.Series).astype(np.float)#convert dataframe column to array
#    target_vector=np.array(data[target_field],dtype=pd.Series).astype(np.float)
#    
#    n=len(datenum_vector)        
#    temp=np.tile(datenum_vector,n) #make replication
#    matrix_fill_h=np.reshape(temp,(n,n))
#    matrix_fill_v=matrix_fill_h.T
#    diff=matrix_fill_v-matrix_fill_h
#    ind=diff<0 #filter out negative value
#    diff[ind]=0
#    diff=diff[0:diff.shape[0]-1,1:diff.shape[0]]*-1.0
#    matrix_fill=diff
#    
#    up_tri_all1=np.triu(np.ones((n-1,n-1),dtype=np.int),0)
#    matrix_fill_use=np.multiply(np.exp(matrix_fill/decay),up_tri_all1)
#    
#    matrix_fill_use_div_rowsum=matrix_fill_use/np.sum(matrix_fill_use,axis=1,keepdims=True)
#    x=np.reshape(target_vector[1:len(target_vector)],(len(target_vector)-1,1))#exclude first elemnt of target vector
#    output=np.vstack((np.dot(matrix_fill_use_div_rowsum,x),np.array([0.0])))#append 0 to last row
#    name='EMA_'+target_field
#    data[name]=output
#    return data



data1=pd.DataFrame({'Datenum':[17363,17348,17307,17286],'nfp': [0.910239226627,0.721347520444,0.558110626551,0.721347520444]}) 
ema_custom_v2(data1,'Datenum','nfp',120)

data1=pd.DataFrame({'Datenum':[17363],'nfp': [0.910239226627]}) 
ema_custom_v2(data1,'Datenum','nfp',120)

data1=pd.DataFrame({'Datenum':[17363],'nfp': [0]}) 
ema_custom_v2(data1,'Datenum','nfp',120)

data1=pd.DataFrame({'Datenum':[17363,17000],'nfp': [0,5]}) 
ema_custom_v2(data1,'Datenum','nfp',120)

data=pd.DataFrame({'Datenum': [100,95,85,75,50,45,30,29],'nfp': [0,0,0,0,0,0,0,0]}) 
ema_custom_v2(data,'Datenum','nfp',120)

data=pd.DataFrame({'Datenum': [100,95,85,75,50,45,30,29],'nfp': [0,0,5,8,0,0,0,9]}) 
ema_custom_v2(data,'Datenum','nfp',120)


9*np.exp(-16.0/120)/(np.exp(-16.0/120)+np.exp(-15.0/120))
9*np.exp(-21.0/120)/(np.exp(-21.0/120)+np.exp(-20.0/120)+np.exp(-5.0/120))

data=pd.DataFrame({'Datenum': [100,95,85,75,50,45,30,29],'nfp': [9,9,9,9,9,8,9,9]}) 
data1=ema_custom_v2(data,'Datenum','nfp',120)


10*np.exp(-240.0/120)


################################
##########backtest_v2###########
################################
import os
os.getcwd()
os.chdir("C:\\Users\\jonathan.james\\Desktop\\yulong")
import paramiko
from paramiko import SSHClient,AutoAddPolicy,client
from scp import SCPClient
from time import sleep
import numpy as np
import shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
#os.chdir("C:\\Users\\jonathan.james\\.Spyder\\notebook")
import commands
import json
#read the setting
from string import ascii_lowercase
from joblib import Parallel, delayed
import multiprocessing as mp
from for_parallel import up_to_management 


from pandas import read_excel
data_setting = read_excel('folder_name.xlsx','Sheet1')
oddoddoddsddo_setting = read_excel('folder_name.xlsx','oddoddoddsddo')

oddoddoddodd2013=str(oddoddoddsddo_setting.loc[0,'2013_oddoddoddodd'])


def simulation(track):
    browser.get(backtest_server_simulation)
    sleep(1)
    wait = WebDriverWait(browser, 10)
    #wait until find the button within 10s
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'md-tab-item[class="md-tab ng-scope ng-isolate-scope md-ink-ripple"]'))).click()
    log.write("found run button\n")
    wait.until(EC.visibility_of_element_located((By.ID, "file"))).send_keys(json_path[track])
    log.write("uploaded json\n")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button[ng-click="vm.importSetting()"]'))).click()
    log.write("imported json\n")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button[ng-click="vm.startSimulation()"]'))).click()
    sleep(1)
    log.write("started simulation\n")
    log.write("\n")

browser = webdriver.Chrome(executable_path=r'C:\Users\jonathan.james\.Spyder\chromedriver.exe')
browser.set_window_position(-10000,0)

################################
##########for_parallel##########
################################

################################
############plot_code###########
################################

report['date']=report['Meeting Date'].str[0:10]

for i in (np.arange(model1_rep)+1):
    locals()["source_path_pnl"+str(i)]=os.path.join(report_destination,str(int(summary_report.loc[summary_report['key1']==(model1+"_rep"+str(i)+"_"+track+"_"+str(alph_year[year])),'BACKTEST ID'].values[0]))+'.xlsx')










#https://sites.google.com/site/aslugsguidetopython/data-analysis/pandas/calling-r-from-python
import pandas as pd
from pandas import read_excel
data_source=r'C:\Users\jonathan.james\Desktop\yulong\demo\hsi_data.csv'
data_source=pd.read_csv(data_source)


from numpy import *
import scipy as sp
from pandas import *
from rpy2.robjects.packages import importr
import rpy2.robjects as ro
import pandas.rpy.common as com

from rpy2.robjects.packages import importr


data_source_convert_R= com.convert_to_r_dataframe(data_source) #pass to R datafame
ro.globalenv['data_source_R'] = data_source_convert_R #pass it to R

formula = 'up ~ f1 + f2'
ro.globalenv['f_r']=formula
#ro.r('formula_R=formula')
ro.r('''fit2=glm(f_r,data = data_source_R, family = "binomial")''')
print(ro.r('summary(fit2)'))
print(ro.r('fitted(fit2)'))


import rpy2.robjects.numpy2ri
rpy2.robjects.numpy2ri.activate()  #activate ro object to python object
fitted_value=ro.r('fitted(fit2)') 




























################################
########miscellanious###########
################################
xx['PT_M_indicate2']=xx.PT_M_indicate.shift(-1)
xx.loc[np.isnan(xx.PT_M_indicate2),'PT_M_indicate2']=0

#find the size of each group
freq=TempA2_use_add_PT.groupby(['PT_M_last','FP2']).size()

#cross tabulation frequency table, row is last perfect trip number, column is this time FP2
freq=pd.crosstab(TempA2_use_add_PT.PT_M_last,TempA2_use_add_PT.FP2)


##convert object(string) to integer
datadef['char'] = datadef['char'].astype('int64')






#output error to log file
#cd C:\Users\jonathan.james\AppData\Local\Continuum\Anaconda2
#python C:\Users\jonathan.james\Desktop\adhot\trifecta_HK\pgm\plot_HK_min_modelcoef_v4.py
 
import sys
sys.stderr = open(r'C:\Users\jonathan.james\Desktop\yulong\log\file.log', 'w')
 
sys.stderr.write('hello\n')
# do whatever
a=5/0
 
 
 
 
sys.stderr.close()
sys.stderr = sys.__stderr__
 
 
 
 
 
cron_try.sh
crontab -l | { cat; echo "* * * * * /usr/bin/python cronexample.py"; } | crontab -
 
 
cronexample.py
import os
ww=os.getcwd()
 
#log = open(r'C:\Users\jonathan.james\Desktop\yulong\log\file.log', "w")
 
log = open(r'/home/jonathan.james/log/file.log', "w")
 
log.write("success")
log.write(ww)
log.close()
 
 
 
import datetime
time_start=datetime.datetime.now()
import numpy as np
 
accuracy_list=[]
t_stat_list=[]
thershole=5
from scipy.stats import t as t_test
t_thershole=t_test.ppf([0.99], 2000-1+20-1)[0] #t statistic percentile
#i=20
for i in range(0,200):    
    max_learning_rate = 0.02
    min_learning_rate = 0.0001
    decay_speed = 1600
    learning_rate = min_learning_rate + (max_learning_rate - min_learning_rate) * math.exp(-i/decay_speed)
    batch_X, batch_Y = mnist.train.next_batch(100)
    sess.run(train_step, {X: batch_X, Y_: batch_Y, lr: learning_rate, tst: False, pkeep: 0.75, pkeep_conv: 1.0})
    accuracy_np=sess.run(accuracy,{X: test_X, Y_: test_Y, lr: learning_rate, tst: False, pkeep: 0.75, pkeep_conv: 1.0})
    accuracy_list.append(accuracy_np)
    print('finished ',i,accuracy_np)
 
 
    if (i%thershole==0) & (i>=2*thershole):
        accuracy_list_np=np.asarray(accuracy_list)
        group1=accuracy_list_np[-thershole:]
        group1_mean=np.mean(group1)
        group2=accuracy_list_np[0:(len(accuracy_list_np)-thershole)]
        group2_mean=np.mean(group2)
        group1_sample_var=np.var(group1,ddof=1)
        group2_sample_var=np.var(group2,ddof=1)
        mean_diff=group1_mean-group2_mean
        group_var=np.sqrt(group1_sample_var/len(group1)+group2_sample_var/len(group2))
        t_stat=np.abs(mean_diff/group_var)
        t_stat_list.append(t_stat)
        print('t_stat ',t_stat,' ',group1_mean,' ',group2_mean)
        if np.abs(group1_mean-group2_mean)<=0.03: #0.04
            break
 
 
 
time_end=datetime.datetime.now()
print(time_end-time_start)
 
import numpy as np
accuracy_list_np=np.asarray(accuracy_list)
 
import matplotlib.pyplot as plt
plt.plot(range(0,len(accuracy_list_np)),accuracy_list_np,'g') 
plt.show()
 
t_stat_list_np=np.asarray(t_stat_list)
plt.plot(range(0,len(t_stat_list_np)),t_stat_list_np,'g') 
plt.show()






from lxml import etree

import urllib.request


#web = urllib.request.urlopen("http://www.ffiec.gov/census/report.aspx?year=2011&state=01&report=demographic&msa=11500")
web = urllib.request.urlopen("http://www.fdmbenzinpriser.dk/searchprices/5/")

s = web.read()

html = etree.HTML(s)

## Get all 'tr'
tr_nodes = html.xpath('//table[@id="Report1_dgReportDemographic"]/tr')

## 'th' is inside first 'tr'
header = [i[0].text for i in tr_nodes[0].xpath("th")]

## Get text from rest all 'tr'
td_content = [[td.text for td in tr.xpath('td')] for tr in tr_nodes[1:]]








#https://stackoverflow.com/questions/28305578/python-get-html-table-data-by-xpath
import lxml.html as LH
import requests
import pandas as pd
def text(elt):
    return elt.text_content().replace(u'\xa0', u' ')

url = 'https://au.finance.yahoo.com/quote/%5EAORD/history?period1=946656000&period2=1893427200&interval=1d&filter=history&frequency=1d'
r = requests.get(url)
root = LH.fromstring(r.content)
 
for table in root.xpath('//*[@id="render-target-default"]'):
    #header = [text(th) for th in table.xpath('//th')]        # 1 You can use table.xpath('//th') to find the column names.
    data2 = [[text(td) for td in tr.xpath('td')] for tr in table.xpath('//tr')]              #for each row, tr.xpath('td') returns the element representing one "cell" of the table.
                              # 2table.xpath('//tr') returns the rows,
    data2 = [row for row in data2 if len(row)==len(header)]    # 3 
    data2 = pd.DataFrame(data2, columns=header)                # 4
    print(data2)











#https://stackoverflow.com/questions/28305578/python-get-html-table-data-by-xpath
import lxml.html as LH
import requests
import pandas as pd
def text(elt):
    return elt.text_content().replace(u'\xa0', u' ')
 
url = 'http://www.fdmbenzinpriser.dk/searchprices/5/'
r = requests.get(url)
root = LH.fromstring(r.content)
 
for table in root.xpath('//table[@id="sortabletable"]'):
    header = [text(th) for th in table.xpath('//th')]        # 1 You can use table.xpath('//th') to find the column names.
    data = [[text(td) for td in tr.xpath('td')]             #for each row, tr.xpath('td') returns the element representing one "cell" of the table.
            for tr in table.xpath('//tr')]                   # 2table.xpath('//tr') returns the rows,
    data = [row for row in data if len(row)==len(header)]    # 3 
    data = pd.DataFrame(data, columns=header)                # 4
    print(data)
 
 
 
 
 
 
 
 
import lxml.html as LH
import requests
import pandas as pd
def text(elt):
    return elt.text_content().replace(u'\xa0', u' ')
 
url = 'https://i...content-available-to-author-only...o.jp/en/nkave/archives/data'
r = requests.get(url)
root = LH.fromstring(r.content)
 
for s in root.xpath('//*[@id="data_list"]'):   #s is the item in this xpath
    data = [[text(td) for td in tr.xpath('td')]  
            for tr in s.xpath('//tr')]                   # tr is row, under each row, each element called td
    header=data[0]
    data=data[1:]
    data = [row for row in data if len(row)==len(header)]    # 3 
    data = pd.DataFrame(data, columns=header)                # 4
    print(data)
 
 
 
 

 
import lxml.html as LH
import requests
import pandas as pd
 
url = 'https://i...content-available-to-author-only...o.jp/en/nkave/archives/data'
r = requests.get(url)
root = LH.fromstring(r.content)
 
for table in root.xpath('//*[@id="data_list"]'):   #
    data2 = [[td.text_content() for td in tr.xpath('td')]  
            for tr in table.xpath('//tr')]                   # tr is row, under each row, each element called td
    header=data2[0]
    data2=data2[1:]
    data2 = [row for row in data2 if len(row)==len(header)]    # 3 
    data2 = pd.DataFrame(data2, columns=header)                # 4
    print(data2)
 
 
 
 
 
 
http://w...content-available-to-author-only...e.com/exchange-en/products/int/fix/government-bonds/15646!onlineStatsReload?productId=15646&productGroupId=862&busDate=20181227
 
 
 
//*[@id="tabs-1"]/div[2]/div/div[1]/div/table
//*[contains(concat( " ", @class, " " ), concat( " ", "clearfix", " " ))]
 
 
 
 
import lxml.html as LH
import requests
import pandas as pd
 
url = 'http://w...content-available-to-author-only...e.com/exchange-en/products/int/fix/government-bonds/15646!onlineStatsReload?productId=15646&productGroupId=862&busDate=20181227'
 
r = requests.get(url)
root = LH.fromstring(r.content)
 
for table in root.xpath('//*[@id="tabs-1"]/div[2]/div/div[1]/div/table'):   #under this xpath, only one table called id="data_list"
    data3 = [[td.text_content() for td in tr.xpath('td')]  
            for tr in table.xpath('//tr')]                   # tr is row, under each row, each element called td
    header = [[k.text_content() for k in s.xpath('tr')]  
            for s in table.xpath('//thead')]                   # tr is row, under each row, each element called td
    data3=data3[1:]
    data3 = [row for row in data3 if len(row)==len(header)]    # 3 
    data3 = pd.DataFrame(data3, columns=header)                # 4
    print(data2)
 
 
for table in root.xpath('//*[@id="tabs-1"]/div[2]/div/div[1]/div/table/thead'):
        for a in table.xpath('//tr'):
            for b in a.xpath('th'):
                print(b.text_content())
 
 
 
 
 
 
 
 
 
 
 
 
 
 
https://w...content-available-to-author-only...e.com/products/219/Brent-Crude-Futures/data?marketId=222466&span=1












#https://w...content-available-to-author-only...h.com/investing/fund/DHFCX
from lxml import etree
import lxml.html as LH
import requests
import pandas as pd
 
url = 'https://w...content-available-to-author-only...h.com/investing/fund/DHFCX'
r = requests.get(url)
root = LH.fromstring(r.content)
 
#the // is telling it to search anywhere in the document
#(it doesn't matter if the current node is a specific div, it always searches from start).
#To find any nodes under the current node, replace // with .// 
#(the . indicates that the search starts with the current node, not the root).
for atag in root.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "element--intraday", " " ))]'):
    data2 = [[td.text_content()] for td in atag.xpath('.//span')]  
    class_name = [[td.classes] for td in atag.xpath('.//span')] 
 
 
 
 
 
 
 
 
 
 
 
 
#https://w...content-available-to-author-only...h.com/investing/fund/DHFCX
from lxml import etree
import lxml.html as LH
import requests
import pandas as pd
import re
import datetime
from collections import OrderedDict
 
#url = 'https://w...content-available-to-author-only...h.com/investing/fund/OTPSX'
url = 'https://www.marketwatch.com/investing/fund/otpsx'
r = requests.get(url)
root = LH.fromstring(r.content)
price_value=root.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "value", " " ))]')[0].text_content() #[0] because under this xpath list only 1 element
price_value=float(price_value.replace(',',''))
 
#format like this "Last Updated: Jan 3, 2019 4:08 p.m. HKST"
updated_time_raw=root.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "timestamp__time", " " ))]')[0].text_content()
result = re.search('Last Updated: (.*)', updated_time_raw).group(1)
result_split=result.split(",")
 
year=int(result_split[1].strip()[0:4])
 
def month_converter(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(month) + 1
month=month_converter(result_split[0].strip()[0:3])
 
 
day=[int(s) for s in result_split[0].split() if s.isdigit()][0]
 
dt = datetime.datetime(year, month, day)
date_updated=dt.strftime('%Y-%m-%d')
 
output_df=pd.DataFrame(OrderedDict({'Date':[date_updated],'Close':[price_value]}))
 
 
 
 
 
 
 
 
# wall street journal
import lxml.html as LH
import requests
import pandas as pd
from collections import OrderedDict
 
#def text(elt):
#    return elt.text_content().replace(u'\xa0', u' ')
 
url = 'https://q...content-available-to-author-only...j.com/index/JP/NIK/historical-prices'
r = requests.get(url)
root = LH.fromstring(r.content)
 
for s in root.xpath('//*[@id="historical_data_table"]'):   #s is the item in this xpath
    data = [[td.text_content() for td in tr.xpath('td')]  
            for tr in s.xpath('//tr')]                   # tr is row, under each row, each element called td
    header = ['Date','Open','High','Low','Close']    
    data = [row for row in data if len(row)==len(header)]    # 3 
    data = pd.DataFrame(data, columns=header)                # 4
    print(data)
 
from datetime import datetime
data['Date1']=data['Date'].apply(lambda x:datetime.strptime(x,'%m/%d/%y'))#convert string (need to tell python string format) to datetime
data['Date2']=data['Date1'].apply(lambda x:x.strftime('%Y-%m-%d')) #convert time to string(need to tell python string format)








import pandas.io.sql as sql
extdate = sql.read_sql('SELECT * FROM Tierce_Capture_oddoddoddsddo_2014 ORDER BY racekey ASC LIMIT 10',engine)
check.to_sql("Tierce_Capture_oddoddoddsddo_2014", engine, if_exists='append',index=False)


















#cron job
from crontab import CronTab 
my_cron = CronTab(user='admin')
job = my_cron.new(command='nothing here',comment='dateinfo')
job.setall('* * 10 8 *')
my_cron.write()
 
print job.enable()
 
from crontab import CronTab 
my_cron = CronTab(user='admin')
job = my_cron.new(command='/usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py > /home/admin/pythontry/temp2.log 2>&1 &',comment='dateinfo')
job.setall('* * * * *')
my_cron.write()
 
print job.enable()
 
from crontab import CronTab 
my_cron = CronTab(user='admin')
job = my_cron.new(command='/usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py',comment='dateinfo')
job.minute.every(50) 
my_cron.write()
 
print job.enable()
 
from crontab import CronTab 
my_cron = CronTab(user='admin')
job = my_cron.new(command='/usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py',comment='dateinfo')
job.minute.every(500) 
my_cron.write()
 
print job.enable()
 
from crontab import CronTab 
my_cron = CronTab(user='admin')
job = my_cron.new(command='/usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py',comment='dateinfo')
job.setall('44 17 * * *')
my_cron.write()
 
print job.enable()
 

 
#there is a bug in python-crontab
#always one comment in multiple cron job
 
#remove cron with comment='dateinfo'
from crontab import CronTab
my_cron = CronTab(user='admin')
for job in my_cron:
    if job.comment == 'coming_cronjob':
        my_cron.remove(job)
        my_cron.write()
 
 
#add cronjob to linux
crontab -l | { cat; echo "* * * * * /usr/bin/python cronexample.py #dateinfo"; } | crontab -            
import os
os.system('crontab -l | { cat; echo "44 17 * * * /usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py #dateinfo2"; } | crontab -')             
os.system('crontab -l | { cat; echo "* * * * * /usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py #dateinfo"; } | crontab -')
os.system('crontab -l | { cat; echo "58 11 21 8 * /usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py #dateinfo"; } | crontab -')   
 
 
 
os.system('crontab -l | { cat; echo "58 11 1 8 * /usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py #dateinfo"; } | crontab -') 
os.system('crontab -l | { cat; echo "58 11 01 8 * /usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py #dateinfo"; } | crontab -') 
 
 
#meaning 06:00 (24 hr time)
#cron_job.setall('00 06 * * *')
 
 
 
 
 
 
 
 
 
 
import os
import sys
import MySQLdb
import pandas as pd
import datetime
from datetime import datetime as dt
mysql_config = {
   'user': ,
   'pw': ,
   'host': ,
   'port': ,
   'database': ''
}
 
rww_racing_day=pd.DataFrame([])
 
 
try:
    cnx = MySQLdb.connect(host=mysql_config['host'], user=mysql_config['user'], passwd=mysql_config['pw'], db=mysql_config['database'], use_unicode=True)
    racedate = pd.read_sql_query('SELECT  WHERE DATE>=CURDATE() LIMIT 1' , cnx).iloc[0,0]
    racedate_string=racedate.strftime('%Y-%m-%d')
 
    racedate_string="2019-07-14"
    print("Doing Raceday ",racedate_string)
    query='SELECT DATE,RaceNo,Race_Time WHERE DATE='+'"'+racedate_string+'"'
    rww_racing_day = pd.read_sql_query(query , cnx)
    #a=1/0
except:
    print("Error message: ",sys.exc_info()[0])
 
 
if rww_racing_day.shape[0]!=0:
    rww_racing_day=rww_racing_day.drop_duplicates()
    rww_racing_day=rww_racing_day.reset_index(drop=True)
    racedate_from_rww=rww_racing_day[0:1]['DATE'][0].strftime('%Y-%m-%d')
 
    #remove cron with comment='coming_cronjob'
    from crontab import CronTab
    my_cron = CronTab(user='admin')
    for job in my_cron:
        if job.comment == 'coming_cronjob':
            my_cron.remove(job)
            my_cron.write()
 
    #i==0
    for idx, rww_row in rww_racing_day.iterrows():
        #print(rww_row)
        #if i==0:
        #    break
        time_ymdhms=racedate_from_rww+":"+str(rww_row['Race_Time'])+':00'
        time_ymdhms_dt=dt.strptime(time_ymdhms,'%Y-%m-%d:%H:%M:%S')-datetime.timedelta(minutes=5)
 
        hour_use=str(time_ymdhms_dt.hour)
        minute_use=str(time_ymdhms_dt.minute)
        day_use=str(time_ymdhms_dt.day)
        month_use=str(time_ymdhms_dt.month)
        race_no=str(rww_row['RaceNo']).replace('.0','')
 
#        minute_use=str(20)
#        hour_use=str(14)
#        day_use=str(21)
#        month_use=str(8)
 
        cron_string=str(minute_use)+' '+str(hour_use)+' '+str(day_use)+' '+str(month_use)+' * '+ '/home/executor/autoupdate.sh '+race_no+' > /home/executor/autoupdate'+race_no+'.log'+' #coming_cronjob'
        #cron_string=minute_use+' '+hour_use+' '+str(day_use)+' '+str(month_use)+' * '+ '/usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py'+' #coming_cronjob'
        cron_shell_cmd='crontab -l | { cat; echo '+'"'+cron_string+'"'+'; } | crontab -'
        os.system(cron_shell_cmd)
        print "finished scheduling cronjobs for race "+race_no+" on "+racedate_string
else:
    print 'rww has no data'
 
 
 
 
 
 
 
 
 
import os
os.system('crontab -l | { cat; echo "44 17 * * * /usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py #dateinfo2"; } | crontab -')             
os.system('crontab -l | { cat; echo "* * * * * /usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py #dateinfo"; } | crontab -')
os.system('crontab -l | { cat; echo "58 11 21 8 * /usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py #dateinfo"; } | crontab -')            
os.system('crontab -l | { cat; echo "1 16 * * * /usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py #dateinfo"; } | crontab -')           
 
os.system('crontab -l | { cat; echo "20 14 21 8 * /usr/local/anaconda/bin/python /home/admin/pythontry/cronexample.py #coming_cronjob"; } | crontab -')          
 





















from lxml import etree
import lxml.html as LH
import html
 
 
import lxml.html as html
 
 
 
    Horse  13   SUNNY ORIENT  will carry  113  lbs. (14/07 12:41)
    Horse  5 ,  YEE CHEONG LUCKY  Scratched. Standby starter  BLISSFUL EIGHT  Promoted. (13/07 09:46)
    Horse  5   BLISSFUL EIGHT , Rider changed to  M Harley . (13/07 09:46)
    Horse  5   BLISSFUL EIGHT  will carry  131  lbs. (13/07 09:47)
 
    Horse[ ]*([0-9]{1,2})             # this is for 13,* mean repeat space 0 to inf times
    (?:(?!Horse[ ]*[0-9]{1,2}).)*?    #this is to match all letters/symbols
    ([0-9]{1,3})
    [ ]*lbs[ ]*\.[ ]*                  #\. is to escape .
    \(([0-9]{1,2}/[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2})\)  #this is for (14/07 12:41)
 
    word="Horse  13   SUNNY ORIENT  will carry  113  lbs. (14/07 12:41) Horse  13   SUNNY ORIENT  will carry  113  lbs. (14/07 12:41) Horse  13   SUNNY ORIENT  will carry  113  lbs. (14/07 12:41)"
    pattern = re.compile(r'Horse[           ]*([0-9]{1,2})')
    pattern.findall(word)               
 
    word="Horse  13   SUNNY ORIENT  will carry  113  lbs. (14/07 12:41)"
    pattern = re.compile(r'(lbs*\.[ ])')
    pattern.findall(word)  
 
    #use this can also do the same thing
    #[ ]* mean 0 to inf occurane of space
    #\d	  Matches with digits [0-9] and /D (upper case D) matches with non-digits.
    # \s 空白字符包括空格,# \S 非空白
    #[\S\s]* means any letter 0 to inf occurane, no need use | inside, because anything inside[ ] already meaning or, but cannot use to find multiple pattern
    word=tds[19]
    pattern=re.compile(r'Horse[ ]*([0-9]{1,2})[A-Za-z0-9 ]*carry[ ]*([0-9]{1,3})[ ]*lbs.[ ]*\(([0-9]{1,2}/[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2})\)')
    pattern.findall(word) 
 
    word='jonathanio 465  75jjrrl../ apple../.4/5.vv  jonathanio 465  75jjrrl../ apple'
    pattern=re.compile(r'(jonathan)(?:.)*?(apple)')
    pattern.findall(word)
    pattern=re.compile(r'(jonathan)[\S\s]*(apple)')
    pattern.findall(word) 
 
    #original version                                  
    pattern = re.compile(r'Horse[ ]*([0-9]{1,2})(?:(?!Horse[ ]*[0-9]{1,2}).)*?([0-9]{1,3})[ ]*lbs[ ]*\.[ ]*\(([0-9]{1,2}/[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2})\)')
    time.sleep(0.05)
    change_url="https://racing.hkjc.com/racing/Info/meeting/Changes/English/Local/"
    res = requests.get(change_url+"20191006")
    if not res.ok:
        raise Exception("Can\'t access Changes url")
    
    import re
    re.search('Description',res.content)
    #in python 2.7
    if res.content.find('Description') < 0:
        raise Exception("Can\'t access Changes url")
    #in python 3.6
    if str(res.content, 'utf-8').find('Description')<0:
        raise Exception("Can\'t access Changes url")    
    
    tree = html.fromstring(res.content)
    tables = tree.xpath('//table')
    tables = [table for table in tables if table.text_content().find('Description')>0]
 
    if len(tables)==0:
        raise Exception('Wrong Changes page')
 
    tds = tables[0].xpath('tr/td')
    tds = [td.text_content().strip() for td in tds]
 
    DF = pd.DataFrame()
    i=0
    for i in range(len(tds)):
        if i==3:
            break
        race_td = re.match('Race[ ]*([0-9]{1,2})',tds[i-1])
        print(race_td)
        if race_td:
            race_no = int(race_td.groups()[0])
            weight_change = pattern.findall(tds[i])
            if len(weight_change)>0:
                tempDF = pd.DataFrame(weight_change,columns = ['HorseNo','WeightUpdated','date_text'],dtype = int)
                tempDF['Time'] = pd.to_datetime(tempDF['date_text'],format = '%d/%m %H:%M')
                tempDF['Time'] += (tempDF['Time'].dt.month==extdate.month) * datetime.timedelta(days=365)
                tempDF['RaceNo'] = race_no
                tempDF = tempDF.sort('Time',ascending = False)
                tempDF.drop_duplicates('HorseNo',inplace=True)  #for the same horseno, there may be more then one update record, use the latest one
                DF = DF.append(tempDF)
    DF_check=DF.copy()




































 
 
 
 
 
 
url = 'https://iosbsinfo02.hkjc.com/infoA/AOSBS/HR_GetInfo.ashx?QT=HR_oddoddoddsddo_ALL&Race=*&Venue=*&Result=1&Dividend=1&JTC=1&JKC=1&Lang=en-US'
def gen_race_cards(url = 'https://i...content-available-to-author-only...c.com/infoA/AOSBS/HR_GetInfo.ashx?QT=HR_oddoddoddsddo_ALL&Race=*&Venue=*&Result=1&Dividend=1&JTC=1&JKC=1&Lang=en-US'):
    ##old_url
    #url = 'http://i...content-available-to-author-only...c.com/infoA/AOSBS/HR_GetInfo.ashx?QT=HR_oddoddoddsddo_Win&Race=*&Venue=*&Lang=en-US'
    extdate = "06/10/2019"
    time.sleep(0.05)
    res = requests.get(url)
    if not res.ok:
        raise Exception("Request Fail - " + url)
    tree = html.fromstring(res.content)
    #rememebr to use small letter r in raceinfo
    
    
    #https://pythontips.com/2018/06/20/an-intro-to-web-scraping-with-lxml-and-python/
#// these double forward slashes tell lxml that we want to search for all
# tags in the HTML document which match our requirements/filters. Another option was
# to use / (a single forward slash). The single forward slash returns only the immediate 
#child tags/nodes which match our requirements/filters

    
    races_list = tree.xpath('//raceinfo')
    races_list = tree.xpath('//RaceInfo')
 
    races_list = tree.xpath('//rec')
    races_list = tree.xpath('//*[@id="collapsible6"]')
 
    races_list = tree.xpath('//*[@id="collapsible3"]/div[1]/div[2]')
 
 
//*[@id="collapsible6"]/div[1]/div[2]/div/span/text()[1]
 
 
//*[@id="collapsible6"]
 

 
    races_list = [r for r in races_list if r.get('postdate') == extdate]
    table = pd.DataFrame(columns=['RaceNo','Going','HorseNo','HorseName','Draw','Jockey','JockeyAllowance','WeightAdjusted','WeightCarried'])
    i=0
    for race in races_list:
        if i==10:
            break
        i=i+1
        print(race.get('raceno'))
        country = race.get('country').upper()
        if not country in ['SHA TIN','HAPPY VALLEY']:
            continue
        raceno = float(race.get('raceno'))
        going = race.get('going')
        runners_list = race.xpath('starters/starter/runner')
#        i=0
        for runner in runners_list:
#            if i==0:
#                break
            if int(runner.get('scratched'))==1:
                continue                                       #continue will go back to for loop, it will not continue below
            horse_no = float(runner.getparent().get('number'))
            horse = runner.get('name')
            draw = float(runner.get('draw'))
            jockey = runner.get('jockey')
            allowance = runner.get('weightallowance')
            allowance = -float(allowance) if len(allowance)>0 else 0
            weight_adj = float(runner.get('handicapweight'))
            carried = weight_adj - allowance
            table = table.append({'RaceNo':raceno,'Going':going,'HorseNo':horse_no,'HorseName':horse,
                          'Draw':draw,'Jockey':jockey,'JockeyAllowance':allowance,'WeightAdjusted':weight_adj,
                          'WeightCarried':carried},ignore_index=True)
    ###Update Weight
    extdate=datetime.date(2019,7,14)
    DF = update_weight(extdate)
    table['WeightCarried2'] = np.nan
    if len(DF)>0:
        DF['ind'] = DF['RaceNo']*1000+DF['HorseNo'] 
        DF = DF.sort('ind')
        if DF.duplicated('ind').sum()>0:           #
            logging.warning('Duplicated Rows in changes')
            DF.drop_duplicates('ind',inplace=True)
        ind = table['RaceNo']*1000+table['HorseNo']
        table.loc[ind.isin(DF['ind']),'WeightCarried2'] = DF['WeightUpdated'].values
                  #for horse with updated in changes, if WeightCarried2 not wqual to WeightAdjusted
        table.loc[(table['WeightCarried2'].notnull())&(table['WeightAdjusted']!=table['WeightCarried2']),'WeightCarried'] = table.loc[(table['WeightCarried2'].notnull())&(table['WeightAdjusted']!=table['WeightCarried2']),'WeightCarried2']
    table.to_csv(race_card_filename,index = False)
    DF_check=DF.copy()
    return None
 
def gen_today_race_data():
    # extract and calculate values from RaceCard csv to a data frame
    #extdate=datetime.date(2019,7,14)
    race_card_df = pd.read_csv(race_card_filename, header=0, na_filter=False)
 
    race_card_df['HorseName'] = map(lambda x: x.upper(), race_card_df['HorseName'])
    race_card_df['Jockey'] = map(lambda x: x.upper(), race_card_df['Jockey'])
    race_card_df['RaceNo'] = race_card_df['RaceNo'].astype(np.float)
    # connect to MySql database (mysql.connector)
    #cnx = mysql.connector.connect(**mysql_config)
 
    # connect to Mysql database (MySQLdb)
    # cnx = MySQLdb.connect(host=mysql_config['host'], user=mysql_config['user'], passwd=mysql_config['password'], db=mysql_config['database'], use_unicode=True)
    extdate = pd.read_sql_query('SELECT DATE FROM HKRACINGCALENDAR WHERE DATE>=CURDATE() LIMIT 1' , cnx).iloc[0,0].strftime('%Y-%m-%d')
    # put the data to a data frame
    extdate=datetime.date(2019,7,14)
    db_df = pd.read_sql_query('SELECT * FROM `RACE_RUNNERS_WITH_W` WHERE `Date` = \'' + str(extdate) + '\'', cnx)
 
    if len(db_df)==0:
        logger.error("*"*25+"ERROR"+"*"*25)
        logger.error('SQL Database have no data on '+str(extdate))
        logger.error("")
        stop=True
        raise Exception('Database error')
 
    # change to suitable case / data type
    db_df['Horse'] = map(lambda x: x.upper(), db_df['Horse'])
    db_df['Jockey'] = map(lambda x: x.upper(), db_df['Jockey'])
    db_df['Stable'] = map(lambda x: x.upper(), db_df['Stable'])
    db_df['Season_'] = map(lambda x: str(x), db_df['Season_'])
    db_df['No_'] = map(lambda x: int(x), db_df['No_'])
    db_df['RaceNo'] = db_df['RaceNo'].astype(np.float)
    ##code from R?
    db_df["Wt__w_Adj_"] = race_card_df["WeightCarried"]
    ##
 
    db_df_check=db_df.copy()
    race_card_df_check=race_card_df.copy()
 
 
 
    runner_in_db = db_df['RaceNo'].map(str) + '--' + db_df['No_'].apply(lambda x: '%02d' % x).map(str)
    runner_in_race_card= race_card_df['RaceNo'].map(str) + '--' + race_card_df['HorseNo'].apply(lambda x: '%02d' % x).map(str)
 
    # sorting
    db_df = db_df.sort(['Season_', 'No_'], ascending=[True, True])
    race_card_df = race_card_df.sort(['RaceNo', 'HorseNo'], ascending=[True, True])
 
    #below two code will make the order weird, race 1 then race 10...
    runner_in_db.sort()
    runner_in_race_card.sort()
 
    #remove a record in runner_in_race_card
    #runner_in_race_card=runner_in_race_card.drop()
 
    # list withdrawn runners and remove them from data frame race runner with w
    if (runner_in_race_card.size != runner_in_db.size):
        missing_runner_ind = runner_in_db.isin(runner_in_race_card)
        missing_runner_idx = list(missing_runner_ind[missing_runner_ind == False].index)
        missing_runners = db_df.iloc[missing_runner_idx]
 
        for idx, missing_runner in missing_runners[['Season_', 'No_', 'RaceNo', 'Horse']].iterrows():
            logger.info('Withdrawn: {}, Race {} - {}. {}'.format(missing_runner['Season_'], int(missing_runner['RaceNo']), missing_runner['No_'], missing_runner['Horse']))
 
        # drop the withdrawn horse from data frame and reset index
        db_df = db_df.drop(db_df.index[missing_runner_idx]).reset_index(drop=True) # index is 133, race 10 horse 11 in 20190714, remove this record 
 
    # error if there is in-existent runner in the data from HKJC
    if (db_df[[0]].size != race_card_df[[0]].size):
        logger.error("*"*25+"ERROR"+"*"*25)
        logger.error('In-existent runner is found in the data from HKJC')
        logger.error("")
        stop = True
        raise Exception('In-existent runner')
 
    # data checking / updating
    i=0
    for idx, db_row in db_df.iterrows():
        print(idx)
        print(db_row)  #the whole row
        if i==0:
            break
        race_card_row = race_card_df.iloc[idx]
 
        # error if runner name can't be matched (no replacement should be allowed after 12:00 pm)
        if (db_row['Horse'] != race_card_row['HorseName']):
            logger.error("*"*25+"ERROR"+"*"*25)
            logger.error('Unmatched runner name: {}, Race {} - {}. "{}" <> "{}"'.format(db_row['Season_'], int(db_row['RaceNo']), db_row['No_'], db_row['Horse'], race_card_row['HorseName']))
            logger.error("")
            logger.error("")
            stop = True
            raise Exception('Unmatched runner')
 
        # compare and update jockey name
        if (db_row['Jockey'] != race_card_row['Jockey']):
            logger.warning('Update jockey: {}, Race {} - {}. {}: "{}" -> "{}"'.format(db_row['Season_'], int(db_row['RaceNo']), db_row['No_'], db_row['Horse'], db_row['Jockey'], race_card_row['Jockey']))
            db_df.loc[idx,'Jockey'] = race_card_row['Jockey']
 
        # compare and update weight carried
        if (db_row['Wt'] != race_card_row['WeightCarried']):
            logger.warning('Update weight carried: {}, Race {} - {}. {}: "{}" -> "{}"'.format(db_row['Season_'], int(db_row['RaceNo']), db_row['No_'], db_row['Horse'], db_row['Wt'], race_card_row['WeightCarried']))
            db_df.loc[idx,'Wt'] = race_card_row['WeightCarried']
 
        # Update Draw
        if (db_row['Draw'] != race_card_row['Draw']):
            logger.warning('Update Draw : {}, Race {} - {}. {}: "{}" -> "{}"'.format(db_row['Season_'], int(db_row['RaceNo']), db_row['No_'], db_row['Horse'], db_row['Draw'], race_card_row['Draw']))
 
        # compare and update jockey allowance
        if (db_row['jckAllowance'] != race_card_row['JockeyAllowance']):
            logger.warning('Update jockey allowance: {}, Race {} - {}. {}: "{}" -> "{}"'.format(db_row['Season_'], int(db_row['RaceNo']), db_row['No_'], db_row['Horse'], db_row['jckAllowance'], race_card_row['JockeyAllowance']))
            db_df.loc[idx,'jckAllowance'] = race_card_row['JockeyAllowance']
 
    # write the data frame to TodayRaceData csv
    db_df.to_csv(today_race_data_filename, na_rep='NA', index=False, encoding='utf-8', quoting=csv.QUOTE_MINIMAL)
 
    # close MySql connection
    # cnx.close()
    return None












#download oddoddoddodd from database
import itertools
import copy
 
#qin oddoddoddodd output
import datetime
from datetime import datetime as dt
aa='2018-12-12';bb='1';cc='19:15'
aa='2018-12-09';bb='1';cc='12:25'
aa='2018-12-05';bb='1';cc='18:30'
aa='2018-12-05';bb='4';cc='20:10'
aa='2018-12-16';bb='2';cc='13:00'
aa='2015-02-04';bb='1';cc='19:15'
 
 
aa='2018-09-02';bb='5';cc='14:45'
bet_type='qin'
bet_type='qpl'
bet_type='tri'
def extract_oddoddoddodd(aa,bb,cc,bet_type):
    oddoddoddsddo_output=pd.DataFrame([])
    race_date=str(aa)
    Race_no=bb
    time_set_full=race_date+":"+str(cc)+':00'
    #time_set_datetime=dt.strptime(time_set_full,'%Y-%m-%d:%H:%M:%S')-datetime.timedelta(minutes=0)
    time_set_datetime=dt.strptime(time_set_full,'%Y-%m-%d:%H:%M:%S')+datetime.timedelta(seconds=25)
    time_set=str(time_set_datetime.hour)+':'+str(time_set_datetime.minute)+':'+str(time_set_datetime.second)
 
#    if aa>="2018-12-09":
#        time_set_full=race_date+":"+str(cc)+':00'
#        time_set_datetime=dt.strptime(time_set_full,'%Y-%m-%d:%H:%M:%S')-datetime.timedelta(minutes=0)
#        time_set=str(time_set_datetime.hour)+':'+str(time_set_datetime.minute)        
#        time_set=dt.strptime(time_set,"%H:%M")
 
    #check if table exist
    table_exist=False
    try:
        try:
            query='select * from oddoddoddsddo'+race_date.replace('-','')+' where oddoddoddsddotype='+'"'+bet_type+'"'+ 'and UpTime<='+'"'+time_set+'"'+' and RaceNo='+Race_no+' '+' and RacingDate='+'"'+race_date+'"'+' order by UpTime desc limit 1'
            oddoddoddsddo = pd.read_sql(query, con=connection_oddoddoddodd)
 
 
        except:
            query='select * from `oddoddoddsddo'+race_date.replace('-','')+'.bak`'+' where oddoddoddsddotype="Qin" and UpTime<='+'"'+time_set+'"'+' and RaceNo='+Race_no+' '+' and RacingDate='+'"'+race_date+'"'+' order by UpTime desc limit 1'        
            oddoddoddsddo = pd.read_sql(query, con=connection_oddoddoddodd)
 
        table_exist=True
    except:
        pass
 
    if table_exist:
 
        try:
            exact_hour=oddoddoddsddo['UpTime'].dt.components['hours'].values[0]
            exact_min=oddoddoddsddo['UpTime'].dt.components['minutes'].values[0]
            exact_sec=oddoddoddsddo['UpTime'].dt.components['seconds'].values[0]
 
 
            up_time_old=dt(1900,1,1,exact_hour,exact_min,exact_sec).strftime("%H:%M:%S") #convert to string
            up_time=race_date+' '+up_time_old
 
            extraction_time=oddoddoddsddo['modified'][0].strftime("%Y-%m-%d %H:%M:%S")
 
            time_set=time_set+':00'
 
            oddoddoddsddo_data=oddoddoddsddo['Data'].values[0]
 
 
            all_oddoddoddodd=oddoddoddsddo_data.split(":")
 
            if (bet_type=='qin')|(bet_type=='qpl'):
                horse_comb=list(itertools.combinations(range(1,15), 2))
                horse_comb2=[str(i).replace("(",'').replace(")",'').replace(", ",'-') for i in horse_comb]
                horse_comb2_oddoddoddodd=map(lambda (x,y):x+'='+y+'=0', zip(horse_comb2,all_oddoddoddodd))            
                horse_comb2_oddoddoddodd_output=";".join(horse_comb2_oddoddoddodd)
 
            if (bet_type=='win')|(bet_type=='pla'):
                horse_comb=list(itertools.combinations(range(1,15), 1))
                horse_comb2=[str(i).replace("(",'').replace(")",'').replace(",",'') for i in horse_comb]
                horse_comb2_oddoddoddodd=map(lambda (x,y):x+'='+y+'=0', zip(horse_comb2,all_oddoddoddodd))            
                horse_comb2_oddoddoddodd_output=";".join(horse_comb2_oddoddoddodd)
 
            if (bet_type=='tri'):
                horse_comb=list(itertools.combinations(range(1,15), 3))
                horse_comb2=[str(i).replace("(",'').replace(")",'').replace(", ",'-') for i in horse_comb]
                horse_comb2_oddoddoddodd=map(lambda (x,y):x+'='+y+'=0', zip(horse_comb2,all_oddoddoddodd))            
                horse_comb2_oddoddoddodd_output=";".join(horse_comb2_oddoddoddodd)
 
            if (bet_type=='F-F'):
                horse_comb=list(itertools.combinations(range(1,15), 4))
                horse_comb2=[str(i).replace("(",'').replace(")",'').replace(", ",'-') for i in horse_comb]
                horse_comb2_oddoddoddodd=map(lambda (x,y):x+'='+y+'=0', zip(horse_comb2,all_oddoddoddodd))            
                horse_comb2_oddoddoddodd_output=";".join(horse_comb2_oddoddoddodd)
 
            oddoddoddodd_size=len(horse_comb2_oddoddoddodd)
 
            #checking:
            a1=dt.strptime(up_time_old,"%H:%M:%S")
            a2=dt.strptime(cc,'%H:%M')
            racetime_uptime_diff=(a1-a2).total_seconds()
 
            temp=pd.DataFrame({'Date':[race_date],'Race_no':[Race_no],'extraction_time':[extraction_time],'up_time':[up_time],'oddoddoddodd_custom':[horse_comb2_oddoddoddodd_output],'oddoddoddodd_original':[oddoddoddsddo_data],'oddoddoddodd_size':[oddoddoddodd_size],'racetime_uptime_diff':[racetime_uptime_diff]})    
        except:
        #20181209, modified change from datetime64(2018-12-05 18:30:03) to object (2018-12-09 09:19:27)
        #uptime change from timedelta64(0 days 18:29:59) to object(09:19:22)\
        #so need to use this exception
            temp=pd.DataFrame({'Date':[race_date],'Race_no':[Race_no],'extraction_time':[None],'up_time':[None],'oddoddoddodd_custom':[None],'oddoddoddodd_original':[None],'oddoddoddodd_size':[None],'racetime_uptime_diff':[None]})
    else:
        temp=pd.DataFrame({'Date':[race_date],'Race_no':[Race_no],'extraction_time':[None],'up_time':[None],'oddoddoddodd_custom':[None],'oddoddoddodd_original':[None],'oddoddoddodd_size':[None],'racetime_uptime_diff':[None]})
    oddoddoddsddo_output=oddoddoddsddo_output.append(temp)
    return oddoddoddsddo_output
 
 
 
main3=racerunner_withw_use[['Date','Season_','RaceNo','Race_Time']].copy()
 
main3=main3.loc[main3['Date']!='2019-03-23',:].copy()
 
main3_oddoddoddodd_key=main3[['Date',"RaceNo",'Race_Time']].copy()
main3_oddoddoddodd_key=main3_oddoddoddodd_key.drop_duplicates()
 
main3_oddoddoddodd_key["RaceNo"]=main3_oddoddoddodd_key['RaceNo'].astype(str)
main3_oddoddoddodd_key["RaceNo"]=main3_oddoddoddodd_key['RaceNo'].apply(lambda x: x.replace('.0',''))
 
main3_oddoddoddodd_key=main3_oddoddoddodd_key.sort_values(by=['Date','RaceNo'],ascending=[True,True])
#main3_oddoddoddodd_key=main3_oddoddoddodd_key.loc[(main3_oddoddoddodd_key['Date'].astype(str)>="2015-09-06")&(main3_oddoddoddodd_key['Date'].astype(str)<="2019-09-15"),:]
main3_oddoddoddodd_key=main3_oddoddoddodd_key.loc[(main3_oddoddoddodd_key['Date'].astype(str)>="2015-10-04")&(main3_oddoddoddodd_key['Date'].astype(str)<="2019-10-01"),:]
main3_oddoddoddodd_key=main3_oddoddoddodd_key.reset_index(drop=True)
 
 
 
connection_oddoddoddodd = create_engine('mysql+mysqldb://admin:obey@192.168.1.32:3306/oddoddoddsddoDBBackup')
 
oddoddoddodd_useful=pd.DataFrame([])
i=2293
i=3
 
bet_type='win'
for i in range(0,main3_oddoddoddodd_key.shape[0]):
    row_use=main3_oddoddoddodd_key[i:i+1]
    temp=extract_oddoddoddodd(row_use['Date'].values[0],row_use['RaceNo'].values[0],row_use['Race_Time'].values[0],bet_type)
    oddoddoddodd_useful=oddoddoddodd_useful.append(temp)
    print(row_use['Date'].values[0])
 
oddoddoddodd_useful=oddoddoddodd_useful.loc[~pd.isnull(oddoddoddodd_useful['up_time']),:]
 
 
if bet_type=='tri':
    oddoddoddodd_useful=oddoddoddodd_useful.loc[~((oddoddoddodd_useful['Date']=='2018-09-02')&(oddoddoddodd_useful['Race_no']=='4')),:]  #no data this date
 
oddoddoddodd_useful=oddoddoddodd_useful.reset_index(drop=True)
 
 
oddoddoddodd_useful['up_time_HMS']=oddoddoddodd_useful['up_time'].apply(lambda x:x[-8:])
oddoddoddodd_useful['extraction_time_HMS']=oddoddoddodd_useful['extraction_time'].apply(lambda x:x[-8:])
 
oddoddoddodd_useful['Race_no']=oddoddoddodd_useful['Race_no'].astype(int)
oddoddoddodd_useful=oddoddoddodd_useful.sort_values(by=['Date','Race_no'],ascending=[True,True])
oddoddoddodd_useful['Race_no']=oddoddoddodd_useful['Race_no'].astype(str)
 
oddoddoddodd_useful[bet_type]=bet_type+'@'+oddoddoddodd_useful['Date']+'@'+oddoddoddodd_useful['Race_no']+'@'+oddoddoddodd_useful['extraction_time_HMS']+'@'+oddoddoddodd_useful['up_time_HMS']+'@'+oddoddoddodd_useful['oddoddoddodd_original']+'|'
oddoddoddodd_useful_output=oddoddoddodd_useful[bet_type].copy()
 
 
oddoddoddodd_useful_output.to_csv(bet_type+"_oddoddoddodd.csv",index=False)
 
 










#create extra date in R, deadheat and late withdrawn
## generate new extradates 
 
library(RMySQL)
library(dplyr)
 
select_q = function(q,con = hkdb_sql){
	rs = dbSendQuery(con,q)
	out = fetch(rs,n=-1)
	dbClearResult(rs)
	return(out)
}
disconnectALL=function(){
	lapply(dbListConnections(MySQL()), function(x) dbDisconnect(x) )
}
 
 
## select sql server
#hkdb_sql = dbConnect(MySQL(), user='TAS-2', password='Bruce2233', dbname='HKDB', host='192.168.1.6')
hkdb_sql = dbConnect(MySQL(), user='admin', password='tas2233', dbname='HKDBForModel', host='192.168.1.7')
 
q1 = "select season_ racekey, No_ horse_no, fp2, jockey, final_oddoddoddsddo,win_oddoddoddsddo_final last_oddoddoddsddo from RACE_RUNNERS_WITH_W where season_<'2014-001' and season_>='2008-001'"
q2 = "select season_ racekey, No_ horse_no, fp2, jockey, final_oddoddoddsddo,win_oddoddoddsddo_capture last_oddoddoddsddo from RACE_RUNNERS_WITH_W where season_>='2014-001'"
 
 
data_q1 = select_q(q1)
data_q2 = select_q(q2)
data_q2$last_oddoddoddsddo=as.numeric(data_q2$last_oddoddoddsddo)
data_q = rbind(data_q1,data_q2)
 
## select deadheat
deadheat = data_q %>% filter(jockey!="* WITHDRAWN *",fp2>0,fp2<15) %>% group_by(racekey) %>% summarize(deadheat = any(table(fp2)>1)>0) %>% filter(deadheat)%>% .$racekey
extra1 = data.frame(racekey = deadheat,remark = "Deadheat",stringsAsFactors=F)
## select late withdrawn
late_withdrawn = data_q %>% filter(last_oddoddoddsddo>0,final_oddoddoddsddo==0) %>% .$racekey %>% unique
extra2 = data.frame(racekey = late_withdrawn,remark = "Late_withdrawn",stringsAsFactors=F)
## select abnormal oddoddoddsddo
#data_q %>% filter(last_oddoddoddsddo>0) %>% group_by(racekey) %>% summarize(ratio = 1/sum(1/last_oddoddoddsddo)) %>% filter(abs(ratio-0.825)>0.25)
 
 
extra = rbind(extra1,extra2)
disconnectALL()
write.csv(extra,file="C:\\Users\\jonathan.james\\Desktop\\setting\\extra_dates_v3.csv",row.names=F)













#check frequency
rww_check_fq=racerunner_withw_use_temp[['Date',"Season_","RaceNo",'No_',"Race_Time",'fp2',"Win_oddoddoddsddo_final","Win_oddoddoddsddo_capture"]].copy()
 
rww_check_fq['Win_oddoddoddsddo_final']=pd.to_numeric(rww_check_fq['Win_oddoddoddsddo_final'],errors='coerce')
rww_check_fq['Win_oddoddoddsddo_capture']=pd.to_numeric(rww_check_fq['Win_oddoddoddsddo_capture'],errors='coerce')
 
rww_check_fq=rww_check_fq.loc[~pd.isnull(rww_check_fq['Win_oddoddoddsddo_capture']),:]
rww_check_fq=rww_check_fq.loc[~pd.isnull(rww_check_fq['Win_oddoddoddsddo_final']),:]
rww_check_fq=rww_check_fq.reset_index(drop=True)
 
#find capture probability
data=rww_check_fq.loc[(rww_check_fq['Date']=='2019-10-01')&(rww_check_fq['RaceNo']==7),:]
col_name="Win_oddoddoddsddo_capture"
output_name="Win_probs_capture"
def rep_sum(data,col_name,output_name):
    data_old=data.index
    data=data.reset_index(drop=True)
    sumtotal=sum(np.reciprocal(data.loc[:,col_name]))
    temp=np.reciprocal(data.loc[:,col_name].values)/sumtotal
    output=pd.Series(temp,index=data_old)
    return output
 
rww_check_fq['Win_probs_final']=rww_check_fq.groupby(['Date',"RaceNo"],group_keys=False).apply(lambda x:rep_sum(x,"Win_oddoddoddsddo_final","Win_probs_final"))
rww_check_fq['Win_probs_capture']=rww_check_fq.groupby(['Date',"RaceNo"],group_keys=False).apply(lambda x:rep_sum(x,"Win_oddoddoddsddo_capture","Win_probs_capture"))
 
 
#read 25s oddoddoddodd
bet_type='win'
file_name=bet_type+"_oddoddoddodd_prob_25s_20191006.csv"
oddoddoddodd_prob_25s = pd.read_csv(file_name)
 
list(rww_check_fq.columns.values)
list(oddoddoddodd_prob_25s.columns.values)
 
 
rww_check_fq=pd.merge(rww_check_fq,oddoddoddodd_prob_25s[['Date','RaceNo','HorseNo','win25s_oddoddoddodd', 'win25s_prob']].copy(),how='left',left_on=['Date','RaceNo','No_'],right_on=['Date','RaceNo','HorseNo'])
list(rww_check_fq.columns.values)
rww_check_fq=rww_check_fq.loc[~pd.isnull(rww_check_fq['win25s_oddoddoddodd']),:]
 
rww_check_fq.loc[rww_check_fq['fp2']==1,'win']=1
rww_check_fq['win']=rww_check_fq['win'].fillna(0)
a=rww_check_fq.describe()
 
 
 
#read model prob
year=[2015,2016,2017,2018]
model_prob=pd.DataFrame([])
i=2015
for i in year:
    model_prob_path=r'C:\Users\jonathan.james\Desktop\zip\HK_Base15.2_20190903_rep1\WinPlaProb_'+str(i)+'.csv'
    temp=pd.read_csv(model_prob_path)
    model_prob=model_prob.append(temp)                                                           
 
#megre date and racno to model prob
model_prob=pd.merge(model_prob,racerunner_withw_use_temp[['Date',"Season_","RaceNo",'No_']].copy(),how='left',left_on=['racekey','HorseNo'],right_on=["Season_",'No_'])
 
rww_check_fq=pd.merge(rww_check_fq,model_prob[['Date','RaceNo','HorseNo','winmodel']].copy(),how='left',left_on=['Date','RaceNo','HorseNo'],right_on=['Date','RaceNo','HorseNo'])
 
rww_check_fq=rww_check_fq.loc[~pd.isnull(rww_check_fq['winmodel']),:]
 
rww_check_fq.dtypes
model_prob.dtypes
 

 
base_name='Win_probs_final'
data=rww_check_fq.copy()
threshold1=0.0
threshold2=0.025
from collections import Counter, OrderedDict
 
def cal_per_set(threshold1,threshold2,base_name):
    data_select=data.loc[(data[base_name]>threshold1)&(data[base_name]<=threshold2),:]
    n=data_select.shape[0]
    ave_prob=np.mean(data_select[base_name].values)
    actual_mean=sum(data_select['win'])/data_select.shape[0]
    name=base_name+'_range'
    name_value=str(threshold1)+'-'+str(threshold2)
    output=pd.DataFrame(OrderedDict({name:[name_value],'sample':[n],'ave_prob':[ave_prob],'actual_mean':[actual_mean]}))
    return output
 
def freq_compare(data,base_name):
    output1=pd.DataFrame([])
    output1=output1.append(cal_per_set(0.0,0.01,base_name))
    output1=output1.append(cal_per_set(0.01,0.02,base_name))
    output1=output1.append(cal_per_set(0.02,0.04,base_name))
    output1=output1.append(cal_per_set(0.04,0.06,base_name))
    output1=output1.append(cal_per_set(0.06,0.08,base_name))
    output1=output1.append(cal_per_set(0.08,0.1,base_name))
    output1=output1.append(cal_per_set(0.1,0.25,base_name))
    output1=output1.append(cal_per_set(0.25,0.5,base_name))
    output1=output1.append(cal_per_set(0.5,1.0,base_name))
    return output1
 
final_table=freq_compare(rww_check_fq,'Win_probs_final')
final_table
capture_table=freq_compare(rww_check_fq,'Win_probs_capture')
capture_table
a_25s_table=freq_compare(rww_check_fq,'win25s_prob')
a_25s_table
model_table=freq_compare(rww_check_fq,'winmodel')
model_table
 
model_table=freq_compare(rww_check_fq.loc[rww_check_fq['winmodel']<rww_check_fq['Win_probs_final'],:].copy(),'winmodel')
model_table
 
model_table=freq_compare(rww_check_fq.loc[rww_check_fq['winmodel']>rww_check_fq['Win_probs_final'],:].copy(),'winmodel')
model_table











import itertools
import copy

#qin oddoddoddodd output
import datetime
from datetime import datetime as dt
aa='2018-12-12';bb='1';cc='19:15'
aa='2018-12-09';bb='1';cc='12:25'
aa='2018-12-05';bb='1';cc='18:30'
aa='2018-12-05';bb='4';cc='20:10'
aa='2018-12-16';bb='2';cc='13:00'
aa='2015-02-04';bb='1';cc='19:15'

aa='2015-10-10';bb='10';cc='14:30'

aa='2016-04-16';bb='8';cc='16:40'


aa='2018-09-02';bb='5';cc='14:45'
aa='2018-07-08';bb='1';cc='12:30'
bet_type='qin'
bet_type='qpl'
bet_type='tri'
bet_type='win'
def extract_oddoddoddodd(aa,bb,cc,bet_type):
    oddoddoddsddo_output=pd.DataFrame([])
    race_date=str(aa)
    Race_no=bb
    time_set_full=race_date+":"+str(cc)+':00'
    #time_set_datetime=dt.strptime(time_set_full,'%Y-%m-%d:%H:%M:%S')-datetime.timedelta(minutes=0)
    time_set_datetime=dt.strptime(time_set_full,'%Y-%m-%d:%H:%M:%S')+datetime.timedelta(seconds=25)
    time_set=str(time_set_datetime.hour)+':'+str(time_set_datetime.minute)+':'+str(time_set_datetime.second)
    
#    if aa>="2018-12-09":
#        time_set_full=race_date+":"+str(cc)+':00'
#        time_set_datetime=dt.strptime(time_set_full,'%Y-%m-%d:%H:%M:%S')-datetime.timedelta(minutes=0)
#        time_set=str(time_set_datetime.hour)+':'+str(time_set_datetime.minute)        
#        time_set=dt.strptime(time_set,"%H:%M")
    
    #check if table exist
    table_exist=False
    try:
        try:
            query='select * from oddoddoddsddo'+race_date.replace('-','')+' where oddoddoddsddotype='+'"'+bet_type+'"'+ 'and UpTime<='+'"'+time_set+'"'+' and RaceNo='+Race_no+' '+' and RacingDate='+'"'+race_date+'"'+' and DownloadDate='+'"'+race_date+'"'+' order by UpTime desc limit 1'
            oddoddoddsddo = pd.read_sql(query, con=connection_oddoddoddodd)
                     
            
        except:
            query='select * from `oddoddoddsddo'+race_date.replace('-','')+'.bak`'+' where oddoddoddsddotype='+'"'+bet_type+'"'+ 'and UpTime<='+'"'+time_set+'"'+' and RaceNo='+Race_no+' '+' and RacingDate='+'"'+race_date+'"'+' and DownloadDate='+'"'+race_date+'"'+' order by UpTime desc limit 1'        
            oddoddoddsddo = pd.read_sql(query, con=connection_oddoddoddodd)
            
        table_exist=True
    except:
        pass
    
    if table_exist:
    
        try:
            exact_hour=oddoddoddsddo['UpTime'].dt.components['hours'].values[0]
            exact_min=oddoddoddsddo['UpTime'].dt.components['minutes'].values[0]
            exact_sec=oddoddoddsddo['UpTime'].dt.components['seconds'].values[0]
            
            
            up_time_old=dt(1900,1,1,exact_hour,exact_min,exact_sec).strftime("%H:%M:%S") #convert to string
            up_time=race_date+' '+up_time_old
            
            extraction_time=oddoddoddsddo['modified'][0].strftime("%Y-%m-%d %H:%M:%S")
            
            time_set=time_set+':00'
            
            oddoddoddsddo_data=oddoddoddsddo['Data'].values[0]
        
            
            all_oddoddoddodd=oddoddoddsddo_data.split(":")
            
            if (bet_type=='qin')|(bet_type=='qpl'):
                horse_comb=list(itertools.combinations(range(1,15), 2))
                horse_comb2=[str(i).replace("(",'').replace(")",'').replace(", ",'-') for i in horse_comb]
                horse_comb2_oddoddoddodd=map(lambda (x,y):x+'='+y+'=0', zip(horse_comb2,all_oddoddoddodd))            
                horse_comb2_oddoddoddodd_output=";".join(horse_comb2_oddoddoddodd)
                
            if (bet_type=='win')|(bet_type=='pla'):
                horse_comb=list(itertools.combinations(range(1,15), 1))
                horse_comb2=[str(i).replace("(",'').replace(")",'').replace(",",'') for i in horse_comb]
                horse_comb2_oddoddoddodd=map(lambda (x,y):x+'='+y+'=0', zip(horse_comb2,all_oddoddoddodd))            
                horse_comb2_oddoddoddodd_output=";".join(horse_comb2_oddoddoddodd)
                
            if (bet_type=='tri'):
                horse_comb=list(itertools.combinations(range(1,15), 3))
                horse_comb2=[str(i).replace("(",'').replace(")",'').replace(", ",'-') for i in horse_comb]
                horse_comb2_oddoddoddodd=map(lambda (x,y):x+'='+y+'=0', zip(horse_comb2,all_oddoddoddodd))            
                horse_comb2_oddoddoddodd_output=";".join(horse_comb2_oddoddoddodd)

            if (bet_type=='F-F'):
                horse_comb=list(itertools.combinations(range(1,15), 4))
                horse_comb2=[str(i).replace("(",'').replace(")",'').replace(", ",'-') for i in horse_comb]
                horse_comb2_oddoddoddodd=map(lambda (x,y):x+'='+y+'=0', zip(horse_comb2,all_oddoddoddodd))            
                horse_comb2_oddoddoddodd_output=";".join(horse_comb2_oddoddoddodd)
            
            oddoddoddodd_size=len(horse_comb2_oddoddoddodd)
            
            #checking:
            a1=dt.strptime(extraction_time,"%Y-%m-%d %H:%M:%S")
            a2=dt.strptime(time_set_full,'%Y-%m-%d:%H:%M:%S')
            racetime_uptime_diff=(a1-a2).total_seconds()
            
            temp=pd.DataFrame({'Date':[race_date],'Race_no':[Race_no],'extraction_time':[extraction_time],'up_time':[up_time],'oddoddoddodd_custom':[horse_comb2_oddoddoddodd_output],'oddoddoddodd_original':[oddoddoddsddo_data],'oddoddoddodd_size':[oddoddoddodd_size],'racetime_uptime_diff':[racetime_uptime_diff]})    
        except:
        #20181209, modified change from datetime64(2018-12-05 18:30:03) to object (2018-12-09 09:19:27)
        #uptime change from timedelta64(0 days 18:29:59) to object(09:19:22)\
        #so need to use this exception
            temp=pd.DataFrame({'Date':[race_date],'Race_no':[Race_no],'extraction_time':[None],'up_time':[None],'oddoddoddodd_custom':[None],'oddoddoddodd_original':[None],'oddoddoddodd_size':[None],'racetime_uptime_diff':[None]})
    else:
        temp=pd.DataFrame({'Date':[race_date],'Race_no':[Race_no],'extraction_time':[None],'up_time':[None],'oddoddoddodd_custom':[None],'oddoddoddodd_original':[None],'oddoddoddodd_size':[None],'racetime_uptime_diff':[None]})
    oddoddoddsddo_output=oddoddoddsddo_output.append(temp)
    return oddoddoddsddo_output



main3=racerunner_withw_use[['Date','Season_','RaceNo','Race_Time']].copy()

main3=main3.loc[main3['Date']!='2019-03-23',:].copy()

main3_oddoddoddodd_key=main3[['Date',"RaceNo",'Race_Time']].copy()
main3_oddoddoddodd_key=main3_oddoddoddodd_key.drop_duplicates()

main3_oddoddoddodd_key["RaceNo"]=main3_oddoddoddodd_key['RaceNo'].astype(str)
main3_oddoddoddodd_key["RaceNo"]=main3_oddoddoddodd_key['RaceNo'].apply(lambda x: x.replace('.0',''))

main3_oddoddoddodd_key=main3_oddoddoddodd_key.sort_values(by=['Date','RaceNo'],ascending=[True,True])
#main3_oddoddoddodd_key=main3_oddoddoddodd_key.loc[(main3_oddoddoddodd_key['Date'].astype(str)>="2015-09-06")&(main3_oddoddoddodd_key['Date'].astype(str)<="2019-09-15"),:]
main3_oddoddoddodd_key=main3_oddoddoddodd_key.loc[(main3_oddoddoddodd_key['Date'].astype(str)>="2015-10-04")&(main3_oddoddoddodd_key['Date'].astype(str)<="2019-10-06"),:]
main3_oddoddoddodd_key=main3_oddoddoddodd_key.reset_index(drop=True)



connection_oddoddoddodd = create_engine('mysql+mysqldb://admin:obey@192.168.1.32:3306/oddoddoddsddoDBBackup')

oddoddoddodd_useful=pd.DataFrame([])
i=2293
i=3

bet_type='win'
for i in range(0,main3_oddoddoddodd_key.shape[0]):
    row_use=main3_oddoddoddodd_key[i:i+1]
    temp=extract_oddoddoddodd(row_use['Date'].values[0],row_use['RaceNo'].values[0],row_use['Race_Time'].values[0],bet_type)
    oddoddoddodd_useful=oddoddoddodd_useful.append(temp)
    print(row_use['Date'].values[0])

oddoddoddodd_useful=oddoddoddodd_useful.loc[~pd.isnull(oddoddoddodd_useful['up_time']),:]


if bet_type=='tri':
    oddoddoddodd_useful=oddoddoddodd_useful.loc[~((oddoddoddodd_useful['Date']=='2018-09-02')&(oddoddoddodd_useful['Race_no']=='4')),:]  #no data this date

oddoddoddodd_useful=oddoddoddodd_useful.reset_index(drop=True)


oddoddoddodd_useful['up_time_HMS']=oddoddoddodd_useful['up_time'].apply(lambda x:x[-8:])
oddoddoddodd_useful['extraction_time_HMS']=oddoddoddodd_useful['extraction_time'].apply(lambda x:x[-8:])

oddoddoddodd_useful['Race_no']=oddoddoddodd_useful['Race_no'].astype(int)
oddoddoddodd_useful=oddoddoddodd_useful.sort_values(by=['Date','Race_no'],ascending=[True,True])
oddoddoddodd_useful['Race_no']=oddoddoddodd_useful['Race_no'].astype(str)

oddoddoddodd_useful[bet_type]=bet_type+'@'+oddoddoddodd_useful['Date']+'@'+oddoddoddodd_useful['Race_no']+'@'+oddoddoddodd_useful['extraction_time_HMS']+'@'+oddoddoddodd_useful['up_time_HMS']+'@'+oddoddoddodd_useful['oddoddoddodd_original']+'|'
oddoddoddodd_useful_output=oddoddoddodd_useful[bet_type].copy()

oddoddoddodd_useful_output=''.join(oddoddoddodd_useful_output)

oddoddoddodd_useful_output.to_csv(bet_type+"_oddoddoddodd_20191006.csv",index=False)


oddoddoddodd_useful_specific_check=oddoddoddodd_useful.copy()

oddoddoddodd_useful_specific_check_tri=oddoddoddodd_useful.copy()


len(oddoddoddodd_useful_output)

oddoddoddodd_useful_output=oddoddoddodd_useful_output.tolist()
oddoddoddodd_useful_output_1=''.join(oddoddoddodd_useful_output[0:1000])
oddoddoddodd_useful_output_2=''.join(oddoddoddodd_useful_output[1000:2000])
oddoddoddodd_useful_output_3=''.join(oddoddoddodd_useful_output[2000:])


#convert oddoddoddodd to a single column
data=oddoddoddodd_useful.loc[(oddoddoddodd_useful['Date']=='2019-10-01')&(oddoddoddodd_useful['Race_no']=='7'),:]
bettype='win'
def rearrange_oddoddoddodd(data,bettype):
    output_col_name_oddoddoddodd=bettype+'25s_oddoddoddodd'
    output_col_name_prob=bettype+'25s_prob'
    
    data=data.reset_index(drop=True)
    date=data['Date'].values[0]
    race_no=data['Race_no'].values[0]
    temp=data['oddoddoddodd_custom'].values[0]
    split_all=temp.split(";")
    horse_no=[i.split("=")[0] for i in split_all]
    oddoddoddodd=[i.split("=")[1] for i in split_all]
    
    #oddoddoddodd=['0','']
    oddoddoddodd2=[np.nan if (i=='')|(i=='0')|(i=='0.0') else float(i) for i in oddoddoddodd]
    sumtotal=np.nansum(np.reciprocal(oddoddoddodd2))
    temp_prob=np.reciprocal(oddoddoddodd2)/sumtotal
    
    no_of_hr=len(horse_no)
    output=pd.DataFrame({'Date':[date]*no_of_hr,'RaceNo':[race_no]*no_of_hr,'HorseNo':horse_no,output_col_name_oddoddoddodd:oddoddoddodd2,output_col_name_prob:temp_prob,'oddoddoddodd_source':oddoddoddodd})
    return output

bet_type='win'
out1=oddoddoddodd_useful.groupby(['Date','Race_no']).apply(lambda x:rearrange_oddoddoddodd(x,bet_type))

out1=out1.loc[~pd.isnull(out1[bet_type+'25s_prob']),:]
out1=out1.reset_index(drop=True)

out1.to_csv(bet_type+"_oddoddoddodd_prob_25s_20191006.csv",index=False)
















#use selenium
import paramiko
from paramiko import SSHClient,AutoAddPolicy,client
from scp import SCPClient
from time import sleep
import numpy as np
import shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



browser = webdriver.Chrome(executable_path=r'C:\Users\jonathan.james\.Spyder\chromedriver.exe')
#browser.set_window_position(-10000,0)
browser.get('https://ideone.com/')
wait = WebDriverWait(browser, 120)
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "btn-singin-wnd-open", " " ))]'))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]'))).send_keys('horsewinwin')
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys('randomhorsewin')
#click sign in
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signin-dropdown"]/li[2]/div/form/div[4]/div/button'))).click()



oddoddoddodd_useful_output2=oddoddoddodd_useful_output.copy()
i=0
for i in range(0,10000):
    increment=80 #qin qpl 120                #win pla use 600# qin use 100, qpla use 80
    start=i*increment
    end=(i+1)*increment
    output=oddoddoddodd_useful_output2[start:end]
    output=output.reset_index(drop=True)
    if end > len(oddoddoddodd_useful_output2):
        end=len(oddoddoddodd_useful_output2)
        

    #click new code
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="primary-navigation"]/div/div/div/ul/li[1]/a'))).click()
    
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="file"]'))).clear()
    #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="file"]'))).send_keys(output)
    output_single=output.str.cat(sep='')
    input_box = browser.find_element_by_xpath('//*[@id="file"]')
    browser.execute_script('arguments[0].value=arguments[1]', input_box, output_single)
    
    
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Submit"]'))).click()
    
    print('finished ' +output[(len(output)-1):len(output)].values[0][0:14])
    print(len(output_single))
    if end==len(oddoddoddodd_useful_output2):
        break
    
browser.close()



len(oddoddoddodd_useful_output2.str.cat(sep=''))
1436942


























import itertools
import copy

#qin oddoddoddodd output
import datetime
from datetime import datetime as dt
aa='2018-12-12';bb='1';cc='19:15'
aa='2018-12-09';bb='1';cc='12:25'
aa='2018-12-05';bb='1';cc='18:30'
aa='2018-12-05';bb='4';cc='20:10'
aa='2018-12-16';bb='2';cc='13:00'
aa='2015-02-04';bb='1';cc='19:15'

aa='2016-04-16';bb='8';cc='16:40'


aa='2018-09-02';bb='5';cc='14:45'
aa='2018-07-08';bb='1';cc='12:30'
bet_type='qin'
bet_type='qpl'
bet_type='tri'
bet_type='win'
def extract_pool(aa,bb,cc,bet_type):
    oddoddoddsddo_output=pd.DataFrame([])
    race_date=str(aa)
    Race_no=bb
    time_set_full=race_date+":"+str(cc)+':00'
    #time_set_datetime=dt.strptime(time_set_full,'%Y-%m-%d:%H:%M:%S')-datetime.timedelta(minutes=0)
    time_set_datetime=dt.strptime(time_set_full,'%Y-%m-%d:%H:%M:%S')+datetime.timedelta(seconds=600)
    time_set=str(time_set_datetime.hour)+':'+str(time_set_datetime.minute)+':'+str(time_set_datetime.second)
    
#    if aa>="2018-12-09":
#        time_set_full=race_date+":"+str(cc)+':00'
#        time_set_datetime=dt.strptime(time_set_full,'%Y-%m-%d:%H:%M:%S')-datetime.timedelta(minutes=0)
#        time_set=str(time_set_datetime.hour)+':'+str(time_set_datetime.minute)        
#        time_set=dt.strptime(time_set,"%H:%M")
    
    #check if table exist
    table_exist=False
    try:
        try:
            #query='select * from oddoddoddsddo'+race_date.replace('-','')+' where oddoddoddsddotype='+'"'+bet_type+'"'+ 'and UpTime<='+'"'+time_set+'"'+' and RaceNo='+Race_no+' '+' and RacingDate='+'"'+race_date+'"'+' order by UpTime desc limit 1'
            multiple_or="(oddoddoddsddoType=\'WinPool' or oddoddoddsddoType='PlaPool' or oddoddoddsddoType='QinPool' or oddoddoddsddoType='QplPool' or oddoddoddsddoType='TcePool' or oddoddoddsddoType='TriPool' or oddoddoddsddoType='F-FPool')"
            query='select * from oddoddoddsddo'+race_date.replace('-','')+' where '+multiple_or+' AND '+'UpTime<='+'"'+time_set+'"'+' and RaceNo='+Race_no+' '+' and RacingDate='+'"'+race_date+'"'+' and DownloadDate='+'"'+race_date+'"'+' order by UpTime desc limit 100'  
            oddoddoddsddo = pd.read_sql(query, con=connection_oddoddoddodd)
                     
            
        except:
            multiple_or="(oddoddoddsddoType=\'WinPool' or oddoddoddsddoType='PlaPool' or oddoddoddsddoType='QinPool' or oddoddoddsddoType='QplPool' or oddoddoddsddoType='TcePool' or oddoddoddsddoType='TriPool' or oddoddoddsddoType='F-FPool')"
            query='select * from oddoddoddsddo'+race_date.replace('-','')+'.bak`'+' where '+multiple_or+' AND '+'UpTime<='+'"'+time_set+'"'+' and RaceNo='+Race_no+' '+' and RacingDate='+'"'+race_date+'"'+' and DownloadDate='+'"'+race_date+'"'+' order by UpTime desc limit 100'
            oddoddoddsddo = pd.read_sql(query, con=connection_oddoddoddodd)
            
        table_exist=True
    except:
        pass
    
    if table_exist:
        
        oddoddoddsddo2=oddoddoddsddo.groupby("oddoddoddsddoType").head(1)
        oddoddoddsddo2=oddoddoddsddo2.reset_index(drop=True)
        temp_all=pd.DataFrame([])
        #i=1
        try:
            for i in range(0,oddoddoddsddo2.shape[0]):
                oddoddoddsddo=oddoddoddsddo2[i:i+1].copy()
                exact_hour=oddoddoddsddo['UpTime'].dt.components['hours'].values[0]
                exact_min=oddoddoddsddo['UpTime'].dt.components['minutes'].values[0]
                exact_sec=oddoddoddsddo['UpTime'].dt.components['seconds'].values[0]
                
                
                up_time_old=dt(1900,1,1,exact_hour,exact_min,exact_sec).strftime("%H:%M:%S") #convert to string
                up_time=race_date+' '+up_time_old
                
                extraction_time=oddoddoddsddo['modified'].apply(lambda x:x.strftime("%Y-%m-%d %H:%M:%S")).values[0]
                
                time_set=time_set+':00'
                
                oddoddoddsddo_data=oddoddoddsddo['Data'].values[0]
                #checking:
                a1=dt.strptime(extraction_time,"%Y-%m-%d %H:%M:%S")
                a2=dt.strptime(time_set_full,'%Y-%m-%d:%H:%M:%S')
                racetime_uptime_diff=(a1-a2).total_seconds()
                
                bettype=oddoddoddsddo['oddoddoddsddoType'].values[0]
                pool=oddoddoddsddo['Data'].values[0]
                
                temp=pd.DataFrame({'Date':[race_date],'Race_no':[Race_no],'extraction_time':[extraction_time],'up_time':[up_time],'bettype':[bettype],'pool':[pool],'racetime_uptime_diff':[racetime_uptime_diff]})    
                temp_all=temp_all.append(temp)
        except:
        #20181209, modified change from datetime64(2018-12-05 18:30:03) to object (2018-12-09 09:19:27)
        #uptime change from timedelta64(0 days 18:29:59) to object(09:19:22)\
        #so need to use this exception
            temp_all=pd.DataFrame({'Date':[race_date],'Race_no':[Race_no],'extraction_time':[None],'up_time':[None],'bettype':[None],'pool':[None],'racetime_uptime_diff':[None]})
    else:
        temp_all=pd.DataFrame({'Date':[race_date],'Race_no':[Race_no],'extraction_time':[None],'up_time':[None],'bettype':[None],'pool':[None],'racetime_uptime_diff':[None]})
    oddoddoddsddo_output=oddoddoddsddo_output.append(temp_all)
    return oddoddoddsddo_output



main3=racerunner_withw_use[['Date','Season_','RaceNo','Race_Time']].copy()

main3=main3.loc[main3['Date']!='2019-03-23',:].copy()

main3_oddoddoddodd_key=main3[['Date',"RaceNo",'Race_Time']].copy()
main3_oddoddoddodd_key=main3_oddoddoddodd_key.drop_duplicates()

main3_oddoddoddodd_key["RaceNo"]=main3_oddoddoddodd_key['RaceNo'].astype(str)
main3_oddoddoddodd_key["RaceNo"]=main3_oddoddoddodd_key['RaceNo'].apply(lambda x: x.replace('.0',''))

main3_oddoddoddodd_key=main3_oddoddoddodd_key.sort_values(by=['Date','RaceNo'],ascending=[True,True])
#main3_oddoddoddodd_key=main3_oddoddoddodd_key.loc[(main3_oddoddoddodd_key['Date'].astype(str)>="2015-09-06")&(main3_oddoddoddodd_key['Date'].astype(str)<="2019-09-15"),:]
main3_oddoddoddodd_key=main3_oddoddoddodd_key.loc[(main3_oddoddoddodd_key['Date'].astype(str)>="2015-10-04")&(main3_oddoddoddodd_key['Date'].astype(str)<="2019-10-06"),:]
main3_oddoddoddodd_key=main3_oddoddoddodd_key.reset_index(drop=True)



connection_oddoddoddodd = create_engine('mysql+mysqldb://admin:obey@192.168.1.32:3306/oddoddoddsddoDBBackup')

oddoddoddodd_useful=pd.DataFrame([])
i=2293
i=3
#i=0
for i in range(0,main3_oddoddoddodd_key.shape[0]):
    row_use=main3_oddoddoddodd_key[i:i+1]
    temp=extract_pool(row_use['Date'].values[0],row_use['RaceNo'].values[0],row_use['Race_Time'].values[0],bet_type)
    oddoddoddodd_useful=oddoddoddodd_useful.append(temp)
    print(row_use['Date'].values[0])

oddoddoddodd_useful=oddoddoddodd_useful.loc[~pd.isnull(oddoddoddodd_useful['up_time']),:]


#if bet_type=='tri':
#    oddoddoddodd_useful=oddoddoddodd_useful.loc[~((oddoddoddodd_useful['Date']=='2018-09-02')&(oddoddoddodd_useful['Race_no']=='4')),:]  #no data this date

oddoddoddodd_useful=oddoddoddodd_useful.reset_index(drop=True)


oddoddoddodd_useful['up_time_HMS']=oddoddoddodd_useful['up_time'].apply(lambda x:x[-8:])
oddoddoddodd_useful['extraction_time_HMS']=oddoddoddodd_useful['extraction_time'].apply(lambda x:x[-8:])

oddoddoddodd_useful['Race_no']=oddoddoddodd_useful['Race_no'].astype(int)
oddoddoddodd_useful=oddoddoddodd_useful.sort_values(by=['Date','Race_no'],ascending=[True,True])
oddoddoddodd_useful['Race_no']=oddoddoddodd_useful['Race_no'].astype(str)

oddoddoddodd_useful['pool_out']=oddoddoddodd_useful['Date']+'@'+oddoddoddodd_useful['Race_no']+'@'+oddoddoddodd_useful['bettype']+'@'+oddoddoddodd_useful['extraction_time_HMS']+'@'+oddoddoddodd_useful['up_time_HMS']+'@'+oddoddoddodd_useful['pool']+'|'
oddoddoddodd_useful_output=oddoddoddodd_useful['pool_out'].copy()


#oddoddoddodd_useful_output.to_csv("pool.csv",index=False)



oddoddoddodd_useful_output_cat=''.join(oddoddoddodd_useful_output)

len(oddoddoddodd_useful_output_cat)






list(oddoddoddodd_useful.columns.values)
oddoddoddodd_useful['extraction_time_2']=oddoddoddodd_useful['extraction_time'].str[0:10]
oddoddoddodd_useful['check']=oddoddoddodd_useful['extraction_time_2']==oddoddoddodd_useful['Date']





















# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:39:54 2019

@author: jonathan.james
"""

from subprocess import Popen, PIPE
import glob
import os
import numpy as np
from pandas import HDFStore,DataFrame
import pandas as pd


script_file=os.path.join(r"C:\Users\jonathan.james\Desktop\yulong","multiple_subprocess_output_text.py")

run_no="1900"
input_value = np.arange(1,11).tolist()

cmds_list = [['python',script_file,str(i),run_no] for i in input_value]
procs_list = [Popen(cmd, stdout=PIPE, stderr=PIPE) for cmd in cmds_list]
for proc in procs_list:
    proc.wait()
    

#output = procs_list[0].communicate()  
#output[0]

#read output
input_path=os.path.join(r'C:\Users\jonathan.james\Desktop\yulong\output_example\temp',run_no)



i=1
train_predict=pd.DataFrame([])
test_predict=pd.DataFrame([])
for i in input_value:
    
    input_hdf5_train_path=os.path.join(input_path,"train"+str(i)+".hdf5")
    input_hdf5_test_path=os.path.join(input_path,"test"+str(i)+".hdf5")
    
    store=pd.HDFStore(input_hdf5_train_path)
    name_temp='train'+str(i)+'_dataframe'
    train_temp=store.select(name_temp)
    store.close()
    train_predict=pd.concat([train_predict,train_temp],axis=1)

    store=pd.HDFStore(input_hdf5_test_path)
    name_temp='test'+str(i)+'_dataframe'
    test_temp=store.select(name_temp)
    store.close()
    test_predict=pd.concat([test_predict,test_temp],axis=1)

















# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:17:22 2019

@author: jonathan.james
"""
import sys
import os
import numpy as np
import pandas as pd
from time import sleep
from random import randrange



in1=sys.argv[1]
runno=sys.argv[2]

#in1='1'
#runno='1900'

output_path=r'C:\Users\jonathan.james\Desktop\yulong\output_example\temp'
output_path=os.path.join(output_path,runno)

import os
if not os.path.exists(output_path):
    os.makedirs(output_path)


out=os.path.join(r'C:\Users\jonathan.james\Desktop\yulong\output_example',"Output"+in1+".txt")
text_file = open(out, "w")
text_file.write("output ok")
text_file.close()

no=300*20000

out1=np.reshape(np.arange(0,no),(300,20000))
out1=pd.DataFrame(out1)
out2=np.reshape(np.arange(0,no),(300,20000))
out2=pd.DataFrame(out2)

sleep(randrange(5))

from pandas import HDFStore,DataFrame

store=pd.HDFStore(os.path.join(output_path,"train"+in1+".hdf5"),"w",complib=str("zlib"),complevel=5)
store.put("train"+in1+'_dataframe',out1,data_columns=out1.columns)
store.close()

store=pd.HDFStore(os.path.join(output_path,"test"+in1+".hdf5"),"w",complib=str("zlib"),complevel=5)
store.put("test"+in1+'_dataframe',out2,data_columns=out2.columns)
store.close()





#print(out2)
#print(in1)
#print(in2)
#print('here is output ',in1)
#print('here is output2 ',out2)











import MySQLdb as mdb
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
 
 
df1 = pd.DataFrame({'name': ['sam', 'lam', 'simon'], 'b': [4, 5, 6],'c':[5,6,7]})
df2 = pd.DataFrame({'name': ['sam', 'lam', 'john'], 'b': [4, 5, 6],'d':[5,6,7]})
 
 
connection = create_engine("mysql+mysqldb://samsung_notebook2:wjkd2383@192.168.3.37:3306/horseracing")
 
df1.to_sql('df1', connection, if_exists='replace', chunksize=1000,index=False)
df2.to_sql('df2', connection, if_exists='replace', chunksize=1000,index=False)
 
 
 
 
 
 
SELECT * FROM df1 INNER JOIN df2 ON df1.name=df2.name;
select df1.b,df1.name,df2.d from df1 inner join df2 on df1.name=df2.name;
SELECT * FROM df1 left JOIN df2 ON df1.name=df2.name;
SELECT * FROM df1 right JOIN df2 ON df1.name=df2.name;
#UNION will remove duplicate rows, to keep all rows, use UNION ALL
SELECT * FROM df1 LEFT JOIN df2 ON df1.name=df2.name union SELECT * FROM df1 RIGHT JOIN df2 ON df1.name=df2.name;
 
SELECT * FROM `df2` ORDER BY d DESC LIMIT 2;   #only show first 2 rows
select * from `df2` order by d desc limit 1, 1; # skip first row and show next one row
 
 
select * from df2 where d<(select max(d) from df2) order by d desc limit 1; #select second max
 
 
 
#create table and insert value
CREATE TABLE shop (
    article INT UNSIGNED  DEFAULT '0000' NOT NULL,
    dealer  CHAR(20)      DEFAULT ''     NOT NULL,
    price   DECIMAL(16,2) DEFAULT '0.00' NOT NULL,
    PRIMARY KEY(article, dealer));
INSERT INTO shop VALUES
    (1,'A',3.45),(1,'B',3.99),(2,'A',10.99),(3,'B',1.45),
    (3,'C',1.69),(3,'D',1.25),(4,'D',19.95);
 
#Maximum of Column per Group
SELECT article, MAX(price) AS price FROM   shop GROUP BY article;
 
#https://w...content-available-to-author-only...y.com/library/view/mysql-reference-manual/0596002653/ch03s05.html
#“For each article, find the dealer(s) with the most expensive price.”
SELECT article, dealer, price
FROM   shop s1
WHERE  price=(SELECT MAX(s2.price)
              FROM shop s2
              WHERE s1.article = s2.article);
 
 
#or use this in one line
SELECT article, SUBSTRING( MAX( CONCAT(LPAD(price,6,'0'),dealer) ), 7) AS dealer,
  0.00+LEFT(MAX(CONCAT(LPAD(price,6,'0'),dealer)), 6) AS price FROM shop GROUP BY article;        
 
 
SELECT LPAD("SQL Tutorial", 20, "ABC");              
SELECT SUBSTRING("SQL Tutorial", 5, 3) AS ExtractString;     
SELECT CONCAT(LPAD(price,6,'0'),dealer) AS dealer FROM shop;
SELECT max(CONCAT(LPAD(price,6,'0'),dealer)) AS dealer FROM shop group by article; 
SELECT substring(MAX(CONCAT(LPAD(price,6,'0'),dealer)),7) AS dealer FROM shop GROUP BY article;      
 
SELECT LEFT(MAX(CONCAT(LPAD(price,6,'0'),dealer)), 6) AS price FROM shop GROUP BY article;   
SELECT 0.00+LEFT(MAX(CONCAT(LPAD(price,6,'0'),dealer)), 6) AS price FROM shop GROUP BY article;#0.00 is digit format          
 
#https://w...content-available-to-author-only...h.com/sql/foreign-key-constraint.html
 
#The PRIMARY KEY constraint uniquely identifies each record in a table. cannot contain NULL values
ALTER TABLE df1 ADD PRIMARY KEY (b);
 
ALTER TABLE df1 DROP PRIMARY KEY;
 
#A FOREIGN KEY is a key used to link two tables together.
# foreign key b in df2 no need distinct, just name key b as f_b
#foreign jey can make sure b in df2 must exist in b in df1, otherwise error occurs
ALTER TABLE df2 ADD constraint f_b FOREIGN KEY  (b) REFERENCES df1(b);
 
#Cannot add or update a child row: a foreign key constraint fails 
INSERT INTO df2 VALUES (9,4,'wong');
 
#cannot remove because therre is reference key linked
delete from df1 where b=6;
#ok to delete
DELETE FROM df2 WHERE b=6;
 
ALTER TABLE df2 DROP FOREIGN KEY f_b;
 
 
select count(*) from df1;
 
 
show processlist;












################################################################################
################################################################################
################################################################################
################################################################################
############################UBS Interview question##############################
################################################################################
################################################################################
################################################################################
################################################################################






#https://www.statsmodels.org/stable/examples/notebooks/generated/glm_weights.html
import os
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
#os.chdir(r"C:\Users\jonathan.james\Desktop\adhot\ub\ub_data")
os.chdir("/home/jonathanjames/aws/notebooks/docs/ubs_data/UBS_TES_Interview")


train=pd.read_csv("trainingdata.csv")
test=pd.read_csv("testdata.csv")
 
#python glm variables' name cannot start with digit and include '-'
train=train.rename(columns={'28-59DaysPastDue':'V28_59DaysPastDue','60-90DaysPastDue':'V60_90DaysPastDue','91DaysLate':'V91DaysLate'})
test=test.rename(columns={'28-59DaysPastDue':'V28_59DaysPastDue','60-90DaysPastDue':'V60_90DaysPastDue','91DaysLate':'V91DaysLate'})
 
#explore data validity
a=train.describe()
 
#max age is 109. max number of dependents is 20. but they are possible. had better double check
#some values in 28-59DaysPastDue, 60-90DaysPastDue and 91DaysLate are greater than 96 simultaniously, which doesn't make sense
#replace them by NA and later after standardization, they will be filled with zero, which is mean.
train.loc[train['V28_59DaysPastDue']>=96,'V28_59DaysPastDue']=np.nan
train.loc[train['V60_90DaysPastDue']>=96,'V60_90DaysPastDue']=np.nan
train.loc[train['V91DaysLate']>=96,'V91DaysLate']=np.nan
 
test.loc[test['V28_59DaysPastDue']>=96,'V28_59DaysPastDue']=np.nan
test.loc[test['V60_90DaysPastDue']>=96,'V60_90DaysPastDue']=np.nan
test.loc[test['V91DaysLate']>=96,'V91DaysLate']=np.nan
 
train['debt_age']=train['DebtRatio']*train['MonthlyIncome']*train['age']
test['debt_age']=test['DebtRatio']*test['MonthlyIncome']*train['age']
 
train['opencredit_income']=train['MonthlyIncome']*train['NumberOfOpenCreditLinesAndLoans']
test['opencredit_income']=test['MonthlyIncome']*train['NumberOfOpenCreditLinesAndLoans']
 
train['realestate_income']=train['MonthlyIncome']*train['NumberRealEstateLoansOrLines']
test['realestate_income']=test['MonthlyIncome']*train['NumberRealEstateLoansOrLines']
 
train.loc[train['UtilisationRatio']>1,'UtilisationRatio']=1
test.loc[test['UtilisationRatio']>1,'UtilisationRatio']=1
 
train.loc[train['DebtRatio']>1,'DebtRatio_greater_1']=train['DebtRatio']
train['DebtRatio_greater_1']=train['DebtRatio_greater_1'].fillna(0)
train.loc[train['DebtRatio']<=1,'DebtRatio_less_1']=train['DebtRatio']
train['DebtRatio_less_1']=train['DebtRatio_less_1'].fillna(0)
 
test.loc[test['DebtRatio']>1,'DebtRatio_greater_1']=test['DebtRatio']
test['DebtRatio_greater_1']=test['DebtRatio_greater_1'].fillna(0)
test.loc[test['DebtRatio']<=1,'DebtRatio_less_1']=test['DebtRatio']
test['DebtRatio_less_1']=test['DebtRatio_less_1'].fillna(0)
 
train['V28morePastDue']=train['V28_59DaysPastDue']+train['V91DaysLate']+train['V60_90DaysPastDue']
test['V28morePastDue']=test['V28_59DaysPastDue']+test['V91DaysLate']+test['V60_90DaysPastDue']
 
 
#explore data validity
a=train.describe()        
 
 
 
 
 
#training set
train_xy=train.iloc[:100000,1:].copy()
#validation set
valid_xy=train.iloc[100000:,1:].copy()
#test set
test_xy=test.iloc[:,1:].copy()
 
 
a=list(train.columns.values)
 
 
 
variable_use=['UtilisationRatio',
 'age',
 'V28_59DaysPastDue',
 'DebtRatio',
 'MonthlyIncome',
 'NumberOfOpenCreditLinesAndLoans',
 'V91DaysLate',
 'NumberRealEstateLoansOrLines',
 'V60_90DaysPastDue',
 'NumberOfDependents']
 
 
response_use='delinquency'
variable_use=['UtilisationRatio','age','debt_age','V28morePastDue','opencredit_income','realestate_income',
              'NumberOfOpenCreditLinesAndLoans','NumberRealEstateLoansOrLines','NumberOfDependents',
              'DebtRatio_greater_1','DebtRatio_less_1']
 
 
 
train_xy=train_xy[[response_use]+variable_use].copy()
valid_xy=valid_xy[[response_use]+variable_use].copy()
test_xy=test_xy[[response_use]+variable_use].copy()
 
 
#take log
list(train_xy.columns.values)
for col in variable_use:
    train_xy[col]=train_xy[col].apply(lambda x:np.log(x) if x!=0 else 0)
    valid_xy[col]=valid_xy[col].apply(lambda x:np.log(x) if x!=0 else 0)
    test_xy[col]=test_xy[col].apply(lambda x:np.log(x) if x!=0 else 0)
 
#find train mean and sd
train_col_mean=train_xy.iloc[:,1:].mean()
train_col_std=train_xy.iloc[:,1:].std()
 
#find train+valid mean and sd
train_valid=train_xy.append(valid_xy)
train_valid_mean=train_valid.iloc[:,1:].mean()
train_valid_std=train_valid.iloc[:,1:].std()
 
 
#apply train's mean and sd to validation
train_xy.iloc[:,1:]=(train_xy.iloc[:,1:]-train_col_mean)/train_col_std
valid_xy.iloc[:,1:]=(valid_xy.iloc[:,1:]-train_col_mean)/train_col_std
 
#apply train and valid's mean and sd to test
test_xy.iloc[:,1:]=(test_xy.iloc[:,1:]-train_valid_mean)/train_valid_std
 
 
 
#fill na by zero
train_xy=train_xy.fillna(0)
valid_xy=valid_xy.fillna(0)
test_xy=test_xy.fillna(0)
 
train_xy=train_xy.reset_index(drop=True)
valid_xy=valid_xy.reset_index(drop=True)
test_xy=test_xy.reset_index(drop=True)
 




import numpy as np
import pandas as pd

arr=[1,1,1,5,3,3]

arr.

import collections
arr = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
# getting the elements frequencies using Counter class

for i in arr:
    a=arr[]






 
 
 
 
#create model
model_formula=response_use+' ~ '+'+'.join(variable_use)
glm = smf.glm(model_formula,data=train_xy, family=sm.families.Binomial())
result = glm.fit()
print(result.summary())  #38685
 
y_pred = result.predict(train_xy)
y_pred_valid = result.predict(valid_xy)
y_pred_test = result.predict(test_xy)
 
y_pred_df=pd.DataFrame(result.predict(train_xy))
y_pred_valid_df=pd.DataFrame(result.predict(valid_xy))
y_pred_test_df=pd.DataFrame(result.predict(test_xy))
 
 
 
 
 
 
#m estimator
train_xy['const']=1
cols=train_xy.columns.tolist()
cols.insert(0, cols.pop(cols.index('const')))
train_xy=train_xy.ix[:,cols]
train_y=train_xy.delinquency
 
 
valid_xy['const']=1
cols=valid_xy.columns.tolist()
cols.insert(0, cols.pop(cols.index('const')))
valid_xy=valid_xy.ix[:,cols]
valid_y=valid_xy.delinquency
 
 
test_xy['const']=1
cols=test_xy.columns.tolist()
cols.insert(0, cols.pop(cols.index('const')))
test_xy=test_xy.ix[:,cols]
test_y=test_xy.delinquency
 
 
 
rlm_model = sm.RLM(train_y,train_xy.loc[:, train_xy.columns != response_use], M=sm.robust.norms.HuberT())
result = rlm_model.fit()
print(result.summary())
 
 
y_pred_df=pd.DataFrame(result.predict(train_xy.loc[:, train_xy.columns != response_use]))
y_pred_valid_df=pd.DataFrame(result.predict(valid_xy.loc[:, valid_xy.columns != response_use]))
y_pred_test_df=pd.DataFrame(result.predict(test_xy.loc[:, test_xy.columns != response_use]))
 
 
 
 
 
 
 
 
 
 
 
 
#plot
import matplotlib.pyplot as plt
plt.hist(y_pred_df.iloc[:,0].values, bins=60)
plt.show()
 
plt.hist(y_pred_valid_df.iloc[:,0].values, bins=60)
plt.show()
 
plt.hist(y_pred_test_df.iloc[:,0].values, bins=60)
plt.show()
 
 
#find AUC
y_pred_df=y_pred_df.rename(columns={0:'prediction'})
y_pred_df['actual']=train_xy['delinquency'].copy()
 
y_pred_valid_df=y_pred_valid_df.rename(columns={0:'prediction'})
y_pred_valid_df['actual']=valid_xy['delinquency'].copy()
 
 
import numpy as np
from sklearn.metrics import roc_auc_score
 
 
roc_auc_score(y_pred_df.actual, y_pred_df.prediction)
roc_auc_score(y_pred_valid_df.actual,y_pred_valid_df.prediction)
 
 
#plot ROC for train
import sklearn.metrics as metrics
# calculate the fpr and tpr for all thresholds of the classification
fpr, tpr, threshold = metrics.roc_curve(y_pred_df.actual, y_pred_df.prediction)
roc_auc = metrics.auc(fpr, tpr)
roc_auc
 
roc_train_df=pd.DataFrame({'tpr':tpr,'fpr':fpr,'threshold':threshold})
roc_train_df['tpr_over_fpr']=roc_train_df['tpr']/roc_train_df['fpr']
roc_train_df=roc_train_df.fillna(0)
roc_train_df=roc_train_df.sort_values(by=['tpr_over_fpr'],ascending=[False])
estimated_threshold=roc_train_df['threshold'].values[0:10].mean()
 
 
# method I: plt
import matplotlib.pyplot as plt
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
 
 
 
 
#confusion matrix for train
from sklearn.metrics import confusion_matrix
 
actual=y_pred_df.actual
predition=y_pred_df.prediction
predition=(predition>0.874976603319)*1
#predition=(predition>estimated_threshold)*1          
cf=confusion_matrix(predition,actual, labels=[1,0]) #row is prediction, column is actual
cf
cf=pd.DataFrame(cf)
cf=cf.rename(columns={0:'actual_1',1:'actual_0'})
cf=cf.rename(index={0:'predicted_1',1:'predicted_0'})
cf
 
 
fpr	threshold	tpr	tpr_over_fpr
0.000107142091842	0.874976603319	0.004800480048	44.80480048
 
true_positive=32/(32+6634)
false_positive=10/(10+93324)
 
 
 
 
 
 
 
 
 
 
#confusion matrix for validation
from sklearn.metrics import confusion_matrix
 
actual=y_pred_valid_df.actual
predition=y_pred_valid_df.prediction
predition=(predition>0.874976603319)*1
cf=confusion_matrix(predition,actual, labels=[1,0]) #row is prediction, column is actual
cf
cf=pd.DataFrame(cf)
cf=cf.rename(columns={0:'actual_1',1:'actual_0'})
cf=cf.rename(index={0:'predicted_1',1:'predicted_0'})
cf                
 
 
 
 
 
 
 
 
#plot ROC for valid
# calculate the fpr and tpr for all thresholds of the classification
fpr, tpr, threshold = metrics.roc_curve(y_pred_valid_df.actual,y_pred_valid_df.prediction)
roc_auc = metrics.auc(fpr, tpr)
roc_auc
 
roc_valid_df=pd.DataFrame({'tpr':tpr,'fpr':fpr,'threshold':threshold})
roc_valid_df['tpr_over_fpr']=roc_valid_df['tpr']/roc_valid_df['fpr']
roc_valid_df=roc_valid_df.fillna(0)
roc_valid_df.loc[roc_valid_df['tpr_over_fpr']==max(roc_valid_df['tpr_over_fpr']),'threshold']  #best threshold
 
# method I: plt
import matplotlib.pyplot as plt
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
 
 
 
 
 
 
 
 
 
 
result.params
result.null_deviance  #2*loglikelihood
result.deviance
 
 
 
#this custom deviance calculation ties with the calculation in both python/R
def deviances(y_true,y_predicted):
    key_one=y_true!=0
    key_zero=y_true==0
    y_true_one=y_true[key_one]
    y_predicted_one=y_predicted[key_one]
    y_true_zero=y_true[key_zero]
    y_predicted_zero=y_predicted[key_zero]
    dev=2*(sum(np.log(y_true_one/y_predicted_one))+sum(np.log((1-y_true_zero)/(1-y_predicted_zero))))
    return dev
 
#deviances in training
y_true=train_xy[response_use].values
y_predicted=result.predict(train_xy)#.values
deviances(y_true,y_predicted)  #40402 40386.53408214874, 39127, 38856, 38842,38685
 
#deviances in validation
y_true_valid=valid_xy[response_use].values
y_predicted_valid=result.predict(valid_xy)#.values
deviances(y_true_valid,y_predicted_valid)   #20099 20090.73519208953, 19502,19361,19352.19311
 








#rearrange columns
cols = outsub.columns.tolist()
cols.insert(1, cols.pop(cols.index('bet_type')))
cols.insert(2, cols.pop(cols.index('year')))
outsub = outsub.reindex(columns= cols)















#%reset -f
import os
import numpy as np
import matplotlib.pyplot as plt
#os.chdir(r'C:\Users\jonathanjames\Desktop\python\WinPython-64bit-3.6.2.0Qt5\notebooks\index_analysis')
target_dir=r'C:\Users\jonathanjames\aws\notebooks\docs\niantic'

os.chdir(target_dir)



from pandas import read_excel
import pandas as pd

from sqlalchemy import create_engine
import configparser
import re

import numpy as np
import pymysql
import pandas.io.sql as sql


from sqlalchemy import create_engine
import configparser
import re
#import MySQLdb as mdb
import pandas as pd
import numpy as np
import pymysql
import pandas.io.sql as sql

#connection=create_engine("mysql+pymysql://root:wjkd2383#@localhost:3306/horseracing")

pokemon_data=pd.read_csv('pokemon_data_science.csv')



#GBM
import sys
sys.path.append(r'C:\Users\jonathanjames\aws\notebooks\gbm\GBM\dist\h2o-3.24.0.3')
sys.path.append(r'C:\Users\jonathanjames\aws\notebooks\gbm\tabulate\dist\tabulate-0.8.3')
sys.path.append(r'C:\Users\jonathanjames\aws\notebooks\gbm\future\dist\future-0.17.1\src')
#sys.path.append(r'C:\Users\jonathanjames\Desktop\python\six\dist\six-1.12.0')

import h2o
import numpy as np
import math
from h2o.estimators.gbm import H2OGradientBoostingEstimator
from h2o.grid.grid_search import H2OGridSearch

h2o.init(nthreads=-1, strict_version_check=True)

#response
response = "isLegendary"


import pandas as pd
df=pd.read_csv('pokemon_data_science.csv')


df.columns.values

#choose features
predictors=['HP', 'Attack','Defense', 'Sp_Atk', 'Sp_Def', 'Speed','Total']
all_use_columns=[response]+predictors

df=df[all_use_columns].copy()
df[response]=df[response]*1

#
#for col in predictors:
#    df[col]=df[col].apply(lambda x:np.log(x) if x!=0 else 0)


#assign first 2/3 of data as training and last 1/3 as validation
split1=round(df.shape[0]*(2/3))

df_train=df[0:split1].copy()
df_valid=df[split1:].copy()


#find training mean and sd
train_mean=df_train.iloc[:,1:].mean()
train_std=df_train.iloc[:,1:].std()
 


#standardize
df_train.iloc[:,1:]=(df_train.iloc[:,1:]-train_mean)/train_std
df_valid.iloc[:,1:]=(df_valid.iloc[:,1:]-train_mean)/train_std


#create H2O dataframe
train= h2o.H2OFrame(df_train)
train[response] = train[response].asfactor()  

valid= h2o.H2OFrame(df_valid)
valid[response] = valid[response].asfactor()  


#modelling with cross validation
cv_gbm = H2OGradientBoostingEstimator(ntrees=15,nfolds = 4,max_depth=4, seed = 0xDECAF)
cv_gbm.train(x = predictors, y = response, training_frame = train)


#get fitted value in training
fitted_training = cv_gbm.predict(train).as_data_frame()

#get fitted value in validation
fitted_validation = cv_gbm.predict(valid).as_data_frame()


#create training confusion matrix, AUC and accuracy
perf = cv_gbm.model_performance(train)
perf.confusion_matrix()
perf.auc()


#plot training scoring history of AUC and loss
sh = cv_gbm.score_history()
sh = pd.DataFrame(sh)
sh.plot(x='number_of_trees',y = ['training_logloss'])
sh.plot(x='number_of_trees',y = ['training_auc'])


#create validation confusion matrix and AUC
perf = cv_gbm.model_performance(valid)
perf.confusion_matrix()
perf.auc()










#millinum test
text=["# Algorithms",
"This chapter covers the most basic algorithms.",
"## Sorting",
"Quicksort is fast and widely used in practice",
"Merge sort is a deterministic algorithm",
"## Searching",
"DFS and BFS are widely used graph searching algorithms",
"Some variants of DFS are also used in game theory applications",
"# Data Structures",
"This chapter is all about data structures"]





outer_count=0
inner_count=0
output=[]
for i in text:
    if i[0:2]=='# ':
        outer_count=outer_count+1
        temp=str(outer_count)+'. '+i[2:]
        inner_count=0
        output.append(temp)
    if i[0:3]=='## ':
        inner_count=inner_count+1
        temp=str(outer_count)+'.'+str(inner_count)+'.'+i[3:]
        output.append(temp)







s=


s = 'lrbb'
t = 'lrbb'

s_len=len(s)
t_len=len(t)
output=-1
if (s_len % t_len)==0:
    repeat=s_len // t_len
    if t*repeat==s:
        #k=0
        for k in range(0,t_len):
            temp=t[0:k+1]
            if (t_len % len(temp))==0:
                repeat2=t_len // len(temp)
                if temp*repeat2==t:
                    output=len(temp)
                    break
    else:
        output=-1
else:
    output=-1
                
            















https://towardsdatascience.com/calculating-string-similarity-in-python-276e18a7d33a



import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
stopwords=stopwords.words('english')






#macro value




#use wsj data
import os
import numpy as np

import requests
import zipfile
import io
import pandas as pd
target_dir='/home/jonathanjames/aws/notebooks/index_analysis'


os.chdir(target_dir)


spx=pd.read_excel("index_SPX_wsj_with_tidy.xlsx","Sheet1")
djia=pd.read_excel("index_DJIA_wsj_with_tidy.xlsx","Sheet1")


djia.dtypes

spx=pd.merge(spx,djia[['Date2','Open_index_DJIA_wsj','Close_index_DJIA_wsj']].copy(),how='left',on=['Date2'])

spx['Close_index_SPX_wsj_lag1']=spx['Close_index_SPX_wsj'].shift(1)
spx['Close_index_DJIA_wsj_lag1']=spx['Close_index_DJIA_wsj'].shift(1)
spx['spx_change']=spx['Close_index_SPX_wsj']/spx['Close_index_SPX_wsj_lag1']-1
spx['djia_change']=spx['Close_index_DJIA_wsj']/spx['Close_index_DJIA_wsj_lag1']-1

spx=spx.loc[spx['Date2']>='1997-01-01',:].copy()


spx=spx.loc[(spx['Date2']>='2019-10-01')&(spx['Date2']<='2022-12-31'),:].copy()



capital=1

spx['spx_60_max']=spx['Close_index_SPX_wsj'].rolling(60).max()
spx['spx_60_dd']=spx['Close_index_SPX_wsj']/spx['spx_60_max']-1
spx['spx_60_dd_shift']=spx['spx_60_dd'].shift(1)


spx=spx.reset_index(drop=True)


#determine when hedge
spx['spx_max']=spx['Close_index_SPX_wsj'].rolling(28).max()

spx['spx_min']=spx['Close_index_SPX_wsj'].rolling(28).min()

spx['spx_close_normalized']=(spx['Close_index_SPX_wsj']-spx['spx_min'])/(spx['spx_max']-spx['spx_min'])
spx['spx_slow']=spx['spx_close_normalized'].rolling(6).mean()


spx['hedge_B']=((spx['spx_close_normalized']>0.2)&(spx['spx_close_normalized']>spx['spx_slow']))*1
spx['hedge_S']=((spx['spx_close_normalized']<0.8)&(spx['spx_close_normalized']<spx['spx_slow']))*1
spx['hedge_B_shift']=spx['hedge_B'].shift(1)



spx_use=spx[['Date2','spx_change','djia_change','spx_60_dd_shift','hedge_B_shift']].copy()

spx_use=spx_use.loc[(~pd.isnull(spx_use['spx_change']))&(~pd.isnull(spx_use['djia_change'])),:].copy()



spx_use=spx_use[60:].copy()
spx_use=spx_use.reset_index(drop=True)






capital=1
spx_use['account_value']=0
spx_use['hedge_size']=0
spx_use['spx_change_1']=(1+spx_use['spx_change'])
spx_use['spx_cum_product']=spx_use['spx_change_1'].cumprod()
spx_use['djia_change_1']=(1+spx_use['djia_change'])
spx_use['djia_cum_product']=spx_use['djia_change_1'].cumprod()


i=0
for i in range(0,spx_use.shape[0]):
    if i==0:
        if spx_use.loc[i,'hedge_B_shift']==0:
            spx_use.loc[i,'hedge_pnl']=0
            spx_use.loc[i,'account_value']=capital*(1+spx_use.loc[i,'spx_change'])
        else:
            spx_use.loc[i,'hedge_pnl']=capital*(1+0.5*spx_use.loc[i,'spx_60_dd_shift'])*spx_use.loc[i,'djia_change']*-1
            spx_use.loc[i,'account_value']=capital*(1+spx_use.loc[i,'spx_change'])+spx_use.loc[i,'hedge_pnl']        

    if i>0:
        if spx_use.loc[i,'hedge_B_shift']==0:
            spx_use.loc[i,'hedge_pnl']=0
            spx_use.loc[i,'account_value']=spx_use.loc[i-1,'account_value']*(1+spx_use.loc[i,'spx_change'])
        else:
            spx_use.loc[i,'hedge_pnl']=spx_use.loc[i-1,'account_value']*(1+0.5*spx_use.loc[i,'spx_60_dd_shift'])*spx_use.loc[i,'djia_change']*-1
            spx_use.loc[i,'account_value']=spx_use.loc[i-1,'account_value']*(1+spx_use.loc[i,'spx_change'])+spx_use.loc[i,'hedge_pnl']              
            
        
    
#https://stackoverflow.com/questions/69861880/plotly-colorize-line-segments
#./python -m pip install plotly
#./python -m pip install kaleido


import numpy as np
from plotly import graph_objects as go
import plotly
from html2image import Html2Image
import os

x = np.linspace(-1, 1, 101)
y = x**2
# Slope in-between of the knots
dy = (x[1:] + x[:-1])
line_cols = np.where(dy > 0,"#F2F013","black")

fig = go.Figure()
for i, col in enumerate(line_cols):
    fig.add_scatter(x=x[i:(i+2)], y=y[i:(i+2)],line=dict(color=col),
                    mode='lines',showlegend=False)

#plot(fig)

fig.write_image("plotly_temp.jpeg")








from plotly.offline import download_plotlyjs, init_notebook_mode,  plot
import numpy as np
from plotly import graph_objects as go
import plotly
from html2image import Html2Image
import os

x =spx_use['Date2'].values
y1 = spx_use['spx_cum_product'].values
y2 = spx_use['djia_cum_product'].values
y3 = spx_use['account_value'].values



layout = go.Layout(autosize=False,width=1300,height=700,
                   title='<span style="font-size: 30px;">abc plot</span>',
                   xaxis_title='<b>Date</b>',#"Date",
                   yaxis_title='<b>Cumulative P&L</b>',#"Cumulative P&L",
                   legend_title='<span style="font-size: 15px;">Legend Description</span>'
                   )
                     
fig = go.Figure(layout=layout)
#obj1 = go.Scatter(x = x,y = y2,mode = 'lines')
#fig.add_trace(obj1)
obj2 = go.Scatter(x = x,y = y3,mode = 'lines',marker=dict(color='#CDAA7D'))
fig.add_trace(obj2)

fig['data'][0]['name'] = 'Account Value'   #change legend first color description name


#defind 2 colors for hedge
line_cols = np.where(spx_use['hedge_B_shift'].values==1,"red","black")
color_legend_name={'red':'SPX','black':'SPX with Hedge'}


distinct_element_first_occurance_index=[]
for k in list(set(line_cols)):
    distinct_element_first_occurance_index.append(np.where(line_cols==k)[0][0])


i=0

#iterate every single points in line_cols, each will show a legend line in right, but only show it when it is in the index of
#distinct color
for i, col in enumerate(line_cols):
    if i in distinct_element_first_occurance_index:
        fig.add_scatter(x=x[i:(i+2)], y=y1[i:(i+2)],line=dict(color=col),
                        mode='lines',showlegend=True)
        fig['data'][i+1]['name'] = color_legend_name[col]  #need to use i+1 because fig['data'][0]['name'] already used above
    else:
        fig.add_scatter(x=x[i:(i+2)], y=y1[i:(i+2)],line=dict(color=col),
                        mode='lines',showlegend=False)        

plot(fig)


fig.write_image("plotly_temp.jpeg")

























#use yahoo finance data
import os
import numpy as np

import requests
import zipfile
import io
import pandas as pd
import yfinance as yf
target_dir='/home/jonathanjames/aws/notebooks/index_analysis'


os.chdir(target_dir)



spx_raw = yf.download('^GSPC',start='1987-09-11',end='2022-06-30',progress=False)
spx_raw=spx_raw.reset_index(drop=False)
spx_raw=spx_raw.rename(columns={'Open':'Open_spx','Close':'Close_spx'})
spx_raw['Date']=spx_raw['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))

second_raw = yf.download('^RUT',start='1987-09-10',end='2024-06-30',progress=False)
second_raw=second_raw.reset_index(drop=False)
second_raw=second_raw.rename(columns={'Open':'Open_rty','Close':'Close_rty'})
second_raw['Date']=second_raw['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))





pd.isnull(spx_raw['Close_spx']).sum()
pd.isnull(second_raw['Close_rty']).sum()




spx0=pd.merge(spx_raw[['Date','Open_spx','Close_spx']].copy(),second_raw[['Date','Open_rty','Close_rty']].copy(),how='left',on=['Date'])

pd.isnull(spx0['Close_spx']).sum()
pd.isnull(spx0['Close_rty']).sum()


spx0['Close_spx_lag1']=spx0['Close_spx'].shift(1)
spx0['Close_rty_lag1']=spx0['Close_rty'].shift(1)
spx0['spx_change']=spx0['Close_spx']/spx0['Close_spx_lag1']-1
spx0['rty_change']=spx0['Close_rty']/spx0['Close_rty_lag1']-1




spx=spx0.loc[(spx0['Date']>='2019-10-01')&(spx0['Date']<='2022-12-31'),:].copy()





capital=1

spx['spx_60_max']=spx['Close_spx'].rolling(60).max()
spx['spx_60_dd']=spx['Close_spx']/spx['spx_60_max']-1
spx['spx_60_dd_shift']=spx['spx_60_dd'].shift(1)


spx=spx.reset_index(drop=True)


#determine when hedge
spx['spx_max']=spx['Close_spx'].rolling(28).max()

spx['spx_min']=spx['Close_spx'].rolling(28).min()

spx['spx_close_normalized']=(spx['Close_spx']-spx['spx_min'])/(spx['spx_max']-spx['spx_min'])
spx['spx_slow']=spx['spx_close_normalized'].rolling(6).mean()

spx['hedge_B']=((spx['spx_close_normalized']>0.2)&(spx['spx_close_normalized']>spx['spx_slow']))*1
spx['hedge_S']=((spx['spx_close_normalized']<0.8)&(spx['spx_close_normalized']<spx['spx_slow']))*1
spx['hedge_B_shift']=spx['hedge_B'].shift(1)



spx_use=spx[['Date','Close_spx','spx_change','Close_rty','rty_change','spx_60_dd_shift','hedge_B_shift']].copy()
#spx_use=spx_use.loc[(~pd.isnull(spx_use['spx_change']))&(~pd.isnull(spx_use['djia_change'])),:].copy()


spx_use=spx_use[60:].copy()
spx_use=spx_use.reset_index(drop=True)

spx_use[['Date','Close_spx']].head(5)
spx_use[['Date','Close_spx']].tail(5)

spx_use[['Date','Close_rty']].head(5)
spx_use[['Date','Close_rty']].tail(5)





capital=1
spx_use['account_value']=0
spx_use['hedge_size']=0
spx_use['spx_change_1']=(1+spx_use['spx_change'])
spx_use['spx_cum_product']=spx_use['spx_change_1'].cumprod()
spx_use['rty_change_1']=(1+spx_use['rty_change'])
spx_use['rty_cum_product']=spx_use['rty_change_1'].cumprod()


i=0
for i in range(0,spx_use.shape[0]):
    if i==0:
        if spx_use.loc[i,'hedge_B_shift']==0:
            spx_use.loc[i,'hedge_pnl']=0
            spx_use.loc[i,'account_value']=capital*(1+spx_use.loc[i,'spx_change'])
        else:
            spx_use.loc[i,'hedge_pnl']=capital*(1+0.5*spx_use.loc[i,'spx_60_dd_shift'])*spx_use.loc[i,'rty_change']*-1
            spx_use.loc[i,'account_value']=capital*(1+spx_use.loc[i,'spx_change'])+spx_use.loc[i,'hedge_pnl']        

    if i>0:
        if spx_use.loc[i,'hedge_B_shift']==0:
            spx_use.loc[i,'hedge_pnl']=0
            spx_use.loc[i,'account_value']=spx_use.loc[i-1,'account_value']*(1+spx_use.loc[i,'spx_change'])
        else:
            spx_use.loc[i,'hedge_pnl']=spx_use.loc[i-1,'account_value']*(1+0.5*spx_use.loc[i,'spx_60_dd_shift'])*spx_use.loc[i,'rty_change']*-1
            spx_use.loc[i,'account_value']=spx_use.loc[i-1,'account_value']*(1+spx_use.loc[i,'spx_change'])+spx_use.loc[i,'hedge_pnl']              





spx_use.tail(10)

        
    
#https://stackoverflow.com/questions/69861880/plotly-colorize-line-segments
#https://medium.com/codex/financial-charts-and-visuals-with-plotly-in-python-843ffa9341a9   #plot stock 
#./python -m pip install plotly
#./python -m pip install kaleido

from plotly.offline import download_plotlyjs, init_notebook_mode,  plot
from plotly import graph_objects as go

x =spx_use['Date'].values
y1 = spx_use['spx_cum_product'].values
y2 = spx_use['rty_cum_product'].values
y3 = spx_use['account_value'].values



layout = go.Layout(autosize=False,width=1300,height=700,
                   title='<span style="font-size: 30px;">abc plot</span>',
                   xaxis_title='<b>Date</b>',#"Date",
                   yaxis_title='<b>Cumulative P&L</b>',#"Cumulative P&L",
                   legend_title='<span style="font-size: 15px;">Legend Description</span>')
fig = go.Figure(layout=layout)
#obj1 = go.Scatter(x = x,y = y2,mode = 'lines')
#fig.add_trace(obj1)
obj2 = go.Scatter(x = x,y = y3,mode = 'lines',marker=dict(color='#CDAA7D'))
fig.add_trace(obj2)

fig['data'][0]['name'] = 'Account Value - S&P hedge with Russel'   #change legend first color description name

#defind 2 colors for hedge
line_cols = np.where(spx_use['hedge_B_shift'].values==1,"red","black")
color_legend_name={'red':'S&P (Own Movement) - Hedging Triggered','black':'S&P (Own Movement) - Hedging Not Triggered'}

#find the index of first occurance of distince emement
distinct_element_first_occurance_index=[np.where(line_cols==k)[0][0] for k in list(set(line_cols))]

i=0
#iterate every single points in line_cols, each will show a legend line in right, but only show it when it is in the index of
#distinct color
for i, col in enumerate(line_cols):
    if i in distinct_element_first_occurance_index:
        fig.add_scatter(x=x[i:(i+2)], y=y1[i:(i+2)],line=dict(color=col),mode='lines',showlegend=True) #don't know why use i+2, just follow it
        fig['data'][i+1]['name'] = color_legend_name[col]  #need to use i+1 because fig['data'][0]['name'] already used above
    else:
        fig.add_scatter(x=x[i:(i+2)], y=y1[i:(i+2)],line=dict(color=col),mode='lines',showlegend=False)        

#add vertical line
fig.add_vline(x='2022-04-07')
#add horizontal line
fig.add_hline(y=0.8, line_dash="dot",annotation_text="hello",annotation_position="bottom left")
#add verticval rectangular
fig.add_vrect(x0="2022-05-18", x1="2022-06-01",annotation_text="decline", annotation_position="top left",fillcolor="green", opacity=0.25, line_width=0)
#fig.layout.yaxis.tickformat = ',.0%'  #display in percentage

plot(fig)

fig.write_image("plotly_temp.jpeg")






















#price - 10 ema indicator

import os
import datetime
import numpy as np
from numpy import inf
import time
import pandas as pd
from datetime import datetime as dt
from pandas import read_excel
from talib import abstract
import scipy.stats
#os.chdir(r'C:\Users\jonathanjames\aws\notebooks\index_analysis')
os.chdir('/home/jonathanjames/aws/notebooks/index_analysis')


hsi_y_path='backtest_linux/database/hkex/hsi_y.xlsx'
tidy_path='backtest_linux/database/tidy'


selection_target='AAPL'  #EA NFLX AAPL AMT MNST
HSI_source=pd.read_excel(os.path.join(selection_target+'_with_tidy.xlsx'),'Sheet1')


indicator_source=pd.read_excel(os.path.join('New Basket_20210128.xlsx'),selection_target)
indicator_source=indicator_source[2:].copy()
indicator_source.columns=['Date','a','indicator']
indicator_source=indicator_source[['Date','indicator']].copy()
indicator_source.dtypes
indicator_source['Date2']=indicator_source['Date'].apply(lambda x:dt.strftime(x,"%Y-%m-%d"))
indicator_source=indicator_source[['Date2','indicator']].copy()


HSI_source=pd.read_excel(selection_target+'_with_tidy.xlsx','Sheet1')
HSI_source=HSI_source[['Date2','Close'+'_'+selection_target]].copy()
HSI_source=HSI_source.rename(columns={'Close'+'_'+selection_target:'close'})
HSI_source['year_cohord']=HSI_source['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y")).astype(int)
HSI_source=pd.merge(HSI_source,indicator_source,how='left',on=['Date2'])


HSI_source['ema_10']=abstract.EMA(HSI_source,7)
HSI_source['RSI']=abstract.RSI(HSI_source,7)
HSI_source['price_ema10']=100*(HSI_source['close']-HSI_source['ema_10'])/HSI_source['ema_10']
HSI_source['f2']=(HSI_source['close']-HSI_source['ema_10'])/HSI_source['ema_10']




#use normalization, substract mean and divided by std
target_variable='f2'
distinct_year=HSI_source['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2010]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=HSI_source.loc[HSI_source['year_cohord']<yy,target_variable].values
    data_use=data_use[~np.isnan(data_use)]
    data_use_mean=np.mean(data_use);data_use_std=np.std(data_use)
    t1='mean';t2='std'
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],t1:[data_use_mean],t2:[data_use_std]}))

HSI_source=pd.merge(HSI_source,percentile_cum,how='left',on=['year_cohord'])
HSI_source['f1_temp']=(HSI_source['f2']-HSI_source['mean'])/HSI_source['std']
HSI_source['f1']=100*(1/(1+np.exp(-1*HSI_source['f1_temp'])))




year_min=HSI_source['year_cohord'].unique()
year_min=min(year_min)
year_min_plus=year_min+2 #make sure use at least 2 year historical data

#use emprical distribution
target_variable='f2'
new_variable='f3'     #new variable name
distinct_year=HSI_source['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=year_min_plus] 
yy=2010
output=pd.DataFrame([])
for yy in distinct_year:
        data_use=HSI_source.loc[(HSI_source['year_cohord']>=yy-100)&(HSI_source['year_cohord']<yy),target_variable].values
        data_use=data_use[~np.isnan(data_use)]
        data_use=pd.DataFrame(data_use)
        data_use.columns=['historical_indicator']
        data_use['key']='k'
        data_use_count=data_use.shape[0]
        
        temp=HSI_source.loc[HSI_source['year_cohord']==yy,['Date2',target_variable]].copy()
        temp['key']='k'
        
        temp=pd.merge(temp,data_use,how='left',on='key')
        temp['check']=1*(temp.historical_indicator<=temp[target_variable])
        
        temp=temp.groupby(['Date2'])['check'].sum()  
        temp=100*temp/data_use_count
        temp=pd.DataFrame(temp)
        temp=temp.reset_index(drop=False)
        temp.columns=['Date2',new_variable]
        output=output.append(temp)

HSI_source=pd.merge(HSI_source,output[['Date2',new_variable]].copy(),how='left',on=['Date2'])
#only export data >year_min_plus
HSI_source=HSI_source.loc[HSI_source['year_cohord']>=year_min_plus,:].copy()

HSI_source=HSI_source.loc[(HSI_source['Date2']>='2020-06-01')&(HSI_source['Date2']<='2020-12-31')&(HSI_source['close']!=100),:].copy()

np.sqrt(sum(np.power(HSI_source['f1']-HSI_source['indicator'],2)))
np.sqrt(sum(np.power(HSI_source['f3']-HSI_source['indicator'],2)))
np.sqrt(sum(np.power(HSI_source['RSI']-HSI_source['indicator'],2)))


import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure


#density plot
plt.figure(figsize=(10,5), dpi=80, facecolor='w', edgecolor='k')        
plt.subplot(2,2,1).set_title('density plot') #fist two argument is the dimension, the three argument is the number for each plot
plt.tight_layout() # Or equivalently,  "plt.tight_layout()"
plt.hist(HSI_source['f3'].values,normed=True,bins=30)#,range=(0,1))  #ravel=flatten
plt.xlabel('x')
plt.ylabel('density') 







plt.figure(figsize=(15,5))
# plot lines
plt.plot(np.arange(0,HSI_source.shape[0]), HSI_source.close, label = "close")
plt.plot(np.arange(0,HSI_source.shape[0]), HSI_source.ema_10, label = "ema_10")
plt.legend()
#plt.show()

plt.figure(figsize=(15,5))
# plot lines
#plt.plot(np.arange(0,HSI_source.shape[0]), HSI_source.close, label = "close")
#plt.plot(np.arange(0,HSI_source.shape[0]), HSI_source.f1, label = "f1")
plt.plot(np.arange(0,HSI_source.shape[0]), HSI_source.f3, label = "f3")
plt.axhline(y = 50, color = 'r', linestyle = '-')
plt.legend()
#plt.show()

plt.figure(figsize=(15,5))
# plot lines
#plt.plot(np.arange(0,HSI_source.shape[0]), HSI_source.f1, label = "f1")
plt.plot(np.arange(0,HSI_source.shape[0]), HSI_source.f3, label = "f3")
plt.plot(np.arange(0,HSI_source.shape[0]), HSI_source.RSI, label = "RSI")
plt.plot(np.arange(0,HSI_source.shape[0]), HSI_source.indicator, label = "indicator")
plt.axhline(y = 50, color = 'r', linestyle = '-')
plt.legend()
plt.show()

































































sql_query.sql
#this script at notebook/horse/mysql_backup
`sddoLive`SELECT * FROM `sddo_20191020` WHERE bettype='win' AND raceno=5 ORDER BY up_time DESC;
SELECT * FROM `sddo_20191020` WHERE bettype='win' AND raceno=7 ORDER BY up_time DESC;
SELECT * FROM `sddo_20191020` WHERE bettype='win' AND raceno=9 ORDER BY up_time DESC;

SELECT * FROM `sddo_20191020` WHERE bettype='tri' AND raceno=5 ORDER BY up_time DESC;
SELECT * FROM `sddo_20191020` WHERE bettype='tri' AND raceno=7 ORDER BY up_time DESC;
SELECT * FROM `sddo_20191020` WHERE bettype='tri' AND raceno=9 ORDER BY up_time DESC;

SELECT * FROM `sddo_20220605` WHERE bettype='win' AND raceno=4 ORDER BY up_time DESC;
SELECT * FROM `sddo_20191027` WHERE bettype='win' AND raceno=2 ORDER BY up_time DESC;
SELECT * FROM `sddo_20191027` WHERE bettype='qpl' AND raceno=9 ORDER BY up_time DESC;

SELECT * FROM `sddo_20221001` WHERE bettype='win' AND raceno=6 ORDER BY up_time DESC;
SELECT * FROM `sddo_20200412` WHERE raceno=1 ORDER BY up_time DESC;
SELECT * FROM `sddo_20220921` WHERE bettype='win' AND raceno=8 ORDER BY up_time DESC;
SELECT * FROM `sddo_20200906` WHERE bettype='fct' AND raceno=1 ORDER BY up_time DESC;

SELECT * FROM sddo_20191103 WHERE bettype="win" AND up_time<='12:15:25' AND raceno=1 AND DATE="2019-11-03" ORDER BY up_time DESC LIMIT 1;
SELECT * FROM `sddo_20200712` WHERE bettype='win' AND raceno=10 ORDER BY up_time DESC;
SELECT * FROM `sddo_20200906` WHERE bettype='fct_pool' AND raceno=2 ORDER BY up_time DESC;
SELECT * FROM `sddo_20220126` WHERE bettype='win_pool' AND raceno=2 ORDER BY up_time DESC;

SELECT * FROM race_result WHERE DATE='2019/05/22' AND raceno='8';

SELECT * FROM dividend WHERE DATE='2019/05/22' AND raceno='8';



SELECT DISTINCT truf_dirt FROM racecard;
SELECT DISTINCT DATE, raceno FROM mset;
SELECT DISTINCT DATE, raceno FROM dividend;
SELECT DISTINCT DATE, raceno FROM race_result;

SELECT * FROM `win_sddo_25s_nice_format` ORDER BY DATE DESC;
SELECT * FROM `tri_sddo_25s_nice_format` ORDER BY DATE DESC;
SELECT * FROM `pla_sddo_25s_nice_format` ORDER BY DATE DESC;
DELETE FROM `win_sddo_25s_nice_format` WHERE DATE='2019-11-06';
DELETE FROM `sddo_25s_after20191006_win` WHERE DATE='2019-11-06' AND raceno="1";
DELETE FROM `race_result` WHERE DATE>'2021/09/01';

SELECT * FROM `qin_sddo_25s_nice_format` ORDER BY DATE DESC;
SELECT * FROM `ff_sddo_25s_nice_format` ORDER BY DATE DESC,raceno DESC;

#DELETE FROM `win_sddo_25s_nice_format` WHERE DATE>'2019-10-06';
#DELETE FROM `pla_sddo_25s_nice_format` WHERE DATE>'2019-10-06';
#DELETE FROM `qin_sddo_25s_nice_format` WHERE DATE>'2019-10-06';
#DELETE FROM `qpl_sddo_25s_nice_format` WHERE DATE>'2019-10-06';
#DELETE FROM `tri_sddo_25s_nice_format` WHERE DATE>'2019-10-06';
#delete from `sickhistory` where date_racecard='2020/02/23';
#delete from racecard where Date='2021/10/13';
#delete from `sddo_20200906` where extraction_time<'2020-09-05 23:59:59';
#delete from `pools_25s_after20191006` where date='2020-09-06';
#DELETE FROM `pools_final_after20191006` WHERE DATE='2020-09-06';

SELECT * FROM `pools_25s_after20191006` WHERE DATE='2020-09-06' AND raceno=1;

SELECT * FROM `pla_sddo_25s_nice_format` WHERE DATE='2016-07-10' AND raceno=2;

CREATE TABLE sddo_store.try2 SELECT * FROM horseracing.try2;


SELECT DATE, raceno, COUNT(*) AS freq FROM main_data GROUP BY DATE, RaceNo;
SELECT * FROM `racecard` WHERE (DATE='2020/09/13' OR DATE='2020/07/15') AND raceno='2';
SELECT race_start_time,RaceNo,Horse FROM `racecard` WHERE (DATE='2020/09/06');

SELECT * FROM `sddo_20200614` WHERE raceno=1 AND bettype='Qin';

SELECT * FROM `sickhistory` WHERE Date_racecard='2022/09/21' AND HorseName_Brand='the runner_D042';

SELECT * FROM `main_data` ORDER BY DATE ASC;

#add new column to `win_sddo_25s_nice_format` and `pla_sddo_25s_nice_format`
#alter table win_sddo_25s_nice_format add column win_oddoddoddodd_before90s double after win_oddoddoddodd_25s;
#ALTER TABLE pla_oddoddoddsddo_25s_nice_format ADD COLUMN pla_oddoddoddodd_before90s DOUBLE AFTER pla_oddoddoddodd_25s;

SELECT * FROM pla_oddoddoddsddo_25s_nice_format WHERE DATE='2022-01-23' AND raceno='5';
DELETE FROM `win_oddoddoddsddo_25s_nice_format` WHERE DATE>='2019-10-09';
DELETE FROM `pla_oddoddoddsddo_25s_nice_format` WHERE DATE>='2019-10-09';

SELECT * FROM `oddoddoddsddo_20220123` WHERE DATE='2022-01-23' AND raceno='3' AND bettype='pla_pool' ORDER BY up_time DESC;

DROP TABLE race_result2;
DROP TABLE main_data;
SELECT COUNT(*) FROM main_data;
CREATE TABLE racecard_backup_20220221 AS SELECT * FROM racecard;

SELECT * FROM `racecard_before_racestart` WHERE DATE='2022/09/14' AND Horse='SKY GEM';
SELECT * FROM `racecard_before_racestart` WHERE DATE='2022/09/21' AND RaceNo=7;
#delete from racecard_before_racestart where DATE='2022/09/11' AND RaceNo='1';







##########################
#########mysql############
##########################

#CREATE DATABASE sql_learning;

SELECT * FROM df1 INNER JOIN df2 ON df1.name=df2.name;
SELECT df1.b,df1.name,df2.d FROM df1 INNER JOIN df2 ON df1.name=df2.name;
SELECT * FROM df1 LEFT JOIN df2 ON df1.name=df2.name;
SELECT * FROM df1 RIGHT JOIN df2 ON df1.name=df2.name;
#UNION will remove duplicate rows, to keep all rows, use UNION ALL
SELECT * FROM df1 LEFT JOIN df2 ON df1.name=df2.name UNION SELECT * FROM df1 RIGHT JOIN df2 ON df1.name=df2.name;
 
SELECT * FROM df2 ORDER BY d DESC LIMIT 2;   #only show first 2 rows
SELECT * FROM `df2` LIMIT 2, 1; # skip first 2 row and show next one row
 
 
SELECT * FROM df2 WHERE d<(SELECT MAX(d) FROM df2) ORDER BY d DESC LIMIT 1; #select second max
 


 
#create table and insert value
#table name is case sensitive, primary key must be unique with no null value
DROP TABLE shop;
CREATE TABLE shop (
    article INT UNSIGNED  DEFAULT '0000' NOT NULL,
    dealer  CHAR(20)      DEFAULT ''     NOT NULL,
    price   DECIMAL(16,2) DEFAULT '0.00' NOT NULL,
    PRIMARY KEY(article, dealer));
INSERT INTO shop VALUES
    (1,'A',3.45),(1,'B',3.99),(2,'A',10.99),(3,'B',1.45),
    (3,'C',1.69),(3,'D',1.25),(4,'D',19.95);
INSERT INTO shop VALUES
    (6,'A',3.46);
SELECT * FROM shop;



 
#Where 是一个约束声明
SELECT AVG(price) FROM shop WHERE article>=2;
#having is Having是一个过滤声明，是在查询返回结果集以后对查询结果进行的过滤操作
SELECT dealer, AVG(price) AS p FROM shop GROUP BY dealer HAVING p>=2; 
 
#Maximum of Column per Group
SELECT article, MAX(price) AS price FROM   shop GROUP BY article;


 
#https://w...content-available-to-author-only...y.com/library/view/mysql-reference-manual/0596002653/ch03s05.html
#“For each article, find the dealer(s) with the most expensive price.”


SELECT article, dealer, price
FROM   shop s1
WHERE  price=(SELECT MAX(price) FROM shop WHERE s1.article = shop.article);



#When subquery returns more than 1 value, you will have to use IN
SELECT article, dealer, price
FROM   shop WHERE  price IN (SELECT MAX(price) FROM shop GROUP BY article);


 
#or use this in one line
SELECT article, SUBSTRING( MAX( CONCAT(LPAD(price,6,'0'),dealer) ), 7) AS dealer,
  0.00+LEFT(MAX(CONCAT(LPAD(price,6,'0'),dealer)), 6) AS price FROM shop GROUP BY article;        
 
#Left-pad the string with "ABC", to a total length of 20:
SELECT LPAD("SQL Tutorial", 20, "ABC");              
SELECT SUBSTRING("SQL Tutorial", 5, 3) AS ExtractString;     
SELECT CONCAT(LPAD(price,6,'0'),dealer) AS dealer FROM shop;
SELECT MAX(CONCAT(LPAD(price,6,'0'),dealer)) AS dealer FROM shop GROUP BY article; 
SELECT SUBSTRING(MAX(CONCAT(LPAD(price,6,'0'),dealer)),7) AS dealer FROM shop GROUP BY article;      
 
SELECT LEFT(MAX(CONCAT(LPAD(price,6,'0'),dealer)), 6) AS price FROM shop GROUP BY article;   
SELECT 0.00+LEFT(MAX(CONCAT(LPAD(price,6,'0'),dealer)), 6) AS price FROM shop GROUP BY article;#0.00 is digit format          
 
 
 
 
 
#https://w...content-available-to-author-only...h.com/sql/foreign-key-constraint.html
 
#The PRIMARY KEY constraint uniquely identifies each record in a table. cannot contain NULL values
ALTER TABLE df1 ADD PRIMARY KEY (b);
 
ALTER TABLE df1 DROP PRIMARY KEY;
 
#A FOREIGN KEY is a key used to link two tables together.
# foreign key b in df2 no need distinct, just name key b as f_b
#foreign jey can make sure b in df2 must exist in b in df1, otherwise error occurs
ALTER TABLE df2 ADD CONSTRAINT f_b FOREIGN KEY  (b) REFERENCES df1(b);
 
#Cannot add or update a child row: a foreign key constraint fails 
INSERT INTO df2 VALUES (9,4,'wong');

#The FOREIGN KEY constraint is used to prevent actions that would destroy links between tables
#cannot remove in df1 because therre is reference key linked
DELETE FROM df1 WHERE b=6;
#ok to delete
DELETE FROM df2 WHERE b=6;

#The FOREIGN KEY constraint also prevents invalid data from being inserted into the foreign key column,
# because it has to be one of the values contained in the table it points to.

ALTER TABLE df2 DROP FOREIGN KEY f_b;
 
 
SELECT COUNT(*) FROM df1;

SELECT DISTINCT b FROM df1;

SELECT DATE FROM race_result WHERE Draw IS NULL;
 
SHOW PROCESSLIST;


/*
LIKE Operator	Description
WHERE CustomerName LIKE 'a%'	Finds any values that start with "a"
WHERE CustomerName LIKE '%a'	Finds any values that end with "a"
WHERE CustomerName LIKE '%or%'	Finds any values that have "or" in any position
WHERE CustomerName LIKE '_r%'	Finds any values that have "r" in the second position
WHERE CustomerName LIKE 'a_%'	Finds any values that start with "a" and are at least 2 characters in length
WHERE CustomerName LIKE 'a__%'	Finds any values that start with "a" and are at least 3 characters in length
WHERE ContactName LIKE 'a%o'	Finds any values that start with "a" and ends with "o"

*/

SELECT * FROM `pokemon_data` WHERE NAME LIKE 'bul%';





SELECT firstname, lastname, Street, District FROM Employee LEFT JOIN Address ON Employee.EmployeeId=Address.EmployeeId;






#find second largest asset size
SELECT assetsize AS SecondLargestAssetSize FROM `Bank` WHERE assetsize < (SELECT MAX(assetsize) FROM `Bank`) ORDER BY assetsize DESC LIMIT 1;

#case example
DROP TABLE marks;
CREATE TABLE marks (n1 INT);
SELECT * FROM marks;
INSERT INTO marks VALUES (10), (11);
ALTER TABLE marks ADD divisible_by_ten CHAR(3);
UPDATE marks
SET divisible_by_ten = CASE WHEN n1 % 10 = 0 THEN 'yes' ELSE 'no' END;
SELECT * FROM marks;










#find first 3 total by type_1
SELECT NAME, Type_1, Total
FROM (
	SELECT
		NAME,
		Type_1,
		Total,
		DENSE_RANK() OVER (PARTITION BY Type_1 ORDER BY Total DESC) AS r
	FROM PokemonStats
) AS temp
WHERE temp.r <=3;




SHOW PROCESSLIST;


#issue 1, hkjc racecard added one more column called "Days since Last Run"

ALTER TABLE racecard_before_racestart ADD COLUMN `Days since Last Run` CHAR(255);


CREATE TABLE shop (
    article INT UNSIGNED  DEFAULT '0000' NOT NULL,
    dealer  CHAR(20)      DEFAULT ''     NOT NULL,
    price   DECIMAL(16,2) DEFAULT '0.00' NOT NULL,
    PRIMARY KEY(article, dealer));
INSERT INTO shop VALUES
    (1,'A',3.45),(1,'B',3.99),(2,'A',10.99),(3,'B',1.45),
    (3,'C',1.69),(3,'D',1.25),(4,'D',19.95);




#create table and insert value
DROP TABLE student;
CREATE TABLE student (
    surname  CHAR(20)      DEFAULT ''     NOT NULL,
    studentnumber  CHAR(20)      DEFAULT ''     NOT NULL,
    ye   DECIMAL(16,2) DEFAULT '0.00' NOT NULL,
    dist  CHAR(20)      DEFAULT ''     NOT NULL);
INSERT INTO student VALUES
    ('jonathan','1',1995,'wan chai'),('simon','2',1998,'kwai fong');

DROP TABLE course;
CREATE TABLE course (
    coursecode  CHAR(20)      DEFAULT ''     NOT NULL,
    studentnumber  CHAR(20)      DEFAULT ''     NOT NULL,
    tutor  CHAR(20)      DEFAULT ''     NOT NULL);
INSERT INTO course VALUES
    ('eng','1','23789'),('math','2','9089');

SELECT * FROM student LEFT JOIN course ON student.studentnumber=course.studentnumber WHERE ye >= 1990 AND tutor='23789' ORDER BY coursecode ASC ;




#hkex interview question
DROP TABLE policy_holder;
CREATE TABLE policy_holder (
    person_id INT NOT NULL,
    pd_type CHAR(50) NOT NULL,
    risk CHAR(50) NOT NULL,
    prenium DECIMAL(19,4) NOT NULL #19 digits and 4 decimals
    );
INSERT INTO policy_holder VALUES
    (1,'life','high',200),(1,'life','high',300),(2,'medical','high',1000),(2,'life','low',300),(3,'medical','low',200),(3,'medical','low',300);
    
SELECT * FROM policy_holder;

#update record
UPDATE policy_holder SET prenium=400 WHERE person_id=2 AND pd_type='medical';


#select column based on condition
SELECT person_id,
       pd_type,
       risk,
       prenium,
       CASE  
           WHEN pd_type = 'life' AND risk='high' THEN 0.1
           WHEN pd_type = 'life' AND risk='low' THEN 0.15
           WHEN pd_type = 'medical' AND risk='high' THEN 0.2
           WHEN pd_type = 'medical' AND risk='low' THEN 0.3
       END AS ratio
FROM policy_holder;

#add new column to table based on condition
ALTER TABLE policy_holder ADD ratio DECIMAL(19,4);
UPDATE policy_holder
SET ratio = CASE
           WHEN pd_type = 'life' AND risk='high' THEN 0.1
           WHEN pd_type = 'life' AND risk='low' THEN 0.15
           WHEN pd_type = 'medical' AND risk='high' THEN 0.2
           WHEN pd_type = 'medical' AND risk='low' THEN 0.3
           END;

SELECT * FROM policy_holder;

#add new column by multiply two columns
ALTER TABLE policy_holder ADD fee DECIMAL(19,4);
UPDATE policy_holder
SET fee=ratio*prenium;

SELECT * FROM policy_holder;

#select sum of fee group by two columns
SELECT person_id, pd_type, SUM(fee) FROM policy_holder GROUP BY person_id, pd_type;


































 
 