import unittest

from compilateur import convert_ligne_to_string_of_0_and_1

OPCODE_AND = "0000"
OPCODE_OR = "0001"
OPCODE_XOR = "0010"
OPCODE_ADD = "0011"
OPCODE_ADC = "0100"
OPCODE_CMP = "0101"
OPCODE_SUB = "0110"
OPCODE_SBC = "0111"
OPCODE_MOV = "1000"
OPCODE_LSH = "1001"
OPCODE_RSH = "1010"

R0 = "0000"
R1 = "0001"
R2 = "0010"
R3 = "0011"
R4 = "0100"
R5 = "0101"
R6 = "0110"
R7 = "0111"
R8 = "1000"
R9 = "1001"
R10 = "1010"
R11 = "1011"
R12 = "1100"
R13 = "1101"
R14 = "1110"
R15 = "1111"


class Test(unittest.TestCase):
    # FEDCBA9876543210FEDCBA9876543210
    def test_convertiLigneEnBinaire(self):
        resultat = "FEDCBA9876543210FEDCBA9876543210"

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('FEDC', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('BA9', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('8', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual('7654', opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual('3210', reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual('FEDC', reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual('BA98', dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('76543210', imm, 'imm n\'est pas correct')

    # B 8
    def test_B_8(self):
        resultat = convert_ligne_to_string_of_0_and_1('B 8')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        opcode = resultat[0:4]
        self.assertEqual('1000', opcode, 'Le opcode n\'est pas correct')

        signe = resultat[4:5]
        self.assertEqual('0', signe, 'Le signe n\'est pas correct')

        offset = resultat[5:32]
        self.assertEqual('000000000000000000000001000', offset, 'L\'offset n\'est pas correct')

    # B -3
    def test_B_negatif_3(self):
        resultat = convert_ligne_to_string_of_0_and_1('B -3')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        opcode = resultat[0:4]
        self.assertEqual('1000', opcode, 'Le opcode n\'est pas correct')

        signe = resultat[4:5]
        self.assertEqual('1', signe, 'Le signe n\'est pas correct')

        offset = resultat[5:32]
        self.assertEqual('000000000000000000000000011', offset, 'L\'offset n\'est pas correct')

    # ADD R1, R2, 4
    def test_ADD_4(self):
        resultat = convert_ligne_to_string_of_0_and_1('ADD R1, R2, 4')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('0000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('1', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual(OPCODE_ADD, opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual(R2, reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual('0000', reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual(R1, dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('00000100', imm, 'imm n\'est pas correct')

    def test_ADDR_4(self):
        resultat = convert_ligne_to_string_of_0_and_1('ADD R1, R2, R4')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('0000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('0', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual(OPCODE_ADD, opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual(R2, reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual(R4, reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual(R1, dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('00000000', imm, 'imm n\'est pas correct')

    def test_SUB_10(self):
        resultat = convert_ligne_to_string_of_0_and_1('SUB R8, R9, 10')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('0000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('1', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual(OPCODE_SUB, opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual(R9, reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual('0000', reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual(R8, dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('00001010', imm, 'imm n\'est pas correct')

    def test_SUB_R15(self):
        resultat = convert_ligne_to_string_of_0_and_1('SUB R8, R9, R15')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('0000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('0', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual(OPCODE_SUB, opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual(R9, reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual(R15, reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual(R8, dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('00000000', imm, 'imm n\'est pas correct')

    def test_AND_R5_R6(self):
        resultat = convert_ligne_to_string_of_0_and_1('AND R4, R5, R6')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('0000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('0', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual(OPCODE_AND, opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual(R5, reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual(R6, reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual(R4, dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('00000000', imm, 'imm n\'est pas correct')

    def test_AND_R5_10(self):
        resultat = convert_ligne_to_string_of_0_and_1('AND R4, R5, 10')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('0000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('1', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual(OPCODE_AND, opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual(R5, reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual('0000', reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual(R4, dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('00001010', imm, 'imm n\'est pas correct')

    def test_OR_R5_R6(self):
        resultat = convert_ligne_to_string_of_0_and_1('ORR R4, R5, R6')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('0000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('0', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual(OPCODE_OR, opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual(R5, reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual(R6, reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual(R4, dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('00000000', imm, 'imm n\'est pas correct')

    def test_OR_R5_10(self):
        resultat = convert_ligne_to_string_of_0_and_1('ORR R4, R5, 10')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('0000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('1', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual(OPCODE_OR, opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual(R5, reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual('0000', reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual(R4, dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('00001010', imm, 'imm n\'est pas correct')

    def test_XOR_R5_R6(self):
        resultat = convert_ligne_to_string_of_0_and_1('EOR R4, R5, R6')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('0000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('0', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual(OPCODE_XOR, opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual(R5, reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual(R6, reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual(R4, dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('00000000', imm, 'imm n\'est pas correct')

    def test_XOR_R5_10(self):
        resultat = convert_ligne_to_string_of_0_and_1('EOR R4, R5, 10')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('0000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('1', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual(OPCODE_XOR, opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual(R5, reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual('0000', reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual(R4, dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('00001010', imm, 'imm n\'est pas correct')

    def test_logical_left_shift_R5_R6(self):
        resultat = convert_ligne_to_string_of_0_and_1('LSH R4, R5, R6')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('0000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('0', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual(OPCODE_LSH, opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual(R5, reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual(R6, reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual(R4, dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('00000000', imm, 'imm n\'est pas correct')

    def test_logical_left_shift_R5_10(self):
        resultat = convert_ligne_to_string_of_0_and_1('LSH R4, R5, 10')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('0000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('1', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual(OPCODE_LSH, opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual(R5, reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual('0000', reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual(R4, dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('00001010', imm, 'imm n\'est pas correct')

    def test_logical_right_shift_R5_R6(self):
        resultat = convert_ligne_to_string_of_0_and_1('RSH R4, R5, R6')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('0000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('0', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual(OPCODE_RSH, opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual(R5, reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual(R6, reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual(R4, dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('00000000', imm, 'imm n\'est pas correct')

    def test_logical_right_shift_R5_10(self):
        resultat = convert_ligne_to_string_of_0_and_1('RSH R4, R5, 10')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('0000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:7]
        self.assertEqual('000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[7]
        self.assertEqual('1', flag, 'flag n\'est pas correct')

        opcode = resultat[8:12]
        self.assertEqual(OPCODE_RSH, opcode, 'opcode n\'est pas correct')

        reg1 = resultat[12:16]
        self.assertEqual(R5, reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[16:20]
        self.assertEqual('0000', reg2, 'reg2 n\'est pas correct')

        dest = resultat[20:24]
        self.assertEqual(R4, dest, 'dest n\'est pas correct')

        imm = resultat[24:32]
        self.assertEqual('00001010', imm, 'imm n\'est pas correct')


if __name__ == '__main__':
    unittest.main()
