from random import shufle
login = input('Login: ')
senha = input('Senha: ')
print('Bem vindo {}'.format(login))
print('site atualizado')
print('venha fazer suas compras')
p1 = 'maçã'
p2 = 'laranja'
p3 = 'abacaxi'
p4 = 'melancia'
produtos = [p1,p2,p3,p4]
print('Esta é a ordem dos produtos')
print(produtos)
print('Porem alguem andou baguncando e agora esta assim')
shufle(produtos)
print(produtos)