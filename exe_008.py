# *-* coding: utf-8 *-*

valor_hora = float(input("Informe o valor pago pela hora de trabalho: "))
quantidade_hora = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario = valor_hora * quantidade_hora

print("Valor da hora R$ {}, quantidade de horas trabalhadas no mês {}. "
      "Salário a receber R$ {}" .format(valor_hora, quantidade_hora, salario))