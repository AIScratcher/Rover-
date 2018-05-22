#include <stdlib.h>
typedef struct Node {
	int key;
	struct Node* next;
} Node;

typedef struct List {
	int size;
	Node* head;
	Node* tail;
	void (*append)(int,struct List);
	int (*remove)(struct List);
} List;

void List_append(int key,List l);
int List_remove(List l);

void List_append(int key,List l) {
	Node new_Node;
	new_Node.key = key;
	l.tail->next = &new_Node;
	l.tail = &new_Node;
}
int List_remove(List l) {
	int key = l.head->key;
	l.head = &l.head->next;
	return key;
}

List setup_list() {
	List l;
	Node h;
	h.key = 0;
	h.next = 0;
	l.head = &h;
	l.tail = &h;
	return l;
}
