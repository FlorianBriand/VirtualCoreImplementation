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

unsigned long fetch(char* instruction_file, int pc);
int calcul_pc(int pc, long instruction);

#endif //UNTITLED1_FETCH_H
