import os

def count_in_text(text):
    characters_count = len(text)
    word_count = len(text.split())
    lines_count = len(text.splitlines())
    print("Number of Characters = ", characters_count)
    print("Number of Words = ", word_count)
    print("Number of Lines = ", lines_count)
    
def count_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        file_name = os.path.basename(file_path)
        characters_count = len(text)
        word_count = len(text.split())
        lines_count = len(text.splitlines())
        
        print("File name: ", file_name)
        print("\tNumber of Characters = ", characters_count)
        print("\tNumber of Words = ", word_count)
        print("\tNumber of Lines = ", lines_count)

    except FileNotFoundError:
        print("ERROR: File not found. Please check the file path.")
    except UnicodeDecodeError:
        print("ERROR:  decoding the file. It may not be in UTF-8 format.")
    except Exception as e:
        print(f"ERROR: An error occurred: {e}")

def count_in_directory(directory_path):
    try:
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)

            if os.path.isdir(file_path):
                print(f"Counting in the internal file: {file_path}")
                count_in_directory(file_path)
            elif os.path.isfile(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        text = file.read()
                        
                    characters_count = len(text)
                    word_count = len(text.split())
                    lines_count = len(text.splitlines())

                    print(f"\tFile: {file_name}")
                    print(f"\t\tNumber of Characters = {characters_count}")
                    print(f"\t\tNumber of Words = {word_count}")
                    print(f"\t\tNumber of Lines = {lines_count}")

                except UnicodeDecodeError:
                    print(f"ERROR: Could not decode {file_name}. It may not be in UTF-8 format.")
                except Exception as e:
                    print(f"ERROR: An error occurred while processing {file_name}: {e}")

    except FileNotFoundError:
        print(f"ERROR: The directory {directory_path} was not found.")
    except Exception as e:
        print(f"ERROR: An error occurred: {e}")



player_choice = ''
while player_choice.lower() != 'q':
    print("1. Text")
    print("2. File")
    print("3. Directory")
    print("q. exit")
    player_choice = input("Choose!: ")
    
    match player_choice:
        case '1':
            text = input("Enter your text: ")
            count_in_text(text)
        case '2':
            path = input("Enter the file path: ")
            count_in_file(path)
        case '3':
            path = input("Enter the directory path: ")
            count_in_directory(path)