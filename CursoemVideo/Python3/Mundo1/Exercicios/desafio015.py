km = float(input('Quantos Km percorridos ? '))
d = int(input('Quantos dias alugados ? '))
ckm = km * 0.15
cd = d * 60.0
ct = ckm + cd
print('Você alugou o carro por {} dias e percorreu {}km.'.format (d, km))
print('Você está sendo cobrado R${:.2f} pelo tempo alugado e R${:.2f} pelo km percorrido'.format(cd, ckm))
print('O total a ser pago é de R${:.2f}.'.format(ct))


