import manager
import note_printer as np
import note
import os


def write_to_file(note_manager, path):
    try:
        if os.path.isfile(path):
            print("File already exists. Would you like to overwrite it?")

        with open(path, 'x') as writer:
            writer.write(manager.note_manager_to_json(note_manager))
    except OSError:
        print("Error writing file. Check filename and working directory path")


def can_be_written(note_manager):
    return os.path.isdir(note_manager.dir_path) and not os.path.isfile(os.path.join(note_manager.dir_path, note_manager.file_name))


if __name__ == '__main__':
    my_manager = manager.Manager()
    my_note_printer = np.get_default_note_printer()

    print(my_manager.add_note("Note name", "Some note text can be too long"))
    print(my_manager.add_note("Note name", "Some note text can be too long"))
    print(my_manager.add_note("Note name", "Some note text can be too long"))
    my_note_printer.print_notes(my_manager.notes)
    print(my_manager.delete_note(2))
    print(my_manager.delete_note(4))
    my_note_printer.print_notes(my_manager.notes)
    print(my_manager.delete_note(3))
    my_note_printer.print_notes(my_manager.notes)
    print(my_manager.add_note("Note name", "Some note text can be too long"))
    print(my_manager.add_note("Note name", "Some note text can be too long"))
    print(my_manager.add_note("Note name", "Some note text can be too long"))
    print(my_manager.add_note("Note name", "Some note text can be too long"))
    my_note_printer.print_notes(my_manager.notes)
    print(my_manager.renum_notes())
    my_note_printer.print_notes(my_manager.notes)
    print(my_manager.add_note("Note name", "Some note text can be too long"))
    print(my_manager.add_note("Note name", "Some note text can be too long"))
    my_note_printer.print_notes(my_manager.notes)
    my_note_printer.print_config()

    json_string = note.note_to_json(my_manager.notes[0])
    print(json_string)
    my_manager.delete_note(1)
    my_note_printer.print_notes(my_manager.notes)
    my_manager.notes.append(note.json_to_note(json_string))
    my_note_printer.print_notes(my_manager.notes)

    write_to_file(my_manager, "Notes.json")


