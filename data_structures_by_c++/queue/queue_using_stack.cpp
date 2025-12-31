#include <bits/stdc++.h>
using namespace std;

class my_queue
{
public:
    stack<int> st;
    void push(int x)
    {
        st.push(x);
    }
    int pop()
    {
        stack<int> st2;
        int val;
        while (!st.empty())
        {
            val = st.top();
            st.pop();
            if (st.empty())
                break;
            st2.push(val);
        }
        while (!st2.empty())
        {
            st.push(st2.top());
            st2.pop();
        }
        return val;
    }

    int front()
    {
        stack<int> st2;
        int val;
        while (!st.empty())
        {
            val = st.top();
            st.pop();
            st2.push(val);
        }

        while (!st2.empty())
        {
            st.push(st2.top());
            st2.pop();
        }
        return val;
    }

    bool empty()
    {
        return st.empty();
    }
};

int main()
{
    my_queue q;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int val;
        cin >> val;
        q.push(val);
    }
    while (!q.empty())
    {
        cout << q.front() << " ";
        q.pop();
    }
}
