#include<iostream>
using namespace std;


class TravelLog{

private :
        int distance;
        int eachTime;
public :
int Speed;
int clockTime;

TravelLog (int a, int b){
 distance=a;
 eachTime=b;
}

void addEntry (int Speed,int clockTime)
{
eachTime = clockTime-eachTime;
distance = distance + (eachTime*Speed);
eachTime=clockTime;
}

int getTotalMiles()const{
return distance;
}
};

int main()
{

  int i ,n;

  while(n!=-1){
	cout << "Please provide information about data set." << endl;
  cin>> n ;
 
 if (n==-1)
 break;
 
 TravelLog trip(0,0);


 for (i=1; i<=n; i++)
 {

          cin >>trip.Speed ;
           cin >>trip.clockTime ;
           trip.addEntry(trip.Speed,trip.clockTime);
 }          
   int total = trip.getTotalMiles( );

    cout << "The total distance is "<<total<<" miles."<< endl;

 }
 return 0;
}



