import matplotlib.pyplot as plt
import pandas as p

inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(inventario)
plt.title("Elemento vs Unidades", fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Unidades"].values(),align="center")
plt.xlabel("Elemento")
plt.ylabel("Unidades")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("ElementovsUnidades.png")
plt.close()


inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(inventario)
plt.title("Elemento vs Viejo", fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Viejo"].values(),align="center")
plt.xlabel("Elemento")
plt.ylabel("Viejo")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("ElementovsViejo.png")
plt.close()


inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(inventario)
plt.title("Elemento vs Nuevos", fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Nuevos"].values(),align="center")
plt.xlabel("Elemento")
plt.ylabel("Nuevos")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("ElementovsNuevos.png")
plt.close()


ppg =p.read_csv("ppg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ppg["muestra"].values())
y = list(ppg["valor"].values())
plt.title("PPG-uV DE PACIENTE DIAGNOSTICADO")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("ppg.png")
print ("Observamos 9 picos")
plt.close()


labels = 'Casa', 'Hospitalizaion', 'UCI'
sizes = [85, 10, 5]
explode = (0, 0, 0.2)
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("% DE ESTUDIO")
plt.savefig("Grafico_Estudio.png")
plt.show()
