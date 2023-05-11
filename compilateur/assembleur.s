# Initial state : R1 : 0x5
#                 R2 : 0x3
#                 R3 : 0x0
# Final state : R4 : 0xf
CMP R2,R3
BEQ 3
ADD R4,R1,R1
B -3