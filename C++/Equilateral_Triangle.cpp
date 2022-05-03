/*
    Write a program to print the equilateral triamgle using * 
    with number pf rows inputted by the user
*/



#include<iostream>
using namespace std;

/*  Function to define the code for pinting th estars related to the nu,ber of row.
    This function will be called recursivly.
*/
void pattern(int n)
{
    int k = n-1;
    for(int i =0;i<n;i++)
    {
        for(int j=0;j<k;j++)
        {
            cout<<" ";
        }

        k -=1;
        for (int j=0;j<i+1;j++)
        {
            cout<<"* ";
        }
        cout<<endl;
    }
} 
int main(){
    int numberOFRows = -1;
    cout<<"Enter the Number of Rows : ";
    cin>>numberOFRows;
    pattern(numberOFRows);

    return 0;
}