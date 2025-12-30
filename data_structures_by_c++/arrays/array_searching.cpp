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

    cout << "Enter elements:\n";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int key;
    cout << "Enter element to search: ";
    cin >> key;

    int found = 0;

    for (int i = 0; i < n; i++)
    {
        if (arr[i] == key)
        {
            cout << "Element found at index " << i;
            found = 1;
            break;
        }
    }

    if (found == 0)
    {
        cout << "Element not found";
    }

    return 0;
}
