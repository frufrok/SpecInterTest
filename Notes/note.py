import datetime
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

def from_json(json_string):
    o = json.loads(json_string)
    # try:
        # local_id = o["local_id"]
        # name = o["name"]
        # text = o["text"]
        # created = datetime.datetime.strftime(o["created"],
        # modified = datetime.datetime.strftime(o["last_modified"])
        # return Note()