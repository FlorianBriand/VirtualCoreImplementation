#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int decode() {
   int instruction = 0x01f46231;

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

    printf("instruction = %x\n", instruction);   
    printf("opcode = %x\n", opcode); 							 
    printf("ope1 = %x\n", ope1); 						     
    printf("ope2 = %x\n", ope2); 			             
    printf("dest = %x\n", dest); 	                 
    printf("IV = %x\n", IV); 	                     
    printf("IVflag = %x\n", IVflag);                           

   return 0;     //return statement added for clarity and to adhere to best practices of always having a return statement in a function. 
}               //braces added for clarity and to adhere to best practices of always using braces with functions. 

                                                              /* Explanation: The code has been refactored to make it more readable, efficient, and adhere to best coding practices. The masks have been moved outside of the print statements, the return statement has been added, and the braces have been added around the function for clarity. */