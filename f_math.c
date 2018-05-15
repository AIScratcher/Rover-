#include <stdio.h>


struct random {
        double x;//PI , can be every number;
	int a; //Coming from a very low number (-10) to (+10);
	int b; //Coming from a very high number (+500) to (-500); (Overflow is wanted)
};
struct random rnd;
void init_random() {
	rnd.x = 3.1415;
	rnd.a = -10;
	rnd.b = +500;
}
double random() {
	rnd.a += 33;
	rnd.b += 33;
	rnd.a *= -1;
	rnd.b *= -1;
	return rnd.a * rnd.x + rnd.b;
}
double random_inrange(double begin,double end) {
	return end-random() +begin;
}
