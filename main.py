from Director import Director
from Gerente import Gerente
from JefeArea import JefeArea

Superior = Director()

Superior.set_nombre_person("Angel")
Superior.set_apellido_person("Sepulveda")
Superior.set_edad_person(44)

Superior.setPuesto("Director")
Superior.setTurno("matutino")
Superior.setSueldo(85000)

Superior.set_nombre_area("Administrativa")
Superior.set_presupuesto(500000.00)
Superior.set_nombre_departamento("Administrativa general")
Superior.set_no_empleados(52)

Superior.setRegion("puebla")
Superior.setPresupuesto_asignado(120000)



jefe = JefeArea()


jefe.set_nombre_person("Raul")
jefe.set_apellido_person("Jimenez")
jefe.set_edad_person(52)

jefe.setPuesto("Jefe de area")
jefe.setTurno("mañana")
jefe.setSueldo(65000)

jefe.set_nombre_area("Administrativa")
jefe.set_presupuesto(150000)
jefe.set_nombre_departamento("Administrativa general")
jefe.set_no_empleados(27)

jefe.set_objetivo_area("mejorar el ambiente laboral")




subjefe = Gerente()

subjefe.set_objetivo_estrategico("llevar a esta empresa un buen nivel para que lo asciendan")

subjefe.set_nombre_person("Julion")
subjefe.set_apellido_person("Alvarez")
subjefe.set_edad_person(25)
#________________________________________
subjefe.setPuesto("Gerente")
subjefe.setTurno("matutino")
subjefe.setSueldo(58000)
#________________________________________
subjefe.set_nombre_area("Administrativa")
subjefe.set_presupuesto(200000)
subjefe.set_nombre_departamento("Administrativa general")
subjefe.set_no_empleados(32)
#___________________________________________
subjefe.set_objetivo_estrategico("Que los trabajadores entreguen un producto de calidad")


#_____________ Metodos____________________

print("Informacion de empleados")

print("\n")
Superior.mostrar_informacion_empleado()
print("\n")
jefe.mostrar_informacion_empleado()
print("\n")
subjefe.mostrar_informacion_empleado()
print("\n")

print("informacion por areas")

print("\n")
Superior.mostrar_informacion_area()
print("\n")
jefe.mostrar_informacion_area()
print("\n")
subjefe.mostrar_informacion_area()