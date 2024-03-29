//
// Created by Florian on 14/04/2023.
//


#include "main.h"

char* FILENAME_INSTRUCTIONS = "file";


unsigned long long R[16];// 16 registres

int get_nb_instructions(const char *string);

void verifier_existence_fichier(char *registers);

//
int main(int argc, char *argv[]) {
    // Vérifier que deux arguments ont été fournis
    if (argc != 3) {
        printf("Erreur : le programme doit être appelé avec deux arguments : le nom du fichier des registres et le nom du fichier des instructions.\n");
        return 1;
    }

    // Récupérer les noms de fichiers des registres et des instructions
    char *filename_registers = argv[2];
    char *filename_instructions = argv[1];

    verifier_existence_fichier(filename_registers);
    verifier_existence_fichier(filename_instructions);

    FILENAME_INSTRUCTIONS = filename_instructions;

    //Fetch
    //récupération des instructions
    unsigned long long result;
    int pc = 0, newpc, nbinstructions;
    unsigned int instruction;
    lire_fichier_registres(filename_registers);
    nbinstructions = get_nb_instructions(filename_instructions);
    //printf("nb instructions : %d\n", nbinstructions);
    while (pc < nbinstructions && pc >= 0) {
        instruction = fetch(filename_instructions, pc);
        int BBC = getBCC(instruction), opcode = getOpcode(instruction);
        if (opcode != 0x5 && BBC != 0x8) {
            result = decode(instruction);
            //printf("result : %llx\n", result);
        }

        newpc = calcul_pc(pc, instruction);
        //printf("new pc : %d\n", newpc);
        pc = newpc;
    }

    if (pc == nbinstructions) {
        printf("Programme terminé\n");
    } else {
        printf("Erreur de segmentation\n");
    }


    sauvegarder_registres(FILENAME_REGISTERS_FINAL);

    return 0;
}

void verifier_existence_fichier(char *registers) {
    FILE *file = NULL;

    file = fopen(registers, "rb");

    if (file == NULL) {
        printf("1 - Erreur dans l'ouverture du fichier %s\n", registers);
        exit(1);
    }

    fclose(file);

}

int get_nb_instructions(const char *string) {
    FILE *file = NULL;
    int c, i = 0;

    file = fopen(string, "rb");

    if (file == NULL) {
        printf("2 - Erreur dans l'ouverture du fichier %s\n", string);
        exit(1);
    }

    while ((c = fgetc(file)) != EOF) {
        i++;
    }

    fclose(file);

    return i / 4;
}

/* Explanation: The code has been refactored to make it more readable, efficient, and adhere to best coding practices. The masks have been moved outside of the print statements, the return statement has been added, and the braces have been added around the function for clarity. */


void lire_fichier_registres(char *nom_fichier) {
    FILE *fichier = fopen(nom_fichier, "r");
    if (fichier == NULL) {
        printf("Erreur: Impossible d'ouvrir le fichier\n");
        return;
    }
    char buffer[256];
    int i = 0;
    while (fgets(buffer, 256, fichier) && i < 16) {
        unsigned long long val;
        if (sscanf(buffer, "R%X=0x%llx", &i, &val) == 2) {
            R[i] = val;
        }
    }
    fclose(fichier);
}

void sauvegarder_registres(char *nom_fichier) {
    FILE *fichier = fopen(nom_fichier, "w");
    if (fichier == NULL) {
        printf("Erreur: Impossible d'ouvrir le fichier\n");
        return;
    }
    for (int i = 0; i < 16; i++) {
        fprintf(fichier, "R%X=0x%llx\n", i, R[i]);
    }
    fclose(fichier);
}