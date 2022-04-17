#include <iostream>

using namespace std;
struct A {
  A() {
    std::cout << "Constructor is called for " << this << std::endl;//то же самое что \n
  }
  ~A() {
    std::cout << "Destructor is called for" << this << '\n';
  }
};

int main()
{
  vector<A>;//динамический массив
  cout << "1" << endl;
  return 0;
}
