# Creating a string:
#=====================

name = "viRat KoHli"
# name = 'Jannik'
# name = """de 
#             Villers""" #maintains line breaks and white spaces.

print(name)
print('''He said, "It's not so difficult to learn Python. 
In fact it's quite Easy".''') 

# length & Indexing a string:
#===============================
lang="Python"
print(len(lang))

print(lang[0], lang[2], lang[5])
# print(lang[18]) #-----> ERROR: string index out of Range
print(lang[-1], lang[-4]) #Negative indexing: pos_index-len()

# Methods on Strings:
#=======================

## 1. count()
print("committee".count('e'))
print("committee".count('E')) #case sensitive
print("committee".count('ee'))
print(name.count('p'))
print("aaaa".count('aa')) #no overlapping --> 2

## case coversion:-
print(name.upper(), name.lower(), name.capitalize(), name.title(), name.swapcase())

## searching & matching
say = "You Know if you Know!"
print(say.find('i'))  #returns the index of a character or substring
print(say.find('Know'))
print(say.find('w'))  #returns the index of the first instance
print(say.find('you Know'))   #Case Sensitive
print(say.find('do not Know'))   #if not present, returns -1
# print(name.index('do')) #if not present, ValueError

print(name.rfind('Know')) #name.rindex('y')

print(name.startswith('vi'))
print(name.endswith('I'))

## Validations:-
# isalpha(), isalnum(), isascii(), isdecimal(), isdigit(), isnumeric(), isspace(), isupper(), islower() etc. --> all returns Bool value.

## Trimming:-
string = "   I have some space     within and around me    "
print(string)
print(string.strip())
print(string.lstrip())
print(string.rstrip())
print("jannik Sinn".strip('jnr'))

## Spliting:-
s1 = "One-Two Three-Four-Five-Six"
print(s1.split())
print(s1.split('-'))
print(s1.split('a'))
print(s1.split('-', 2)) #split with `maxsplit``
print(s1.rsplit('-', 2)) #split from right -- the order is still maintained, even though split from right.

#splitlines()

## Joining:-
print("-**-".join(['A', 'B', 'C']))
print("".join(('A', 'B', 'C'))) #can pass a tuple too, but the items inside should be strings

## Partitioning:-
### diff from split? -- Always splits the string into three parts... left_of_separator, separator, right_of_separator
print(s1.partition('-'))

### similarly there is rpartition()

## Replacement:-
print("ToDo".replace("o","a"))
print("ToDo".replace("O","a")) #no change is not found
print("ToDo".replace("o","a",1))

print("aaa".replace('aa','b')) #--> 'ba' not 'bb' --> just like count, it is non-overlapping.

## Padding and Alignement:-
s2 = "align_me"
print(s2.center(10))
print(s2.center(9))
print(s2.center(10,"*"))
print(s2.center(9, "*"))
# print(s2.center(9, "**")) #Filler should always be of one character.

print(s2.ljust(12,"*"))
print(s2.rjust(3, "*")) #no trim of the string

print("42".zfill(5)) #fills extra spots with ZEROS
print("-42".zfill(5)) # -, + are kept at the beginning only
