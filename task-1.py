# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name: str, last_name: str, age: int, email: str, can_teach_subjects: set[str]):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects: list[str] = []

def create_schedule(subjects: set[str], teachers: list[Teacher]):
    uncovered = set(subjects)
    chosen_teachers = []

    while uncovered:
        best_teacher = None
        best_cover = set()

        for teacher in teachers:
            cover = teacher.can_teach_subjects & uncovered
            if len(cover) > len(best_cover) or (
                len(cover) == len(best_cover) and best_teacher and teacher.age < best_teacher.age
            ):
                best_teacher = teacher
                best_cover = cover

        if not best_teacher or not best_cover:
            return None  # не можна покрити всі предмети

        best_teacher.assigned_subjects.extend(best_cover)
        uncovered -= best_cover
        chosen_teachers.append(best_teacher)

    return chosen_teachers

if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    # Створення списку викладачів
    teachers = [
        Teacher("Олександр","Іваненко", 45, "o.ivanenko@example.com", {'Математика', 'Фізика'}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {'Хімія'}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {'Інформатика', 'Математика'}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {'Біологія', 'Хімія'}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {'Фізика', 'Інформатика'}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {'Біологія'})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
