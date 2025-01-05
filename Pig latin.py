vocals = ['a','e','i','o','u']


def rule1(wrd):
    return wrd.startswith(('xr', 'yt')) or wrd[0] in vocals


def rule2(wrd, i):
    return wrd[i] not in vocals


# Checks for cases 'q' is followed by 'u' somewhere at the start of the text
def rule3(wrd, i):
    return (wrd[i]=='q' and wrd[i+1]=='u') or (wrd[i-1]=='q' and wrd[i]=='u') 


def rule4(wrd, i):
    return not (i>0 and wrd[i] == 'y')


# Pushes the consonants (with some exceptions) at the start of the text to the end. 
def pushConsonants(wrd):
    i = 0
    while ((rule2(wrd,i) or rule3(wrd,i)) and rule4(wrd,i)):
        i += 1
    return wrd[i:] + wrd[0:i]


# Translates a word to piglatin and returns it.
def translatedWrd(wrd):
    ret = wrd
    if (not rule1(wrd)):
        ret = pushConsonants(wrd)
    return ret + 'ay'


# Returns an entire lowercase text translated to piglatin.
# The text can't have special characters
def translate(text):
    wrds = text.split()
    ret = ""
    for w in wrds:
        ret += translatedWrd(w) + ' '
    return ret[:-1]
  
