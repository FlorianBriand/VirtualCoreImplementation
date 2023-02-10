

def verifiSiFichierExiste(nomFichier):
    try:
        fichier = open(nomFichier, "r")
        fichier.close()
        return True
    except:
        return False

        # Lit le fichier et retourne une liste de lignes


def lireFichier(nomFichier):
    fichier = open(nomFichier, "r")
    lignes = fichier.readlines()
    fichier.close()
    return lignes

    # Ecrit dans le fichier


def convertiAssembleurEnBinaire(lignes):
    for ligne in lignes:
        convertiLigneEnBinaire(ligne)


# An instruction is 32 bit wide, the 31st is the most significant bit.
# The instruction encoding must be organized as follow:
# Bits 28 to 31: Branch Condition Code (BCC)
# Bits 25 to 27: always set to 0
# Bit 24: Immediate Value (IV) flag
# Bits 20 to 23: Operation Code (opcode)
# Bits 16 to 19: First Operand (ope1)
# Bits 12 to 15: Second Operand (ope2)
# Bits 8 to 11: Destination Register (dest)
# Bits 0 to 7: Immediate Value (IV)

# The different values for the BCC are:
# Value Description Code
# 0x8 Unconditional branch B
# 0x9 Branch if equal BEQ
# 0xa Branch if not equal BNE
# 0xb Branch if lower or equal BLE
# 0xc Branch if greater or equal BGE
# 0xd Branch if lower BL
# 0xe Branch if greater BG

# 0x0 Logical AND AND dest = ope1 and ope2
# 0x1 Logical OR ORR dest = ope1 or ope2
# 0x2 Logical XOR EOR dest = ope1 xor ope2
# 0x3 Addition ADD dest = ope1 + ope2
# 0x4 Addition with carry ADC dest = ope1 + ope2 + carry
# 0x5 Comparison CMP See section on CMP (2.5.5)
# 0x6 Subtraction SUB dest = ope1 − ope2
# 0x7 Subtraction with carry SBC dest = ope1 − ope2 + carry − 1
# 0x8 Move data MOV dest = ope2
# 0x9 Logical left shift LSH dest = ope1 << ope2
# 0xa Logical right shift RSH dest = ope1 >> ope2

def gestionOpcodeInstruction(opcode):
    # on vérifie que l'opcode est valide
    if opcode != "AND" and opcode != "ORR" and opcode != "EOR" and opcode != "ADD" and opcode != "ADC" and opcode != "CMP" and opcode != "SUB" and opcode != "SBC" and opcode != "MOV" and opcode != "LSH" and opcode != "RSH":
        print("Erreur: opcode invalide")
        exit(0)

    # on ajoute les bits de l'opcode
    if opcode == "AND":
        opcode = "0000"
    elif opcode == "ORR":
        opcode = "0001"
    elif opcode == "EOR":
        opcode = "0010"
    elif opcode == "ADD":
        opcode = "0011"
    elif opcode == "ADC":
        opcode = "0100"
    elif opcode == "CMP":
        opcode = "0101"
    elif opcode == "SUB":
        opcode = "0110"
    elif opcode == "SBC":
        opcode = "0111"
    elif opcode == "MOV":
        opcode = "1000"
    elif opcode == "LSH":
        opcode = "1001"
    elif opcode == "RSH":
        opcode = "1010"
    return opcode


def gestionDestionation(destination):
    # on vérifie que le destination est valide
    if not destination.isdigit():
        print("Erreur: destination invalide")
        exit(0)

    destination = int(destination)

    # on vérifie que le destination est dans la plage [0, 15]
    if destination < 0 or destination > 15:
        print("Erreur: destination invalide, doit être dans la plage [0, 15]")
        exit(0)

    # on convertit le destination en binaire
    destinationBinaire = bin(destination)[2:]

    # on ajoute des 0 au début du destination pour que le destination soit de 4 bits
    while len(destinationBinaire) < 4:
        destinationBinaire = "0" + destinationBinaire

    # on ajoute les bits du destination
    return destinationBinaire


def gestionFirstOperand(firstOperand):
    # on vérifie que le firstOperand est valide
    if not firstOperand.isdigit():
        print("Erreur: firstOperand invalide")
        exit(0)

    firstOperand = int(firstOperand)

    # on vérifie que le firstOperand est dans la plage [0, 15]
    if firstOperand < 0 or firstOperand > 15:
        print("Erreur: firstOperand invalide, doit être dans la plage [0, 15]")
        exit(0)

    # on convertit le firstOperand en binaire
    firstOperandBinaire = bin(firstOperand)[2:]

    # on ajoute des 0 au début du firstOperand pour que le firstOperand soit de 4 bits
    while len(firstOperandBinaire) < 4:
        firstOperandBinaire = "0" + firstOperandBinaire

    # on ajoute les bits du firstOperand
    return firstOperandBinaire


# The difference between a register and an immediate value
# for the second operand is the presence of the r for register.
def gestionSecondOperand(secondOperand):
    # on vérifie que le premier caractère du secondOperand est un r
    if secondOperand[0] == "r":
        immediateValueFlag = "0"
        immediateValue = "00000000"
        # on enlève le r du secondOperand
        secondOperand = secondOperand[1:]
        # on vérifie que le secondOperand est valide
        if not secondOperand.isdigit():
            print("Erreur: secondOperand invalide")
            exit(0)

        secondOperand = int(secondOperand)

        # on vérifie que le secondOperand est dans la plage [0, 15]
        if secondOperand < 0 or secondOperand > 15:
            print(
                "Erreur: secondOperand invalide, doit être dans la plage [0, 15]")
            exit(0)

    else:
        immediateValueFlag = "1"
        secondOperand = secondOperand[1:]
        # on vérifie que le secondOperand est valide
        if not secondOperand.isdigit():
            print("Erreur: secondOperand invalide")
            exit(0)

        secondOperand = int(secondOperand)

        # on vérifie que le secondOperand est dans la plage [0, 255]
        if secondOperand < 0 or secondOperand > 255:
            print(
                "Erreur: secondOperand invalide, doit être dans la plage [0, 255]")
            exit(0)

        # on convertit le secondOperand en binaire
        immediateValue = bin(secondOperand)[2:]

        # on ajoute des 0 au début du secondOperand pour que le secondOperand soit de 8 bits
        while len(immediateValue) < 8:
            immediateValue = "0" + immediateValue

        secondOperand = "0000"

    # on ajoute les bits du secondOperand
    return secondOperand, immediateValueFlag, immediateValue


