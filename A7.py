def construct_magic_square_matrix(M,n) :    
    for i in range(n) :
       A = []
       for j in range (n) :
          A.append(int(-1))
       M.append(A)
    i = 0
    j = int((n - 1) / 2)
    s = 1
    count = 0
    while(count < (n * n)) :
        M[i][j] = s
        s = s + 1
        count = count + 1
        
        if(i == 0) :
            ni = n - 1
        else:
            ni = i - 1;
        if(j == 0) :
            nj = n - 1
        else:
            nj = j - 1;
        if(M[ni][nj] != -1) :
            ni = int((i + 1 ) % n)
            nj = j
        i = ni
        j = nj
        
    print("\nMagic Square Matrix constructed successfully\n")


def display_matrix(M,n): 
   print("Magic Square Matrix (%d,%d) : "%(n,n))
   for i in range(n) :
      print("\t\t",end=' ')
      for j in range(n):
          print("%2d"%M[i][j],end='   ')
      print("")	
   print("Sum in each row & each column = %d"%int(n*(n*n+1)/2)) 

       

def main():
   
   while True :
       print("\t\t\t1: Find Magic Square");
       print("\t\t\t2: Exit");
       ch = int(input("Enter your choice : "))       
       if (ch == 2):
           print ("End of Program")
           break
       elif (ch==1):
           M = []
           n = int(input("\nEnter the order of the Square Matrix (n,n) : "))
           construct_magic_square_matrix(M,n);
           display_matrix(M,n)	
       else :
           print ("Wrong choice entered !! Try again")

main()
quit()
