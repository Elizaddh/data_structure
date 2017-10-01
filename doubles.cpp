#include<iostream>
using namespace std;

int main(){

int i,j;
int arr[16];

while (arr[i]!=-1){

	int c=0;

	for ( i=0;i<16;i++){
		cin >> arr[i];
		
		if (arr[i]==0||arr[i]==-1)
		break;

	}
	
	if (arr[i]==-1)
	break;
	
	for (i=0;i<16; i++){

	for (j=0;j<16; j++){
	if(arr[i]!=0 &&  arr[i]*2==arr[j])
		
		c=c+1;
		}
		}
	
	cout<< c << endl;
	for (i=0; i<16 ; i++)
	
	arr[i]=0;
	}
	return 0;
}
