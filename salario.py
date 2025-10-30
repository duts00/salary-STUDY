#| Código | Cargo      | Percentual |
#| ------ | ---------- | ---------- |
#| GER    | Gerente    | 10%        |
#| ENG    | Engenheiro | 20%        |
#| TEC    | Técnico    | 30%        |
# Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o cargo, conforme a tabela abaixo. Faça um programa que leia o salário e o código do cargo de um funcionário e calcule o novo salário. Se o cargo do funcionário não estiver na tabela, ele deverá então receber 40% de aumento. Mostre o salário antigo, o novo salário e a diferença

print('    === SALÁRIO DE CARGOS ===')
print('== GERENTE - ENGENHEIRO - TÉCNICO ==\n')

def salario():
    while True:
        cargo = input('Cargo do funcionário (GER/ENG/TEC): ').strip().upper()
        
        try:
            salario_atual = float(input("Salário R$: "))
            percentuais = {
                'GER': 0.10,  
                'ENG': 0.20,  
                'TEC': 0.30   
            }
            
            
            aumento_percentual = percentuais.get(cargo, 0.40)
            
            aumento = salario_atual * aumento_percentual
            novo_salario = salario_atual + aumento
            
            print(f'\nResultado do cálculo:')
            print(f'Salário antigo: R$ {salario_atual:.2f}')
            print(f'Aumento ({int(aumento_percentual*100)}%): R$ {aumento:.2f}')
            print(f'Salário final: R$ {novo_salario:.2f}')
            print(f'Diferença: R$ {novo_salario - salario_atual:.2f}\n')
            
            continuar = input('Calcular outro salário? (S/N): ').strip().upper()
            if continuar != 'S':
                break
                
        except ValueError:
            print('Por favor, digite um valor válido para o salário.')

salario()
