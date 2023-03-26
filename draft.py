from IPv4Calculator import IPv4NetworkCalculator

numero_redes = input('Quantas Redes Você quer fazer? ')


ip = input('Digite o número IP: ')
prefixo = input('Caso tenha o Prefixo(ex. /24), Digite-o: ')
mascara = input('Caso tenha a Máscara(ex. 255.255.255.0), Digite-a: ')
if prefixo != '':
    ip = f'{ip}/{prefixo}'
    
if prefixo and mascara == '':
    print('Pelo menos a mascara ou prefixo devem ser enviados.')

print(ip)
teste = IPv4NetworkCalculator(ip, prefixo, mascara)
print(teste.get_all())