from pathlib import Path
import re


def read_file(relative_path: str) -> str:
    base_dir = Path(__file__).parent.parent
    file_path = base_dir / relative_path

    with open(file_path, "r") as file:
        return file.read()


def run_logs():
    text = read_file("data/logs.txt")
    print("\n--------LOGS-------\n")
    # print(text)

    lines = text.splitlines() # splits the whole text file into items that are each a line

    for line in lines:

        if re.search(r"\bERROR\b", line): # check if it has the word ERROR in it, if there is a match (it does) print the line
            print(line)

    ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)
    # (?:\d{1,3}\.){3} = find this pattern ( between 1 and 3 digits followed by a dot) 3 times
    # then find between 1 and 3 digits then end
    print(ips)

    redacted_text = re.sub(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", "REDACTED", text)
    print(f"\n {redacted_text}")

    timestamps = re.findall(r"\b\d{4}\-\d{2}\-\d{2}\s\d{2}(?:\:\d{2}){2}\b",text)
    print(timestamps)


def run_contacts():
    text = read_file("data/contacts.txt")

    print("-----Contacts-------")
    
    emails = re.findall(r"\b[\w.-]+@(?:[\w.-]+\.)+[A-Za-z]{2,}\b", text)

    # [] = character choice, match exactly one character, it must be one of these
    # () = Pattern / group of characters all together
    print(emails)

    phones = re.findall(r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]\d{4}", text)
    print(phones)


def run_inventory():
    text = read_file("data/inventory.txt")

    skus = re.findall(r"\bA\-\d{4}\b", text)
    print(skus)

    prices = re.findall(r"\b\d+\.\d{2}\b", text)
    print(prices)

    products = re.findall(r',\s*"([^"]+)"\s*,|,\s*([^,]+)\s*,', text)
    print([p1 or p2 for p1, p2 in products])

    valid_skus = re.findall(r'^A-\d{4},\s*(".+?"|[^,]+),\s*\$?\d+\.\d{2}$', text, re.MULTILINE)
    print(valid_skus)


def run_sample():
    base_dir = Path(__file__).parent.parent
    file_path = base_dir / "data" / "sample.txt"

    with open(file_path, "r") as file:
        text = file.read()

    print(text)

    # numbers = re.findall(r"\d+", text)

    # print("\n -------Numbers-------")
    # print(numbers)

    emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)
    # r"" = python language to treat \ as part of the regex not an escape char
    # \b = word boundary 
    # [\w.-]+ = match one char from these options [], + means match one or more of those chars (Ex: john, john.smith, john-doe)
    # @ = Then after matching those it needs to be followed by an @
    # [\w.-]+ same logic as before (find any sequence of chars, ., or -) but now for the email address
    # \. = then it is followed by a literal . (dot doesnt represent any char)
    # \w+ = then it is followed by any char one or more characters long
    # \b = ending the word boundary

    print("\n-----Emails-----")
    print(emails)

    # cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        # ^ = not any character inside the brackets
        # Match any character that is NOT a letter, number or whitespace
        # Middle comma = what you replace those things with, a space in our case
        # last comma = where we get the text from / where we search through
    # print("\n-------Cleaned text------")
    # print(cleaned)

    words = re.findall(r"[a-zA-Z]+", text)
    # [] character class - find all things in this group
    # a-z = find all lowercase numbers OR
    # A-Z = Or all uppercase numbers
    # + = one or more chars
    # this is how we find all words, the regex says: 
    # Find all places where there is lowercase or uppercase letters in a row and make those chunks (how regex understands a word)

    print("-----Words-------")
    print(words)

    years = re.findall(r"\b(?:19|20)\d{2}\b", text)
    # (?: = match this group but dont save it as a separate result
    # () = return what is in this group
    # (?:) = Return what is in this group AND what is after it

    print("-------Years-------")
    print(years)

    phones = re.findall(r"\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}", text)
    # ( = special regex character, use \ to make it just normal (
    # ? = optional, so accept either ( or nothing
    # \d{3} = find 3 digits in a row
    # \)? = optional ending ), accept if its there or if its not
    # [\s.-] = class of characters, accept \s (space) OR . (dot), OR - (dash) next 
    # \d{3} = then 3 more digits
    # [\s.-] = then a space OR dot OR dash
    # \d{4} = then 4 digits

    print("-----Phone Numbers----")
    print(phones)

def main():
    # run_sample()
    # run_logs()
    # run_contacts()
    run_inventory()

if __name__ == "__main__":
    main()