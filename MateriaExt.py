import Materia,json
import os
import time

#allMaterias = Materia.notas_provider2
DictNotas = Materia.Database.ratings

#index
print("\n\n")
opcao = ""


class manipNotas:
    def MenuPrincipal():
        print("\n\n")
        print(
            "1 - Crear una nueva materia\n2 - Mostrar las materias\n3 - Actualizar una materia\n4 - Borra una Materia\n5 - Sair del programa\n\nDigite a opcion permitida: "
        )
    def mostrarNotas(Notas):  # sourcery skip: instance-method-first-arg-name
        listaNota = "\tCODIGO\tIdEstudiante\tIdMateria\tnota1\tnota2\tnota3\n"
        for Nota in Notas:
            listaNota += (
                "\t"
                + str(Nota)
                + "\t"
                + str(Notas[Nota]["idEstudiantes"])
                + "\t\t"
                + str(Notas[Nota]["idMateria"])
                + "\t\t"
                + str(Notas[Nota]["nota1"])
                +"\t"
                +str(Notas[Nota]["nota2"])
                +"\t"
                +str((Notas[Nota]["nota3"]))
                + "\n"
            )
        return listaNota

    def crearNota(Notas, idEstudiante,IdMateria):
        # sourcery skip: instance-method-first-arg-name
        try:
            idNota = str(int(list(Notas.keys())[len(Notas) - 1]) + 1) or 1
        except:
            idNota = "1"
        Notas[idNota] = {
            "idEstudiantes": idEstudiante,  
            "idMateria": IdMateria,
            "nota1": "p",
            "nota2": "p",
            "nota3": "p",
        }
        return Notas
    
    def actualizarNotas(notas):
        print("Ingrese el id de la nota")
        codigodeNota = input()
        print(
            "La nota 1 es  :",
            notas[codigodeNota]["nota1"],
            "\n Desea cambiarlo?y/n",
        )
        changes = input()
        if changes == "y":
            notas[codigodeNota]["nota1"] = input(
                "Ingrese la nueva nota 1: "
            )
            print(
                "====================== Nota 1 Actualizada... ================================="
            )
        elif changes == "n":
            print(
                "====================== Nota 1 NO Actualizado ================================="
            )
            print(
                "La nota 2 es  :",
                notas[codigodeNota]["nota2"],
                "\n Desea cambiarlo?y/n",
            )
            changes = input()
            if changes == "y":
                notas[codigodeNota]["nota2"] = input(
                    "Ingrese la nueva nota 2: "
                )
                print(
                    "====================== Nota 2 Actualizada... ================================="
                )
            elif changes == "n":
                print(
                    "====================== Nota 2 NO Actualizado ================================="
                )
                print(
                "La nota 3 es  :",
                notas[codigodeNota]["nota3"],
                "\n Desea cambiarlo?y/n",
                )
                changes = input()
                if changes == "y":
                    notas[codigodeNota]["nota3"] = input(
                    "Ingrese la nueva nota 3: "
                )
                    print(
                    "====================== Nota 3 Actualizada... ================================="
                )
                elif changes == "n":
                    print(
                    "====================== Nota 3 NO Actualizado ================================="
                )
                
        time.sleep(2.5)
        return notas
    def mostrarNotasxMateria(idEstudiante):
            listaNota = "\tCODIGO\tIdMateria\tnota1\tnota2\tnota3\n"
            #for Nota in idEstudiante:
            #    listaNota += (
            #        "\t"
            #        + str(Nota)
            #        + "\t"
            #        + str(Notas[Nota]["idEstudiantes"])
            #        + "\t\t"
            #       + str(Notas[Nota]["idMateria"])
            #        + "\t\t"
            #        + str(Notas[Nota]["nota1"])
            #       +"\t"
            #        +str(Notas[Nota]["nota2"])
            #        +"\t"
            #        +str((Notas[Nota]["nota3"]))
            #       + "\n"
            #    )
            #return listaNota
        



def starts():
    manipNotas.MenuPrincipal()
    opcao = int(input("\r"))
    if opcao == 1:
        print("Ingresa el id del estudiante: ")
        idStudent = input()
        print("Ingresa el id del materia: ")
        idSubject = input()
        with open("Notas.json","w")as f:
            json.dump(manipNotas.crearNota(DictNotas,idStudent, idStudent),f)
        f.close()
        time.sleep(2.5)
        try:
            os.system("clear")
        except:
            os.system("cls")
        print(manipNotas.mostrarNotas(DictNotas),"\n")
    elif opcao == 2:
        #allMaterias
        print(manipNotas.mostrarNotas(DictNotas),"\n")
        time.sleep(2.5)
        try:
            os.system("clear")
        except :
            os.system("cls")
        print(manipNotas.mostrarNotas(DictNotas),"\n")
    elif opcao == 3:
        with open("Notas.json","w")as f:
            json.dump(manipNotas.actualizarNotas(DictNotas),f)
        f.close()
        time.sleep(2.5)
        try:
            os.system("clear")
        except :
            os.system("cls")
        print(manipNotas.mostrarNotas(DictNotas),"\n")
    elif opcao == 4:
        print("Ingrese el codigo de la nota")
        codigoNota = input()
        del DictNotas[codigoNota]
        with open("Notas.json","w")as f:
            json.dump(DictNotas,f)
        f.close()
        print(
            "====================== Nota Borrada con Exito ================================="
        )
        time.sleep(2.2)
        try:
            os.system("clear")
        except :
            os.system("cls")
        print(manipNotas.mostrarNotas(DictNotas),"\n")
    elif opcao == 5:
        print(
            "====================== Saliendo del programa ================================="
        )
        time.sleep(2.2)
        os.system("clear")
        exit()








