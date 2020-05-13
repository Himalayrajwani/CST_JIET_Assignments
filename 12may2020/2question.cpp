#include<bits/stdc++.h>
using namespace std;
int main()
{
	int r,count=0,i,j;
	cout<<"\nEnter size of nxn matrix : ";
	cin>>r;
	int arr[r][r];
	for(i=0;i<r;i++)
	{
		for(j=0;j<r;j++)
		{
			cout<<"\n Enter element : "<<i+1<<j+1<<" : ";
			cin>>arr[i][j];
		}
	}
	int n;
	cout<<"Enter number for search : ";
	cin>>n;
	i=0;
	j=0;
	int f=0;
	while(i<r && j<r)
	{
		if(arr[i][j]==n)
		{
			cout<<"Number found at position ("<<i<<" , "<<j<<")"<<endl;
			f=1;
			break;
		}
		if(arr[i][j+1]<n && j+1<r)
		{
			j=j+1;
		}
		else
		{
			i=i+1;
		}
	}
	if(f==0)
	{
		cout<<"Number not found"<<endl;
	}
}