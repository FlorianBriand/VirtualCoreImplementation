//
// Created by Florian on 14/04/2023.
//

#ifndef VIRTUALCOREIMPLEMENTATION_MAIN_H
#define VIRTUALCOREIMPLEMENTATION_MAIN_H

#include <stdio.h>
#include <stdlib.h>
#include "decode.h"
#include "fetch.h"

void lire_fichier_registres(char *nom_fichier);
void sauvegarder_registres(char *nom_fichier);
// define location of the file registers.txt
//#define FILENAME_REGISTERS "core/first_program.txt"
//#define FILENAME_REGISTERS "core/third_program.txt"
#define FILENAME_REGISTERS "core/registers.txt"

#define FILENAME_REGISTERS_FINAL "core/final.txt"



#endif //VIRTUALCOREIMPLEMENTATION_MAIN_H
