"""
       Group B - Assignment 17
Write a python program to store 12th class percentage of students in array.
Write function for sorting array of integer numbers in ascending order
using bucket sort and display top five scores.
"""

def accept_array(A): 
   n = int(input("Enter the total no. of student : "))
   for i in range(n):
      x = int(input("Enter the  12th class percentage of student %d : "%(i+1)))
      A.append(x)
   print("Array accepted successfully\n\n");

def display_array(A): 
   n = len(A)
   if(n == 0) :
      print("\nNo records in the database")
   else :
      print("Array of 12th class percentage scored by students : ",end=' ')
      for i in range(n) :
         print("%d  "%A[i],end=' ')
      print("\n");

def find_max_digit(A,n) :
   max_element = max(A)
   count=0
   while(max_element > 0 ):
      count=count+1
      max_element = max_element // 10
   return count


def CombineBucket(A,B):
   c=0
   for i in range(10):
      for j in range(len(B[i])) :
         A[c] = B[i][j]
         c = c + 1         

def initialize_bucket(B):
   for i in range(10) :
      T = []
      B.append(T)
   
def Bucket_sort(A,n):
   shift=1
   keysize = find_max_digit(A,n)
   for loop in range(keysize) :
      B = []
      initialize_bucket(B)
      for i in range(n) :
         b_no = int((A[i]/shift)) % 10
         B[b_no].append(A[i])
      CombineBucket(A,B)
      shift = shift * 10

     
def Main() :   
   A = []
   while True :
      print ("\t1 : Accept & Display the FE Marks")      
      print ("\t2 : Bucket sort ascending order and display top five scores")
      print ("\t3 : Exit")
      ch = int(input("Enter your choice : "))
      if (ch == 3):
         print ("End of Program")
         quit()
      elif (ch==1):
         A = []
         accept_array(A)
         display_array(A)
      elif (ch==2):
         print("Marks before sorting")
         display_array(A)
         n =len(A)
         Bucket_sort(A,n)
         print("Marks after sorting")
         display_array(A)         
         if(n >= 5) :
            print("Top Five Scores : ")
            for i in range(n-1,n-6,-1) :
               print("\t%d"%A[i])
         else :
            print("Top Scorers : ")
            for i in range(n-1,-1,-1) :
               print("\t%d"%A[i])                               
      else :
           print ("Wrong choice entered !! Try again")


Main()

