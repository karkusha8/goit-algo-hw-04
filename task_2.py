from pathlib import Path

def get_cats_info(path):
    if not path.strip():
        return "Шлях до файлу не вказано"

    file_path = Path(path)

    if not file_path.exists():
        return "Файл не знайдено."

    cats = []
    try:
        with file_path.open('r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    if age.isdigit():
                        cat_dict = {
                            "id": cat_id,
                            "name": name,
                            "age": age
                        }
                        cats.append(cat_dict)
    except Exception as e:
        return f"Помилка при читанні файлу: {e}"

    if not cats:
        return "У файлі немає коректних записів."

    return '\n'.join(str(cat) for cat in cats)
print(get_cats_info(r"Вказати шлях до файлу"))