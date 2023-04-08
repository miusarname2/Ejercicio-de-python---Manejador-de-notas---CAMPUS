import executeE,MateriaExt,MatExecute


opcao = ""

while opcao != "0" or opcao != 0:
    print("Bienvenido al sistema de calificaciones de CAMPUS ¿Que accion deseas realizar hoy?\n1 <- Modificar Estudiantes...\n2 <-Modificar Notas\n3 <-Modificar Materias...")
    opcao = input()
    if opcao == "1":
        executeE.starts()
        #print("\n\n")
    elif opcao == "2":
        MatExecute.starts()
        #print("\n\n")
    elif opcao == "3":
        MateriaExt.starts()
        #print("\n\n")
    else:
        print("\n\n")

