//
// Created by raphi on 14/04/2023.
//

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>
#include "fetch.h"
#include "decode.h"

int calcul_pc_branchement(int pc, long instruction) {
    int signe, offset, newpc;

    signe = getSigne(instruction);
    printf("signe : %x\n", signe);

    offset = getOffset(instruction);
    printf("offset : %x\n", offset);

    newpc = pc + (pow(-1, signe) * offset);
    printf("new pc : %d\n", newpc);
    return newpc;
}

int calcul_pc(int pc, long instruction){
    int BCC;
    BCC = getBCC(instruction);
    if (BCC == 0x8){
        printf("branchement\n");
        return calcul_pc_branchement(pc, instruction);
    }
    //TODO: Si on a une comparaison


}

unsigned long fetch(char* instruction_file, int pc){
    FILE *file = NULL;
    int c, i;

    unsigned char* instruction;
    instruction = malloc(4);
    unsigned long hex_instruction = 0;

    file = fopen(instruction_file, "rb");

    if(file==NULL){
        printf("Erreur dans l'ouverture du fichier instructions\n");
        exit(1);
    }

    fseek(file, 4*pc, SEEK_SET);
    fread(instruction, 4, 1, file);

    printf("fetched instruction : ");
    for(i=0;i<4;i++){
        printf("%02x ", instruction[i]);
    }
    printf("\n");

    hex_instruction = (instruction[0]<<24) | (instruction[1]<<16) | (instruction[2]<<8) | instruction[3];

    printf("hex instruction : %lx\n", hex_instruction);

    fclose(file);

    return hex_instruction;
}