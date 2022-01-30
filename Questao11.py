deposito = float(input('Valor depositado: '))
taxa = float(input('Taxa de juros: '))
mensal = float(input('Valor depositado mensalmente: '))

mes = 1
saldo = deposito

while mes <= 12:
    saldo = saldo + (saldo * (taxa / 100)) + mensal
    print(f"Mês {mes}: de R${saldo}.")
    mes = mes + 1
print(f'O juros em seu total foram de: R${saldo - deposito}')