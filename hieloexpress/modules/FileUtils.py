import os

class FileUtils:
    def write_value(file_name, value):
        file = open(file_name, WRITE_MODE)
        if not "\n" in value:
            value = value + "\n"
        file.write(value)
        file.close()
    def write_values(file_name, values):
        for value in values:
            write_value(file_name, value)
    def read(file_name):
        try:
            file = open(file_name, READ_MODE)
            lines = file.readlines()
            file.close()
            return lines
        except FileNotFoundError:
            print("file not found.")
            return []
    def delete_line_by_content(file_name, line_content):
        file_content = read(file_name)
        delete_file(file_name)
        line_content = line_content + "\n"
        if line_content in file_content:
            file_content.remove(line_content)
        write_values(file_name, file_content)
    def delete_line_by_index(file_name, index):
        file_content = read(file_name)
        delete_file(file_name)
        file_content.remove(file_content[index])
        write_values(file_name, file_content)
    def delete_file(file_name):
        os.remove(file_name)
