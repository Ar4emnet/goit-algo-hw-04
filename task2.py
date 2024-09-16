from pathlib import Path

def get_cats_info(path):
    cats_info = []
    try:
        p = Path(path)
        with (open(p, 'r', encoding='utf8') as file):
            for line in file:
                try:
                    id, name, age = line.strip().split(',')
                    cats_info.append({'id': id, 'name': name, 'age': age})
                except ValueError:
                    print(f'Invalid data format in line: {line}')
    except FileNotFoundError:
        print(f'File "cats_file.txt" not found in {path}')
    return cats_info


if __name__ == '__main__':
    path = input("enter path to file")
    print("list cats information",get_cats_info(path))