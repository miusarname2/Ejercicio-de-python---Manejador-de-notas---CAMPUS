import time, os,json


#Call of database

try:
    with open("Estudiantes.json","r+") as archive :
        estudiantesDict=json.load(archive)
    archive.close()
except:
    estudiantesDict = {}


# Master class
class Students:
    def MenuPrincipal():
        print("\n\n")
        print(
            "1 - Crear un nuevo estudiantes\n2 - Mostrar los estudiantes\n3 - Actualizar un estudiante\n4 - Borra un estudiante\n5 - Sair del programa\n\nDigite a opcion permitida: "
        )

    def crearId(diccionario):
        id = list(diccionario.keys())[len(diccionario) - 1]
        return id + 1

    def crearEstudiantes(self, Estudiantes, nombreEstudiante, Apellido, Correo):
        try:
            id = str(int(list(Estudiantes.keys())[len(Estudiantes) - 1]) + 1)
        except:
            id="1"
        Estudiantes[id] = {
            "nomEstudiante": nombreEstudiante,
            "apellido": Apellido,
            "Correo": Correo,
        }
        return Estudiantes

    def mostrarEstudiantes(estudiantes):
        listaEstudiante = "\tCODIGO\tEstudiante\tApellido\tCorreo\n"
        for estudiante in estudiantes:
            listaEstudiante += (
                "\t"
                + str(estudiante)
                + "\t"
                + estudiantes[estudiante]["nomEstudiante"]
                + "\t\t"
                + estudiantes[estudiante]["apellido"]
                + "\t\t"
                + estudiantes[estudiante]["Correo"]
                + "\n"
            )
        return listaEstudiante

    def actualizarEstudiante(estudiantes):
        print("Ingrese el codigo del estudiante")
        codigoEstudiante = input()
        print(
            "El nombre actual es :",
            estudiantes[codigoEstudiante]["nomEstudiante"],
            "\n Desea cambiarlo?y/n",
        )
        changes = input()
        if changes == "y":
            estudiantes[codigoEstudiante]["nomEstudiante"] = input(
                "Ingrese el nuevo nombre del estudiante: "
            )
            print(
                "====================== Nombre del Estudiante Actualizado ================================="
            )
        elif changes == "n":
            print(
                "====================== Nombre del Estudiante NO Actualizado ================================="
            )
        print(
            "El apellido actual es :",
            estudiantes[codigoEstudiante]["apellido"],
            "\n Desea cambiarlo?y/n",
        )
        changes = input()
        if changes == "y":
            estudiantes[codigoEstudiante]["apellido"] = input(
                "Ingrese el nuevo apellido del estudiante: "
            )
            print(
                "====================== Apellido del Estudiante Actualizado ================================="
            )
        elif changes == "n":
            print(
                "====================== Apellido del Estudiante NO Actualizado ================================="
            )
        print(
            "El correo actual es :",
            estudiantes[codigoEstudiante]["Correo"],
            "\n Desea cambiarlo?y/n",
        )
        changes = input()
        if changes == "y":
            estudiantes[codigoEstudiante]["Correo"] = input(
                "Ingrese el nuevo correo del estudiante: "
            )
            print(
                "====================== Correo del Estudiante Actualizado ================================="
            )
        elif changes == "n":
            print(
                "====================== Correo del Estudiante NO Actualizado ================================="
            )
        return estudiantes

        time.sleep(2.5)

    #   data

    dictEstudiantes = estudiantesDict
