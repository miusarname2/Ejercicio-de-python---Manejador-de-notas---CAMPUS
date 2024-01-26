# Ejercicio-de-python - Manejador-de-notas - CAMPUS
## En español

### 🧐 Contexto
Este es un ejercicio que se nos propuso realzar en el programa de <strong>CAMPUS{Proggrammer Land}</strong> que se realizo desde el  ≈27 de marzo

### 🤔 El problema
#### Version 0.1 : Se nos propuso que con funciones, diccionarios y listas(<- Esto ultimo era opcional) debiamos realizar un sistema de notas el cual debia estar " dividido " en 3 " secciones " :
<ul>
<li>Estudiantes</li>
<li>Materias</li>
<li>Notas</li>
</ul>
Los estudiantes debian cada estudiante las materias, las materias a su vez deben tener 3 notas:
<ol>
<li>Nota 1 ≈30% </li>
<li>Nota 2 ≈30% </li>
<li>Nota 3 ≈40% </li>
<li>Nota final (La suma de las 3 notas deacuerdo con sus porcentajes) </li>
</ol>


#### Version 1.0: Ahora solo cambiaba que solo debiamos usar diccionarios para almacenar los datos(Esto no lo tomeis mucho en cuenta pues no estoy seguro)
#### Version 1.2(Actual) :
<ul>
<li>Todos los estudiantes registrados inicialmente, deben registrarse en todas las materias (luego de este registro se pueden eliminar estudiantes, materias o realizar las demás operaciones con estos, lo cual determina que luego de este registro inicial, las materias pueden tener regisrados, diferentes cantidades de estudiantes)</li>
<li>Si una nota no se ha registrado debe guardarse como P (Pendiente)</li>
<li>Las 3 notas de los cortes NO se deben registrar al tiempo, las notas del segundo cortes sólo se podrán registrar hasta que todos los estudiantes de la materia seleccionada, tengan la nota del corte anterior, lo mismo sucede con el tercer corte</li>
<li>Luego de que todos los estudiantes de una materia tengan registrada la nota 1, no se podrán agregar más estudiantes a esta</li>
<li>Luego de registrada la nota final, no se podrán manipular las notas</li>
<li>Si hay notas registradas de una materia, esta no se puede eliminar</li>
<li><strong>OPCIONAL</strong>: Si se elimina un estudiante, se deben eliminar los registros de este en notas</li>
<li><strong>OPCIONAL</strong>: Si se elimina una materia se deben eliminar los registros de esta en notas</li>
<li>Los diccionarios deben guardarse en un archivo JSON (uno para cada diccionario)</li>
<li>La nota del primer y segundo corte, tienen una equivalencia del 30% cada una, la del tercero del 40%, para así determinar la nota final</li>
<li>Las notas se deben ver por materia o por estudiante, no todas en conjunto</li>

### Postdata:
😅 Aun no he complido con todos lo requerimiento de la version 1.2 pero ahi voy...

## English
 
 ### 🧐 Context
This is an exercise that was proposed to us to carry out in the <strong>CAMPUS{Proggrammer Land}</strong> program that was carried out since ≈March 27

### 🤔 El problema
#### Version 0.1 : We were proposed that with functions, dictionaries and lists (<- This last was optional) we should make a system of notes which should be "divided" into 3 "sections" :
<ul>
<li>Students</li>
<li>Subjects</li>
<li>Grades</li>
</ul>
The students had each student the subjects, the subjects in turn must have 3 notes:
<ol>
<li>Mark 1 ≈30% </li>
<li>Mark 2 ≈30% </li>
<li>Mark 3 ≈40% </li>
<li>Final note (The sum of the 3 notes according to their percentages) </li>
</ol>


#### Version 1.0: Now it only changes that we should only use dictionaries to store the data (Don't take this into account because I'm not sure)
#### Version 1.2(Current) :
<ul>
<li>All students initially registered must register in all subjects (after this registration students, subjects can be deleted or perform other operations with them, which determines that after this initial registration, the subjects can have registered, different amounts of students)</li>
<li>If a note has not been recorded it should be saved as P (Pending)</li>
<li>The 3 cut notes should NOT be registered at the same time, the notes of the second cut can only be registered until all the students of the selected subject have the note of the previous cut, the same happens with the third cut</li>
<li>After all the students of a subject have registered grade 1, no more students can be added to this subject.</li>
<li>After registering the final grade, the grades cannot be manipulated</li>
<li>If there are marks registered for a subject, it cannot be deleted</li>
<li><strong>OPTIONAL</strong>: If a student is deleted, the student's records must be deleted in notes</li>
<li><strong>OPTIONAL</strong>: If a subject is eliminated, its records must be eliminated in notes</li>
<li>Dictionaries must be saved in a JSON file (one for each dictionary)</li>
<li>The note of the first and second cut, have an equivalence of 30% each, that of the third of 40%, in order to determine the final note</li>
<li>Notes should be viewed by subject or by student, not all together</li>

### Postdata:
😅 I have not complied with all the requirements of version 1.2 yet but here I go...
 
</ul>

