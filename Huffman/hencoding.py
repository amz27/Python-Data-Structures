import sys

def Encoder(codeDict, inputStr):
    s = ''
    for i in range(0, len(inputStr)):
         s += ((codeDict[inputStr[i]]))
    return s
# Read input
n = int(sys.stdin.readline().strip('\n'))
codeDictionary = {}

for i in xrange(n):
    character, code = sys.stdin.readline().strip('\n').split()
    codeDictionary[character] = code
plainString = sys.stdin.readline().strip('\n')
codedString = Encoder(codeDictionary, plainString)
print codedString
