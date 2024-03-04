import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    if link := re.search(r'"https?://(?:www\.)?youtube.com/embed/(.+?)"', s):
        return "https://youtu.be/"+link.group(1)
    else:
        return None


if __name__ == "__main__":
    main()
