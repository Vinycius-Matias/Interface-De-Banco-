# 💰 Sistema de Gerenciamento de Conta Bancária

Programa em Python que simula operações básicas de uma conta bancária: criação de conta, depósito, saque e consulta de saldo, via menu interativo no terminal.

## 📋 Descrição

O sistema inicia solicitando um saldo inicial para criar a conta. Em seguida, exibe um menu onde o usuário pode realizar operações financeiras até optar por encerrar o programa.

## ⚙️ Funcionalidades

- **Criar conta**: define o saldo inicial (não permite valores negativos)
- **Depositar**: adiciona um valor positivo ao saldo
- **Sacar**: subtrai um valor do saldo, verificando saldo insuficiente
- **Consultar saldo**: exibe o saldo atual formatado
- **Validação de entrada**: trata valores inválidos (não numéricos) sem quebrar o programa

## 🚀 Como executar

### Pré-requisitos
- [Python 3.x](https://www.python.org/downloads/) instalado

### Passos

\`\`\`bash
# Clone o repositório
git clone https://github.com/seu-usuario/sistema-conta-bancaria.git

# Acesse a pasta do projeto
cd sistema-conta-bancaria

# Execute o programa
python conta_bancaria.py
\`\`\`

## 🖥️ Exemplo de uso

\`\`\`
Digite o saldo inicial da conta: R$ 100
Conta criada com sucesso!

====== MENU ======
1 - Depositar
2 - Sacar
3 - Consultar saldo
4 - Encerrar programa
Escolha uma opção: 1
Digite o valor do depósito: R$ 50
Depósito realizado com sucesso!

====== MENU ======
1 - Depositar
2 - Sacar
3 - Consultar saldo
4 - Encerrar programa
Escolha uma opção: 3
Saldo atual: R$ 150.00
\`\`\`

## 🛠️ Tecnologias utilizadas

- Python 3 (sem bibliotecas externas)



## 👤 Autor

Desenvolvido por Vinycius 
