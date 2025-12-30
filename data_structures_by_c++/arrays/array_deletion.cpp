#include <bits/stdc++.h>
using namespace std;

int main()
{
    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);
    
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
    int arr[100];
    cout << "Enter elements: " << endl;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    int pos;
    cout << "Enter position to delete (0-based index): ";
    cin >> pos;
    for (int i = pos; i < n - 1; i++)
    {
        arr[i] = arr[i + 1];
    }
    n--;
    cout << "Array after deletion: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}
