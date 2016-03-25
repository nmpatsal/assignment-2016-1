import argparse

parser = argparse.ArgumentParser()
parser.add_argument("k", help="name of input file")
parser.add_argument("size_of_truss", help="size of truss",
                    type=int, default=3)

args = parser.parse_args()
lista = []
lex = {}
file = args.k
with open(file) as lista_file:
        for line in lista_file:
            part = line.rstrip()
            lista.append(part.split(" "))

truss = args.size_of_truss
for x in lista:
    neo = []
    for z in lista:
        if(x[0] == z[0]):
            neo.append(int(z[1]))
        elif(x[0] == z[1]):
            neo.append(int(z[0]))
    neo.sort()
    lex[int(x[0])] = neo
for x in lista:
    neo1 = []
    for z in lista:
        if(x[1] == z[1]):
            neo1.append(int(z[0]))
        elif(x[1] == z[0]):
            neo1.append(int(z[1]))
        neo1.sort()
        lex[int(x[1])] = neo1
no = 0
while no < len(lista):
    for x in lista:
        if(len(set(lex[int(x[0])]).intersection(lex[int(x[1])])) < truss - 2 ):
            lex[int(x[0])].remove(int(x[1]))
            lex[int(x[1])].remove(int(x[0]))
            lista.remove(x)
    no += 1
output = []
for x in lista:
    out = []
    tom = set(lex[int(x[0])]).intersection(lex[int(x[1])])
    for to in tom:
        out.append(int(to))
    out.append(int(x[0]))
    out.append(int(x[1]))
    out.sort()
    output.append(out)
for ou in output:
    while(output.count(ou) > 1):
        output.remove(ou)
        output.sort()
for user in output:
    print("(" + ", ".join( str(stoixeio) for stoixeio in user ) + ")" )
