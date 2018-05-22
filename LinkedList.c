#include <stdlib.h>
typedef struct Node {
	int key;
	struct Node* next; //Next Node 
} Node;

typedef struct List {
	Node* head; //First Node
	Node* tail; //Last Node
	void (*append)(int,struct List); //Add a   new node
	int (*remove)(struct List); //Remove the Node at head
} List;

void List_append(int key,List l);
int List_remove(List l);

void List_append(int key,List l) {
	Node* new_Node = (Node*) malloc(sizeof(Node));
	new_Node->key = key;
	l.tail->next = new_Node;
	l.tail = new_Node;
}
int List_remove(List l) {
	int key = l.head->key;
	l.head = l.head->next;
	return key;
}

List setup_list() {
	List l;
	Node* first_node = (Node*) malloc(sizeof(Node));
	first_node->key = 0;
	l.head = first_node;
	l.tail = first_node;
	l.append = &List_append;
	l.remove = &List_remove;
	return l;
}
