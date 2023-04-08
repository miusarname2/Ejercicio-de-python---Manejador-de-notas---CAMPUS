#imports
import estudiantes,time,os,json

#Call database
#with open("Estudiantes.json","r") as archive :
#    std=json.load(archive)
#archive.close()


opcao = ""

#Function start...

def starts():
    estudiantes.Students.MenuPrincipal()
    opcao = int(input("\r"))
    if opcao == 1:
        print("Ingresa el nombre del estudiante a crear")
        nombreEstudiante = input()
        print("Ingresa el apellido del estudiante a crear")
        ApellidoE = input()
        print("Ingresa el correo del estudiante a crear")
        CorreoE = input()
        with open("Estudiantes.json","w")as archives:
            json.dump(estudiantes.Students.crearEstudiantes(
            estudiantes.Students, estudiantes.Students.dictEstudiantes, nombreEstudiante, ApellidoE, CorreoE
        ),archives)
        archives.close()
        
        print(
            "====================== Estudiante Creado ================================="
        )
        time.sleep(2.2)
        try:
            os.system("clear")
        except :
            os.system("cls")
        print(estudiantes.Students.mostrarEstudiantes(estudiantes.Students.dictEstudiantes))
    elif opcao == 2:
        print(estudiantes.Students.mostrarEstudiantes(estudiantes.Students.dictEstudiantes))
        time.sleep(2.2)
        try:
            os.system("clear")
        except :
            os.system("cls")
        print(estudiantes.Students.mostrarEstudiantes(estudiantes.Students.dictEstudiantes))
    elif opcao == 3:
        print(estudiantes.Students.mostrarEstudiantes(estudiantes.Students.dictEstudiantes))
        with open("Estudiantes.json","w")as archives:
            json.dump(estudiantes.Students.actualizarEstudiante(estudiantes.Students.dictEstudiantes),archives)
        archives.close()
        #print(estudiantes.Students.actualizarEstudiante(estudiantes.Students.dictEstudiantes))
        print(
            "====================== Estudiante Actualizado con Exito ================================="
        )
        time.sleep(2.2)
        try:
            os.system("clear")
        except :
            os.system("cls")
        print(estudiantes.Students.mostrarEstudiantes(estudiantes.Students.dictEstudiantes))
    elif opcao == 4:
        print("Ingrese el codigo del estudiante")
        codigoEstudiante = input()
        del estudiantes.Students.dictEstudiantes[codigoEstudiante]
        print(
            "====================== Estudiante Borrado con Exito ================================="
        )
        time.sleep(2.2)
        try:
            os.system("clear")
        except :
            os.system("cls")
        print(estudiantes.Students.mostrarEstudiantes(estudiantes.Students.dictEstudiantes))
    elif opcao == 5:
        print(
            "====================== Saliendo del programa ================================="
        )
        time.sleep(2.2)
        try:
            os.system("clear")
        except :
            os.system("cls")
        exit()
