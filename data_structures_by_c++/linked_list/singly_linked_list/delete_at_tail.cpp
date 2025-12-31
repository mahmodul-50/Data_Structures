#include <bits/stdc++.h>
using namespace std;

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

void insert_at_tail(Node* &head, Node* &tail, int val)
{
    Node* newnode = new Node(val);
    if(head == NULL)
    {
        head = newnode;
        tail = newnode;
        return;
    }
    tail->next = newnode;
    tail = newnode;
}

void delete_at_tail(Node* &head, Node* &tail)
{
    if(head == NULL) return;
    if(head->next == NULL)
    {
        delete head;
        head = NULL;
        tail = NULL;
        return;
    }
    Node* tmp = head;
    while(tmp->next->next != NULL)
    {
        tmp = tmp->next;
    }
    delete tmp->next;
    tmp->next = NULL;
    tail = tmp;
}

void print_linked_list(Node* head)
{
    Node* tmp = head;
    while(tmp != NULL)
    {
        cout << tmp->val << " ";
        tmp = tmp->next;
    }
    cout << endl;
}

int main()
{
    Node* head = NULL;
    Node* tail = NULL;

    insert_at_tail(head, tail, 10);
    insert_at_tail(head, tail, 20);
    insert_at_tail(head, tail, 30);
    insert_at_tail(head, tail, 40);

    print_linked_list(head);
    cout << "Tail before delete : " << tail->val << endl;
    delete_at_tail(head,tail);
    print_linked_list(head);
    cout << "Tail after delete: " << tail->val << endl;
    return 0;
}
