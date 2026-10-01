#include <stdio.h>

int buscaBinaria(int vetor[], int tamanho, int chave) {
    int inicio = 0;
    int fim = tamanho - 1;

    while (inicio <= fim) {
        int meio = inicio + (fim - inicio) / 2;

        if (vetor[meio] == chave) {
            return meio;
        }

        if (vetor[meio] > chave) {
            fim = meio - 1;
        } 

        else {
            inicio = meio + 1;
        }
    }

    return -1;
}

int main() {
    int vetor[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int tamanho = sizeof(vetor) / sizeof(vetor[0]);
    int chave = 23;

    int resultado = buscaBinaria(vetor, tamanho, chave);

    if (resultado != -1) {
        printf("Elemento encontrado no indice %d\n", resultado);
    } else {
        printf("Elemento nao encontrado no vetor\n");
    }

    return 0;
}
