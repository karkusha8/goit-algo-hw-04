from pathlib import Path

def get_cats_info(path):
    if not path.strip():
        return []

    file_path = Path(path)

    if not file_path.exists():
        return []

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
        return []


    if not cats:
        return []

    return cats
cats_info = get_cats_info(r"path/to/cats_file.txt")
print(cats_info)