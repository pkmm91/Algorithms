/*complexity O(n)*/
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
    int givensum = 12;
    int currsum = arr[0];
    int start = 0 , e = 0;
    while (e < n)
    {
        if(currsum == givensum)
        {
            cout<<start << e;
        }
        if(currsum <= givensum)
         {
             e++;
            if(e < n)
                currsum += arr[e];
         }
        else
        {
            currsum -= arr[start];
            start++;
    }
    }
    return 0;
}
