def calculate_gpa(filename):
    """Calculates the GPA based on a text file containing grades.

    Args:
        filename: The name of the text file.

    Returns:
        The calculated GPA.
    """

    total_points = 0
    total_credits = 0

    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            stripped_line = line.strip()
            if stripped_line == "" or stripped_line.startswith("#"):
                continue
            course, grade, credits = stripped_line.split("|")
            credits = int(credits)

            if grade == 'A+':
                points = 4.0 * credits
            elif grade == 'A':
                points = 4.0 * credits
            elif grade == 'A-':
                points = 3.7 * credits
            elif grade == 'B+':
                points = 3.3 * credits
            elif grade == 'B':
                points = 3.0 * credits
            elif grade == 'B-':
                points = 2.7 * credits
            elif grade == 'C+':
                points = 2.3 * credits
            elif grade == 'C':
                points = 2.0 * credits
            elif grade == 'C-':
                points = 1.7 * credits
            elif grade == 'D+':
                points = 1.3 * credits
            elif grade == 'D':
                points = 1.0 * credits
            elif grade == 'D-':
                points = 1.0 * credits
            elif grade == 'F':
                points = 0.0 * credits
            else:
                print(f"Invalid grade: {grade}")
                return

            total_points += points
            total_credits += credits

    gpa = total_points / total_credits
    return gpa

if __name__ == "__main__":
    filename = "courses.csv"
    gpa = calculate_gpa(filename)
    print(f"Your GPA is: {gpa:.3f}")