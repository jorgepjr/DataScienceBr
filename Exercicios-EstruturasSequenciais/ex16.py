
area = float(input('Informe o tamanho em M² da área: '))
# 1 litro cobre 3 metros quadrados  18 litros cobre 54 m²
# 1 lata de 18 litros custa R$ 80.00
# Informar a qtd de latas de tinta para pintar
# Total a pagar
latas = 0

cobre = 18 * 3
latas = area / cobre
litros = area / 3
totalPagar = latas * 80

print('É necessário: {} litros de tinta em uma área de {} M²'.format(litros, area))
print('Quantidade de latas: {}'.format(latas))
print('Total a pagar: {}'.format(totalPagar))








    






