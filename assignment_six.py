#
#
#

mytext = open("unit6test", "r")
listOfFileContents = mytext.readlines()
def file_calculations(listOfFileContents):
    lines = 0
    words = ""
    characters = 0
    lines = len(listOfFileContents)
    for x in range(lines):
        list1 = listOfFileContents[x]
        words = list1.split(" ")
        x = x +1
        characters = characters + len(list1)
    print(characters)
    print(lines)
    print(words)

file_calculations(listOfFileContents)