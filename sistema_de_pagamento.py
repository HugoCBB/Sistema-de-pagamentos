# Sistema-de-pagamentos 
#Para o primeiro projeto em que me empenhei bastante, é basicamente um sistema de pagamentos. Ele abre no terminal 5 escolhas, dependendo da escolha do usuario o preço do produto final pode mudar. Além da escolha de produtos tempos a forma de pagamento que também ira mudar muito o valor quando escolhido.Segue codigo abaixo

from time import sleep
def dezporcent(d):
    calc = d * 0.1
    tot = d - calc
    return tot

def juros(d):
    calc = d * 0.2
    tot = d + calc   
    return tot

def cincoporcent(d):
    calc = d * 0.05
    tot = d - calc
    
    return tot

print('='*25)
print('CONCESIONARIA SIMAS TURBO')
print('='*25)
 
print('Qual carro voce quer comprar?')
print('[1]Honda Civic R$50.000')
print('[2]Astra 2.0 R$70.000')
print('[3]BMW X1 R$100.000')
print('[4]Porsche 911 R$1.000.000')
print('[5]Lamborguine Urus R$1.500.000')
esc = int(input())

print('PROCESSANDO...')
sleep(5)

#Atribuiçao de valores
if (esc == 1):
    c = 50000
elif (esc == 2):
    c = 70000
elif (esc == 3):
    c = 100000
elif (esc == 4):
    c = 1000000
else:
    c = 1500000
#Formas de pagamento
print('='*19)
print('Formas de pagamento')
print('='*19)
print('[1]Dinheiro ou PIX (10% de desconto)')
print('[2]Avista no cartão (5% de desconto)')
print('[3]6X no cartão')
print('[4]12X no cartão (20% de juros)')
fp = int(input())

print('PROCESSANDO SEU PEDIDO...')
sleep(3)
print('PROCESSANDO PAGAMENTO...')
sleep(3)
print('COMPRA APROVADA PARABENS!!')
print('-'*26)
if (fp == 1):
    dez = dezporcent(c)
    print('TOTAL A PAGAR:R${:.2f}'.format(dez))
elif (fp == 2):
    cinc = cincoporcent(c)
    print('TOTAL A PAGAR:R${:.2f}'.format(cinc))
elif (fp == 3):
    
    print('6X DE R${:.2f}\nTOTAL A PAGAR:R${:.2f}'.format(c/6,c))
else:
    jrs = juros(c)
    print('12X DE R${:.2f}\nTOTAL A PAGAR:R${:.2f}'.format(jrs/12,jrs))

