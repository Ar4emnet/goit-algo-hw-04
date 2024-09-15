from pathlib import Path


def total_salary(path):
    sum = 0
    count = 0
    try:
        p = Path(path)
        with open(p, "r", encoding='utf8') as file:
            try:
                for line in file.readlines():
                    sum += int(line.strip().split(",")[1])
                    count += 1
            except ValueError:
                print("Invalid data format in line:", line)
        try:
            return (sum, sum / count)
        except ZeroDivisionError:
            print("No data in the file")
    except FileNotFoundError:
        print("File not found")


if __name__ == '__main__':
    path = input("Please enter a path:")
    total, average = total_salary(path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


