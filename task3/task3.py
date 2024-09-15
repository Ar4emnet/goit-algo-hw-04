from pathlib import Path
from colors_func import dir_color, files_color
import sys

def dir_reader(path,tab=0,start_position = True):
    try:
        p = Path(path)
        if not p.exists():
            print("Directory does not exist")
        if start_position:
            print("📂",dir_color(p.name))

        items = p.iterdir()
        items_list = list(items)

        for id_item,item in enumerate(items_list):
            tabulator = "┃\t"*tab if tab != 0 else ""
            prefix = "┗" if id_item == len(items_list)-1 else "┣"

            if item.is_dir():
                print(f"{tabulator}{prefix}📂{dir_color(item.name)}")
                dir_reader(item,tab+1,False)
            else:
                print(f"{tabulator}{prefix}📂{files_color(item.name)}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    dir_reader(sys.argv[1])