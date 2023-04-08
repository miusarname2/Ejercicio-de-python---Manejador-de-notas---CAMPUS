#Imports
import os,time,Materias,json

#Flag...
opcao = ""

#Function Starts....
def starts():
    #print(Materias.Materias.mostrarMaterias(Materias))
    Materias.Materias.MenuPrincipal()
    opcao = int(input("\r"))
    if opcao == 1:
        print("Ingresa el nombre del materia a crear")
        nameSubject = input()
        with open("Materias.json","w") as archive:
            json.dump(Materias.Materias.crearMateria(Materias.Materias.Materias, nameSubject), archive)
        print(
            "====================== Materia Creada ================================="
        )
        time.sleep(2.2)
        try:
            os.system("clear")
        except :
            os.system("cls")
        print(Materias.Materias.mostrarMaterias(Materias.Materias.Materias))
    elif opcao == 2:
        print(Materias.Materias.mostrarMaterias(Materias.Materias.Materias))
        time.sleep(2.2)
        try:
            os.system("clear")
        except :
            os.system("cls")
        print(Materias.Materias.mostrarMaterias(Materias.Materias.Materias))
    elif opcao == 3:
        print(Materias.Materias.mostrarMaterias(Materias.Materias.Materias))
        with open("Materias.json","w") as archive:
            json.dump(Materias.Materias.actualizarMateria(Materias.Materias.Materias), archive)
        print(
            "====================== Materia Actualizada con Exito ================================="
        )
        time.sleep(2.2)
        try:
            os.system("clear")
        except :
            os.system("cls")
        print(Materias.Materias.mostrarMaterias(Materias.Materias.Materias))
    elif opcao == 4:
        print("Ingrese el codigo de la materia")
        codigoEstudiante = input()
        del Materias.Materias.Materias[codigoEstudiante]
        print(
            "====================== Materia Borrada con Exito ================================="
        )
        time.sleep(2.2)
        try:
            os.system("clear")
        except :
            os.system("cls")
        #print(Materias.Materias.mostrarMaterias(Materias))
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
