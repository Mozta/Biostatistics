#Media aritmética
import matplotlib.pyplot as plt

x = list()
y = list()
sum = 0

#Lee el archivo de texto
with open('dataset_anos.txt', 'rt') as reader:
    #Recorre el archivo de texto líne a línea
    for point in reader:
        #Separa la cadena en elementos y se toma el elemento en la posición 0 para guardarlo en x
        x.append(int(point.split(",")[0]))
        #Separa la cadena en elementos y se toma el elemento en la posición 1 para guardarlo en y
        y.append(float(point.split(",")[1]))
#Media
for i in x:
    sum =+ x[1]

media = (1/float(len(x))) * sum

print "El total es = " + str(sum)
print "La media es = " + str(media)
