import os
import shutil


def get_temp_folder(username):
    return "C:\\Users\\{}\\AppData\\Local\\Temp".format(username)

def print_temp_folder_content(temp_folder):
    files = [f for f in os.listdir(temp_folder)]
    print("Content in your temp folder:\n\n")
    for item in files:
        print(item)

def delete_temp_folder(temp_folder):
    try:
        shutil.rmtree(temp_folder)
    except PermissionError:
        print("Some files are kept as some processes are using it")
        print("Please close those applications and then run this script again.")
        return False
    except FileNotFoundError:
        print("No Temporary files exist!")
        return False

    return True

def main():
    print("Save your work and close all the programs.")
    username = input("Enter your registered username on Windows: ")
    temp_folder = get_temp_folder(username)

    while True:
        if not os.path.exists(temp_folder):
            print("\nThe temp folder doesn't exist.")
            choice = input("Type 'quit' to exit: ") 
            if choice.lower() == 'quit':
                exit()

        else:
            print_temp_folder_content(temp_folder)
            print()
            choice = input("Do you want to continue?[y/n]: ")
            if choice.lower() == 'y':
                success = delete_temp_folder(temp_folder)
                if success:
                    print("\nAll temporary files have been deleted from the temp folder.\n")
                choice = input("Type 'quit' to exit: ") 
                if choice.lower() == 'quit':
                    exit()
            else:
                exit()

if __name__ == "__main__":
    main()
