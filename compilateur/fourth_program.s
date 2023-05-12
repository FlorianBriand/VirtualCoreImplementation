# Initial state : R0 : 0x5
#                 R1 : 0x3
#                 R2 : 0x0
# Final state : R4 : 0xf
ADC R4, R4, R0
ADC R5, R5, 0
ADC R3, R3, 1
CMP R1, R3
BNE -4