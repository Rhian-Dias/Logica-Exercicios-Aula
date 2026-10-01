function busca_binaria(lista, chave)
    local inicio = 1
    local fim = #lista

    while inicio <= fim do
        local meio = math.floor((inicio + fim) / 2)
        local chute = lista[meio]

        if chute == chave then
            return meio
        elseif chute > chave then
            fim = meio - 1
        else
            inicio = meio + 1
        end
    end

    return nil
end
