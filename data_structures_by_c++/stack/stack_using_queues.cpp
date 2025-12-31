#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int val;
    Node *next;
    Node *prev;
    Node(int val)
    {
        this->val = val;
        this->next = NULL;
        this->prev = NULL;
    }
};

class my_stack
{
public:
    queue<int> q;
    my_stack()
    {
    }

    void push(int x)
    {
        q.push(x);
    }

    int pop()
    {
        queue<int> q2;
        int val;
        while (!q.empty())
        {
            val = q.front();
            q.pop();
            if (q.empty() == true)
                break;
            q2.push(val);
        }
        q = q2;
        return val;
    }

    int top()
    {
        return q.back();
    }

    bool empty()
    {
        return q.empty();
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