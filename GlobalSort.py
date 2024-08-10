#!/usr/bin/python3
from pathlib import Path
import sys
from src.constants import (
    MENU_CHOICE,
    EXTENSIONS_MUSIC,
    EXTENSIONS_VIDEO,
    EXTENSIONS_IMAGE,
    EXTENSIONS_DOCUMENT,
    EXTENSIONS_DOWNLOAD,
    EXTENSIONS_ALL,
)
from src.logger import setup_logging
from src.menu import print_message
from src.language import os_language, directories_name, messages, LANGUAGE_FUNCTIONS
from src.utils import (
    sort_directory,
    clear_console,
    ensure_extensions_file_exists,
    modify_extensions,
    ensure_folder_paths_file_exists,
    modify_folder_paths,
    load_folder_paths_from_file,
    ensure_log_file_exists,
)
from src.undo import undo_all_operations
from colorama import Fore, Style
import sys
import subprocess
import platform


def update_program():  # Function to update the program
    try:
        # Get the path to the top-level directory of the current Git repository
        repo_path = (
            subprocess.check_output(["git", "rev-parse", "--show-toplevel"])
            .strip()
            .decode("utf-8")
        )
    except subprocess.CalledProcessError:
        print(Fore.RED + "-" * 100 + Style.RESET_ALL)
        print(
            Fore.RED
            + "{}".format(
                "Not in the Project Github repository. Skipping update and continuing execution.".center(100)
            )
            + Style.RESET_ALL
        )
        launch_program()
    try:
        # Fetch the latest changes from the remote repository
        subprocess.run(["git", "-C", repo_path, "fetch"], check=True)

        # Check if there are any differences between the local and remote repositories
        diff_output = subprocess.check_output(
            ["git", "-C", repo_path, "diff", "--stat", "HEAD..origin/main"]
        ).strip()

        if diff_output:
            print("Updates are available. Do you want to update? (Y/n)")
            choice = input().lower()
            if choice == "Y" or choice == "":
                if platform.system() == "Windows":
                    subprocess.check_call(["git", "-C", repo_path, "pull"])
                else:
                    subprocess.run(["git", "-C", repo_path, "pull"], check=True)

                print(Fore.BLUE + "-" * 100 + Style.RESET_ALL)
                print(
                    Fore.BLUE
                    + "{}".format(
                        "The program has been updated. Please restart the program.".center(
                            100
                        )
                    )
                    + Style.RESET_ALL
                )
                print(Fore.BLUE + "-" * 100 + Style.RESET_ALL)
                sys.exit(0)
        else:
            print(Fore.GREEN + "-" * 100 + Style.RESET_ALL)
            print(Fore.GREEN + "No updates available.".center(100) + Style.RESET_ALL)
            print("\n")
            print(
                Fore.GREEN
                + "{}".format("Starting the program...".center(100))
                + Style.RESET_ALL
            )
            print(Fore.GREEN + "-" * 100 + Style.RESET_ALL)
            launch_program()

    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)


