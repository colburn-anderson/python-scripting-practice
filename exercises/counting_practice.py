from pathlib import Path
import re

def counting_practice():
    text = (Path(__file__).parent.parent / "data" / "events.txt").read_text()
    print(text)

    users = re.findall(r"\buser=\w+\b", text)
    print(users)

    login_attempts = re.findall(r"\buser=\w+(?=\saction=login)", text)
    print(f"\n{login_attempts}")

    counts = {}
    lines = text.splitlines()

    for line in lines:
        if "action=login" in line:
            user = re.search(r"user=\w+", line).group()
            username = user.split("=")[1]
            counts[username] = counts.get(username, 0) + 1
    print(counts)


        



def main():
    text = counting_practice()
    if not text:
        return



if __name__ =="__main__":
    main()    