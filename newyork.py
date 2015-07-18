r = ['BLUE', 'LBUE', 'LUBE', 'LUEB', 'BULE', 'UBLE', 'ULBE', 'ULEB', 'BUEL', 'UBEL', 'UEBL', 'UELB', 'BLEU', 'LBEU', 'LEBU', 'LEUB', 'BELU', 'EBLU', 'ELBU', 'ELUB', 'BEUL', 'EBUL', 'EUBL', 'EULB']
def replaceBLUE(str):
    new_list = str.split()
    index = [i for i , x in enumerate(new_list) if x in r]
    for i in index:
        new_list[i] = 'XXXX'
    print new_list
s = raw_input()
res = replaceBLUE(s)
#print res
