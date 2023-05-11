//
// Created by raphi on 19/04/2023.
//

#include "execute.h"

char carry = 0;

extern unsigned long long R[16];

/*Toute les opérations*/
//and
unsigned long long et(unsigned long long a, unsigned long long b) {
    unsigned long long resultat = a & b;
    return resultat;
}

//or
unsigned long long ou_inclusif(unsigned long long a, unsigned long long b) {
    unsigned long long resultat = a | b;
    return resultat;
}

//xor
unsigned long long xor(unsigned long long a, unsigned long long b) {
    unsigned long long resultat = a ^ b;
    return resultat;
}

//add
unsigned long long addition(unsigned long long a, unsigned long long b) {
    unsigned long long resultat = a + b;
    return resultat;
}

//add with carry
unsigned long long addition_with_carry(unsigned long long a, unsigned long long b) {
    unsigned long long resultat = a + b + carry;
    if(resultat<a || resultat<b){
        carry = 1;
    }
    else{
        carry = 0;
    }
    return resultat;
}

//sous
unsigned long long soustraction(unsigned long long a, unsigned long long b) {
    unsigned long long resultat = a - b;
    return resultat;
}

//sous with carry
unsigned long long soustraction_with_carry(unsigned long long a, unsigned long long b) {
    unsigned long long resultat = a - b - carry;
    if(resultat>a || resultat>b){
        carry = 1;
    }
    else{
        carry = 0;
    }
    return resultat;
}

//Move Data
unsigned long long movedata(unsigned long long b) {
    unsigned long long resultat = b;
    return resultat;
}

//lls
unsigned long long logical_left_shift(unsigned long long a, unsigned long long b) {
    unsigned long long resultat = a << b;
    return resultat;
}

//lrs
unsigned long long logical_right_shift(unsigned long long a, unsigned long long b) {
    unsigned long long resultat = a >> b;
    return resultat;
}

void stocker_resultat(unsigned long long dest, unsigned long long res) {
    if (dest >= 0x0 && dest <= 0xf) {
        R[dest] = res;   // set the appropriate register
    }
}

unsigned long long res_ope1(unsigned long long ope1) {
    unsigned long long var1;
    if (ope1 >= 0x0 && ope1 <= 0xf) {
        var1 = R[ope1];
    }
    return var1;
}

unsigned long long res_ope2(unsigned long long ope2) {
    unsigned long long var2;
    if (ope2 >= 0x0 && ope2 <= 0xf) {
        var2 = R[ope2];
    }
    return var2;
}

unsigned long long execute(int opcode,int ope1,int ope2,int dest,int IV,int IVflag) {
    //int res
    unsigned long long res, var1, var2;

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
        case 0x4:
            res = IVflag == 0x01 ? addition_with_carry(var1, IV) : addition_with_carry(var1, var2);
            break;
        case 0x6:
            res = IVflag == 0x01 ? soustraction(var1, IV) : soustraction(var1, var2);
            break;
        case 0x7:
            res = IVflag == 0x01 ? soustraction_with_carry(var1, IV) : soustraction_with_carry(var1, var2);
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