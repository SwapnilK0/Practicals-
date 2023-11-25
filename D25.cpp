/*A palindrome is a string of character that‘s the same forward and backward. Typically,
punctuation, capitalization, and spaces are ignored. For example, ?Poor Dan is in a droop? is
a palindrome, as can be seen by examining the characters ?
poor danisina droop? and
observing that they are the same forward and backward. One way to check for a
palindrome is to reverse the characters in the string and then compare with them the
original-in a palindrome, the sequence will be identical. Write C++ program with functions-
1. To check whether given string is palindrome or not that uses a stack to determine whether
a string is a palindrome.
2. to remove spaces and punctuation in string, convert all the Characters to lowercase, and
then call above Palindrome checking function to check for a palindrome
3. to print string in reverse order using stack.
*/
 
#include<iostream>
#include<string.h>
#define MAX 100
using namespace std;

 struct stack
 {
     char data[MAX];
     int top;
 };

 void init(stack *stck)
 {
     int i;
     for(i=0;i<MAX;i++)
     {
         stck->data[i]='\0';
         stck->top=-1;
     }
 }

 void print(stack stck)
 {
     int i;
     cout<<"\n Stack elements are";
     for(i=0;i<MAX;i++)
     {
         cout<<"stck.data[i]";
         cout<<"\t top="<<stck.top;
     }
 }

 int isempty(stack stck)
 {
     return stck.top==-1?1:0;
 }

 int isfull(stack stck)
 {
     return stck.top==MAX-1?1:0;

 }

 void push(stack *stck,char data[MAX])
 {
     int i;
     for(i=0;data[i]!='\0';i++)
     {
     stck->top+=1;
     stck->data[stck->top]=data[i];
     }
 }

 void push1(stack *stck,char data[MAX])
 {
     int i;
     for(i=0;data[i]!='\0';i++)
     {
       if(data[i]!=' ')
       {
     stck->top+=1;
     stck->data[stck->top]=data[i];
       }
     }
 }


 void pop(stack *stck)
 {
     char rev[MAX];
     int i=0;
     while(!isempty(*stck))
     {
     rev[i]=stck->data[stck->top];
     stck->top-=1;
     i++;
     }
     rev[i]='\0';
     cout<<"\n Original string is="<<stck->data;
     cout<<"\n reverse string is=";
     cout<<rev;
     if(strcmp(rev,stck->data))
     {
     cout<<"\n string is not palindrome";
     }
     else
     {
     cout<<"\n String is palindrome";
     }
 }

 int main()
 {
     stack stck;
     char data[MAX]={'E','v','a',',',' ','c','a','n',' ','I',' ','s','e','e',' ','b','e','e','s',' ','i','n',' ','a',' ','c','a','v','e','\0'};

     init(&stck);
     int ch,i,j=0;

     while(ch!=3)
     {
     cout<<"\n1.Push the string;Print reverse string & check palindrome or not(pop)";

     cout<<"\n2.Remove blank space,convert upperspace into lowercase,push the string & check palindrome or not";

     cout<<"\n3.Exit";

     cout<<"\n Enter your choice";
     cin>>ch;

     switch(ch)
     {
     case 1:
         if(isfull(stck))
         {
         cout<<"\n Stack is full";
         }
         else
         {
         push(&stck,data);
         }
         if(isempty(stck))
         {
         cout<<"\n Stack is empty";
         }
         else
         {
         pop(&stck);
         }
         break;

     case 2:
         init(&stck);
         if(isfull(stck))
         {
         cout<<"\n Stack is full";
         }
         else
         {
         for(i=0;data[i]!='\0';i++)
          {
            if(data[i]!=' ')
            {
             if(data[i]>=65 && data[i]<=90)
              {
                data[i]=data[i]+32;
              }

            }
          }
        push1(&stck,data);

         }
         pop(&stck);
         break;
         }
     }
     return (0);
 }
/* output

1.Push the string;Print reverse string & check palindrome or not(pop)
2.Remove blank space,convert upperspace into lowercase,push the string & check palindrome or not
3.Exit
 Enter your choice1

 Original string is=Poor Dan is in a droop
 reverse string is=poord a ni si naD rooP
 string is not palindrome
1.Push the string;Print reverse string & check palindrome or not(pop)
2.Remove blank space,convert upperspace into lowercase,push the string & check palindrome or not
3.Exit
 Enter your choice2

 Original string is=poordanisinadroop
 reverse string is=poordanisinadroop
 String is palindrome
1.Push the string;Print reverse string & check palindrome or not(pop)
2.Remove blank space,convert upperspace into lowercase,push the string & check palindrome or not
3.Exit
 Enter your choice
*/
