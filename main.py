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
            content = file.read()
        
        characters_count = len(content)
        words_count = len(content.split())
        lines_count = len(content.splitlines())
        
        file_base_name, file_extension = os.path.splitext(file_path)
        file_name = os.path.basename(file_base_name)

        print(f"\tFile: {file_name}{file_extension}")
        print(f"\t\tNumber of Characters = {characters_count}")
        print(f"\t\tNumber of Words = {words_count}")
        print(f"\t\tNumber of Lines = {lines_count}")

    except UnicodeDecodeError:
        print(f"ERROR: Could not decode {file_path}. It may not be in UTF-8 format.")
    except Exception as e:
        print(f"ERROR: An error occurred while processing {file_path}: {e}")

def count_in_directory(directory_path):
    try:
        for item_name in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item_name)

            if os.path.isdir(item_path):
                print(f"Counting in the internal directory: {item_path}")
                count_in_directory(item_path)
            elif os.path.isfile(item_path):
                count_in_file(item_path)

    except FileNotFoundError:
        print(f"ERROR: The directory {directory_path} was not found.")
    except Exception as e:
        print(f"ERROR: An error occurred: {e}")

def main():
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


if __name__ == "__main__":
    main()