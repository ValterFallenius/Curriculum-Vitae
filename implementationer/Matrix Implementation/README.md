# Matrix module

Grundläggande matris implementation i python3:

## metoder för Matrix():

### \_\_init\_\_: 
Skapa m x n-matriser som  är objekt i klassrm Matrix.

### \_\_get\_\_ och \_\_set\_\_:
Indexera matrisobjekt direkt med heltalslistor, alltså A[i, j]. Matrix följer python konventionen. Elementet högst upp till vänster har index [0, 0]. 

### \_\_add\_\_ och \_\_sub\_\_ :
Använd standard operatorer +/- för att addera och subtrahera matriser.

### \_\_mul\_\_ :
Använd operatorn * för att genomföra matrismultiplikation eller skalärmultiplikation. 

### \_\_iadd\_\_, \_\_isub\_\_ och  \_\_imul\_\_ :
Utöver det stödjer Matrix() assignments som +=, -= och *=. 

### \_\_str\_\_:
Returnerar matriser i snygga strängformat.

### \_\_eq\_\_ and \_\_ne\_\_:
Evaluera booleanska uttryck på objekten som A == B eller A != C.

### transpose():
Transposes the matrix.

### v1.angle_to(v2):
Returnerar vinkeln mellan två vektorer.
