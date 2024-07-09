def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:  # Перевірка на порожній рядок
                    cat_id, name, age = line.split(',')
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": int(age)  # Приведення віку до цілого числа
                    }
                    cats_info.append(cat_info)
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")
    
    return cats_info