def convertiDataProcessingInstructionEnBinaire(ligne):
    # OPCODE DESTINATION FIRST_OPERAND SECOND_OPERAND
    opcode = ligne[0]
    destination = ligne[1].replace(",", "")
    firstOperand = ligne[2].replace(",", "")
    secondOperand = ligne[3].replace(",", "")

    opcode = gestionOpcodeInstruction(opcode)

    if (opcode != "0101"):
        destionation = gestionDestionation(destination)
    else:
        destionation = "0000"

    # on vérifie que le firstOperand est valide: soit un registre, soit un nombre
    firstOperand = gestionFirstOperand(firstOperand)

    # on vérifie que le secondOperand est valide: soit un registre, soit un nombre
    secondOperand, immediateValueFlag, immediateValue = gestionSecondOperand(
        secondOperand)
# TODO Gérer le branch condition code
    binaire = +"000" + immediateValueFlag + opcode + firstOperand + \
        secondOperand + destionation + immediateValue
    # vérifier que binaires est de 32 bits
    if len(binaire) != 32:
        print("Erreur: binaire invalide | taille: " +
              str(len(binaire)) + " | binaire: " + binaire)
        exit(0)

    # on ajoute les bits de l'opcode
    print(binaire)

    # on écrit dans le fichier binaire
    fichier = open("binaireCompile", "ab")
    fichier.write(binaire)
    fichier.close()


def convertiLigneEnBinaire(ligne):
    ligne = ligne.strip()
    ligne = ligne.split(" ")

    # si la ligne a plus de 4 mots, c'est une erreur
    if len(ligne) > 4:
        print("Erreur: trop de mots dans la ligne")
        exit(0)
    # si la ligne a 2 mots, c'est une instruction de branchement
    if len(ligne) == 2:
        # BRANCH_OPCODE OFFSET
        convertiBranchementEnBinaire(ligne)
    else:
        # OPCODE DESTINATION FIRST_OPERAND SECOND_OPERAND
        convertiDataProcessingInstructionEnBinaire(ligne)

    # OPCODE DESTINATION FIRST_OPERAND SECOND_OPERAND


def gestionOpcodeBranchement(opcode):

    # on vérifie que l'opcode est valide
    if opcode != "B" and opcode != "BEQ" and opcode != "BNE" and opcode != "BLE" and opcode != "BGE" and opcode != "BL" and opcode != "BG":
        print("Erreur: opcode invalide")
        exit(0)

    # on ajoute les bits de l'opcode
    if opcode == "B":
        opcode = "1000"
    elif opcode == "BEQ":
        opcode = "1001"
    elif opcode == "BNE":
        opcode = "1010"
    elif opcode == "BLE":
        opcode = "1011"
    elif opcode == "BGE":
        opcode = "1100"
    elif opcode == "BL":
        opcode = "1101"
    elif opcode == "BG":
        opcode = "1110"

    return opcode


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
    print("offset: " + str(offset))
    offsetBinaire = bin(offset)[2:]
    print("offsetBinaire: " + offsetBinaire)

    # on ajoute des 0 au début de l'offset pour que l'offset soit de 27 bits
    while len(offsetBinaire) < 27:
        offsetBinaire = "0" + offsetBinaire

        # on ajoute le signe
    offsetBinaire = signe + offsetBinaire

    # print("8 + 0 :"+offsetBinaire + "size: " + str(len(offsetBinaire)))

    # on ajoute les bits de l'offset

    return offsetBinaire


def convertiBranchementEnBinaire(ligne):
    # BRANCH_OPCODE OFFSET
    opcode = ligne[0]
    offset = ligne[1]

    opcode = gestionOpcodeBranchement(opcode)

    offset = gestionOffsetBranchement(offset)

    binaire = opcode + offset

    print("Taille de l'offset: " + str(len(offset)))
    print("Taille de l'opcode: " + str(len(opcode)))
    print("Taille du binaire: " + str(len(binaire)))

    # vérifier que binaires est de 32 bits
    if len(binaire) != 32:
        print("Erreur: binaire invalide | taille: " +
              str(len(binaire)) + " | binaire: " + binaire)
        exit(0)

    # on ajoute les bits de l'opcode
    print(binaire)

    # on écrit dans le fichier binaire
    fichier = open("binaireCompile", "ab")
    # converti le binaire en bytes
    binaire = bytearray(binaire, 'utf-8')
    fichier.write(binaire)
    fichier.close()
    # offset encoded on the bits 0 to 26 of the instruction.
    # The bit 27 encoded if the offset is positive or negative


def main():
    nomFichier = "assembleur.s"
    if verifiSiFichierExiste(nomFichier):
        lignes = lireFichier(nomFichier)

    else:
        print("Le fichier n'existe pas")
        exit(0)
    print(lignes)

    # création du fichier binaire
    fichier = open("binaireCompile", "wb")
    fichier.close()

    convertiAssembleurEnBinaire(lignes)

    # hexedit pour débuger


main()
