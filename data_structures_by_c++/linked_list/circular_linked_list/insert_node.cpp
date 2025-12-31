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

void insert_node(Node *&head, int val)
{
    Node *newnode = new Node(val);
    if (head == NULL)
    {
        head = newnode;
        newnode->next = head;
        return;
    }
    Node *tmp = head;
    while (tmp->next != head)
    {
        tmp = tmp->next;
    }
    tmp->next = newnode;
    newnode->next = head;
}

void traversal(Node *head)
{
    if (head == NULL)
        return;
    Node *tmp = head;
    while(true)
    {
        cout << tmp->val << " ";
        tmp = tmp->next;
        if (tmp == head)
            break;
    }
    cout << endl;
}

int main()
{
    Node *head = NULL;

    insert_node(head, 10);
    insert_node(head, 20);
    insert_node(head, 30);
    insert_node(head, 40);

    traversal(head);
}
