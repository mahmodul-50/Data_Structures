#include<bits/stdc++.h>
using namespace std;

#define int long long

int32_t main()
{
    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);

    int n;
    cout << "enter number of elements:";
    cin >> n;
    int arr[n];
    cout << "Enter element:" << endl;
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "Array elements are:";
    for(int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}