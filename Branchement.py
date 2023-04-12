
def gestionOpcodeBranchement(opcode):

    # on vérifie que l'opcode est valide
    if opcode != "B":
        print("Erreur: opcode invalide")
        exit(0)

    return "1000"



def gestionOffsetBranchement(offset):
    # on vérifie que l'offset est valide (un nombre soit positif soit négatif)
    if not offset.isdigit() and not offset[1:].isdigit():
        print("Erreur: offset invalide")
        exit(0)

    offset = int(offset)

    # on vérifie que l'offset est dans la plage [-2^26, 2^26-1]
    if offset < -67108864 or offset > 67108863:
        print(
            "Erreur: offset invalide, doit être dans la plage [-2^26, 2^26-1]")
        exit(0)

        # on vérifie que l'offset est positif ou négatif
    if offset >= 0:
        signe = "0"
    else:
        signe = "1"
        offset = offset * -1

    # on convertit l'offset en binaire
    # print("offset: " + str(offset))
    offsetBinaire = bin(offset)[2:]
    # print("offsetBinaire: " + offsetBinaire)

    # on ajoute des 0 au début de l'offset pour que l'offset soit de 27 bits
    while len(offsetBinaire) < 27:
        offsetBinaire = "0" + offsetBinaire

        # on ajoute le signe
    offsetBinaire = signe + offsetBinaire

    # print("8 + 0 :"+offsetBinaire + "size: " + str(len(offsetBinaire)))

    # on ajoute les bits de l'offset

    return offsetBinaire




def convertiBranchementEnBinaire(ligne):

    if len(ligne) != 2:
        print("Erreur: une instruction branchement doit avoir 2 arguments")
        exit(0)

    # BRANCH_OPCODE OFFSET
    opcode = ligne[0]
    offset = ligne[1]

    opcode = gestionOpcodeBranchement(opcode)

    offset = gestionOffsetBranchement(offset)

    binaire = opcode + offset


    # vérifier que binaires est de 32 bits
    if len(binaire) != 32:
        print("Erreur: binaire invalide | taille: " +
              str(len(binaire)) + " | binaire: " + binaire)
        exit(0)

    return binaire