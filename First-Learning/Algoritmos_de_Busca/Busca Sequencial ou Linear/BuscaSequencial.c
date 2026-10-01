#include <stdio.h>

int buscaSequencial(int vet[], int tamanho, int valor) {
    for (int i = 0; i < tamanho; i++) {
        if (vet[i] == valor) {
            return i;
        }
    }
    return -1;
}

int main() {
    int numeros[] = {1,2,3,4};
    int tamanho = 4;
    int chave = 4;

    int resultado = buscaSequencial(numeros, tamanho, chave);

    printf("O resultado é: %d\n", resultado)

   }
