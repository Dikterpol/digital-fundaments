researcher_name = input("Введите ФИО исследователя: ")
date = input("Введите дату (ДД.ММ.ГГГГ): ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")
with open('journal.txt', 'w', encoding='utf-8') as file:
    file.write("+" + "-" * 40 + "+\n")
    
    file.write(f"| Электронный лабораторный журнал{' ' * 8}|\n")
    file.write("+" + "-" * 40 + "+\n")
    
    file.write(f"| ФИО исследователя: {researcher_name:<20}|\n")
    file.write(f"| Дата: {date:<30}|\n")
    file.write(f"| Эксперимент: {experiment_name:<23}|\n")
    
    file.write("+" + "-" * 40 + "+\n")
    
    file.write(f"| Вывод:{' ' * 34}|\n")
print("\nДанные успешно сохранены в journal.txt")