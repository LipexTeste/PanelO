
import time
import os
import random
#dicionario que vai receber todos os dados
registrar = dict()

pergunta = ' '



#Menu do outro codigo, tive dor de cabeça e preferir assim
def mainq():
    menu()
    opcao_1 = int(input('\033[1;32mSua opção: \033[m'))
    if opcao_1 == 1 or opcao_1 == '01':
        logar()
    
    elif opcao_1 == 2 or opcao_1 == '02':
        Registrar()

    
    
    elif opcao_1 == 3 or opcao_1 == '03':
        time.sleep(0.5)
        print('\033[1;31m---------\033[0;0m')
        time.sleep(0.5)
        print('\033[1;32mSaindo... ')
        time.sleep(0.5)
        print('\033[1;31m----------\033[0;0m')
        exit()
    else:
        print()
        print('\033[1;31mOPÇÂO INVALIDA\033[m')
        mainq()


#menu esteticamente
def menu():
    time.sleep(0.5)
    print('''\033[1;35m
| __ )  ___ _ __ ___   __   _(_)_ __   __| | ___  
|  _ \ / _ \ '_ ` _ \  \ \ / / | '_ \ / _` |/ _ \ 
| |_) |  __/ | | | | |  \ V /| | | | | (_| | (_) |
|____/ \___|_| |_| |_|   \_/ |_|_| |_|\__,_|\___/ 
    \033[0;0m''')
    time.sleep(0.5)
    print('\033[1;31m-------------------------------------------------\033[0;0m')
    time.sleep(0.5)
    print('''
\033[1;35m[ 1 ]\033[m \033[1;32m<=\033[m \033[1;33mLogar\033[m
\033[1;35m[ 2 ]\033[m \033[1;32m<=\033[m \033[1;33mRegistrar\033[m
\033[1;35m[ 3 ]\033[m \033[1;32m<=\033[m \033[1;33mSAIR\033[m
    ''')



#estetica do menu de login
def menu_logar():
    os.system('clear')
    time.sleep(0.5)
    print('\033[1;31m-------------------------------------------------\033[0;0m')
    time.sleep(0.5)
    print('''
\033[1;35m[ 1 ]\033[m \033[1;32m<=\033[m \033[1;33mLogar\033[m
\033[1;35m[ 2 ]\033[m \033[1;32m<=\033[m \033[1;33mVoltar ao menu\033[m
    ''')
    time.sleep(0.5)
    print('\033[1;31m-------------------------------------------------\033[0;0m')








#estetica do menu de registrar
def menu_registrar():
    os.system('clear')
    time.sleep(0.5)
    print('''\033[1;35m
| __ )  ___ _ __ ___   __   _(_)_ __   __| | ___  
|  _ \ / _ \ '_ ` _ \  \ \ / / | '_ \ / _` |/ _ \ 
| |_) |  __/ | | | | |  \ V /| | | | | (_| | (_) |
|____/ \___|_| |_| |_|   \_/ |_|_| |_|\__,_|\___/ 
    \033[0;0m''')
    time.sleep(0.5)
    print('\033[1;31m-------------------------------------------------\033[0;0m')
    time.sleep(0.5)
    print('''
\033[1;35m[ 1 ]\033[m \033[1;32m<=\033[m \033[1;33mRegistrar\033[m
\033[1;35m[ 2 ]\033[m \033[1;32m<=\033[m \033[1;33mVoltar ao menu\033[m
    ''')
    time.sleep(0.5)
    print('\033[1;31m-------------------------------------------------\033[0;0m')




