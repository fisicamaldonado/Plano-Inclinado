import math

masa = float(input("Ingrese masa del cuerpo (en Kg): "))
mu = float(input("Ingrese el coeficiente de rozamiento: "))
theta = float(input("¿Cuál es el ángulo del plano (en grados) respecto a la horizontal? "))
theta_rad=theta*math.pi/180

class Cuerpo:
	def __init__(self,masa,mu,theta_rad):
		self.P = round(masa*9.8,2)
		self.Px=round(self.P*math.sin(theta_rad),2)
		self.Py=round(self.P*math.cos(theta_rad),2)
		self.Fr=round(self.Py*mu,2)


c = Cuerpo(masa,mu,theta_rad)

print(f"El peso del cuerpo es {c.P} N")
print("Las componentes del peso son: ")
print(f"Px = {c.Px} N y Py = {c.Py} N")
print(f"La fuerza Normal tiene un valor de {c.Py} N")

if c.Fr >= c.Px:
	print(f"La fuerza de Rozamiento tiene un valor de {c.Px} N")
	print("El cuerpo está en equilibrio")
else:
	print(f"La fuerza de Rozamiento tiene un valor de {c.Fr} N")
	a = round((c.Px - c.Fr)/masa,2)
	print(f"El cuerpo acelera a razón de {a} m/s^2")
	