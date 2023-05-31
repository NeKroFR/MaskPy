import sys
from functions import obfuscate

def display_banner_and_collect_filename():
    """
    Display a banner and collect filename input from the user.
    
    Returns:
        str: The input filename.
    """
    banner = """\033[92m
  __  __           _    _____       
 |  \/  |         | |  |  __ \      
 | \  / | __ _ ___| | _| |__) |   _ 
 | |\/| |/ _` / __| |/ /  ___/ | | |
 | |  | | (_| \__ \   <| |   | |_| |
 |_|  |_|\__,_|___/_|\_\_|    \__, |
                               __/ |
                              |___/ """
    print(banner)
    filename = input("""\033[1;35mDrag the file to be obfuscated here : \033[0m""")
    
    # Remove enclosing quotes if present
    if filename[0] == filename[-1] and filename[0] in ("'", '"'):
        filename = filename[1:-1]

    return filename


def read_file(filename):
    """
    Open and read a Python file.

    Parameters:
        filename (str): The name of the file to be opened.

    Returns:
        list: The content of the file split by lines.

    Raises:
        SystemExit: If the filename does not end in '.py' or if the file does not exist.
    """
    if not filename.endswith(".py"):
        print("\033[91mError: \033[0mYou must choose a Python file!")
        sys.exit()

    try:
        with open(filename, "r", encoding='utf-8') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print("\033[91mError: \033[0mFile does not exist!")
        sys.exit()


def write_obfuscated_file(code, filename):
    """
    Write obfuscated code to a file.

    Parameters:
        code (str): The obfuscated code to be written.
        filename (str): The name of the file to be written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(code)

    print("\033[1;32mSuccess:\033[0m The file has been successfully obfuscated")


def main():
    """
    The main function to handle user input, file obfuscation, and saving.
    """
    arg_count = len(sys.argv)

    if arg_count == 1:
        filename = display_banner_and_collect_filename()
        obfuscated_filename = filename[:-3] + "_obfuscated.py"        
    elif arg_count in (2, 3):
        filename = sys.argv[1]
        obfuscated_filename = sys.argv[2] if arg_count == 3 else filename[:-3] + "_obfuscated.py"
    else:
        print("Error: Too many arguments")
        sys.exit()

    obfuscated = obfuscate(read_file(filename))
    write_obfuscated_file(obfuscated, obfuscated_filename)


if __name__ == "__main__":
    main()
