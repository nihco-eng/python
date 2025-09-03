import os

path = os.getcwd()
print('현재폴더', path)

check = "04.모듈과패키지"
print(check)
file_path = os.path.join(check, "my file.py")
print(file_path)

with open(file_path, 'w') as f:
    f.write('')
if os.path.exists(file_path):
    os.remove(file_path)
