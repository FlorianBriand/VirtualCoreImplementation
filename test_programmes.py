import os

if __name__ == "__main__":
    # Programme 1
    
    print("Lancement du programme 1")

    # Execute lammande ./main out/init_test core/init_state
    os.system("./main out/init_test core/init_state")

    print("Affichage du fichier des registres finaux")

    # Affiche le contenu du fichier core/final.txt les 6 premières lignes
    os.system("head -n 6 core/final.txt")

    print()
    print()

    # Programme 2

    print("Lancement du programme 2")

    # Execute la commande ./main out/add128_test core/add128_state
    os.system("./main out/add128_test core/add128_state")

    print("Affichage du fichier des registres finaux")
    # Affiche le contenu du fichier core/final.txt les 6 premières lignes
    os.system("head -n 6 core/final.txt")

    print()
    print()

    # Programme 3

    print("Lancement du programme 3")

    # Execute la commande ./main out/lshift_64_128_test core/lshift_64_128_state
    os.system("./main out/lshift64_128_test core/lshift64_128_state")

    print("Affichage du fichier des registres finaux")
    # Affiche le contenu du fichier core/final.txt les 6 premières lignes
    os.system("head -n 6 core/final.txt")

    print()
    print()

    # Programme 4

    print("Lancement du programme 4")    

    # Execute la commande ./main out/mul64_test core/mul64_state
    os.system("./main out/mul64_test core/mul64_state")

    print("Affichage du fichier des registres finaux")
    # Affiche le contenu du fichier core/final.txt les 6 premières lignes
    os.system("head -n 6 core/final.txt")

    print()
    print()

