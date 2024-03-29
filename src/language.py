import locale
from .menu import (
    generate_menu,
    generate_help_menu,
    generate_menu_choose_extensions,
    generate_menu_edit_extensions,
    generate_menu_edit_folder,
)
from colorama import Fore

LANGUAGE_FUNCTIONS = {
    "fr": {
        "menu": generate_menu("fr"),
        "help": generate_help_menu("fr"),
        "choose_extensions": generate_menu_choose_extensions("fr"),
        "edit_extensions": generate_menu_edit_extensions("fr"),
        "edit_folder": generate_menu_edit_folder("fr"),
        "color": Fore.RED,
        "invalid_choice_message": "Veuillez entrer un choix valide",
    },
    "en": {
        "menu": generate_menu("en"),
        "help": generate_help_menu("en"),
        "choose_extensions": generate_menu_choose_extensions("en"),
        "edit_extensions": generate_menu_edit_extensions("en"),
        "edit_folder": generate_menu_edit_folder("en"),
        "edit_folder": generate_menu_edit_folder("en"),
        "color": Fore.GREEN,
        "invalid_choice_message": "Please enter a valid choice",
    },
    "es": {
        "menu": generate_menu("es"),
        "help": generate_help_menu("es"),
        "choose_extensions": generate_menu_choose_extensions("es"),
        "edit_extensions": generate_menu_edit_extensions("es"),
        "edit_folder": generate_menu_edit_folder("es"),
        "color": Fore.YELLOW,
        "invalid_choice_message": "Por favor ingrese una opción válida",
    },
    "it": {
        "menu": generate_menu("it"),
        "help": generate_help_menu("it"),
        "choose_extensions": generate_menu_choose_extensions("it"),
        "edit_extensions": generate_menu_edit_extensions("it"),
        "edit_folder": generate_menu_edit_folder("it"),
        "color": Fore.BLUE,
        "invalid_choice_message": "Si prega di inserire una scelta valida",
    },
    "de": {
        "menu": generate_menu("de"),
        "help": generate_help_menu("de"),
        "choose_extensions": generate_menu_choose_extensions("de"),
        "edit_extensions": generate_menu_edit_extensions("de"),
        "edit_folder": generate_menu_edit_folder("de"),
        "color": Fore.MAGENTA,
        "invalid_choice_message": "Bitte geben Sie eine gültige Auswahl ein",
    },
    "ru": {
        "menu": generate_menu("ru"),
        "help": generate_help_menu("ru"),
        "choose_extensions": generate_menu_choose_extensions("ru"),
        "edit_extensions": generate_menu_edit_extensions("ru"),
        "edit_folder": generate_menu_edit_folder("ru"),
        "color": Fore.CYAN,
        "invalid_choice_message": "Пожалуйста, введите действительный выбор",
    },
}
DIRECTORY_NAMES = {  # Map directory names to the correct language
    "en": {
        "Music": "Music",
        "Videos": "Videos",
        "Images": "Images",
        "Documents": "Documents",
        "Downloads": "Downloads",
    },
    "fr": {
        "Music": "Musique",
        "Videos": "Vidéos",
        "Images": "Images",
        "Documents": "Documents",
        "Downloads": "Téléchargements",
    },
    "es": {
        "Music": "Música",
        "Videos": "Videos",
        "Images": "Imágenes",
        "Documents": "Documentos",
        "Downloads": "Descargas",
    },
    "it": {
        "Music": "Musica",
        "Videos": "Video",
        "Images": "Immagini",
        "Documents": "Documenti",
        "Downloads": "Scaricati",
    },
    "de": {
        "Music": "Musik",
        "Videos": "Videos",
        "Images": "Bilder",
        "Documents": "Dokumente",
        "Downloads": "Downloads",
    },
    "ru": {
        "Music": "Музыка",
        "Videos": "Видео",
        "Images": "Изображения",
        "Documents": "Документы",
        "Downloads": "Загрузки",
    },
}
LOG_MESSAGES = {  # Map log messages to the correct language
    "en": {
        "dir_not_exist": "The directory {directory} does not exist.",
        "error_moving": "Error moving file {file}: {error}",
        "file_sorted": "The file {directory} has been sorted",
        "moved": "Moved file from {src} to {dst}",
        "no_operation_to_cancel": "There is no operation to cancel.",
        "console_cleared": "Console cleared",
        "extension_not_found": "Extension not found",
        "file_exists": "The file {file} already exists in {directory}",
    },
    "fr": {
        "dir_not_exist": "Le répertoire {directory} n'existe pas.",
        "error_moving": "Erreur lors du déplacement du fichier {file}: {error}",
        "file_sorted": "Le fichier {directory} a bien été trié",
        "moved": "Fichier déplacé de {src} à {dst}",
        "no_operation_to_cancel": "Il n'y a aucune opération à annuler.",
        "console_cleared": "Console effacée",
        "extension_not_found": "Extension non trouvée",
        "file_exists": "Le fichier {file} existe déjà dans {directory}",
    },
    "es": {
        "dir_not_exist": "El directorio {directory} no existe.",
        "error_moving": "Error al mover el archivo {file}: {error}",
        "file_sorted": "El archivo {directory} ha sido ordenado",
        "moved": "Archivo movido de {src} a {dst}",
        "no_operation_to_cancel": "No hay operación para cancelar.",
        "console_cleared": "Consola borrada",
        "extension_not_found": "Extensión no encontrada",
        "file_exists": "El archivo {file} ya existe en {directory}",
    },
    "it": {
        "dir_not_exist": "La directory {directory} non esiste.",
        "error_moving": "Errore durante lo spostamento del file {file}: {error}",
        "file_sorted": "Il file {directory} è stato ordinato",
        "moved": "File spostato da {src} a {dst}",
        "no_operation_to_cancel": "Non c'è alcuna operazione da annullare.",
        "console_cleared": "Console cancellata",
        "extension_not_found": "Estensione non trovata",
        "file_exists": "Il file {file} esiste già in {directory}",
    },
    "de": {
        "dir_not_exist": "Das Verzeichnis {directory} existiert nicht.",
        "error_moving": "Fehler beim Verschieben der Datei {file}: {error}",
        "file_sorted": "Die Datei {directory} wurde sortiert",
        "moved": "Datei von {src} nach {dst} verschoben",
        "no_operation_to_cancel": "Es gibt keine Operation zum Abbrechen.",
        "console_cleared": "Konsole gelöscht",
        "extension_not_found": "Erweiterung nicht gefunden",
        "file_exists": "Die Datei {file} existiert bereits in {directory}",
    },
    "ru": {
        "dir_not_exist": "Каталог {directory} не существует.",
        "error_moving": "Ошибка при перемещении файла {file}: {error}",
        "file_sorted": "Файл {directory} был отсортирован",
        "moved": "Файл перемещен из {src} в {dst}",
        "no_operation_to_cancel": "Нет операции для отмены.",
        "console_cleared": "Консоль очищена",
        "extension_not_found": "Расширение не найдено",
        "file_exists": "Файл {file} уже существует в {directory}",
    },
}
# Get the user's operating system language
os_language = locale.getlocale()[0][:2] if locale.getlocale()[0] else "en"

# Get the system language
lang = locale.getlocale()[0].split("_")[0]

# Get the correct log messages based on the OS language (default to English)

messages = LOG_MESSAGES.get(locale.getlocale()[0][:2], LOG_MESSAGES["en"])
# Get the correct directory names based on the OS language (default to English)

directories_name = DIRECTORY_NAMES.get(lang, DIRECTORY_NAMES["en"])
