import test_utilidades
import time
#Parte principal do codigo "menu"
def mainq():
    test_utilidades.menu()
    opcao_1 = int(input('\033[1;32mSua opção: \033[m'))
    if opcao_1 == 1 or opcao_1 == '01':
        test_utilidades.logar()
    elif opcao_1 == 2 or opcao_1 == '02':
        test_utilidades.Registrar()
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

mainq()