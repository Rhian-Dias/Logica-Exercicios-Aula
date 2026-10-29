#include <iostream>
#include <vector>

int buscaBinariaRecursiva(const std::vector<int>& arr, int esquerda, int direita, int alvo) {
    if (esquerda > direita) {
        return -1; 
    }

    int meio = esquerda + (direita - esquerda) / 2;

    if (arr[meio] == alvo) {
        return meio; 
    }

    if (arr[meio] > alvo) {
        return buscaBinariaRecursiva(arr, esquerda, meio - 1, alvo); 
    }

    return buscaBinariaRecursiva(arr, meio + 1, direita, alvo); 
}


int buscaBinaria(const std::vector<int>& arr, int alvo) {
    return buscaBinariaRecursiva(arr, 0, arr.size() - 1, alvo);
}

int main() {
    std::vector<int> dados = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int alvo = 23;

    int resultado = buscaBinaria(dados, alvo);

    if (resultado != -1) {
        std::cout << "Elemento " << alvo << " encontrado no índice: " << resultado << std::endl;
    } else {
        std::cout << "Elemento " << alvo << " não encontrado no vetor." << std::endl;
    }

    return 0;
}
