//
// Created by Florian on 14/04/2023.
//

#include "main.h"

// define location of the file registers.txt
#define FILENAME_REGISTERS "core/registers.txt"
#define FILENAME_REGISTERS_FINAL "core/final.txt"
#define FILENAME_INSTRUCTIONS "out/bin.out"


// TODO : Change int to long long (64 bits)
int R[16];// 16 registres

int main() {
    //Fetch
    //récupération des instructions
    int pc=0;
    unsigned long instruction = fetch(FILENAME_INSTRUCTIONS, pc);
    for (int i = 0; i < 3; i++) {
        int newpc = calcul_pc(pc, instruction);
        pc = newpc;
        instruction = fetch(FILENAME_INSTRUCTIONS, pc);
    }

    //Decode
    //Initialisation des variables globales
    lire_fichier_registres(FILENAME_REGISTERS);
    int result;
    printf("Debut !\n");
    result = decode(instruction);
    printf("Resultat = %x\n", result);
    sauvegarder_registres(FILENAME_REGISTERS_FINAL);
    return 0;
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