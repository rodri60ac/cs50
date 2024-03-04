def main():
    sentence = input("Sentence: ")
    sentence = convert(sentence)
    print("Converted Sentence: " + sentence)


def convert(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    return string


main()
