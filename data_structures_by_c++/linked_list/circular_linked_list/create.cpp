#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int val;
    Node *next;
    Node(int val)
    {
        this->val = val;
        this->next = NULL;
    }
};

int main()
{
    Node *head = new Node(10);
    Node *a = new Node(20);
    Node *b = new Node(30);

    head->next = a;
    a->next = b;
    b->next = head;

    Node *tmp = head;
    for (int i = 0; i < 3; i++)
    {
        cout << tmp->val << " ";
        tmp = tmp->next;
    }
    cout << endl;
}
