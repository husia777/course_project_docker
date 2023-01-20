import os
from config.settings import BASE_DIR

operation_number = 0

list_emails_and_files = []


def check_and_write_result_to_file(filename, email, operation_num):
    path = os.path.join(BASE_DIR, "media")
    path = os.path.join(path, f"{filename}")
    path_to_result = os.path.join(BASE_DIR, "result")
    path_to_result = os.path.join(path_to_result, f"{operation_num}.txt")
    os.system(f" flake8 {path} > {path_to_result}")
    list_emails_and_files.append((email, path_to_result))
    print(list_emails_and_files)
