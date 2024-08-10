import os
import json
from pathlib import Path
from colorama import Fore, Style
from .shared import undo_stack  # Updated import from shared.py
from .language import messages, os_language, LANGUAGE_FUNCTIONS
from .logger import log_message
from collections import Counter
import shutil
from .constants import (
    EXTENSIONS_PERSONNALISER,
    EXTENSIONS_DOCUMENT,
    EXTENSIONS_DOWNLOAD,
    EXTENSIONS_IMAGE,
    EXTENSIONS_MUSIC,
    EXTENSIONS_VIDEO,
    EXTENSIONS_ALL,
    extension_dicts,
)


language_functions = LANGUAGE_FUNCTIONS.get(os_language, LANGUAGE_FUNCTIONS["en"])


def get_folder_category(folder_path, extensions):
    file_types = []

    # Traverse through the folder to identify file types
    for root, _, files in os.walk(folder_path):
        for file in files:
            _, ext = os.path.splitext(file)
            ext = (
                ext.lower().strip()
            )  # Normalize extension: lowercase and strip whitespace
            if ext in extensions:
                file_types.append(extensions[ext])

    # Determine the most common category in the folder
    if file_types:
        most_common_category = Counter(file_types).most_common(1)[0][0]
        return most_common_category
    else:
        return "Divers"  # Fallback if no known file types are found



def move_file(file, target_directory):
    try:
        target_directory.mkdir(parents=True, exist_ok=True)
        original_location = file.resolve()
        shutil.move(str(file), str(target_directory / file.name))
        undo_stack.append(
            (target_directory / file.name, original_location)
        )  # Track the operation
    except Exception as e:
        print(f"Exception when moving file: {e}")


def move_folder(folder, target_directory):
    try:
        target_directory.mkdir(parents=True, exist_ok=True)
        original_location = folder.resolve()
        shutil.move(str(folder), str(target_directory / folder.name))
        undo_stack.append(
            (target_directory / folder.name, original_location)
        )  # Track the operation
    except Exception as e:
        print(f"Exception when moving folder: {e}")


def sort_directory(directory, extensions):
    sorted_folders = set()

    if not directory.exists():
        return False, sorted_folders

    # Sort individual files first
    files = [f for f in directory.iterdir() if f.is_file()]
    for file in files:
        dossier_cible = extensions.get(file.suffix.lower(), "Divers")
        dossier_cible_absolu = directory / dossier_cible
        move_file(file, dossier_cible_absolu)
        sorted_folders.add(str(dossier_cible_absolu))

    # Now sort folders based on their individual contents
    folders = [f for f in directory.iterdir() if f.is_dir()]
    for folder in folders:
        # Analyze the folder independently
        category = get_folder_category(folder, extensions)
        target_directory = directory / category

        # Prevent moving a folder into itself or its own subfolder
        if not str(target_directory).startswith(str(folder)):
            move_folder(folder, target_directory)
            sorted_folders.add(str(target_directory))

    return True, sorted_folders


def clear_console():  # Function to clear the console
    os.system("cls" if os.name == "nt" else "clear")
    log_message("info", messages["console_cleared"])


def save_extensions_to_file(
    EXTENSIONS_MUSIC,
    EXTENSIONS_VIDEO,
    EXTENSIONS_IMAGE,
    EXTENSIONS_DOCUMENT,
    EXTENSIONS_DOWNLOAD,
    EXTENSIONS_PERSONNALISER,
):
    with open("User_Files/extensions.json", "w") as f:
        json.dump(
            {
                "EXTENSIONS_MUSIC": EXTENSIONS_MUSIC,
                "EXTENSIONS_VIDEO": EXTENSIONS_VIDEO,
                "EXTENSIONS_IMAGE": EXTENSIONS_IMAGE,
                "EXTENSIONS_DOCUMENT": EXTENSIONS_DOCUMENT,
                "EXTENSIONS_DOWNLOAD": EXTENSIONS_DOWNLOAD,
                "EXTENSIONS_PERSONNALISER": EXTENSIONS_PERSONNALISER,
            },
            f,
            indent=4,
        )


