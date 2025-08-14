#Reverse a given string without using built-in reverse functions
string = input()
rev = ""
for char in string:
    rev=char+rev
print(rev)
