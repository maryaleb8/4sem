#include <cstdio>

struct A {
  A() {
    printf("Constructor is called for %p\n", this);//this это тот тип который сейчас
  }
  -A() {
    printf("Destructor is called for %p\n", this);
  }
};

int main()
{
  A x1, x2;
  puts("1");
  return 0;
}

//con is caller for 0x1, con is called for 0x2, 1, des 0x2, des0x1
//то есть уничтожаются в обратном порядке, вдруг одна ссылается на другую при создании
