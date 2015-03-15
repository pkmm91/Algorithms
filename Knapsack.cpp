#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
using namespace std;
long long  V[501][2000001];
int max (int a , int b)
{
    if (a >= b)
        return a;
    else
        return b;
}
int knapsack(int value[] , int wt[] , int W , int n)
{
    int i , j;
    for(i = 0 ; i <= n ; i++)
        for(j = 0 ; j <= W ; j++)
            if (i == 0 || j == 0)
                V[i][j] = 0;
            else if (wt[i - 1] <= j)
                  V[i][j] = max ( value[i - 1] + V[i - 1][ j - wt[i - 1]] , V[i - 1][j]);
            else
                  V[i][j] = V[i - 1][j];
    return V[n][W];
}
int main()
{
    int s,  W , item;
    scanf("%d %d",&W, &item);
    int value[item], wt[item];
    for(int i = 0; i < item; i++)
        scanf("%d %d" , &value[i] , &wt[i]);
    printf("%d\n",knapsack(value , wt , W , item));
   return 0;
}
