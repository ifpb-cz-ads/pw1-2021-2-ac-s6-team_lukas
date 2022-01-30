
divida = float(input("Dívida: "))
taxa = float(input("Juros (Ex.: 3 para 3%): "))
pagamento = float(input("Pagamento mensal:"))

mes = 1
saldo = divida
jurosPago = 0

while saldo > pagamento:
    juros = saldo * taxa / 100
    saldo = saldo + juros - pagamento
    jurosPago = jurosPago + juros
    print(f"A dívida no mês {mes} é de R${saldo}.")
    mes = mes + 1
    
print(f"Para pagar uma dívida de R${divida}, a {taxa} % de juros,")
print(f"Serão necessários {mes - 1} meses, pagando um total de R${jurosPago} de juros.")
