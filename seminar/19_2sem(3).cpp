#include <iostream>

struct A {
  A() {
    std::cout << "Constructor is called for " << this << std::endl;//то же самое что \n
  }
  ~A() {
    std::cout << "Destructor is called for" << this << '\n';
  }
};

A *f()
{
  A *result = new A;
  return result;
}

int main()
{
  A *x = f();
  cout << "1" << (void *)x << endl;
  delete x;
  return 0;
}
