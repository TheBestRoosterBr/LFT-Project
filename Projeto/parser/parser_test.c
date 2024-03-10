#include <stdio.h>

void funcao(int[][1]);
void funcao2(int[][1]);
int funcao3(int);

int a[100];

union a{
    union b{

    };
};

struct id{
    int nossa;
    struct a{
        struct {
            int a;
        };
    };
};

int main()
{
    struct a b = {12, "Noosa"};
    int a = {12, 21};
    LABEL:

    goto LABEL;
}


int funcao(int a[][1])
{
    return a[1][0];
}