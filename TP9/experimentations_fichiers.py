f1 = open('fichier1.txt', 'w')
f1.write('bla1\n')
f1.write('blabla1\n')
f1.close()

with open('fichier2.txt', 'w') as f2:
    f2.write('texte1\ntexte2\n')
    f2.writelines(['texte3', 'texte4'])
    f2.writelines(['texte5\n', 'texte6\n'])
