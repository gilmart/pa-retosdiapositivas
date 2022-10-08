#Crear una subrutina llamada "Login", que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el  nombre de usuario es "admin"
#y la contraseña es "admin123*". Ademas recibe el numero de intentos que se han intentado hacer login y si no se ha podido hacer login incremente este valor


def login(usuarioConsola, passwordConsola):
    usuario= "admin"
    password= "admin123*"
    fallidos=1
    while (usuarioConsola != usuario and passwordConsola !=password):
        print(f'intento fallido numero {fallidos} - intente nuevamente')
        usuarioConsola=input("Digite el usuario: ")
        passwordConsola=input("Digite password: ")
        fallidos=fallidos+1

    if(usuario==usuarioConsola and password==passwordConsola):
        print(f'verdadero!')

    return(usuario)


usuarioConsola=input("Digite el usuario: ")
passwordConsola=input("Digite password: ")
login(usuarioConsola,passwordConsola)
