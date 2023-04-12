import unittest

from compilateur import convertiLigneEnBinaire


class Test(unittest.TestCase):

    def test_convertiLigneEnBinaire(self):
        resultat = "FEDCBA9876543210FEDCBA9876543210"

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('FEDC', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:8]
        self.assertEqual('BA98', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[8]
        self.assertEqual('7', flag, 'flag n\'est pas correct')

        opcode = resultat[9:13]
        self.assertEqual('6543', opcode, 'opcode n\'est pas correct')

        reg1 = resultat[13:17]
        self.assertEqual('210F', reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[17:21]
        self.assertEqual('EDCB', reg2, 'reg2 n\'est pas correct')

        dest = resultat[21:25]
        self.assertEqual('A987', dest, 'dest n\'est pas correct')

        imm = resultat[25:32]
        self.assertEqual('6543210', imm, 'imm n\'est pas correct')

    def test_convertiLigneEnBinaireB3(self):
        resultat = convertiLigneEnBinaire('B -3')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('1000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:8]
        self.assertEqual('0000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[8]
        self.assertEqual('0', flag, 'flag n\'est pas correct')

        opcode = resultat[9:13]
        self.assertEqual('0000', opcode, 'opcode n\'est pas correct')

        reg1 = resultat[13:17]
        self.assertEqual('0000', reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[17:21]
        self.assertEqual('0000', reg2, 'reg2 n\'est pas correct')

        dest = resultat[21:25]
        self.assertEqual('0000', dest, 'dest n\'est pas correct')

        imm = resultat[25:32]
        self.assertEqual('0000011', imm, 'imm n\'est pas correct')


    def test_convertiLigneEnBinaireB8(self):
        resultat = convertiLigneEnBinaire('B 8')

        # On vérifie que la longueur est correcte
        self.assertEqual(32, len(resultat), 'La longueur du résultat n\'est pas correcte')

        bcc = resultat[0:4]
        self.assertEqual('1000', bcc, 'Le bcc n\'est pas correct')

        alwaysSetToZero = resultat[4:8]
        self.assertEqual('0000', alwaysSetToZero, 'alwaysSetToZero n\'est pas correct')

        flag = resultat[8]
        self.assertEqual('0', flag, 'flag n\'est pas correct')

        opcode = resultat[9:13]
        self.assertEqual('0000', opcode, 'opcode n\'est pas correct')

        reg1 = resultat[13:17]
        self.assertEqual('0000', reg1, 'reg1 n\'est pas correct')

        reg2 = resultat[17:21]
        self.assertEqual('0000', reg2, 'reg2 n\'est pas correct')

        dest = resultat[21:25]
        self.assertEqual('0000', dest, 'dest n\'est pas correct')

        imm = resultat[25:32]
        self.assertEqual('0001000', imm, 'imm n\'est pas correct')


if __name__ == '__main__':
    unittest.main()
