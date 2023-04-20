//
// Created by Florian on 14/04/2023.
//

#ifndef VIRTUALCOREIMPLEMENTATION_DECODE_H
#define VIRTUALCOREIMPLEMENTATION_DECODE_H
#include "execute.h"

unsigned long long decode(long instruction);

int getBCC(long instruction);
int getOpcode(long instruction);
int getOpe1(long instruction);
int getOpe2(long instruction);
int getDest(long instruction);
int getIV(long instruction);
int getIVflag(long instruction);
int getSigne(long instruction);
int getOffset(long instruction);



#endif //VIRTUALCOREIMPLEMENTATION_DECODE_H
