# 🏋️ Nara Fit

Um sistema simples de gerenciamento de alunos para academias desenvolvido em **Python** utilizando apenas recursos nativos da linguagem.

O programa permite cadastrar alunos, calcular automaticamente o **IMC (Índice de Massa Corporal)**, classificar o estado físico de cada pessoa e visualizar estatísticas gerais através de um menu interativo no terminal.

---

## ✨ Funcionalidades

- ✅ Cadastro de alunos
- ✅ Validação de entradas numéricas
- ✅ Cálculo automático do IMC
- ✅ Classificação do IMC
  - Abaixo do peso
  - Peso Normal
  - Sobrepeso
  - Obeso
- ✅ Listagem completa dos alunos cadastrados
- ✅ Estatísticas da academia
  - Média de idade
  - Alunos mais novos
  - Alunos mais velhos
  - Quantidade de alunos por categoria de IMC

---

## 📸 Demonstração

```text
1 - Deseja cadastrar um usuário?
2 - Consultar os usuários e valores?
3 - Consultar estatísticas?
4 - Sair

Escolha a opção:
```

Após o cadastro:

```text
1° - João | 20 anos | 72Kg | 1.75m
IMC: 23.51 Kg/m²
Status: Peso Normal
```

---

## 🧮 Como o IMC é calculado

O sistema utiliza a fórmula padrão:

```text
IMC = Peso / Altura²
```

Tabela utilizada:

| IMC | Classificação |
|------|---------------|
| Menor que 18.5 | Abaixo do peso |
| 18.5 até 24.9 | Peso Normal |
| 25 até 29.9 | Sobrepeso |
| 30 ou mais | Obeso |

---

## 🛠️ Tecnologias

- Python 3

Nenhuma biblioteca externa é necessária.

---
