#include <iostream>

template <typename T>
class Node {
public:
  Node(T v = NULL) {
    this.value = v;
  }
private:
  T value;
  Node *next;
}
