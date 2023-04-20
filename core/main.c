//
// Created by Florian on 14/04/2023.
//


#include "main.h"




// TODO : Change int to long long (64 bits)
int R[16];// 16 registres

int get_nb_instructions(const char *string);

int main() {
    //Fetch
    //récupération des instructions
    int pc=0, result, newpc, nbinstructions;
    unsigned long instruction;
    lire_fichier_registres(FILENAME_REGISTERS);
    nbinstructions= get_nb_instructions(FILENAME_INSTRUCTIONS);
    printf("nb instructions : %d\n", nbinstructions);
    while (pc < nbinstructions && pc >= 0) {
        instruction = fetch(FILENAME_INSTRUCTIONS, pc);
        int BBC = getBCC(instruction), opcode = getOpcode(instruction);
        if(opcode != 0x5 && BBC != 0x8){
            result = decode(instruction);
            printf("result : %x\n", result);
        }

        newpc = calcul_pc(pc, instruction);
        printf("new pc : %d\n", newpc);
        pc = newpc;
    }

    if (pc == nbinstructions){
        printf("Programme terminé\n");
    }
    else{
        printf("Erreur de segmentation\n");
    }


    sauvegarder_registres(FILENAME_REGISTERS_FINAL);

    return 0;
}

int get_nb_instructions(const char *string) {
    FILE *file = NULL;
    int c, i = 0;

    file = fopen(string, "rb");

    if (file == NULL) {
        printf("Erreur dans l'ouverture du fichier instructions\n");
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
        unsigned int val;
        if (sscanf(buffer, "R%X=0x%x", &i, &val) == 2) {
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
        fprintf(fichier, "R%X=0x%X\n", i, R[i]);
    }
    fclose(fichier);
}