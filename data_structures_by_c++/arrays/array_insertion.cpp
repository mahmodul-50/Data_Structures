#include<bits/stdc++.h>
using namespace std;

#define int long long

int32_t main()
{
    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);

    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    int arr[100];

    cout << "Enter elements:" << endl;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int pos, val;
    cout << "Enter position to insert (0-based index): ";
    cin >> pos;

    cout << "Enter value to insert: ";
    cin >> val;

    for (int i = n; i > pos; i--)
    {
        arr[i] = arr[i - 1];
    }

    arr[pos] = val;
    n++;

    cout << "Array after insertion: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}