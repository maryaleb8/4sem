#include <iostream>

//std::cin, std::cout, std::cerr ввод вывод в си++б компилятор сам определяет тип
// лучше не смешивать си и си++ функции

//endl блочно завершают, \n строчно

//std это пространство имен, то есть куча констант и имен подгружаются
//1)можно using std::cout; using std::endl; отдельно вверху
//2)using namespace std;
//3)или перед каждым именем писать std::cout

struct A {
  A() {
    std::cout << "Constructor is called for " << this << std::endl;//то же самое что \n
  }
  ~A() {
    std::cout << "Destructor is called for" << this << '\n';
  }
};

void f()
{
  static A x;
  cout << "f()" << endl
}

int main()
{
  cout << "1" << endl;
  f(); //так как x создается внутри функции, но она статичная,
  //то создается в функции а уничтожается после выхода из main
  cout << "2" << endl;
  f();
  cout << "3" << endl;
  return 0;
}
