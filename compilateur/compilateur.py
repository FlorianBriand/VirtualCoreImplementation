from compilateur.Branchement import convertiBranchementEnBinaire
from compilateur.DataProcessingInstruction import convertiDataProcessingInstructionEnBinaire

TMP_FILE_ASSEMBLY_TO_STRING_OF_0_AND_1 = "out/tmp_file_assembly_to_string_of_0_and_1.txt"

# Dossier des binaires
DIR_BINARY = "out/"

# Assembleurs des programmes 1 à 4
FILE_S_init = "compilateur/init.s"
FILE_S_add128 = "compilateur/add128.s"
FILE_S_lshift_64_128 = "compilateur/lshift64_128.s"
FILE_S_mul64 = "compilateur/mul64.s"


def read_line_by_line(lignes):
    conversion = ""
    for ligne in lignes:
        conversion += convert_ligne_to_string_of_0_and_1(ligne)

    # safe to write the file now

    fichier = open(TMP_FILE_ASSEMBLY_TO_STRING_OF_0_AND_1, "w")
    fichier.write(conversion)
    fichier.close()


def convert_ligne_to_string_of_0_and_1(ligne):
    ligne = ligne.strip()
    ligne = ligne.split(" ")

    # si la ligne a plus de 4 mots, c'est une erreur
    if len(ligne) > 4:
        print("Erreur: trop de mots dans la ligne")
        exit(0)

    if ligne[0][0].upper() == "B":
        # BRANCH_OPCODE OFFSET
        resultat = convertiBranchementEnBinaire(ligne)

    else:
        # OPCODE DESTINATION FIRST_OPERAND SECOND_OPERAND
        resultat = convertiDataProcessingInstructionEnBinaire(ligne)
    return resultat


def convert_file_of_0_and_1_to_binary_file(nomFichier):
    contenu = lireFichier(TMP_FILE_ASSEMBLY_TO_STRING_OF_0_AND_1)
    contenu = contenu[0]

    print(contenu)

    # Creation of list of 0 and 1
    binaire = []

    for i in range(0, len(contenu), 8):
        bit = int(contenu[i:i + 8], 2)
        binaire.append(bit)

    print(binaire)
    arrayBin = bytes(binaire)
    print(arrayBin)

    # Creation of binary file

    # Enlever le .s du nom du fichier
    nomFichier = nomFichier[:-2]
    # Enlever le compilateur/ du nom du fichier
    nomFichier = nomFichier[12:]
    nomFichier = DIR_BINARY + nomFichier + "_test"
    fichier = open(nomFichier, "wb")
    fichier.write(arrayBin)
    fichier.close()


# Compile les 4 premiers programmes
def main():
    compilateur_fichier(FILE_S_init)
    compilateur_fichier(FILE_S_add128)
    compilateur_fichier(FILE_S_lshift_64_128)
    compilateur_fichier(FILE_S_mul64)


def compilateur_fichier(nomFichier):
    if verifiSiFichierExiste(nomFichier):
        lignes = lireFichier(nomFichier)

    # remove all ligne with # in it
    lignes = [ligne for ligne in lignes if ligne[0] != "#"]

    print(lignes)

    read_line_by_line(lignes)

    convert_file_of_0_and_1_to_binary_file(nomFichier)



def verifiSiFichierExiste(nomFichier):
    try:
        fichier = open(nomFichier, "r")
        fichier.close()
        return True
    except:
        print("Le fichier " + nomFichier + " n'existe pas")
        exit(0)
        return False

        # Lit le fichier et retourne une liste de lignes


def lireFichier(nomFichier):
    verifiSiFichierExiste(nomFichier)
    fichier = open(nomFichier, "r")
    lignes = fichier.readlines()
    fichier.close()
    return lignes
