# Fet per: Frank Carreres Catalá

print("____________________________________________________________________")
print("")
print("                 * SISTEMA DE GESTIÓ DE VENDES *")
print("____________________________________________________________________")

print("")
print("                       · MENU D'OPCIONS:")
print("")
print("                   1. Introduïr un article nou")
print("")
print("                   2. Fer una venda")
print("")
print("                   3. Mostrar informació")
print("")
print("                   4. Esborrar tots els articles")
print("")
print("                   5. Eixir")

article = []
preu = []
quantitat = []

continuar = True
respostaContinuar = 0
acumImport = 0
importTotal = 0
nomIngressos = 0
quantIngressos = 0
artMesVenut = ""
quantMesVenut = 0


while continuar == True:

    print("")
    print("____________________________________________________________________")
    print("")
    opcioElegida = int(input("· Dis-me l'opció triada --> "))
    print("____________________________________________________________________")
    print("")

    if opcioElegida > 6 or opcioElegida < 1:

        print("- L'opcio triada no es valida, dis-me una altra opció.")

    elif opcioElegida == 1:

        article.append(str(input("- Dis-me el nom del article --> ")))
        print("")
        preu.append(float(input("- Dis-me el preu del article --> ")))
        print("")
        quantitat.append(0)

    elif opcioElegida == 2:

        nomArticle = str(input("· Dis-me el nom de l'article --> "))

        for posArticle in range (len(article)):

            if nomArticle == article[posArticle]:
                print("")
                qArticles = (int(input("- Quina quantitat d'aquest article vols? --> ")))
                quantitat[posArticle] += qArticles
                break

        else:
            print("- L' article no s'ha trobat...")

    elif opcioElegida == 3:

        print("     ARTICLE\t   " "QUANTITAT\t     " "PREU\t    " "IMPORT")



        for posArticle in range (len(article)):

            importTotal = preu[posArticle]*quantitat[posArticle]
            acumImport += importTotal

            print (f"     {article[posArticle].ljust(10)[:10]}\t       {quantitat[posArticle]}\t     {preu[posArticle]}€\t     {importTotal}€")
            print("")
            print("")
            print (f"    - TOTAL A PAGAR --> {acumImport}")

            if (quantitat[posArticle] > quantMesVenut):

                artMesVenut = article[posArticle]
                quantMesVenut = quantitat[posArticle]

            if (importTotal > quantIngressos):
                
                nomIngressos = article[posArticle]
                quantIngressos = importTotal

            print("")
            print(f"    - Article més venut: {artMesVenut} amb, {quantMesVenut} unitats")
            print(f"    - Article amb més ingresos: {nomIngressos} amb {quantIngressos} euros")
    
    elif opcioElegida == 4:

        print ("- La llista d'articles s'ha esborrat")

        article = []
        preu = []
        quantitat = []
        importTotal = []

    elif opcioElegida == 5:

        respostaContinuar = str(input("- Vols eixir del sistema de gestió (S,s/N,n) --> "))

        if respostaContinuar == "S" or respostaContinuar == "s":
            continuar = False
        
            