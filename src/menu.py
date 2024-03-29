from colorama import Fore, Style
from .constants import extension_dicts


def generate_menu(language):  # Function to generate the menu in the correct language
    menu_options = {
        "fr": [
            "OPTIONS DE MENU:",
            "1 - Trier les fichiers de musique",
            "2 - Trier les fichiers de vidéo",
            "3 - Trier les fichiers de images",
            "4 - Trier les fichiers de documents",
            "5 - Trier les fichiers de download",
            "6 - Trier les fichiers d'un dossier spécifique",
            "7 - Trier tous les répertoires",
            "8 - Modifier les dossiers du programme de trie",
            "9 - Modifier les extensions du programme de trie",
            "10 - Annuler la dernière opération",
            "11 - Afficher le menu d'aide",
            "12 - Quitter le programme",
        ],
        "en": [
            "MENU OPTIONS:",
            "1 - Sort music files",
            "2 - Sort video files",
            "3 - Sort image files",
            "4 - Sort document files",
            "5 - Sort download files",
            "6 - Sort files from a specific directory",
            "7 - Sort all directories",
            "8 - Edit the folders of the sorting program",
            "9 - Edit the extensions of the sorting program",
            "10 - Undo last operation",
            "11 - Display the help menu",
            "12 - Quit the program",
        ],
        "es": [
            "OPCIONES DE MENÚ:",
            "1 - Ordenar archivos de música",
            "2 - Ordenar archivos de video",
            "3 - Ordenar archivos de imágenes",
            "4 - Ordenar archivos de documentos",
            "5 - Ordenar archivos de descarga",
            "6 - Ordenar archivos de un directorio específico",
            "7 - Ordenar todos los directorios",
            "8 - Editar las carpetas del programa de clasificación",
            "9 - Editar las extensiones del programa de clasificación",
            "10 - Deshacer la última operación",
            "11 - Mostrar el menú de ayuda",
            "12 - Salir del programa",
        ],
        "it": [
            "OPZIONI MENU:",
            "1 - Ordina i file musicali",
            "2 - Ordina i file video",
            "3 - Ordina i file immagine",
            "4 - Ordina i file di documento",
            "5 - Ordina i file di download",
            "6 - Ordina i file da una directory specifica",
            "7 - Ordina tutte le directory",
            "8 - Modifica le cartelle del programma di ordinamento",
            "9 - Modifica le estensioni del programma di ordinamento",
            "10 - Annulla l'ultima operazione",
            "11 - Visualizza il menu di aiuto",
            "12 - Esci dal programma",
        ],
        "de": [
            "MENÜOPTIONEN:",
            "1 - Musikdateien sortieren",
            "2 - Videodateien sortieren",
            "3 - Bilddateien sortieren",
            "4 - Dokumentdateien sortieren",
            "5 - Download-Dateien sortieren",
            "6 - Dateien aus einem bestimmten Verzeichnis sortieren",
            "7 - Alle Verzeichnisse sortieren",
            "8 - Ordner des Sortierprogramms bearbeiten",
            "9 - Erweiterungen des Sortierprogramms bearbeiten",
            "10 - Letzte Operation rückgängig machen",
            "11 - Hilfe anzeigen",
            "12 - Programm beenden",
        ],
        "ru": [
            "ОПЦИИ МЕНЮ:",
            "1 - Сортировать музыкальные файлы",
            "2 - Сортировать видео файлы",
            "3 - Сортировать файлы изображений",
            "4 - Сортировать документы",
            "5 - Сортировать файлы для скачивания",
            "6 - Сортировать файлы из определенного каталога",
            "7 - Сортировать все каталоги",
            "8 - Изменить папки программы сортировки",
            "9 - Изменить расширения программы сортировки",
            "10 - Отменить последнюю операцию",
            "11 - Показать меню помощи",
            "12 - Выйти из программы",
        ],
    }

    colors = [
        Fore.BLUE,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.LIGHTMAGENTA_EX,
    ]

    menu = "\n".join(
        f"{colors[i%len(colors)]}{option.center(100)}{Style.RESET_ALL}"
        for i, option in enumerate(menu_options.get(language, menu_options["en"]))
    )
    return f"{Fore.BLUE}{'-'*100}{Style.RESET_ALL}\n{menu}\n{Fore.BLUE}{'-'*100}{Style.RESET_ALL}\n{Fore.GREEN}{'↪ Your Choice : '.center(100)}{Style.RESET_ALL}"


