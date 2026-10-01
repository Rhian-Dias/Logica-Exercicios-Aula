function buscaSequencial(lista, alvo)
    for i = 1, #lista do
        if lista[i] == alvo then
            return i
        end
    end
    return nil
end

local minhaLista = {1,2,3,4}
local itemProcurado = 4

local resultado = buscaSequencial(minhaLista, itemProcurado)

if resultado then
    print("Elemento " .. itemProcurado .. " encontrado no índice: " .. resultado)
else
    print("Elemento " .. itemProcurado .. " não foi encontrado na lista.")
end
