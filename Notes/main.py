import manager
import note_printer as np


if __name__ == '__main__':
    my_manager = manager.Manager("Name", "Path")
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

