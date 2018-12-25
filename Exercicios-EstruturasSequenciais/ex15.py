valorHora = float(input('Informe quanto ganha por hora: '))
horasMes = float(input('Informe quantas horas trabalhou no mês: '))

salarioBruto = horasMes * valorHora

sindicato = (salarioBruto * 5)/100
descInss = (salarioBruto * 11)/100
descIr = ((salarioBruto - descInss) * 8)/100

if salarioBruto <= 1693:
    descIr = 0
    salarioLiquido = salarioBruto - descInss - sindicato
    

elif salarioBruto > 1693:
    salarioLiquido = salarioBruto - descInss - descIr - sindicato

print('Salário Bruto: {}\n Descontos ########\n Sindicato(5%): {}\n INSS(11%): {}\n IR(8%): {}\n Salário Liquido: {}'
.format(salarioBruto, sindicato,descInss, descIr, salarioLiquido))


    
    

