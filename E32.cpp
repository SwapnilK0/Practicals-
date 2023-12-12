/*parlor accepting maximum M orders. Orders are served in first come first served basis. Order once placed cannot be cancelled. Write C++ program to simulate the system using circular queue using array.*/


#include<iostream>
#include<stdlib.h>
#include<unistd.h>
using namespace std;

int front=0,rear=-1;
int cnt=0;
int data[5];


void enque(int no)
{
rear=(rear+1)%5;
data[rear]=no;
cnt++;
}

int isfull()
{
if(cnt==5)
return 1;
else
return 0;
}

void display()
{
int i;
for(i=front;i!=rear;i=(i+1)%5)
{
cout<<"\nOrder of table no  has been served"<<data[i];
sleep(2);
}
cout<<"\nOrder of table no has been served"<<data[i];
sleep(2);
}

int main()
{
int ch,n;
cout<<"\nMaximum orders served are 5";
do
{
cout<<"\n\nMenu\n1.Place an order\n2.Display the serving list";
cin>>ch;

switch(ch)
{
case 1: if(!isfull())
	{
		
	
		cout<<"\nEnter your table no.";
		cin>>n;
		enque(n);
			
        }
	else
	cout<<"\nOrders Full!!!!";

	break;

case 2: display();
	break;
}
}while(ch!=3);
return 0;
}


