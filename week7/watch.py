import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(r"(?:https://|http://)(?:www\.)?youtube\.com/embed/(.+?)(?=\")", s):
        return pack(matches.group(1))
    else:
        return None
    
def pack(url):
    return f"https://youtu.be/{url}"







if __name__ == "__main__":
    main()