def load_extensions_from_file():
    try:
        with open("User_Files/extensions.json", "r") as f:
            extensions = json.load(f)
            return (
                extensions["EXTENSIONS_MUSIC"],
                extensions["EXTENSIONS_VIDEO"],
                extensions["EXTENSIONS_IMAGE"],
                extensions["EXTENSIONS_DOCUMENT"],
                extensions["EXTENSIONS_DOWNLOAD"],
                extensions["EXTENSIONS_PERSONNALISER"],
            )
    except FileNotFoundError:  # load the default extensions
        log_message("info", messages["extensions_not_found"])


def ensure_extensions_file_exists():
    extensions_file = Path("User_Files/extensions.json")
    if extensions_file.is_file():
        load_extensions_from_file()
    else:
        extensions = {
            "EXTENSIONS_MUSIC": EXTENSIONS_MUSIC,
            "EXTENSIONS_VIDEO": EXTENSIONS_VIDEO,
            "EXTENSIONS_IMAGE": EXTENSIONS_IMAGE,
            "EXTENSIONS_DOCUMENT": EXTENSIONS_DOCUMENT,
            "EXTENSIONS_DOWNLOAD": EXTENSIONS_DOWNLOAD,
            "EXTENSIONS_PERSONNALISER": EXTENSIONS_PERSONNALISER,
        }
        extensions_file.parent.mkdir(
            parents=True, exist_ok=True
        )  # Ensure the directory exists
        with extensions_file.open("w") as f:
            json.dump(extensions, f, indent=4)


