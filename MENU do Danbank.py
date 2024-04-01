print('Bem-vindo ao MENU do Danbank. Selecione uma das opções:')
print('------------------------------')
print('(1) SALDO.')
print('(2) SAQUE.')
print('(3) CADASTRAR NOVA SENHA.')
print('(4) DESBLOQUEIO DE CARTÃO.')
print('(5) FALAR COM ATENDENTE.')
print('------------------------------')

saldo = 1000


r1 = input('Digite uma das opções do menu: ')

if r1 == '1':
    print(f'Seu saldo é exatamente: {saldo}.')
elif r1 == '2':
    saque_imediato = int(input(f'Seu saldo é {saldo}, quanto gostaria de sacar? '))
    saldo -= saque_imediato
    print(f'Certo,um momento que seu saque dinheiro está saindo........................Seu novo saldo é: {saldo}')
elif r1== '3':
    print('Ok! Um codigo foi enviado para seu email. Nele vocẽ vai ser direcionado para nosso aplicativo.')
elif r1== '4':
    print('Certo, vou está te passando as instruções para que você faça o desbloqueio.')
    print('Acesse o seu aplicativo, vá até as configurações e aperte a última opção. Ele irá pedir os dados do seu cartão.')
else:
    input('Certo. Enquanto nosso sistema procura um dos nossos especialista para te atender, digite em poucas palavras sua dúvida: ')
    #continua........