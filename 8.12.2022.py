file = open("C:/Users/skola/Desktop/subory/tabulka_pocetnosti.txt", "r")

lines = file.readlines()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = [0]*26
fin = " "

for i in range(len(lines)):
    fin += lines[i].lower().strip("\n") + " "

for i in range(len(alphabet)):
    nums[i] = fin.count(alphabet[i])












