#
#
#
mytext = open("unit6test", "r")
listOfFileContents = mytext.readlines()


def file_calculations(listOfFileContents):
    lines = 0
    z = 0
    words = 0
    characters = 0
    lines = len(listOfFileContents)
    for x in range(lines):
        list1 = listOfFileContents[x]
        s = list1.split(" ")
        z = z + len(s)
        characters = characters + len(list1)
    print(characters)
    print(lines)
    print(words)
file_calculations(listOfFileContents)