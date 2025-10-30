print('=== tabuada do 1 a 10  ===')


numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\nTabuada do {numero}\n")
print('-'*20)
for tabuada in range(1, 11):
    print(f"{numero} x {tabuada} = {numero * tabuada}")

print("Fim da tabuada !" )
print('-'*20)



