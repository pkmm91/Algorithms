/* O(nlogn)*/
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
    int arr[] = {5 , 2 , 1 , 4 , 6};
    int n  = sizeof(arr) / sizeof(arr[0]);
    std::sort(arr , arr + n);
    int start = 0 , e = n-1;
    int sum = 0;
    while(start < e)
    {
        sum = arr[start] + arr[e];
        if (sum == 7)
        {
           cout<<arr[start]<<" "<< arr[e] << endl;
           start++;
           e--;
        }
        else if(sum < 7)
            start++;
        else
            e--;
    }
    return 0;
}
