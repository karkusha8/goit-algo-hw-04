from pathlib import Path

def total_salary(path):
    if not path.strip():
        return None, None

    file_path = Path(path)

    if not file_path.exists():
        return None, None

    total = 0
    count_developers = 0
    with file_path.open('r', encoding='utf-8') as file:
        for line in file:
            line = line.strip().split(',')
            if len(line) == 2 and line[0].strip() != '':
                try:
                    salary = float(line[1])
                    total += salary
                    count_developers += 1
                except ValueError:
                    continue

    if count_developers == 0:
        return None, None

    average = total / count_developers
    total = round(total, 2)
    average = round(average, 2)
    return total, average

result = total_salary(r'path')


if isinstance(result, tuple):
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}, ")
else:
    print(result)