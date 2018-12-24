ganhoHora = float(input('Quanto você ganha por hora ?'))
horasMes = float(input('Quantas horas você trabalhou este mês ?'))

salTotal = ganhoHora * horasMes

print('Você ganha R${} h, e trabalhou {} h este mês, seu salário é de R${}'.format(ganhoHora, horasMes, salTotal))