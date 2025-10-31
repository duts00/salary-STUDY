# Projetos de Exercícios em Python

> Projetos simples de Python para prática de lógica, operações matemáticas e estruturas de repetição. Desenvolvidos para aprendizado e testes educativos.

---

## 1. `salario.py`

### Objetivo

Calcular o **novo salário de um funcionário** com base no cargo e percentual de aumento definido pela empresa.

### Funcionamento

* O usuário informa o cargo (`GER`, `ENG`, `TEC`) e o salário atual.
* O programa aplica o aumento correspondente:

  * GER: 10%
  * ENG: 20%
  * TEC: 30%
  * Outros cargos: 40%
* Exibe:

  * Salário antigo
  * Valor do aumento
  * Novo salário
  * Diferença

### Execução

```bash
python3 salario.py
```

### Observações

* Valida entrada de salário (não permite texto ou valores inválidos)
* Permite calcular múltiplos salários sem reiniciar o programa

---

## 2. `soma1.py`

### Objetivo

Gerar a **tabuada de 1 a 100**.

### Funcionamento

* Loop de 1 a 100
* Para cada número, gera a tabuada de 1 a 10
* Exibe de forma organizada

### Execução

```bash
python3 soma1.py
```

---

## 3. `soma2.py`

### Objetivo

Gerar a **tabuada de um número específico** fornecido pelo usuário.

### Funcionamento

* Usuário digita um número
* Programa imprime a tabuada do número de 1 a 10
* Exibe linha separadora e mensagem de fim

### Execução

```bash
python3 soma2.py
```

---

## Conceitos praticados

* Estruturas de repetição (`for`, `while`)
* Estruturas condicionais (`if`, `else`)
* Dicionários e listas (`dict`, `list`)
* Entrada e saída de dados (`input()`, `print()`)
* Formatação de strings (`f-strings`)
* Validação de entradas

---

---

## Como contribuir

1. Faça um fork do repositório.
2. Crie uma branch para sua alteração: `git checkout -b feat/nova-funcionalidade`
3. Faça commits claros e objetivos.
4. Abra um Pull Request explicando o que foi alterado.

---

## Nota final

Esses scripts são de caráter **educacional**, destinados à prática de lógica, Python e manipulação de dados simples.
