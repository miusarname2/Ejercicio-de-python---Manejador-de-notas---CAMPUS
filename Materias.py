# imports
import time,json

#DB Call
try:
    with open("Materias.json","r") as archive:
        MateriasDict= json.load(archive)
    archive.close()
except:
    MateriasDict = {}



# Master class
class Materias:
    def MenuPrincipal():
        print("\n\n")
        print(
            "1 - Crear un nueva Materia\n2 - Mostrar las materias\n3 - Actualizar una materia\n4 - Borra una materia\n5 - Sair del programa\n\nDigite a opcion permitida: "
        )


    def crearId(diccionario):
        id = list(diccionario.keys())[len(diccionario) - 1]
        return id + 1

    def crearMateria(subjects, nameSubjects):
        try:
            id = str(int(subjects.popitem()[0]) + 1)
        except:
            id = "1"
        subjects[id] = nameSubjects
        return subjects

    def mostrarMaterias(subjects):
        listSubjects = "\tCODIGO\tMateria\n"
        for subject in subjects:
            listSubjects += (
                "\t" + str(subject) + "\t" + subjects[subject] + "\t\t" + "\n"
            )
        return listSubjects

    def actualizarMateria(subjects):
        print("Ingrese el codigo de la material")
        codeSubject = input()
        print(
            "El nombre actual es :",
            subjects[codeSubject],
            "\n Desea cambiarlo?y/n",
        )
        changes = input()
        if changes == "y":
            subjects[codeSubject] = input("Ingrese el nuevo nombre de la materia: ")
            print(
                "====================== Nombre de la Materia Actualizado ================================="
            )
        elif changes == "n":
            print(
                "====================== Nombre de la Materia NO Actualizado ================================="
            )
        time.sleep(2.5)
        return subjects

    # database
    Materias = MateriasDict


class util:

    def Eliminar(codigo):
        del Materias.Materias[codigo]
# Starts
