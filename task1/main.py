from total_salary import total_salary

if __name__ == "__main__":
    file_path = "./salary_file.txt"

    total, average = total_salary(file_path)

    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
