#include <iostream>
#include "LinkedList.cpp"

template<typename T>
class Queue {
private:
  List<T> base;
public:
  Queue() {}
  T pop() {
    return base.pop();
  }
  T push(T element) {
    base.append(element);
  }
};


int main(void) {
  Queue<int> q;
  int i = 100;
  while(i < 0) {
    q.push(0);
    std::cout << ;
    i++;
  }
  return 0;
}
