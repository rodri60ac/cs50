def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    
    if s[0:1].isalpha() == False:
        return False
    
    for c in s:
        if c in ['.',' ','?','!']:
            return False

    for c in range(len(s)):
        if s[c].isnumeric():
            if s[c] == '0':
                return False
            elif s[c:].isdigit() == False:
                return False
            else:
                return True



main()
