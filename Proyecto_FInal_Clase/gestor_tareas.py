import os

runProgram = True
todoList = []

# Funcion para mostrar las opciones del menu
def showMenuOption():
    print("Por favor seleccione una opcion:")
    print("")
    print("1. Crear una tarea")
    print("2. Marcar como realizada una tarea")
    print("3. Borrar una tarea")
    print("4. Salir")

def showTodoList():
    global todoList
    print("")
    print("")
    print("***************************************")
    for todo in todoList:
        print(f"{todoList.index(todo) + 1}. {todo}")
    print("***************************************")
    print()
    print()

# Funcion para guardar las tareas en la variable "todolist"
def createTodo():
    os.system("clear")
    global todoList
    print("Crear una nueva tarea")
    todo = input("Por favor ingrese el nombre de la tarea: ")
    todoList.append(todo)
    showTodoList()

# Funcion para marcar una tarea como ya realizada
def updateTodo():
    os.system("clear")
    global todoList
    print("Actualizar una tarea")
    todoId = int(input("Ingrese el numero de la tarea que quiere marcar como hecha: "))
    todoList[todoId - 1] = todoList[todoId - 1] + " ✅"
    showTodoList()

def deleteTodo():
    os.system("clear")
    global todoList
    print("Borrar una tarea")
    todoId = int(input("Ingrese el nummero de la tarea que quiere borrar: "))
    del todoList[todoId -1]
    showTodoList()

# Mostrar la lista de tareas
    


# Funcion principal
def main():
    global runProgram
    print("====================================")
    print(".: WELCOME TO A PYTHON TO DO LIST :.")
    print("====================================")

    while runProgram:
        showMenuOption() # Aqui invocamos a la funcion para mostrar las opciones del menu
        option = int(input("Ingrese el numero de opcion: "))

        match option:
            case 1:
                createTodo()
            case 2:
                updateTodo()
            case 3:
                deleteTodo()
            case 4:
                print("Hasta luego !!")
                runProgram = False
            case _:
                print("Opcion no reconocida. Ingrese una opcion valida")
            

if __name__ == "__main__":
    main()


