# Per ora ci siamo limitati a trattare dati in input presi da linea di comando, ma naturalmente è possibile elaborare
# dati presi da file presenti sul filesystem.


# leggere il contenuto di un file da python è semplicissimo:

f = open("demofile.txt", "r")
print(f.read())

# open è una funzione che prende come parametro il path del file (percorso) e la modalità di lettura
# la funzione read legge il file per intero e lo restituisce come stringa

# è possibile anche leggere il file riga per riga

f = open("demofile.txt", "r")
for x in f:
  print(x)


# terminata l'elaborazione del file è necessario chiuderne l'accesso con la funzione

f.close()

# per semplicità è anche possibile usare la keyword `with` che ci da accesso al file e lo chiude quando finisce il suo scope

with open('readme.txt', 'w') as f:
    f.read()

# la scrittura è altrettanto semplice
lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')


# esistono anche altre funzioni che rendono la scrittura/lettura lievemente più comoda, come readlines() e writelines() che lavorano con liste di stringhe

# ecco degli esempi

lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    f.writelines(lines)

lines = []
with open('readme.txt', 'r') as f:
    lines = f.readlines()


# --------------------------------------------------------------------

# Alcuni file di testo sono codificati in modo da essere facilmente trattati da linguaggi di programmazione sia in input che output 
# questo formato si chiama JSON (https://www.json.org/json-en.html)
# nel quale dizionari, liste, interi e stringhe sono facilmente codificati come testo
# in python è prima di tutto necessario importare il modulo json

import json

# È possibile lavorare con json sia a partire da stringhe che da file. Se lavoriamo con stringhe possiamo:

my_json_string = '{"name": "Bob", "languages": ["Python", "Java"]}'
now_its_an_object = json.loads(my_json_string) # converte una stringa in formato json in un oggetto python classico

# oppure, all'inverso

person_dict = {'name': 'Bob', 'age': 12, 'children': None }
person_json = json.dumps(person_dict) #converte un oggetto di python in un json equivalente



ev al 
 
# https://www.programiz.com/python-programming/json

