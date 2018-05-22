#include "LinkedList.c"
#include <stdio.h>
int main(void) {
	List L;
	L.append(1);
	L.append(2);
	printf("%d", L.remove());//1
	prinf("%d", L.remove());//2
	return 0;
}
