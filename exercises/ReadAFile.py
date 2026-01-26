import re

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()
            words = re.findall(r'\b\w+\b', content)
            return len(words)
            
            
    except FileNotFoundError:
        return f"Error: '{file_path}' not found. "     


'''
def read_a_file:
    
        try:
            with open(file_path, 'r') as file:
                for i in range(4):
                     print(file.readline().strip())
                     print("line break")
                
        except FileNotFoundError:
            print("File not found")            
        
'''            
''' prints each line of the file line by line, uses for loop
        try:
            with open(file_path, 'r') as file:
                for line in file:
                     print(line, end='')


        except FileNotFoundError:
            print("file not found")
    
'''


''' opens the file nicely and prints the entire thing in the terminal
    try:
            with open(file_path, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("Error: 'sample.txt' not found")

    pass
'''

def main():
    file_path = "data/sample.txt"


if __name__ == "__main__":
    main()