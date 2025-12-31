#include<bits/stdc++.h>
using namespace std;

#define int long long

class Node
{
    public:
        int val;
        Node* next;
        Node(int val)
        {
            this->val = val;
            this->next = NULL;
        }
};

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    Node a(10),b(20),c(30);

    a.next = &b;
    b.next = &c;

    cout << a.val << endl;
    cout << a.next->val << endl;
    cout << a.next->next->val << endl;
}