#include<bits/stdc++.h>
using namespace std;

#define int long long

int32_t main()
{
    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);

    int arr[] = {10, 20, 30, 40, 50};

    cout << "Traversing: ";
    for(int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
    {
        cout << arr[i] << " ";
    }
}