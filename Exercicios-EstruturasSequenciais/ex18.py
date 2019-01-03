arquivo = float(input('Informe o tamanho do arquivo em MB: '))
taxaTransferencia = float(input('Informe a velocidade do link em MB: '))

velocidade = (taxaTransferencia * 1024)/8
resultado = (arquivo * 1024)/velocidade
velMin = resultado/60

print('velocidade: {} Mbps'.format(velocidade))
print('Tempo de download : {} min'.format(round(velMin, 2)))


