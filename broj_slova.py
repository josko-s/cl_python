import pwinput

def letter_count(str):
    moj_x = {}
    for l in str:
        if moj_x.get(l) != None:
            moj_x.update({l:moj_x.get(l)+1})
        else:
            moj_x[l] = 1
            #print(moj_x)
    return moj_x

def pozicija(str, stara, lett):
    novi_blanks = ""
    for p in range(len(str)):
        if lett == str[p]:
            novi_blanks = novi_blanks + lett
        else:
            novi_blanks = novi_blanks + stara[p]
    return novi_blanks

def create_blanks(str):
    blanks = ""
    for a in str:
        blanks = blanks + '_'
    return blanks

a = pwinput.pwinput(prompt='',mask="")
#print(a)
b = create_blanks(a)
print(b)

novi = ""

while novi != a:
    slovo = input("Pokusaj: ")
    novi = pozicija(a, b, slovo)
    b = novi
    print(novi)

