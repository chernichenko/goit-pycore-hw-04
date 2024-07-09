def total_salary(path):
    total_sum = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на ім'я та заробітну плату за комою
                parts = line.strip().split(',')
                if len(parts) == 2:
                    name = parts[0].strip()
                    salary = int(parts[1].strip())
                    total_sum += salary
                    count += 1
                else:
                    print(f"Неправильний формат рядка у файлі: {line}")

        # Обчислюємо середню заробітню плату
        if count > 0:
            average_salary = total_sum / count
        else:
            average_salary = 0
        
        return total_sum, average_salary

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка при обробці файлу: {e}")
        return 0, 0
    