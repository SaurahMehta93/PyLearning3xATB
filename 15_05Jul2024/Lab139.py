# Wal in DIR
import os

for root, dir, files in os.walk('D:\\python_project\\PyLearning3xATB\\15_05Jul2024'):
    print(root)
    for file in files:
        print(file)

print("***************")

for root, dir, files in os.walk('D:\\python_project\\PyLearning3xATB\\15_05Jul2024'):
    print(f"Root - {root}")
    print(f"Director - {dir}")
    print(f"File - {files}")
    print(len(files))
