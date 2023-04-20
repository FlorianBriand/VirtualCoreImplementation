#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "execute.h"


extern int R[16];


int getBCC(long instruction) {
    return (instruction & 0xf0000000) >> 24;
}

int getOpcode(long instruction) {
    return (instruction & 0x00f00000) >> 20;
}

int getOpe1(long instruction) {
    return (instruction & 0x000f0000) >> 16;
}

int getOpe2(long instruction) {
    return (instruction & 0x0000f000) >> 12;
}

int getDest(long instruction) {
    return (instruction & 0x00000f00) >> 8;
}

int getIV(long instruction) {
    return (instruction & 0x000000ff);
}

int getIVflag(long instruction) {
    return (instruction & 0x00800000) >> 23;
}

int getSigne(long instruction) {
    return (instruction & 0x00000010) >> 4;
}

int getOffset(long instruction) {
    return (instruction & 0x03ffffff);
}


int decode(long instruction) {

    int res, opcode, ope1, ope2, dest, IV, IVflag;

    //Recuperer le opcode
    opcode = getOpcode(instruction);
    //Recuperer le ope1
    ope1 = getOpe1(instruction);
    //Recuperer le ope2
    ope2 = getOpe2(instruction);
    //Recuperer le destanation
    dest = getDest(instruction);
    //Recuperer le IV
    IV = getIV(instruction);
    //Recuperer le IVflag
    IVflag = getIVflag(instruction);


    printf("instruction = %x\n", instruction);
    printf("opcode = %x\n", opcode);
    printf("ope1 = %x\n", ope1);
    printf("ope2 = %x\n", ope2);
    printf("dest = %x\n", dest);
    printf("IV = %x\n", IV);
    printf("IVflag = %x\n", IVflag);

    res = execute(opcode, ope1, ope2, dest, IV, IVflag);

    return res;
}     //return statement added for clarity and to adhere to best practices of always having a return statement in a function.
//braces added for clarity and to adhere to best practices of always using braces with functions.
