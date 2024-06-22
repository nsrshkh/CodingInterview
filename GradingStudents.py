def gradingStudents(grades):
    r_grades = []
    for grade in grades:
        if grade < 38:
            r_grades.append(grade)
        else:
            r = grade % 5
            if r >= 3:
                r_grades.append(grade + (5 - r))
            else:
                r_grades.append(grade)
    return r_grades


def gradingStudents1(grades):
    return [grade if (grade < 38) or (5 * round(grade / 5) < grade) else 5 * round(grade / 5) for grade in grades]


# grades = [84, 29, 57]
grades = [73, 67, 38, 33]
# grades = 57


print(gradingStudents1(grades))