#função registrar um novo usuario
sessao = random.randint(0, 100)
tam = '12345678910123456789'
tam_user = '1234567891'
def Registrar():
    menu_registrar()
    opcao_registrar = int(input('\033[1;32mSua opção: \033[m'))
    if opcao_registrar == 1:
        while True:
            os.system('clear')
            print('\033[1;31m-------------------------------------------------\033[0;0m')
            registrar['usuario'] = str(input('\033[1;33mUsúario: '))
            registrar['senha'] = str(input('\033[1;33mSenha: '))
            if registrar['usuario'] == registrar['senha']:
                time.sleep(1)
                print('\033[1;31mUsúario e Senha iguais!')
                time.sleep(0.5)
                continue
            elif len(registrar['usuario']) > len(tam_user):
                time.sleep(1)
                print('\033[1;31mUsúario maior que 10 caracteres, TENTE NOVAMENTE!')
                time.sleep(0.5)
                continue
            elif len(registrar['senha']) > len(tam):
                time.sleep(1)
                print('\033[1;31mSenha maior que 20 caracteres, TENTE NOVAMENTE!')
            
            registrar['email'] = str(input('\033[1;33mEmail: '))
            if '@' not in registrar['email']:
                time.sleep(1)
                print('\033[1;31mDigite o email corretamente, ex: exemplo123@...')
                time.sleep(3)
                continue
            registrar['idade'] = str(input('\033[1;33mIdade: '))
            registrar['sexo'] = str(input('\033[1;33mSexo [M/F] > ')).strip().upper()[0]
            print()
            print(f'\033[1;32mSua chave de sessão é \033[1;35m{sessao}.\033[1;32m Use ela para conseguir logar!')
            print('\033[1;31m-------------------------------------------------\033[0;0m')
            pergunta = ''
            time.sleep(0.5)
            pergunta = str(input('\033[1;33mDeseja continuar cadastrando? \033[1;32mS\033[m|\033[1;31mN > ')).strip().upper()[0]
            if pergunta == 'S':
                print()
                print('\033[1;31m-------------------------------------------------\033[0;0m')
                time.sleep(0.5)
                print('\033[1;31mSistema de Re-Cadastramento ainda não disponivel\033[m')
                time.sleep(0.5)
                print('\033[1;32mSeu cadastro foi REGISTRADO!\033[m')
                time.sleep(0.5)
                print('\033[1;32mVoltando pro MENU PRINCIPAL...\033[m')
                print('\033[1;31m-------------------------------------------------\033[0;0m')
                print()
                mainq()
            if pergunta == 'N':
                print()
                time.sleep(0.5)
                print('\033[1;32mVoltando pro MENU PRINCIPAL...\033[m')
                print()
                mainq()
        time.sleep(0.5)
        print('\033[1;31m-------------------------------------------------\033[0;0m')
    if opcao_registrar == 2:
        mainq()
    else:
        print()
        time.sleep(2)
        print('\033[1;31mOPÇÂO INVALIDA\033[m')
        Registrar()   


#função que recebe o login dos usuarios cadastrados e autentica-os
def logar():
    menu_logar()
    opcao_logar = int(input('\033[1;32mSua opção: \033[m'))
    if opcao_logar == 1:
        os.system('clear')
        print('\033[1;31m-------------------------------------------------\033[0;0m')
        
        sesao = int(input('\033[1;33mCódigo de sessão: '))
        if sesao == sessao:
            usuario = str(input('\033[1;33mUsúario: '))
            senha = str(input('\033[1;33mSenha: '))
            while senha != registrar['senha']:
                senha = str(input('Senha incorreta. Tente novamente! '))
            if senha == registrar['senha']:
                print('\033[1;31m-------------------------------------------------\033[0;0m')
                print('\033[1;32mLOGIN EFETUADO COM EXITO')
                print('\033[1;32mSEUS DADOS SÂO:')
                print('\033[1;31m-------------------------------------------------\033[0;0m')
                for key, valores in registrar.items():
                    time.sleep(1)
                    if registrar['sexo'] == 'M':
                        registrar['sexo'] = 'Masculino'
                    elif registrar['sexo'] == 'F':
                        registrar['sexo'] = 'Feminino'
                    print(f'\033[1;33m{key} -> {valores}')
                print('\033[1;31m-------------------------------------------------\033[0;0m')
                mainq()
        else:
          
            print('\033[1;31mVocê não tem uma conta, REGISTRE-SE')
            mainq()
    elif opcao_logar == 2:
        mainq()
    else:
        print()
        time.sleep(2)
        print('\033[1;31mOPÇÂO INVALIDA\033[m')
        logar()
       

















