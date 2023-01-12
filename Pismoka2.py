file = open("C:/Users/skola/Desktop/subory/tabulka_pocetnosti.txt", "r")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']

fin = len(alphabet) * [0]

lines = file.readlines()

for j in range(len(lines)):
    x = lines[j].strip("\n").lower()

    for i in range(len(x)):
        if x[i] in alphabet:
            fin[alphabet.index(x[i])] +=1

fin

most_common = alphabet[fin.index(max(fin))]
most_common