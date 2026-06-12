#Entrada del sistema
nombre_usuario=input("digita tu nombre: ")
correo_usuario=input("digita tu correo: ")
contraseña_usuario=input("digita tu contraseña: ")
ciudad_usuario=input("digita tu ciudad: ")
edad_usuario=int(input("digita tu edad: "))

CORREO_BD="cris@peta.com"
CONTRASEÑA_BD="123321"

if(correo_usuario==CORREO_BD and contraseña_usuario==CONTRASEÑA_BD):
    print("bienvenido")
else:
    print("que falla")