def modify_extensions():
    while True:
        choice = input(language_functions["choose_extensions"].center(100))
        print(Fore.BLUE + "--" * 50 + Style.RESET_ALL)
        if int(choice) == len(extension_dicts) + 1:
            clear_console()
            break
        if (
            not choice.isdigit()
            or int(choice) < 1
            or int(choice) > len(extension_dicts)
        ):
            print(Fore.RED + "Invalid choice.".center(100) + Style.RESET_ALL)
            return

        extension_dict_key = extension_dicts[int(choice) - 1]
        selected_dict = globals()[extension_dict_key]
        clear_console()

        while True:  # other loop to stay in the edit menu
            operation = input(
                language_functions["edit_extensions"].center(100)
            )  # Use the translated menu
            print(Fore.BLUE + "--" * 50 + Style.RESET_ALL)
            clear_console()
            if operation == "1":  # Add an extension
                clear_console()
                print(Fore.CYAN + "--" * 50 + Style.RESET_ALL)
                extension = input(
                    Fore.CYAN
                    + "Enter the extension you want to add (Exemple: .txt): ".center(
                        100
                    )
                    + Style.RESET_ALL
                )
                print(Fore.CYAN + "--" * 50 + Style.RESET_ALL)
                if not extension.startswith("."):
                    extension = "." + extension
                category = input(
                    Fore.CYAN
                    + "Enter the category for this extension (Exemple: Documents): ".center(
                        100
                    )
                    + Style.RESET_ALL
                )
                print(Fore.CYAN + "--" * 50 + Style.RESET_ALL)
                if extension not in selected_dict:
                    selected_dict[extension] = category
                    save_extensions_to_file(
                        EXTENSIONS_MUSIC,
                        EXTENSIONS_VIDEO,
                        EXTENSIONS_IMAGE,
                        EXTENSIONS_DOCUMENT,
                        EXTENSIONS_DOWNLOAD,
                        EXTENSIONS_PERSONNALISER,
                    )
                    print(
                        Fore.GREEN
                        + f"Extension {extension} added to category {category}.".center(
                            100
                        )
                        + Style.RESET_ALL
                    )
                    print(Fore.CYAN + "--" * 50 + "\n" + Style.RESET_ALL)
                    log_message("info", f"Extension {extension} added.")
                else:
                    print(
                        Fore.YELLOW
                        + f"Extension {extension} is already in the dictionary.".center(
                            100
                        )
                        + Style.RESET_ALL
                    )
                    log_message(
                        "warning", f"Attempted to add existing extension {extension}."
                    )
            elif operation == "2":  # Remove an extension
                clear_console()
                # Center the text
                centered_text = "Enter the extension to remove: ".center(100)
                print(Fore.RED + "--" * 50 + Style.RESET_ALL)
                # Get the input with centered text
                extension = input(Fore.GREEN + centered_text + Style.RESET_ALL)
                print(Fore.RED + "--" * 50 + "\n" + Style.RESET_ALL)
                if not extension.startswith("."):
                    extension = "." + extension
                removed = False
                for ext_dict in [
                    EXTENSIONS_MUSIC,
                    EXTENSIONS_VIDEO,
                    EXTENSIONS_IMAGE,
                    EXTENSIONS_DOCUMENT,
                    EXTENSIONS_DOWNLOAD,
                    EXTENSIONS_PERSONNALISER,
                ]:
                    if extension in ext_dict:
                        del ext_dict[extension]
                        removed = True
                        print(Fore.RED + "--" * 50 + Style.RESET_ALL)
                        print(
                            Fore.GREEN
                            + f"Removed {extension} from dictionary.".center(100)
                            + Style.RESET_ALL
                        )
                        print(Fore.RED + "--" * 50 + "\n" + Style.RESET_ALL)
                if removed:
                    save_extensions_to_file(
                        EXTENSIONS_MUSIC,
                        EXTENSIONS_VIDEO,
                        EXTENSIONS_IMAGE,
                        EXTENSIONS_DOCUMENT,
                        EXTENSIONS_DOWNLOAD,
                        EXTENSIONS_PERSONNALISER,
                    )
                    log_message("info", f"Extension {extension} removed.")
                else:
                    print(
                        Fore.YELLOW
                        + f"Extension {extension} does not exist.".center(100)
                        + Style.RESET_ALL
                    )
                    log_message(
                        "warning",
                        f"Attempted to remove non-existing extension {extension}.",
                    )
            elif operation == "3":  # Display all extensions
                clear_console()
                print(Fore.GREEN + "-" * 100 + Style.RESET_ALL)
                for extension, filetype in selected_dict.items():
                    print(Fore.GREEN + f"{extension}: {filetype}" + Style.RESET_ALL)
                print(Fore.GREEN + "-" * 100 + "\n" + Style.RESET_ALL)
                log_message("info", "Displayed all extensions.")
            elif operation == "4":  # Quit the edit menu
                clear_console()
                break
            else:
                print(Fore.RED + "--" * 50 + Style.RESET_ALL)
                print(
                    Fore.RED
                    + "Invalid choice, please try again.".center(100)
                    + Style.RESET_ALL
                )
                print(Fore.RED + "--" * 50 + "\n" + Style.RESET_ALL)


def save_folder_paths_to_file(folder_paths):
    with open("User_Files/folder_paths.json", "w") as f:
        json.dump(folder_paths, f, indent=4)


def load_folder_paths_from_file():
    try:
        with open("User_Files/folder_paths.json", "r") as f:
            folder_paths = json.load(f)
            return folder_paths
    except FileNotFoundError:
        log_message("info", "Folder paths file not found.")
        return {}


def ensure_folder_paths_file_exists():
    folder_paths_file = Path("User_Files/folder_paths.json")
    if folder_paths_file.is_file():
        load_folder_paths_from_file()
    else:
        folder_paths = {}  # default folder paths
        folder_paths_file.parent.mkdir(
            parents=True, exist_ok=True
        )  # Ensure the directory exists
        with folder_paths_file.open("w") as f:
            json.dump(folder_paths, f, indent=4)


def ensure_log_file_exists():
    log_file = Path("User_Files/file_sorter.log")
    if not log_file.exists():
        log_file.parent.mkdir(parents=True, exist_ok=True)
        log_file.touch()


