def executa(comandos, locks, letraLocks):
    global countits
    for i in range(len(comandos)):
        if i not in commits:
            linha = comandos[i].split(":")
            linha = linha[1].split(",")
            lul = linha[len(linha)-1].split("\n")
            linha[len(linha)-1] = lul[0]


            if contador.count(i) < len(linha):
                rw = linha[contador.count(i)].split("(")
                rw = rw[0].split(" ")
                rw = rw[1]

                linha = linha[contador.count(i)].split(",")
                letra = linha[0].split("(")
                letra = letra[1].split(")")
                letra = letra[0]

                if letra not in letraLocks:
                    print("T%d: %s" % (i + 1, linha[0]))
                    if rw == 'w':
                        letraLocks.append(letra)
                        locks.append(str(i)+letra+"w")
                        letraRwLocks.append(letra+"w")
                        contador.append(i)

                    elif rw == 'r':
                        letraLocks.append(letra)
                        locks.append(str(i)+letra+"r")
                        letraRwLocks.append(letra+"r")
                        contador.append(i)


                elif rw == 'w':
                    locks.append(str(i) + letra + "w")
                    letraRwLocks.append(letra+"w")

                elif rw == 'r':
                    if letra+"w" not in letraRwLocks:
                        print("T%d: %s" % (i + 1, linha[0]))
                        contador.append(i)



            elif contador.count(i) == len(linha):
                commits.append(i)
                print("T%d: commit" % (i + 1))
                unlocks(linha, locks)
                countits = countits + 1










def unlocks(linha, locks):
    for w in range(len(letraLocks)-1):

        if str(countits) + letraLocks[w] + "w" in locks:
            aux = str(countits) + letraLocks[w] + "w"
            locks.remove(aux)
            letraLocks.remove(letraLocks[w])

        if str(countits) + letraLocks[w] + "r" in locks:
            aux = str(countits) + letraLocks[w] + "r"
            locks.remove(aux)
            letraLocks.remove(letraLocks[w])









ler = open("entrada.txt", "r")
comandos = ler.readlines()
ler.close()

print("Lista de comandos: %s" % comandos)

transac = len(comandos)
print("\nNumero de Transacoes: %d" % (transac))
print("\n")

locks = []
letraLocks = []
letraRwLocks = []
contador = []
commits = []
countits = 0
while len(commits) != len(comandos):
    executa(comandos, locks, letraLocks)









