word = input("Input: ")
out = ""

for i in range(len(word)):
    if word[i].lower() in ["a","e","i","o","u"]:
        out = out
    else:
        out = out + word[i]

print("Output: " + out)