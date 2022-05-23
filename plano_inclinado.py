import math
import sys
import os

os.system('clear') #Comenzamos limpiando la pantalla

#Usaremos 'try' y 'except' para evitar errores al ingresar los datos
try:
	masa = float(input("Ingrese masa del cuerpo (en Kg): "))
	mu = float(input("Ingrese el coeficiente de rozamiento: "))
	theta = float(input("¿Cuál es el ángulo del plano (en grados) respecto a la horizontal? "))
	theta_rad=theta*math.pi/180

except (ValueError, TypeError):
	print("Has ingresado un valor incorrecto")
	sys.exit(0)

#Definimos la clase 'Cuerpo' para instanciar el objeto que se coloca sobre el plano.
class Cuerpo:
	def __init__(self,masa,mu,theta_rad):
		self.P = round(masa*9.8,2)
		self.Px=round(self.P*math.sin(theta_rad),2)
		self.Py=round(self.P*math.cos(theta_rad),2)
		self.Fr=round(self.Py*mu,2)
		#Hemos definido todas las fuerzas que actúan sobre el cuerpo como atributos de esta clase.


c = Cuerpo(masa,mu,theta_rad)

#Imprimimos los valores de las fuerzas definidas como atributos
print(f"El peso del cuerpo es {c.P} N")
print("Las componentes del peso son: ")
print(f"Px = {c.Px} N y Py = {c.Py} N")
print(f"La fuerza Normal tiene un valor de {c.Py} N")


#Utilizamos el siguiente condicional para determinar si la componente del peso Px es mayor o no al rozamiento
# y por lo tanto saber si el cuerpo está en equilibro o bien acelera.
if c.Fr >= c.Px:
	print(f"La fuerza de Rozamiento tiene un valor de {c.Px} N")
	print("El cuerpo está en equilibrio")
else:
	print(f"La fuerza de Rozamiento tiene un valor de {c.Fr} N")
	a = round((c.Px - c.Fr)/masa,2)
	print(f"El cuerpo acelera a razón de {a} m/s^2")
	
