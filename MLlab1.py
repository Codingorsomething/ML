something=input("Enter a word: ")
vowels=0
consonents=0
for x in something:
    if x.lower() in "aeiou":
        vowels+=1
    else:
        consonents+=1
print("No of vowels=",vowels)
print("No of consonents=",consonents)





