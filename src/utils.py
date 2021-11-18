import os


def delete_file_if_exists(file_path):
    if file_exists(file_path):
        os.remove(file_path)


def file_exists(file_path):
    return os.path.exists(file_path)


def get_element_or_none(element, attribute, method_to_apply):
    a = 0
    if attribute not in element.attrib:
        return None
    return method_to_apply(element.attrib[attribute])
