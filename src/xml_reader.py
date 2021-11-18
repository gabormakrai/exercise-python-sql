import defusedxml.ElementTree as et


def read_xml_file_and_call_method(file_path, method_to_pass_data):
    with open(file_path, 'r') as posts_in:
        tree = et.parse(posts_in)
        for elem in tree.getroot():
            method_to_pass_data(elem)
