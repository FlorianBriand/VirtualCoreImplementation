# Initial state : r0 : 0xf458f452145147de ; r1 : 0xc
# Final state :   r2 : 0x8f452145147de000 ; r3 : 0xf45
MOV r5, 0xf4
#SUB r4, r5, r1
RSH r3, r0, r5
LSH r2, r0, r1