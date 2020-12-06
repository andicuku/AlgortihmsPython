string1 = input("Enter first string ")
string2 = input("Enter second string ")
def anagrams(string1,string2):
    string1=sorted(string1)
    string2=sorted(string2)
    if len(string1)==len(string2) and string1==string2:
        return True
    else:
        return False
if anagrams(string1,string2):
    print(True)
else:
    print(False)