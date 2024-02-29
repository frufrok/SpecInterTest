import notes_file as nf
import note_printer as np
import datetime as dt
import os
from json.decoder import JSONDecodeError


def invitation():
    while True:
        print("Для продолжения необходимо открыть существующий файл или создать новый.")
        print("Введите \"h\" для получения справки.")
        command = input().lower()
        if command == 'n':
            new_file_dialog()
        elif command == 'o':
            open_file_dialog()
        elif command == 'e':
            break
        elif command == 'h':
            print_command_help('n', 'create new file')
            print_command_help('o', 'open file')
            print_command_help('e', 'exit program')
        else:
            print("Неверный ввод.")


def new_file_dialog():
    file = nf.NotesFile()
    work_with_file("", file)


def open_file_dialog():
    while True:
        print("Укажите путь к существующему файлу или пустую строку, чтобы вернуться в предыдущее меню.")
        path = input()
        if path == '':
            break
        elif os.path.isfile(path):
            read_file(path)
        else:
            print("Файл не найден")


def read_file(path):
    print(f"Reading file {path}...")
    with open(path, 'r') as reader:
        try:
            file = nf.json_to_note_manager(reader.read())
            work_with_file(path, file)
        except OSError:
            print("Error reading file. Check your permissions.")
        except JSONDecodeError:
            print("File was corrupted or it is not Notes file.")
        except KeyError:
            print("File was corrupted or it is not Notes file.")


def work_with_file(path, file):
    print(f"Working with file {path}...")
    mynp = np.get_default_note_printer()
    while True:
        print("Введите \"h\" для получения справки.")
        command = input().lower()

        if command == 'q':
            break

        elif command == 'n':
            new_note(file)

        elif command == 'd':
            delete_note(file)

        elif command == 'f':
            configure_filters(file, mynp)

        elif command == 'l':
            mynp.print_notes(file.notes)

        elif command == 'r':
            print(file.renum_notes())

        elif command == 'e':
            edit_note(file)

        elif command == 'o':
            show_note(file)

        elif command == 's':
            if path == '':
                print("Вы работаете с новым файлом. Используете команду \'a\' (save file as) для сохранения.")
            else:
                print(save_file(path, file))

        elif command == 'a':
            save_file_as(file)

        elif command == 'w':
            mynp.print_config()

        elif command == 'h':
            print("Show commands:")
            print_command_help('o', 'show note')
            print_command_help('l', 'show notes list')
            print_command_help('f', 'configure filters')
            print_command_help('w', 'show filters configuration')
            print("Edit commands:")
            print_command_help('n', 'new note')
            print_command_help('e', 'edit note')
            print_command_help('d', 'delete note')
            print_command_help('r', 'renumerate notes')
            print("Save commands:")
            print_command_help('s', 'save file')
            print_command_help('a', 'save file as')
            print("Exit commands:")
            print_command_help('q', 'close file without saving')
        else:
            print("Неверный ввод.")


def print_command_help(char, command):
    print(f"\'{char}\' - {command}")


def show_note(file):
    print("Введите ID заметки для отображения")
    try:
        id_to_show = int(input())
        index = file.get_note_index_by_id(id_to_show)
        if index > -1:
            note_to_show = file.notes[index]
            print(f"ID: {note_to_show.local_id}")
            print(f"Name: {note_to_show.name}")
            print(f"Text: {note_to_show.text}")
            print(f"Created at: {note_to_show.created.ctime()}")
            print(f"Last modified at: {note_to_show.last_modified.ctime()}")
        else:
            print(f"Заметки с ID={id_to_show} не существует.")
    except ValueError:
        print("Ошибка ввода.")


def new_note(file):
    print("Введите название заметки")
    name = input()
    print("Введите текст заметки")
    text = input()
    print(file.add_note(name, text))


def edit_note(file):
    print("Введите ID заметки для редактирования")
    try:
        id_to_edit = int(input())
        index = file.get_note_index_by_id(id_to_edit)
        if index > -1:
            enote = file.notes[index]
            print(f"Введите название заметки или пустую строку, чтобы сохранить название [{enote.name}]:")
            name = input()
            print(f"Введите текст заметки или пустую строку, чтобы сохранить текст [{enote.text}]:")
            text = input()
            print(file.edit_note(id_to_edit, name, text))
        else:
            print(f"Заметки с ID={id_to_edit} не существует.")
    except ValueError:
        print("Ошибка ввода.")


def delete_note(file):
    print("Введите ID заметки для удаления")
    try:
        id_to_delete = int(input())
        print(file.delete_note(id_to_delete))
    except ValueError:
        print("Ошибка ввода.")


def save_file(path, file):
    try:
        with open(path, 'w') as writer:
            writer.write(nf.note_manager_to_json(file))
            return f"File was successfully written to {path}"
    except OSError:
        return "Error writing file. Check filename and working directory path"


def save_file_as(file):
    print("Введите новое имя файла:")
    path = input()
    if os.path.isfile(path):
        print("File already exists. Would you like to overwrite it? (y/n)")
        while True:
            agreement = input().lower()
            if agreement == 'y':
                print(save_file(path, file))
                break
            elif agreement == 'n':
                break
            else:
                print("Ошибка ввода.")
    else:
        print(save_file(path, file))


def configure_filters(file, printer):
    while True:
        print("Введите индекс границы интервала, который желаете изменить, или \'h\' для справки:")
        command = input()

        if command == 'h':
            print_command_help('c1', 'нижняя граница даты создания')
            print_command_help('c2', 'верхняя граница даты создания')
            print_command_help('m1', 'нижняя граница даты изменения')
            print_command_help('m2', 'верхняя граница даты изменения')
            print_command_help('d', 'done')

        elif command == 'c1':
            printer.created_filter_from = edit_datetime()
            print("Фильтр c1 настроен.")

        elif command == 'c2':
            printer.created_filter_to = edit_datetime()
            print("Фильтр c2 настроен.")

        elif command == 'm1':
            printer.modified_filter_from = edit_datetime()
            print("Фильтр m1 настроен.")

        elif command == 'm2':
            printer.modified_filter_to = edit_datetime()
            print("Фильтр m2 настроен.")

        elif command == 'd':
            break


def edit_datetime():
    print("Введите 'd', чтобы удалить фильтр, или 'c', чтобы настроить:")
    while True:
        command = input()
        if command == 'd':
            print("Фильтр удален.")
            return None
        elif command == 'c':
            return read_datetime()
        else:
            print("Ошибка ввода.")

def read_datetime():
    try:
        year = int(input("Год: ").strip() or "2000")
        month = int(input("Месяц: ").strip() or "1")
        day = int(input("День: ").strip() or "1")
        hour = int(input("Час: ").strip() or "0")
        minute = int(input("Минута: ").strip() or "0")
        second = int(input("Секунда: ").strip() or "0")
        return dt.datetime(year, month, day, hour, minute, second)

    except ValueError:
        print("Ошибка ввода")
        return None


if __name__ == '__main__':
    invitation()
