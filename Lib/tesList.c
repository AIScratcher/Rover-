#include "LinkedList.c"
#include <stdio.h>
int main(void) {
	List L;
	L.append(1,L);
	L.append(2,L);
	printf("%d", L.remove(L));//1
	printf("%d", L.remove(L));//2
	return 0;
}
