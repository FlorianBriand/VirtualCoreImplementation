//
// Created by raphi on 14/04/2023.
//

#include "fetch.h"


extern unsigned long long R[16];// 16 registres

extern char* FILENAME_INSTRUCTIONS;

int getPCcomparaison(unsigned int instruction, int pc);

int comparaison(bool resultat_comparaison, int pc, long instruction_suivante);

int recup_var2(int vflag, int iv, int ope2);

int calcul_pc_branchement(int pc, long instruction) {
    int signe, offset, newpc;

    signe = getSigne(instruction);

    offset = getOffset(instruction);

    newpc = pc + (pow(-1, signe) * offset);

    return newpc;
}

int calcul_pc(int pc, long instruction) {
    int BCC, opcode;
    BCC = getBCC(instruction);
    opcode = getOpcode(instruction);
    if (BCC == 0x8) {
        return calcul_pc_branchement(pc, instruction);
    }
    if (opcode == 0x5) {
        int newpc = getPCcomparaison(instruction, pc);
        return newpc;
    } else {
        return pc + 1;

    }
}

int getPCcomparaison(unsigned int instruction, int pc) {
    unsigned int instruction_suivante = fetch(FILENAME_INSTRUCTIONS, pc + 1);
    int BCC = getBCC(instruction_suivante), ope1 = getOpe1(instruction), ope2 = getOpe2(instruction);
    int IVflag = getIVflag(instruction), IV = getIV(instruction);

    int var1 = R[ope1];
    int var2 = recup_var2(IVflag, IV, ope2);
    switch (BCC) {
        case 0x9:
            return comparaison(var1 == var2, pc, instruction_suivante);
        case 0xA:
            return comparaison(var1 != var2, pc, instruction_suivante);
        case 0xB:
            return comparaison(var1 <= var2, pc, instruction_suivante);
        case 0xC:
            return comparaison(var1 >= var2, pc, instruction_suivante);
        case 0xD:
            return comparaison(var1 < var2, pc, instruction_suivante);
        case 0xE:
            return comparaison(var1 > var2, pc, instruction_suivante);
        default:
            printf("Erreur dans le BCC\n");
            exit(1);

    }


    return 0;
}

int recup_var2(int vflag, int iv, int ope2) {
    if (vflag == 0) {
        return R[ope2];
    } else {
        return iv;
    }
}

int comparaison(bool resultat_comparaison, int pc, long instruction_suivante) {
    if (resultat_comparaison) {
        return calcul_pc_branchement(pc + 1, instruction_suivante);;
    } else {
        return pc + 2;
    }
}

unsigned int fetch(char *instruction_file, int pc) {
    FILE *file = NULL;
    int i;

    unsigned char *instruction;
    instruction = malloc(4);
    unsigned int hex_instruction = 0;

    file = fopen(instruction_file, "rb");

    if (file == NULL) {
        printf("3 - Erreur dans l'ouverture du fichier %s\n", instruction_file);
        exit(1);
    }

    fseek(file, 4 * pc, SEEK_SET);
    fread(instruction, 4, 1, file);

    //printf("fetched instruction : ");
    for (i = 0; i < 4; i++) {
        //printf("%02x ", instruction[i]);
    }
    //printf("\n");

    hex_instruction = (instruction[0] << 24) | (instruction[1] << 16) | (instruction[2] << 8) | instruction[3];

    fclose(file);

    return hex_instruction;
}