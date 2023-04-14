#include <stdio.h>
#include <stdlib.h>
#include <string.h>


static int R[16];

void lire_fichier_registres(char* nom_fichier) {
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

void sauvegarder_registres(char* nom_fichier) {
    FILE* fichier = fopen(nom_fichier, "w");
    if (fichier == NULL) {
        printf("Erreur: Impossible d'ouvrir le fichier\n");
        return;
    }
    for (int i = 0; i < 16; i++) {
        fprintf(fichier, "R%X=0x%X\n", i, R[i]);
    }
    fclose(fichier);
}

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

int res_ope1(int ope1){
    int var1;
    if (ope1 >= 0x0 && ope1 <= 0xf) {
        var1 = R[ope1];
    }    
    return var1;
}

int res_ope2(int ope2){
    int var2;
    if (ope2 >= 0x0 && ope2 <= 0xf) {
        var2 = R[ope2];
    }    
    return var2;
}

int decode() {
   int instruction = 0x031231a;

   //Recuperer le opcode
   int opcode = (instruction & 0x00f00000) >> 20;

   //Recuperer le ope1
   int ope1 = (instruction & 0x000f0000) >> 16;

   //Recuperer le ope2
   int ope2 = (instruction & 0x0000f000) >> 12;

   //Recuperer le destanation
   int dest = (instruction & 0x00000f00) >> 8;

   //Recuperer le IV
   int IV = (instruction & 0x000000ff);

   //Recuperer le IVflag
   int IVflag = (instruction & 0x00800000) >> 23;

    //int res
    int res, var1, var2;

    printf("instruction = %x\n", instruction);   
    printf("opcode = %x\n", opcode); 							 
    printf("ope1 = %x\n", ope1); 						     
    printf("ope2 = %x\n", ope2); 			             
    printf("dest = %x\n", dest); 	                 
    printf("IV = %x\n", IV); 	                     
    printf("IVflag = %x\n", IVflag);

    var1 = res_ope1(ope1);
    var2 = res_ope2(ope2);

    switch (opcode)
    {
    case 0x0:
        if (IVflag == 0x01) {
            res=et(var1, IV);
        }
        else {
            res=et(var1, var2);
        }
        break;
    case 0x1:
        if (IVflag == 0x01) {
            res=ou_inclusif(var1, IV);
        }
        else {
            res=ou_inclusif(var1, var2);
        }
        break;
    case 0x2:
        if (IVflag == 0x01) {
            res=xor(var1, IV);
        }
        else {
            res=xor(var1, var2);
        }
        break;
    case 0x3:
        if (IVflag == 0x01) {
            res=addition(var1, IV);
        }
        else {
            res=addition(var1, var2);
        }
        break;
    case 0x6:
        if (IVflag == 0x01) {
            res=soustraction(var1, IV);
        }
        else {
            res=soustraction(var1, var2);
        }
        break;
    case 0x8:
        if (IVflag == 0x01) {
            res=movedata(IV);
        }
        else {
            res=movedata(ope2);
        }
        break;
    case 0x9:
        if (IVflag == 0x01) {
            res=logical_left_shift(var1, IV);
        }
        else {
            res=logical_left_shift(var1, var2);
        }
        break;
    case 0xa:
        if (IVflag == 0x01) {
            res=logical_right_shift(var1, IV);
        }
        else {
            res=logical_right_shift(var1, var2);
        }
        break;
    default:
        res=0;
        break;
    }                        

    stocker_resultat(dest, res);
    return res;     //return statement added for clarity and to adhere to best practices of always having a return statement in a function. 
}               //braces added for clarity and to adhere to best practices of always using braces with functions. 

int main(){
   //intialisation des variables globales
   lire_fichier_registres("registers.txt");
   int result;
   printf("R3=%x\n", R[3]);
   printf("Debut !\n");
   result = decode();
   printf("Resultat = %x\n", result);
   printf("R3=%x\n", R[3]);
   sauvegarder_registres("registerFinal.txt");
   return 0;
}
/* Explanation: The code has been refactored to make it more readable, efficient, and adhere to best coding practices. The masks have been moved outside of the print statements, the return statement has been added, and the braces have been added around the function for clarity. */