def generate_help_menu(  # Function to generate the help menu in the correct language
    language,
):
    help_options = {
        "fr": [
            "OPTIONS D'AIDE:",
            "1. Trier les fichiers musicaux: Cette option triera tous les fichiers musicaux.",
            "2. Trier les fichiers vidéo: Cette option triera tous les fichiers vidéo.",
            "3. Trier les fichiers image: Cette option triera tous les fichiers image.",
            "4. Trier les fichiers de document: Cette option triera tous les fichiers de document.",
            "5. Trier les fichiers de téléchargement: Cette option triera tous les fichiers de téléchargement.",
            "6. Trier les fichiers d'un répertoire spécifique: Cette option triera tous les fichiers d'un répertoire spécifique.",
            "7. Trier tous les répertoires: Cette option triera tous les fichiers de tous les répertoires inclue de base dans le programme.",
            "8. Ajouter un répertoire au programme de tri: Cette option ajoutera un nouveau répertoire au programme de tri.",
            "9. Modifier les extensions du programme de trie: Cette option modifiera les extensions du programme de trie.",
            "10. Annuler la dernière opération: Cette option annulera la dernière opération de tri effectuée.",
            "11. Afficher le menu d'aide: Cette option affichera ce menu d'aide.",
            "12. Quitter le programme: Cette option fermera le programme.",
        ],
        "en": [
            "HELP OPTIONS:",
            "1. Sort music files: This option will sort all music files.",
            "2. Sort video files: This option will sort all video files.",
            "3. Sort image files: This option will sort all image files.",
            "4. Sort document files: This option will sort all document files.",
            "5. Sort download files: This option will sort all download files.",
            "6. Sort files from a specific directory: This option will sort all files from a specific directory.",
            "7. Sort all directories: This option will sort all files from all directories.",
            "8. Add a directory to the sorting program: This option will add a new directory to the sorting program.",
            "9. Edit the extensions of the sorting program: This option will edit the extensions of the sorting program.",
            "10. Undo last operation: This option will undo the last sorting operation performed.",
            "11. Display the help menu: This option will display this help menu.",
            "12. Quit the program: This option will close the program.",
        ],
        "es": [
            "OPCIONES DE AYUDA:",
            "1. Ordenar archivos de música: Esta opción ordenará todos los archivos de música.",
            "2. Ordenar archivos de video: Esta opción ordenará todos los archivos de video.",
            "3. Ordenar archivos de imagen: Esta opción ordenará todos los archivos de imagen.",
            "4. Ordenar archivos de documento: Esta opción ordenará todos los archivos de documento.",
            "5. Ordenar archivos de descarga: Esta opción ordenará todos los archivos de descarga.",
            "6. Ordenar archivos de un directorio específico: Esta opción ordenará todos los archivos de un directorio específico.",
            "7. Ordenar todos los directorios: Esta opción ordenará todos los archivos de todos los directorios.",
            "8. Agregar un directorio al programa de clasificación: Esta opción agregará un nuevo directorio al programa de clasificación.",
            "9. Editar las extensiones del programa de clasificación: Esta opción editará las extensiones del programa de clasificación.",
            "10. Deshacer la última operación: Esta opción deshará la última operación de clasificación realizada.",
            "11. Mostrar el menú de ayuda: Esta opción mostrará este menú de ayuda.",
            "12. Salir del programa: Esta opción cerrará el programa.",
        ],
        "it": [
            "OPZIONI DI AIUTO:",
            "1. Ordina file musicali: Questa opzione ordinerà tutti i file musicali.",
            "2. Ordina file video: Questa opzione ordinerà tutti i file video.",
            "3. Ordina file di immagini: Questa opzione ordinerà tutti i file di immagini.",
            "4. Ordina file di documenti: Questa opzione ordinerà tutti i file di documenti.",
            "5. Ordina file di download: Questa opzione ordinerà tutti i file di download.",
            "6. Ordina file da una directory specifica: Questa opzione ordinerà tutti i file da una directory specifica.",
            "7. Ordina tutte le directory: Questa opzione ordinerà tutti i file da tutte le directory.",
            "8. Aggiungi una cartella al programma di ordinamento: Questa opzione aggiungerà una nuova cartella al programma di ordinamento.",
            "9. Modifica le estensioni del programma di ordinamento: Questa opzione modificherà le estensioni del programma di ordinamento.",
            "10. Annulla l'ultima operazione: Questa opzione annullerà l'ultima operazione di ordinamento eseguita.",
            "11. Visualizza il menu di aiuto: Questa opzione visualizzerà questo menu di aiuto.",
            "12. Esci dal programma: Questa opzione chiuderà il programma.",
        ],
        "de": [
            "HILFE OPTIONEN:",
            "1. Musikdateien sortieren: Diese Option sortiert alle Musikdateien.",
            "2. Videodateien sortieren: Diese Option sortiert alle Videodateien.",
            "3. Bilddateien sortieren: Diese Option sortiert alle Bilddateien.",
            "4. Dokumentdateien sortieren: Diese Option sortiert alle Dokumentdateien.",
            "5. Download-Dateien sortieren: Diese Option sortiert alle Download-Dateien.",
            "6. Dateien aus einem bestimmten Verzeichnis sortieren: Diese Option sortiert alle Dateien aus einem bestimmten Verzeichnis.",
            "7. Alle Verzeichnisse sortieren: Diese Option sortiert alle Dateien aus allen Verzeichnissen.",
            "8. Ordner zum Sortierprogramm hinzufügen: Diese Option fügt dem Sortierprogramm einen neuen Ordner hinzu.",
            "9. Erweiterungen des Sortierprogramms bearbeiten: Diese Option bearbeitet die Erweiterungen des Sortierprogramms.",
            "10. Letzte Operation rückgängig machen: Diese Option macht die letzte Sortieroperation rückgängig.",
            "11. Hilfe anzeigen: Diese Option zeigt dieses Hilfemenü an.",
            "12. Programm beenden: Diese Option schließt das Programm.",
        ],
        "ru": [
            "ПОМОЩЬ ОПЦИИ:",
            "1. Сортировать музыкальные файлы: Эта опция отсортирует все музыкальные файлы.",
            "2. Сортировать видео файлы: Эта опция отсортирует все видео файлы.",
            "3. Сортировать файлы изображений: Эта опция отсортирует все файлы изображений.",
            "4. Сортировать документы: Эта опция отсортирует все документы.",
            "5. Сортировать файлы для скачивания: Эта опция отсортирует все файлы для скачивания.",
            "6. Сортировать файлы из определенного каталога: Эта опция отсортирует все файлы из определенного каталога.",
            "7. Сортировать все каталоги: Эта опция отсортирует все файлы из всех каталогов.",
            "8. Добавить папку в программу сортировки: Эта опция добавит новую папку в программу сортировки.",
            "9. Изменить расширения программы сортировки: Эта опция изменит расширения программы сортировки.",
            "10. Отменить последнюю операцию: Эта опция отменит последнюю выполненную операцию сортировки.",
            "11. Показать меню помощи: Эта опция отобразит это меню помощи.",
            "12. Выйти из программы: Эта опция закроет программу.",
        ],
    }

    colors = [
        Fore.BLUE,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
    ]

    help_menu = "\n".join(
        f"{colors[i%len(colors)]}{option.center(100)}{Style.RESET_ALL}"
        for i, option in enumerate(help_options.get(language, help_options["en"]))
    )
    return f"{Fore.BLUE}{'-'*100}{Style.RESET_ALL}\n{help_menu}\n{Fore.BLUE}{'-'*100}{Style.RESET_ALL}\n{Fore.GREEN}{'↪ Your Choice : '.center(100)}{Style.RESET_ALL}"


