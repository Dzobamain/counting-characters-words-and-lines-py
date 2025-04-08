from count import count_in_text, count_in_file, count_in_directory

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