'''Escriba un bloque cualquiera de código en Python en donde
utilice 2 condicionales (if) anidados.'''

password = input("Ingrese la contraseña: ")

if (len(password) >= 8):
    print('Tu contraseña es larga')
    if(password == 'Laclaveessegura'):
        print('La contraseña es la correcta')
    else:
        print('La contraseña es incorrecta')
else:
    print('Tu contraseña es corta e insegura')



