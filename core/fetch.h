//
// Created by raphi on 14/04/2023.
//

#ifndef UNTITLED1_FETCH_H
#define UNTITLED1_FETCH_H


#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>
#include <stdbool.h>
#include "decode.h"
#include "main.h"

unsigned int fetch(char* instruction_file, int pc);
int calcul_pc(int pc, long instruction);

int logical_left_shift(int value, int shift);

#endif //UNTITLED1_FETCH_H