def modify_folder_paths():
    clear_console()
    while True:
        folder_paths = load_folder_paths_from_file()
        choice = input(
            Fore.GREEN + language_functions["edit_folder"].center(100) + Style.RESET_ALL
        )
        print(Fore.BLUE + "--" * 50 + "\n" + Style.RESET_ALL)

        if choice == "1":  # Add a new folder
            clear_console()
            add_new_folder()
        elif choice == "2":  # Delete a folder
            clear_console()
            remove_folder_path()
        elif choice == "3":  # Display all folders
            clear_console()
            show_all_folder_paths()
        elif choice == "4":  # Quit the edit menu
            clear_console()
            break
        else:
            print(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL)


def add_new_folder():
    print(Fore.BLUE + "--" * 50 + Style.RESET_ALL)
    folder_name = input(
        Fore.GREEN + "Enter the name of the folder: ".center(100) + Style.RESET_ALL
    )
    print(Fore.BLUE + "--" * 50 + Style.RESET_ALL)
    folder_path = input(
        Fore.GREEN
        + "Enter the absolute path to the folder: ".center(100)
        + Style.RESET_ALL
    )
    print(Fore.BLUE + "--" * 50 + Style.RESET_ALL)

    # If the user didn't enter anything, use the current directory
    if not folder_path:
        folder_path = str(Path.cwd())
    # Check if the path exists
    elif not Path(folder_path).exists():
        print(
            Fore.RED
            + f"Path {folder_path} does not exist.".center(100)
            + Style.RESET_ALL
        )
        return

    # Load the existing data from the JSON file
    try:
        with open("User_Files/folder_paths.json", "r") as file:
            folder_paths = json.load(file)
    except FileNotFoundError:
        folder_paths = {}

    # Add the new folder to the folder_paths dictionary
    folder_paths[folder_name] = folder_path

    # Write the updated folder_paths dictionary back to the JSON file
    with open("User_Files/folder_paths.json", "w") as file:
        json.dump(folder_paths, file, indent=4)

    print(
        Fore.BLUE
        + f"Folder path {folder_path} added with name {folder_name}.".center(100)
        + Style.RESET_ALL
    )


def remove_folder_path():
    print(Fore.BLUE + "--" * 50 + Style.RESET_ALL)
    folder_name = input(
        Fore.GREEN
        + "Enter the name of the folder you want to delete:".center(100)
        + Style.RESET_ALL
    )
    print(Fore.BLUE + "--" * 50 + Style.RESET_ALL)
    folder_paths = load_folder_paths_from_file()

    # If the folder name is in the dictionary, delete it
    if folder_name in folder_paths:
        del folder_paths[folder_name]
        save_folder_paths_to_file(folder_paths)
        print(
            Fore.BLUE + f"Folder {folder_name} deleted.".center(100) + Style.RESET_ALL
        )
    else:
        print(
            Fore.RED + f"Folder {folder_name} not found.".center(100) + Style.RESET_ALL
        )
    print(Fore.BLUE + "--" * 50 + "\n" + Style.RESET_ALL)


def show_all_folder_paths():
    folder_paths = load_folder_paths_from_file()

    # If there are folder paths, display them
    if folder_paths:
        for name, path in folder_paths.items():
            print(
                Fore.LIGHTBLUE_EX
                + f"Name: {name}, Path: {path}".center(100)
                + Style.RESET_ALL
            )
    else:
        print(Fore.RED + "No folder paths found.".center(100) + Style.RESET_ALL)


def validate_folder_paths():
    folder_paths = load_folder_paths_from_file()
    for folder_name, folder_path in folder_paths.items():
        print(f"Folder Name: {folder_name}")
        print(f"Folder Path: {folder_path}")
        if Path(folder_path).is_dir():
            print(f"The folder {folder_name} exists at the given path.")
        else:
            print(f"The folder {folder_name} does not exist at the given path.")
