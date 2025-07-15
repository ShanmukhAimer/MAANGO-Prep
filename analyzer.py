import string

def analyzer(text):
    txtLower = text.lower()                                 #Characters coverted to lower case
    Ptext = (''.join([char for char in txtLower if char not in string.punctuation])).split()    #Removed punctuations using string module
    dic = dict(map(lambda pt:(pt,len(pt)), Ptext))                                              #Used Lambda expression to create a dictonary
    tup = tuple(dic.items())                                                                    #Converted into tuple
    sortedTup = sorted(tup, key=lambda pair: pair[1], reverse=True)                             #Rearranged into descending order
    return sortedTup


print(analyzer("""
The quick brown fox jumps over the lazy dog. 
Never underestimate the power of a good book. 
The best time to plant a tree was 20 years ago. The second best time is now.
"""))
