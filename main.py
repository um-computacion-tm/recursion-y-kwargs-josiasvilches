#--------------------FIBONACCI-----------------------------
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
#------------------FACTORIALES-----------------------------
def factoriales (n):
    if n == 0:
        return 1
    return n * factoriales(n-1)

#-----------------DATABASE---------------------------------
database = {"persona1": {"primer_nombre": "Franco", "segundo_nombre": "José","apellido_1": "Vaccarezza", "apellido_2": "Toro"},
            "persona2": {"primer_nombre": "Nahuel", "segundo_nombre": "Ian", "apellido_1": "Galera"},
            "persona3": {"primer_nombre": "Alejandro", "apellido_1": "Sanchez", "apellido_2": "Castellino"},
            "persona4": {"primer_nombre": "Maximo", "segundo_nombre": "José", "apellido_1": "Lucentini", "apellido_2": "Sanchez"},
            "persona5": {"primer_nombre": "Franco", "apellido_1": "Aporta", "apellido_2": "Barzola"}, 
            "persona6": {"primer_nombre": "Josias", "segundo_nombre": "Lautaro", "apellido_1": "Vilches", "apellido_2": "Nuñez"}, 
            "persona7": {"primer_nombre": "Candela", "segundo_nombre": "Victoria", "apellido_1": "Gonzalez"}}

def buscar_datos(*args, **kwargs):
    args_set = set(args)
    for key, value in kwargs.items():
        values_set = set(value.values()) 
        if args_set == values_set:
            return key
    return None



# print(buscar_datos("Franco", "José", "Vaccarezza", "Toro", **database))  # Debería imprimir True
# print(buscar_datos("Nombre", "Inexistente", "Apellido", "Inexistente", **database))  # Debería imprimir False