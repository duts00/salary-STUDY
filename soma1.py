print('=== tabuada de 1 a 100 ===') 

for numero in range(1, 101):
    print(f"\nTabuada do {numero}\n")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")