def generate_menu_edit_extensions(
    language,
):  # Function to generate the edit menu in the correct language
    edit_options = {
        "fr": [
            "OPTIONS D'ÉDITION DES EXTENSIONS:",
            "1. Ajouter une extension.",
            "2. Supprimer une extension.",
            "3. Afficher toutes les extensions.",
            "4. Quitter le menu d'édition.",
        ],
        "en": [
            "EDIT EXTENSIONS OPTIONS:",
            "1. Add an extension.",
            "2. Remove an extension.",
            "3. Display all extensions.",
            "4. Quit the edit menu.",
        ],
        "es": [
            "OPCIONES DE EDICIÓN DE EXTENSIONES:",
            "1. Agregar una extensión.",
            "2. Eliminar una extensión.",
            "3. Mostrar todas las extensiones.",
            "4. Salir del menú de edición.",
        ],
        "it": [
            "OPZIONI DI MODIFICA ESTENSIONI:",
            "1. Aggiungi un'estensione.",
            "2. Rimuovi un'estensione.",
            "3. Visualizza tutte le estensioni.",
            "4. Esci dal menu di modifica.",
        ],
        "de": [
            "ERWEITERUNGEN BEARBEITEN OPTIONEN:",
            "1. Eine Erweiterung hinzufügen.",
            "2. Eine Erweiterung entfernen.",
            "3. Alle Erweiterungen anzeigen.",
            "4. Bearbeitungsmenü beenden.",
        ],
        "ru": [
            "ОПЦИИ РЕДАКТИРОВАНИЯ РАСШИРЕНИЙ:",
            "1. Добавить расширение.",
            "2. Удалить расширение.",
            "3. Показать все расширения.",
            "4. Выйти из меню редактирования.",
        ],
    }

    colors = [
        Fore.BLUE,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
    ]

    edit_menu = "\n".join(
        f"{colors[i%len(colors)]}{option.center(100)}{Style.RESET_ALL}"
        for i, option in enumerate(edit_options.get(language, edit_options["en"]))
    )
    return f"{Fore.BLUE}{'-'*100}{Style.RESET_ALL}\n{edit_menu}\n{Fore.BLUE}{'-'*100}{Style.RESET_ALL}\n{Fore.GREEN}{'↪ Your Choice : '.center(100)}{Style.RESET_ALL}"


