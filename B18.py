"""
       Group B - Assignment 18
Write python program to store 10th class percentage of students in array.
Write function for sorting array of integer numbers in ascending order
using radix sort and display top five scores
"""

def accept_array(A): 
   n = int(input("Enter the total no. of student : "))
   for i in range(n):
      x = int(input("Enter the  10th class percentage of student %d : "%(i+1)))
      A.append(x)
   print("Array accepted successfully\n\n");

def display_array(A): 
   n = len(A)
   if(n == 0) :
      print("\nNo records in the database")
   else :
      print("Array of 10th class percentage scored by students : ",end=' ')
      for i in range(n) :
         print("%d  "%A[i],end=' ')
      print("\n");


def countSort(A,n,exp)  :
   count = [0,0,0,0,0,0,0,0,0,0]
   output  = []
   for i in range(n) :
      output.append(0)
   for i in range(n) :
      ind = int(A[i]/exp)%10
      count[ind] += 1
   for  i in range(1,10) :
      count[i] += count[i-1]

   for i in range(n - 1, -1,-1) :
      ind = int(A[i]/exp)%10
      output[count[ind] - 1] = A[i]
      count[ind] -= 1
   for i in range(n) :
      A[i] = output[i]
  
def Radix_sort(A,n) :
   m = max(A)
   exp = 1
   while( m / exp > 0 ) :
      countSort(A, n, exp)
      exp *= 10

def Main() :   
   A = []
   while True :
      print ("\t1 : Accept & Display the FE Marks")      
      print ("\t2 : Radix sort ascending order and display top five scores")
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
         Radix_sort(A,n)
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

