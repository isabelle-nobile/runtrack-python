def calculate_grades(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 40:
            rounded_grades.append(grade)
        elif grade % 5 >= 3:
            rounded_grades.append((grade // 5 + 1) * 5)
        else:
            rounded_grades.append(grade)
    return print(rounded_grades)

grades = [23, 67, 89, 75, 83]
calculate_grades(grades)