def generate_menu_choose_extensions(language):
    i = 0
    menu_options = {
        "fr": ["Choisissez un dictionnaire d'extension à modifier:", "Sortir"],
        "en": ["Choose an extension dictionary to modify:", "Exit"],
        "es": ["Elija un diccionario de extensiones para modificar:", "Salir"],
        "it": ["Scegli un dizionario di estensioni da modificare:", "Uscire"],
        "de": ["Wählen Sie ein Erweiterungswörterbuch zum Bearbeiten aus:", "Ausfahrt"],
        "ru": ["Выберите словарь расширений для изменения:", "Выход"],
    }

    colors = [
        Fore.BLUE,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.LIGHTMAGENTA_EX,
    ]

    menu = f"{Fore.GREEN}{menu_options.get(language, menu_options['en'])[0].center(100)}{Style.RESET_ALL}\n"
    for i, extension_dict_key in enumerate(extension_dicts, start=1):
        menu += f"{colors[i%len(colors)]}{(' '.join([str(i), '-', extension_dict_key])).center(100)}{Style.RESET_ALL}\n"

    # Add exit option
    menu += f"{colors[(i+1)%len(colors)]}{(' '.join([str(i+1), '-', menu_options.get(language, menu_options['en'])[1]])).center(100)}{Style.RESET_ALL}\n"

    return f"{Fore.BLUE}{'-'*100}{Style.RESET_ALL}\n{menu}\n{Fore.BLUE}{'-'*100}{Style.RESET_ALL}\n{Fore.GREEN}{'↪ Your Choice : '.center(100)}{Style.RESET_ALL}"


def generate_menu_edit_folder(language):
    folder_options = {
        "fr": [
            "OPTIONS D'ÉDITION DES DOSSIERS:",
            "1. Ajouter un dossier.",
            "2. Supprimer un dossier.",
            "3. Afficher tous les dossiers.",
            "4. Quitter le menu d'édition.",
        ],
        "en": [
            "EDIT FOLDERS OPTIONS:",
            "1. Add a folder.",
            "2. Remove a folder.",
            "3. Display all folders.",
            "4. Quit the edit menu.",
        ],
        "es": [
            "OPCIONES DE EDICIÓN DE CARPETAS:",
            "1. Agregar una carpeta.",
            "2. Eliminar una carpeta.",
            "3. Mostrar todas las carpetas.",
            "4. Salir del menú de edición.",
        ],
        "it": [
            "OPZIONI DI MODIFICA CARTELLE:",
            "1. Aggiungi una cartella.",
            "2. Rimuovi una cartella.",
            "3. Visualizza tutte le cartelle.",
            "4. Esci dal menu di modifica.",
        ],
        "de": [
            "ORDNER BEARBEITEN OPTIONEN:",
            "1. Einen Ordner hinzufügen.",
            "2. Einen Ordner entfernen.",
            "3. Alle Ordner anzeigen.",
            "4. Bearbeitungsmenü beenden.",
        ],
        "ru": [
            "ОПЦИИ РЕДАКТИРОВАНИЯ ПАПОК:",
            "1. Добавить папку.",
            "2. Удалить папку.",
            "3. Показать все папки.",
            "4. Выйти из меню редактирования.",
        ],
    }

    colors = [
        Fore.BLUE,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
    ]

    folder_menu = "\n".join(
        f"{colors[i%len(colors)]}{option.center(100)}{Style.RESET_ALL}"
        for i, option in enumerate(folder_options.get(language, folder_options["en"]))
    )
    return f"{Fore.BLUE}{'-'*100}{Style.RESET_ALL}\n{folder_menu}\n{Fore.BLUE}{'-'*100}{Style.RESET_ALL}\n{Fore.GREEN}{'↪ Your Choice : '.center(100)}{Style.RESET_ALL}"


def print_message(color, message):  # Function to print a message in the correct color
    print(f"{color}{message}{Style.RESET_ALL}")
