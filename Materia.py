# imports
import os, time
import estudiantes, Materias,json

#DB Call

try:
    with open("Notas.json","r") as archive:
        ratingDict=json.load(archive)
    archive.close()
except:
    ratingDict={}



# Variables

print("\n\n")
opcao = ""

DictEstudiantes = estudiantes.Students.dictEstudiantes
DictMaterias = Materias.Materias.Materias
# classes
class notasProvider:
    def notasCalc(score,):
        temp_sum=[]
        for i in range(3):
            temp_sum.append(score[f"nota{i+1}"])
        temp_sum = int(sum(temp_sum)/len(temp_sum))
        return temp_sum

# Database
class Database:
    ratings = ratingDict
        
#class notas_provider2:
#    for i in range(len(Database.ratings)):
#        Database.ratings[i+1]["notaF"]=notasProvider.notasCalc(Database.ratings[i+1]) if Database.ratings[i+1]["nota1"] != "p" and Database.ratings[i+1]["nota2"] != "p" and Database.ratings[i+1]["nota3"] != "p" else "p"

    


# Starts
# a=list(Notas.ratings.keys())
#print(Database.ratings)

