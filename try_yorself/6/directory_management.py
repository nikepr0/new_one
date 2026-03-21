import os
import shutil

# directory management в Python
os.mkdir("new_folder")              # создать папку
os.makedirs("parent/child/grand", exist_ok=True)  # создать вложенные папки
shutil.copytree("source", "backup")  # копировать папку целиком
os.rmdir("empty_folder")             # удалить пустую папку
shutil.rmtree("old_folder")          # удалить папку с содержимым