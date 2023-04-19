//
// Created by raphi on 19/04/2023.
//

#include "execute.h"

extern int R[16];

/*Toute les opérations*/
//and
int et(int a, int b) {
    int resultat = a & b;
    return resultat;
}

//or
int ou_inclusif(int a, int b) {
    int resultat = a | b;
    return resultat;
}

//xor
int xor(int a, int b) {
    int resultat = a ^ b;
    return resultat;
}

//add
int addition(int a, int b) {
    int resultat = a + b;
    return resultat;
}

//sous
int soustraction(int a, int b) {
    int resultat = a - b;
    return resultat;
}

//Move Data
int movedata(int b) {
    int resultat = b;
    return resultat;
}

//lls
int logical_left_shift(int a, int b) {
    unsigned int resultat = a << b;
    return resultat;
}


//lrs
int logical_right_shift(int a, int b) {
    unsigned int resultat = a >> b;
    return resultat;
}

void stocker_resultat(int dest, int res) {
    if (dest >= 0x0 && dest <= 0xf) {
        R[dest] = res;   // set the appropriate register
    }
}

int res_ope1(int ope1) {
    int var1;
    if (ope1 >= 0x0 && ope1 <= 0xf) {
        var1 = R[ope1];
    }
    return var1;
}

int res_ope2(int ope2) {
    int var2;
    if (ope2 >= 0x0 && ope2 <= 0xf) {
        var2 = R[ope2];
    }
    return var2;
}

int execute(int opcode,int ope1,int ope2,int dest,int IV,int IVflag) {
    //int res
    unsigned long res, var1, var2;

    var1 = res_ope1(ope1);
    var2 = res_ope2(ope2);

    switch (opcode) {
        case 0x0:
            res = IVflag == 0x01 ? et(var1, IV) : et(var1, var2);
            break;
        case 0x1:
            res = IVflag == 0x01 ? ou_inclusif(var1, IV) : ou_inclusif(var1, var2);
            break;
        case 0x2:
            res = IVflag == 0x01 ? xor(var1, IV) : xor(var1, var2);
            break;
        case 0x3:
            res = IVflag == 0x01 ? addition(var1, IV) : addition(var1, var2);
            break;
        case 0x6:
            res = IVflag == 0x01 ? soustraction(var1, IV) : soustraction(var1, var2);
            break;
        case 0x8:
            res = IVflag == 0x01 ? movedata(IV) : movedata(ope2);
            break;
        case 0x9:
            res = IVflag == 0x01 ? logical_left_shift(var1, IV) : logical_left_shift(var1, var2);
            break;
        case 0xa:
            res = IVflag == 0x01 ? logical_right_shift(var1, IV) : logical_right_shift(var1, var2);
            break;
        default:
            res = 0;
            break;
    }
    stocker_resultat(dest, res);

    return res;
}