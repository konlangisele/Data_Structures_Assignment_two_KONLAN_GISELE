#KONLAN GISELE YENNULOM
#ASSIGNMENT_2
#DEQUES


import random #importing the random function to generate a set of random numbers when needed
class Deque:# creation of a deque class
    def __init__(self,array,arrayLength,currentLength): #creation of a function that will contain the variables responsible for checking the arrays and array lengths
        if len(array)>arrayLength:#an if statement to check that the array is not more than the array length
            return error#an error statement
        self.array=array
        self.arrayLength=arrayLength
        self.currrentLength=array.Length #assigning the respective variables      
    def isEmpty(self): #function to check if the array is empty or not
        return len(self.array)==0 #a return statement to return zero if the array is emty
    def isFull(self):#function to check if the array is full or 
        return len(self.array)==self.length#a return statement to return the length of the array.
    def getLength(self):#a getter to obtain the length of the array
        return len(self.currentLength)
    def addToFront(self,x):#a function to add a number to the front of the array
        if self.array==self.arrayLength:#if statement to tell us the array is full 
            return ('array is already full')
        self.array.insert(0,x)#inserting zero in the position of x when necessary
    def addToBack(self,x):#a function to add a number to the back of the array
        if self.array==self.arrayLength:#if statement to tell us the array is full
            return ('array is already full')
        self.array.append(x)#statement to add on to the array if it is not full
    def removeFromFront(self):#a function to delete any number from the front
        self.array.pop(0)#a statement to remove the preferred number from the front
    def removeFromBack(self):#a function to delete any number from the back
        self.array.pop()#a statement to remove the preferred number from the back
    def halfFull(s):#a function to divide the array into equal halves
        halfFull=list(range(rand.randint(1,100)//2))#statement with the formular to make the array half full


        
#INTERPOLATION


def interSearch(array,target): #creation of a function that takes 2 parameters that is the array and the target number we are looking for
    lowest=0 #the lowest number of the array is zero
    highest=(len(array)-1)#the highest number of the array is the total length of the array minus one since indexing starts from zero
    while lowest<=highest and target>=array[lowest] and target<=array[highest]:#while loop to ensure that the target is in the sorted array
        index = lowest + int(((float(highest - lowest) / ( array[highest] - array[lowest])) * ( target- array[lowest]))) #the constant formula for finding the index using interpolation by estimating the midpoint.
        if array[index] == target:#a target is reached when the index of the input array goes with the target number and the index is returned 
            return index
        elif array[index] < target:#for each target being inputted, if the value of the target is larger than the index of the targetted value of the array, the program does a re-evaluation using the left part formula of the sub array
            lowest = index + 1; #the lowest value becomes the index that is found plus one
        else:
            highest = index - 1;# else,for every target inputted, if the value of the target is smaller than the index of the target value of the array, python re-evaluates using the right part formula of the sub array
    return -1 #-1  is retunred if the target does not exist
print(interSearch([1,2,3,4,5,6,7,8],6))

# Python program to implement interpolation search 

# If x is present in arr[0..n-1], then returns 
# index of it, else returns -1
import random #importing random for random numbers
import time #importing time to be able to obtain the time
def InterSearch(array, x, y): 
    # Find indexs of two corners 
    low=0
    high=(x- 1)
    # Since array is sorted, an element present 
    # in array must be in range defined by corner 
    while low<=high and y>=array[low] and y<=array[high]: 
        if low==high: 
            if array[low]==y: 
                return low; 
            return -1; 
     # Probing the position with keeping 
    # uniform distribution in mind. 
        position=low+int(((float(high-low)/(array[high]-array[low]))*(y-array[low]))) 
   # Condition of target found 
        if array[position]==y: 
            return True 
     # If y is larger, y is in upper part 
        if array[position] < y: 
            low = position + 1; 

        # If y is smaller, y is in lower part 
        else: 
            high=position-1; 
    
    return False
TimeInter=[] #variable for the time interval
for e in range(1,6):#for loop to go through the list for 5 different runs
    startingTime=time.time()#intializing a variable for time
    testList = random.sample(range(1,32767),100)#variable to test the list of random numbers generated
    NewList=sorted(testList)#a variable created to sort out the new list for the new set of numbers
    print(NewList)#to print out the new list
    X= int(input("type number: "))#variable initialized to input your preferred number by the user
    print(InterSearch(NewList,100,X))
    endingTime=time.time()#variable to initialize the time it ends
    Interval=(endingTime-startingTime)*1000#variable to initialize the interval between the starting time and ending time
    TimeInter.append(Interval)#used to add or append the interval list
print ("the msecs after trying 5 times for N=100 is: " (TimeInter)//5)

TimeInter=[]
for a in range(1,6):
    startingTime=time.time()
    testList = random.sample(range(1,32767),1000)
    NewList=sorted(testList)
    print(NewList)
    X= int(input("enter number: "))
    print(InterSearch(NewList,1000,X))
    endingTime= time.time()
    Interval=(endingTime-startingTime)*1000
    TimeInterval.append(Interval)
print (sum(TimeInter)//5)

TimeInter=[]
for i in range(1,6):
    startingTime=time.time()
    testList = random.sample(range(1,32767),5000)
    NewList=sorted(testlist)
    print(NewList)
    X= int(input("enter number: "))
    print(InterSearch(NewList,5000,X))
    endingTime= time.time()
    Interval=(endingTime-startingTime)*1000
    TimeInter.append(Interval)
print (sum(TimeInterval)//5)

'''Repeated time code with similar variable names to repeatedly run for 1000 and 5000'''





#Binary Search


import random #importing random to generate random numbers
import time #importing time to enable the time function run
def binary_Search(seq,target): #function for the binarySearch
    lo=0 #initializing the lowest number to zero
    hi=len(seq)-1#initializing the highest number to the length of the sequence minus one
    been_Found=False #a variable to see if the number has been found
    while lo<=hi and not beenFound:
        mid_point=(lo+hi)//2 #used to find the middlepoint of the numbers but adding the lowest and highest numbers and dividing by 2
        if seq[mid_point]==target:#if statement to determine if the sequence of the midpoint is equal to the target
            been_Found=True #if so, then the target has been found
        else:
            if target<seq[mid_point]: #if the target is less than the sequence midpoint
                hi=mid_point-1#then the highest number will be the midpoint minus one
            else:
                lo=mid_point+1#else the lowest number will be the midpoint plus one.
    return been_Found #a return statement to end the while loop

Time_Interval=[]#variable for the time interval
for i in range(1,6):#for loop to go through the list for 5 different runs
    start_Time=time.time()#a variable to start the time 
    TestList = random.sample(range(1,32767),100)#a test variable to generate a set of random numbers to be tested
    NewList=sorted(testlist)#a variable to create a new list and sort it out
    print(NewList)#to print the new list
    X= int(input("Input number: "))#to input the preferred number by the user
    print(binary_Search(NewList,X))
    endTime= time.time()#to end the time
    Interval=(end_Time-start_Time)*1000#to obtain the interval
    Time_Interval.append(Interval)
print (sum(Time_Interval)//5)#to get the sum of the time interval
Time_Interval=[]
for i in range(1,6):
    start_Time=time.time()
    TestList = random.sample(range(1,32767),1000)
    NewList=sorted(testlist)
    print(NewList)
    X= int(input("enter number: "))
    print(InterpolationSearch(Newlist,1000,X))
    end_Time= time.time()
    Interval=(end_Time-start_Time)*1000
    Time_Interval.append(Interval)
print (sum(Time_Interval)//5)

TimeInter=[]
for i in range(1,6):
    starTime=time.time()
    testlist = random.sample(range(1,32767),5000)
    newList=sorted(testlist)
    print(newList)
    X= int(input("input number: "))
    print(InterSearch(Newlist,5000,X))
    endTime= time.time()
    Interval=(endTime-startTime)*1000
    TimeInter.append(Interval)
print (sum(TimeInter)//5)

'''Repeated time code with similar variable names to repeatedly run for 1000 and 5000'''







