lista = ["ciro","luca"]

def menu ():
    print("scegli 0 per fermare il rpogramma")
    print("scegli 1 per aggiungiere elementi")
    print("scegli 2 per visualizzare elementi")
    print("scegli 3 per rimuovere elementi")
    print("scegli 4 per contare quanti elementi ci sono inlista")
    print("scegli 5 per svuotare\n")

def aggiungi ():
    elementi = int(input("quanti elementi vuoi inserire ? "))
    for i in range (elementi):
        x = input("inserirsci gli elementi: ")
        lista.append(x)

def visualizza ():
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")

def rimuovi ():
    visualizza()
    indice = int(input())
    lista.pop(indice -1)

def conta_elementi():
    print(len(lista))

def svuota():
    lista.clear()

while True:
    try:
        menu ()
        scelta = (int(input("scegli cosa fare ? \n")))
        if scelta == 0:
            break
        if scelta == 1:
            aggiungi()
        if scelta == 2:
            visualizza()
        if scelta == 3:
            rimuovi()
        if scelta == 4:
            conta_elementi()
        if scelta == 5:
            svuota()
    except:
        print("riprova, hai fatto qualcosa di sbagliato")