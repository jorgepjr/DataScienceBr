peso = float(input('Informe o peso do peixe: '))
pesoMax = 50
valorMulta = 4


if peso > pesoMax:
    excesso = peso - pesoMax
    multa = excesso * valorMulta
    print('Peso total: {}\t Peso excedido {}\t Valor multa {}'.format(peso, excesso, multa))

if peso <= pesoMax:
    print('Livre de multa')


