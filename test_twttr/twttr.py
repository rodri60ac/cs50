def main():
    word = input("Input:")
    output = shorten(word)
    print("Output: " + output)

def shorten(word):
    out = ""
    for i in range(len(word)):
        if word[i].lower() in ["a","e","i","o","u"]:
            out = out
        else:
            out = out + word[i]
    
    return out


if __name__ == "__main__":
    main()
