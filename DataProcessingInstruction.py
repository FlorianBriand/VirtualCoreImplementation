OPCODE_MOV = "1000"


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
    if destination[0].upper() != "R":
        print("Erreur: destination invalide")
        exit(0)
    destination = destination[1:]

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
    if firstOperand[0].upper() != "R":
        print("Erreur: destination invalide")
        exit(0)

    firstOperand = firstOperand[1:]

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
    if secondOperand[0].upper() == "R":

        immediateValueFlag = "0"
        immediateValue = "00000000"

        # on enlève le r du secondOperand
        secondOperand = secondOperand[1:]
        secondOperand = int(secondOperand)

        # on vérifie que le secondOperand est valide
        if secondOperand < 0 or secondOperand > 15:
            print("Erreur: secondOperand is not between 0 and 15")
            exit(0)

        # on convertit le secondOperand en binaire
        secondOperand = bin(secondOperand)[2:]

        # on ajoute des 0 au début du secondOperand pour que le secondOperand soit de 4 bits
        while len(secondOperand) < 4:
            secondOperand = "0" + secondOperand

    else:
        immediateValueFlag = "1"
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
    bcc = "0000"
    opcode = ligne[0]
    opcode = gestionOpcodeInstruction(opcode)

    destination = ligne[1].replace(",", "")
    firstOperand = ligne[2].replace(",", "")

    destination = gestionDestionation(destination)

    if opcode != OPCODE_MOV:
        secondOperand = ligne[3].replace(",", "")

        # on vérifie que le firstOperand est valide: soit un registre, soit un nombre
        firstOperand = gestionFirstOperand(firstOperand)
        # on vérifie que le secondOperand est valide: soit un registre, soit un nombre
        secondOperand, immediateValueFlag, immediateValue = gestionSecondOperand(
            secondOperand)
    else:
        secondOperand, immediateValueFlag, immediateValue = gestionSecondOperand(
            firstOperand)
        firstOperand = "0000"

    ligne_en_binaire = bcc + "000" + immediateValueFlag + opcode + firstOperand + \
                       secondOperand + destination + immediateValue
    # vérifier que binaires est de 32 bits
    if len(ligne_en_binaire) != 32:
        print("Erreur: binaire invalide | taille: " +
              str(len(ligne_en_binaire)) + " | binaire: " + ligne_en_binaire)
        exit(0)
    return ligne_en_binaire
