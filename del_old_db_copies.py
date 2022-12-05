#######################################
# Удаление копий БД, в директории path,
# старше n-1 дней
#######################################

import glob, os

path = '/home/user/test/testdir/'
n = 4
d = {}

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

num_files = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])

if num_files >= n:
    for file in glob.glob(f"{path}*.sql"):
        d[file] = os.path.getmtime(file)

    min_date = min(d.values())
    min_date_value = get_key(d, min_date)

    os.remove(min_date_value)
    print(f"file {min_date_value} is deleted")

