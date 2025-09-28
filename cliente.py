import requests
import getpass

BASE = "http://127.0.0.1:5000"

def registrar_usuario():
    usuario = input("Usuario nuevo: ")
    contraseña = getpass.getpass("Contraseña: ")
    resp = requests.post(BASE + "/registro", json={"usuario": usuario, "contraseña": contraseña})
    print("Registro:", resp.json())

def login():
    usuario = input("Usuario: ")
    contraseña = getpass.getpass("Contraseña: ")
    resp = requests.post(BASE + "/login", json={"usuario": usuario, "contraseña": contraseña})
    print("Login:", resp.json())
    return usuario if resp.json().get("mensaje") == "Login exitoso" else None

def agregar_tarea(usuario):
    desc = input("Descripción de la tarea: ")
    resp = requests.post(BASE + "/agregar_tarea", json={"usuario": usuario, "descripcion": desc})
    print("Agregar tarea:", resp.json())

def listar_tareas(usuario):
    resp = requests.post(BASE + "/listar_tareas", json={"usuario": usuario})
    print("Tareas:", resp.json())

def main():
    usuario_actual = None
    while True:
        print("\n1) Registrar usuario")
        print("2) Login")
        print("3) Agregar tarea")
        print("4) Listar tareas")
        print("5) Salir")
        opcion = input("> ")
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            usuario_actual = login()
        elif opcion == "3":
            if usuario_actual:
                agregar_tarea(usuario_actual)
            else:
                print("Debes iniciar sesión primero.")
        elif opcion == "4":
            if usuario_actual:
                listar_tareas(usuario_actual)
            else:
                print("Debes iniciar sesión primero.")
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()