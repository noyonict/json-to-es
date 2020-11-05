import os

for file in os.listdir():
    if file.endswith('.json'):
        print(file)
        index_name = file.split('.')[0]
        print(index_name)
