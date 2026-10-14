import sys
sys.setrecursionlimit (2000000)

def exponencial (base, expoente):
   if expoente ==0:
      return 1
   else:
      return base * exponencial (base, expoente - 1)


base = int(input("Digite um valor para a base: "))
expoente = int(input("Digite um valor para o expoente: "))


teste = exponencial (base, expoente)
print (teste)


