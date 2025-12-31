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

class my_stack
{
public:
    Node *head = NULL;
    int sz = 0;

    void push(int val) // O(1)
    {
        sz++;
        Node *newnode = new Node(val);
        newnode->next = head;
        head = newnode;
    }

    void pop() // O(1)
    {
        if (head == NULL)
            return;
        sz--;
        Node *deletenode = head;
        head = head->next;
        delete deletenode;
    }

    int top() // O(1)
    {
        return head->val;
    }

    int size() // O(1)
    {
        return sz;
    }

    bool empty() // O(1)
    {
        return head == NULL;
    }
};

int main()
{
    my_stack st;

    st.push(10);
    st.push(20);
    st.push(30);
    st.push(40);

    cout << st.top() << endl;

    while (!st.empty())
    {
        cout << st.top() << " ";
        st.pop();
    }
}
