import note
import json
from operator import attrgetter


class NotesFile:
    def __init__(self):
        self.notes = []
        self.max_id = 0

    def add_note(self, name, text):
        local_id = self.max_id + 1
        self.notes.append(note.Note(local_id, name, text))
        self.max_id = local_id
        return f"Note with id={local_id} was created."

    def delete_note(self, local_id):
        note_index = self.get_note_index_by_id(local_id)
        if note_index >= 0:
            self.notes.pop(note_index)
            return f"Note with id={local_id} was deleted."
        else:
            return f"There is no id={local_id}."

    def edit_note(self, local_id, new_name, new_text):
        index = self.get_note_index_by_id(local_id)
        if index > -1:
            self.notes[index].edit(new_name, new_text)
            return f"Note with id={local_id} was edited."
        else:
            return f"There is no id={local_id}."

    def sort_notes_by_id(self):
        self.notes = sorted(self.notes, key=attrgetter('local_id'))
        for i in range(len(self.notes)):
            self.notes[i].locad_id = i + 1

    def get_short_list(self):
        result = []
        for elem in self.notes:
            result.append(f"{elem.local_id}\t{elem.name}\n")
        return result

    def get_note_index_by_id(self, local_id):
        indexes_by_id = dict()
        for i in range(len(self.notes)):
            indexes_by_id[self.notes[i].local_id] = i
        try:
            return indexes_by_id[local_id]
        except KeyError:
            return -1

    def renum_notes(self):
        for i in range(len(self.notes)):
            self.notes[i].local_id = i + 1
        self.max_id = len(self.notes)
        return "Notes were renumerated."


def note_manager_to_json(manager):
    my_dict = {"notes": list(map(lambda x: note.note_to_json(x), manager.notes)),
               "max_id": manager.max_id}
    return json.dumps(my_dict)


def json_to_note_manager(json_string):
    o = json.loads(json_string)
    notes = o["notes"]
    max_id = o["max_id"]
    result = NotesFile()
    result.notes = list(map(lambda x: note.json_to_note(x), notes))
    result.max_id = max_id
    return result

