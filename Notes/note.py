import datetime as dt
import json


class Note:
    def __init__(self, local_id, name, text):
        self.local_id = local_id
        self.name = name
        self.text = text
        self.created = dt.datetime.now()
        self.last_modified = dt.datetime.now()

    def to_json(self):
        return json.dumps({
            "local_id": self.local_id,
            "name": self.name,
            "text": self.text,
            "created": self.created,
            "last_modified": self.last_modified
        })


def json_to_note(json_string):
    o = json.loads(json_string)
    try:
        local_id = o["local_id"]
        name = o["name"]
        text = o["text"]
        created = o["created"]
        modified = o["modified"]
        result = Note(local_id, name, text)
        result.created = dt.datetime(created[0],
                                     created[1],
                                     created[2],
                                     created[3],
                                     created[4],
                                     created[5])
        result.last_modified = dt.datetime(modified[0],
                                           modified[1],
                                           modified[2],
                                           modified[3],
                                           modified[4],
                                           modified[5])
        return result
    except KeyError:
        return Note(0, "Read error", "Error occurred when reading this note.")


def note_to_json(note):
    my_dict = {"local_id": note.local_id,
               "name": note.name,
               "text": note.text,
               "created": note.created.timetuple(),
               "modified": note.last_modified.timetuple()}
    return json.dumps(my_dict)
