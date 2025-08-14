#count no of vowels and consonents
string="air"
vowelscount=0
consonantscount=0
for char in string:
    if char.isalpha():
        if char.upper() in "AEIOU":
            vowelscount+=1
        else:
            consonantscount+=1
print(vowelscount)
print(consonantscount)
