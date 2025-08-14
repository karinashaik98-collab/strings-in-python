#check the given string is palindrome or not
string = input()
rev = ""
for char in string:
    rev=char+rev
if string == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
