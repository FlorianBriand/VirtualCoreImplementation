# Initial state : 0x0000000000000000
# Final state : 0x0123456789abcdef
MOV r0, 0x01
# r0 = 0x0000000000000001
LSH r0, r0, 56
# r0 = 0x0100000000000000
MOV r1, 0x23
LSH r1, r1, 48
# r1 = 0x0000000000000023
#LSH r1, r1, 12
# r1 = 0x0023000000000000
ADD r0, r0, r1
# r0 = 0x0123000000000000