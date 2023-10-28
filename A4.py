"""

Write a python program that computes the net amount of a bank account
based a transaction log from console input. The transaction log format
is shown as following: D 100 W 200 (Withdrawal is not allowed if balance
is going negative. Write functions for withdraw and deposit) D means deposit
while W means withdrawal.
Suppose the following input is supplied to the program: 
D 300 
D 300 
W 200 
D 100 
Then, the output should be: 500


"""

def withdrawal(amount,balance):
   balance = balance-amount
   return balance

def deposit(amount,balance):
   balance += amount
   return balance


def main():
   
   while True :
      print ("\t\t1 : Input a new Transaction log")
      print ("\t\t2 : Exit")
      ch = int(input("Enter your choice : "))      
      if (ch == 2):
         print ("End of Program")
         quit()
         break
      elif (ch == 1) :
         balance = 0
         list1 = []
         print("Enter the transaction log of a user : ")
         while True :
            data = input()
            if(data == ""):
               break;
            list1.append(data.split())
         for transaction in list1 :
            if(transaction[0] == 'W') :
               if(balance < int(transaction[1])) :
                  print("[%s %d] : Transaction Declined : Insufficent balance"%(transaction[0],int(transaction[1])))
               else:
                  balance = withdrawal(int(transaction[1]),balance)
                  print("[%s %d] : Successful Transaction "%(transaction[0],int(transaction[1])))
            elif (transaction[0] == 'D') :
               balance = deposit(int(transaction[1]),balance)
               print("[%s %d] : Successful Transaction "%(transaction[0],int(transaction[1])))
               
         print("\nTotal balance in the account : Rs %d"%balance)            
      else :
         print ("Wrong choice entered !! Try again")

main()
quit()