def main():  # Main function that runs the program
    sorted_flag = False  # Flag to keep track if any file has been moved
    sorted_folders = set()  # Set to keep track of the sorted folders
    while True:
        language_functions = LANGUAGE_FUNCTIONS.get(
            os_language, LANGUAGE_FUNCTIONS["en"]
        )
        user_choice = input(language_functions["menu"])
        print(Fore.BLUE + "--" * 50 + Style.RESET_ALL)
        if user_choice not in MENU_CHOICE:
            clear_console()
            print_message(
                language_functions["color"],
                language_functions["invalid_choice_message"],
            )
            print(Fore.BLUE + "-" * 100 + Style.RESET_ALL)
            continue
        if user_choice == "1":  # Sort music files
            sorted_flag, new_folders = sort_directory(
                Path.home() / directories_name["Music"], EXTENSIONS_MUSIC
            )
            clear_console()
            sorted_folders.update(new_folders)
            if sorted_flag:  # Only print if any file has been moved
                for folder in sorted_folders:
                    print(
                        Fore.BLUE
                        + "{}\n".format("-" * 100)
                        + Fore.BLUE
                        + "{}".format(
                            messages["file_sorted"]
                            .format(directory=folder)
                            .center(100),
                        )
                        + Style.RESET_ALL
                    )
            else:  # Print a different message if no files have been moved
                print(
                    Fore.BLUE
                    + "{}\n".format("-" * 100)
                    + Fore.RED
                    + "{}".format("No files were moved.".center(100))
                    + Style.RESET_ALL
                )
        elif user_choice == "2":  # Sort video files
            sorted_flag, new_folders = sort_directory(
                Path.home() / directories_name["Videos"], EXTENSIONS_VIDEO
            )
            clear_console()
            sorted_folders.update(new_folders)
            if sorted_flag:  # Only print if any file has been moved
                for folder in sorted_folders:
                    print(
                        Fore.BLUE
                        + "{}\n".format("-" * 100)
                        + Fore.BLUE
                        + "{}".format(
                            messages["file_sorted"]
                            .format(directory=folder)
                            .center(100),
                        )
                        + Style.RESET_ALL
                    )
            else:  # Print a different message if no files have been moved
                print(
                    Fore.BLUE
                    + "{}\n".format("-" * 100)
                    + Fore.RED
                    + "{}".format("No files were moved.".center(100))
                    + Style.RESET_ALL
                )
        elif user_choice == "3":  # Sort image files
            sorted_flag, new_folders = sort_directory(
                Path.home() / directories_name["Images"], EXTENSIONS_IMAGE
            )
            clear_console()
            sorted_folders.update(new_folders)
            if sorted_flag:  # Only print if any file has been moved
                for folder in sorted_folders:
                    print(
                        Fore.BLUE
                        + "{}\n".format("-" * 100)
                        + Fore.BLUE
                        + "{}".format(
                            messages["file_sorted"]
                            .format(directory=folder)
                            .center(100),
                        )
                        + Style.RESET_ALL
                    )
            else:  # Print a different message if no files have been moved
                print(
                    Fore.BLUE
                    + "{}\n".format("-" * 100)
                    + Fore.RED
                    + "{}".format("No files were moved.".center(100))
                    + Style.RESET_ALL
                )
        elif user_choice == "4":  # Sort document files
            sorted_flag, new_folders = sort_directory(
                Path.home() / directories_name["Documents"], EXTENSIONS_DOCUMENT
            )
            clear_console()
            sorted_folders.update(new_folders)
            if sorted_flag:  # Only print if any file has been moved
                for folder in sorted_folders:
                    print(
                        Fore.BLUE
                        + "{}\n".format("-" * 100)
                        + Fore.BLUE
                        + "{}".format(
                            messages["file_sorted"]
                            .format(directory=folder)
                            .center(100),
                        )
                        + Style.RESET_ALL
                    )
            else:  # Print a different message if no files have been moved
                print(
                    Fore.BLUE
                    + "{}\n".format("-" * 100)
                    + Fore.RED
                    + "{}".format("No files were moved.".center(100))
                    + Style.RESET_ALL
                )
        elif user_choice == "5":  # Sort download files
            sorted_flag, new_folders = sort_directory(
                Path.home() / directories_name["Downloads"], EXTENSIONS_DOWNLOAD
            )
            clear_console()
            sorted_folders.update(new_folders)
            if sorted_flag:  # Only print if any file has been moved
                for folder in sorted_folders:
                    print(
                        Fore.BLUE
                        + "{}\n".format("-" * 100)
                        + Fore.BLUE
                        + "{}".format(
                            messages["file_sorted"]
                            .format(directory=folder)
                            .center(100),
                        )
                        + Style.RESET_ALL
                    )
            else:  # Print a different message if no files have been moved
                print(
                    Fore.BLUE
                    + "{}\n".format("-" * 100)
                    + Fore.RED
                    + "{}".format("No files were moved.".center(100))
                    + Style.RESET_ALL
                )
        elif user_choice == "6":  # Sort a specific folder
            try:
                print(Fore.BLUE + "{}".format("-" * 100) + Style.RESET_ALL)
                Custom_DIR = Path(
                    input(
                        Fore.BLUE
                        + "{}".format("Enter the path of the folder? ".center(100, " "))
                        + Style.RESET_ALL
                    )
                )
                if not Custom_DIR.exists():
                    print(Fore.BLUE + "{}".format("-" * 100) + Style.RESET_ALL)
                    print(
                        Fore.RED
                        + "{}".format(
                            "The specified path does not exist.".center(100, " ")
                        )
                        + Style.RESET_ALL
                    )
                    print(Fore.BLUE + "{}".format("-" * 100) + Style.RESET_ALL)
                    return
                sorted_flag, new_folders = sort_directory(Custom_DIR, EXTENSIONS_ALL)
                clear_console()
                sorted_folders.update(new_folders)
                if sorted_flag:  # Only print if any file has been moved
                    for folder in sorted_folders:
                        print(
                            Fore.BLUE
                            + "{}\n".format("-" * 100)
                            + Fore.BLUE
                            + "{}".format(
                                messages["file_sorted"]
                                .format(directory=folder)
                                .center(100),
                            )
                            + Style.RESET_ALL
                        )
                else:  # Print a different message if no files have been moved
                    print(
                        Fore.BLUE
                        + "{}\n".format("-" * 100)
                        + Fore.RED
                        + "{}".format("No files were moved.".center(100))
                        + Style.RESET_ALL
                    )
            except Exception as e:
                print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)
        elif user_choice == "7":  # Sort all the directories
            sorted_flag, new_folders = sort_directory(
                Path.home() / directories_name["Music"], EXTENSIONS_MUSIC
            )
            clear_console()
            sorted_folders.update(new_folders)
            sorted_flag, new_folders = sort_directory(
                Path.home() / directories_name["Videos"], EXTENSIONS_VIDEO
            )
            clear_console()
            sorted_folders.update(new_folders)
            sorted_flag, new_folders = sort_directory(
                Path.home() / directories_name["Images"], EXTENSIONS_IMAGE
            )
            clear_console()
            sorted_folders.update(new_folders)
            sorted_flag, new_folders = sort_directory(
                Path.home() / directories_name["Downloads"], EXTENSIONS_DOWNLOAD
            )
            clear_console()
            sorted_folders.update(new_folders)
            sorted_flag, new_folders = sort_directory(
                Path.home() / directories_name["Documents"], EXTENSIONS_DOCUMENT
            )
            clear_console()
            sorted_folders.update(new_folders)
            folder_paths = load_folder_paths_from_file()
            try:
                folder_name, folder_path = next(iter(folder_paths.items()))
            except StopIteration:
                print("No custom folders to sort.")
            else:
                for folder_name, folder_path in folder_paths.items():
                    if Path(folder_path).is_dir():
                        sorted_flag, new_folders = sort_directory(
                            Path(folder_path), EXTENSIONS_ALL
                        )
                        clear_console()
                        sorted_folders.update(new_folders)
            if sorted_flag:  # Only print if any file has been moved
                clear_console()
                for folder in sorted_folders:
                    print(
                        Fore.BLUE
                        + "{}\n".format("-" * 100)
                        + Fore.BLUE
                        + "{}".format(
                            messages["file_sorted"]
                            .format(directory=folder)
                            .center(100),
                        )
                        + Style.RESET_ALL
                    )
            else:  # Print a different message if no files have been moved
                clear_console()
                print(
                    Fore.BLUE
                    + "{}\n".format("-" * 100)
                    + Fore.RED
                    + "{}".format("No files were moved.".center(100))
                    + Style.RESET_ALL
                )
        elif user_choice == "8":  # Add a folder to the sorting program
            clear_console()
            modify_folder_paths()
        elif user_choice == "9":  # Modify extensions
            clear_console()
            modify_extensions()
        elif user_choice == "10":  # Revert the changes
            clear_console()
            undo_all_operations()
        elif user_choice == "11":  # Display the help menu
            clear_console()
            print(language_functions["help"])
        elif user_choice == "12":  # Quit the program
            print(Fore.BLUE + "-" * 100 + Style.RESET_ALL)
            if os_language == "fr":
                clear_console()
                print(
                    Fore.BLUE
                    + "-" * 100
                    + "\n"
                    + Fore.RED
                    + "Fermeture du programme".center(100)
                    + Style.RESET_ALL
                )
            elif os_language == "en":
                clear_console()
                print(
                    Fore.BLUE
                    + "-" * 100
                    + "\n"
                    + Fore.RED
                    + "Closing the program".center(100)
                    + Style.RESET_ALL
                )
            elif os_language == "es":
                clear_console()
                print(
                    Fore.BLUE
                    + "-" * 100
                    + "\n"
                    + Fore.YELLOW
                    + "Cerrando el programa".center(100)
                    + Style.RESET_ALL
                )
            elif os_language == "it":
                clear_console()
                print(
                    Fore.BLUE
                    + "-" * 100
                    + "\n"
                    + Fore.BLUE
                    + "Chiusura del programma".center(100)
                    + Style.RESET_ALL
                )
            elif os_language == "de":
                clear_console()
                print(
                    Fore.BLUE
                    + "-" * 100
                    + "\n"
                    + Fore.MAGENTA
                    + "Schließen des Programms".center(100)
                    + Style.RESET_ALL
                )
            elif os_language == "ru":
                clear_console()
                print(
                    Fore.BLUE
                    + "-" * 100
                    + "\n"
                    + Fore.CYAN
                    + "Закрытие программы".center(100)
                    + Style.RESET_ALL
                )
            print(Fore.BLUE + "-" * 100 + Style.RESET_ALL)
            sys.exit()

def launch_program():
    ensure_log_file_exists()
    setup_logging()
    ensure_extensions_file_exists()
    ensure_folder_paths_file_exists()
    main()


if __name__ == "__main__":  # Run the main function
    update_program()
