import datetime
import note
import datetime as dt


def eq_len_string(string, length):
    string_length = len(string)
    string = string.replace("\n", " ")
    if string_length > length:
        return string[0: length - 3] + "..."
    else:
        return string + " " * (length - string_length)


def get_default_note_printer():
    return NotePrinter(3, True, 20,
                       True, 25,
                       True, 25, None, None,
                       True, 25, None, None)


class NotePrinter:
    def __init__(self, id_field_length, to_show_name, name_field_length,
                 to_show_text_preview, text_preview_field_length,
                 to_show_created, created_field_length, created_filter_from, created_filter_to,
                 to_show_modified, modified_field_length, modified_filter_from, modified_filter_to):
        self.id_field_length = id_field_length
        self.to_show_name = to_show_name
        self.name_field_length = name_field_length
        self.to_show_text_preview = to_show_text_preview
        self.text_preview_field_length = text_preview_field_length
        self.to_show_created = to_show_created
        self.created_field_length = created_field_length
        self.created_filter_from = created_filter_from
        self.created_filter_to = created_filter_to
        self.to_show_modified = to_show_modified
        self.modified_field_length = modified_field_length
        self.modified_filter_from = modified_filter_from
        self.modified_filter_to = modified_filter_to

    def print_notes(self, notes_list):
        result = []

        head_string = eq_len_string("ID", self.id_field_length)
        if self.to_show_name:
            head_string += "\t" + eq_len_string("Name", self.name_field_length)
        if self.to_show_text_preview:
            head_string += "\t" + eq_len_string("Text", self.text_preview_field_length)
        if self.to_show_created:
            head_string += "\t" + eq_len_string("Created at", self.created_field_length)
        if self.to_show_modified:
            head_string += "\t" + eq_len_string("Last modified at", self.modified_field_length)

        result.append(head_string)

        for item in notes_list:
            if self.created_filter_from is not None:
                if item.created < self.created_filter_from:
                    continue

            if self.created_filter_to is not None:
                if item.created > self.created_filter_to:
                    continue

            if self.modified_filter_from is not None:
                if item.last_modified < self.modified_filter_from:
                    continue

            if self.modified_filter_to is not None:
                if item.last_modified > self.modified_filter_to:
                    continue

            item_string = eq_len_string(f"{item.local_id}", self.id_field_length)
            if self.to_show_name:
                item_string += "\t" + eq_len_string(item.name, self.name_field_length)
            if self.to_show_text_preview:
                item_string += "\t" + eq_len_string(item.text, self.text_preview_field_length)
            if self.to_show_created:
                item_string += "\t" + eq_len_string(item.created.ctime(), self.created_field_length)
            if self.to_show_modified:
                item_string += "\t" + eq_len_string(item.last_modified.ctime(), self.modified_field_length)
            result.append(item_string)

        for result_item in result:
            print(result_item)

    def print_config(self):
        print(eq_len_string("Field", 25)
              + "\t" + eq_len_string("Show", 5)
              + "\t" + eq_len_string("Length", 6)
              + "\t" + eq_len_string("After", 25)
              + "\t" + eq_len_string("Before", 25))

        print_config_string("ID", True, self.id_field_length, "", "")
        print_config_string("Name", self.to_show_name, self.name_field_length, "", "")
        print_config_string("Text", self.to_show_text_preview, self.text_preview_field_length, "", "")
        print_config_string("Created at", self.to_show_created, self.created_field_length,
                            self.created_filter_from.ctime() if self.created_filter_from is not None else "",
                            self.created_filter_to.ctime() if self.created_filter_to is not None else "")
        print_config_string("Last modified at", self.to_show_modified, self.modified_field_length,
                            self.modified_filter_from.ctime() if self.modified_filter_from is not None else "",
                            self.modified_filter_to.ctime() if self.modified_filter_to is not None else "")


def print_config_string(name, is_shown, length, filter1, filter2):
    print(eq_len_string(name, 25)
          + "\t" + eq_len_string(f"{is_shown}", 5)
          + "\t" + eq_len_string(f"{length}", 6)
          + "\t" + eq_len_string(f"{filter1}", 25)
          + "\t" + eq_len_string(f"{filter2}", 25))
