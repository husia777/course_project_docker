import os
from config.settings import BASE_DIR

dict_emails_and_files = dict()


def check_and_write_result_to_file(filename):
    x = 0
    path = os.path.join(BASE_DIR, "media")
    path = os.path.join(path, f"{filename}")
    path_to_result = os.path.join(BASE_DIR, "result")
    path_to_result = os.path.join(path_to_result, f"{x}.log")
    os.system(f" flake8 {path} > {path_to_result.replace('user_files/', '')}")
    x += 1


