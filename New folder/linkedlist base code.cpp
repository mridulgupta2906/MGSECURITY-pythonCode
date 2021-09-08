/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

struct Node
{
    int data;
    struct Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
};


int main()
{
    int n;
	cin>>n;
    int data;
		cin>>data;
		struct Node *head = new Node(data);
		struct Node *tail = head;
		for (int i = 0; i < n-1; ++i)
		{
			cin>>data;
			tail->next = new Node(data);
			tail = tail->next;
		}
			cout<<"\n";
        struct Node* head2= head;
		while (head2 != NULL) { 
		cout << head2->data <<" "; 
		head2 = head2->next; 
	}  
	cout<<"\n";

    return 0;
}
