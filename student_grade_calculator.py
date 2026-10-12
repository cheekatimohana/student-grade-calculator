
def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


def main():
    name = input("Enter student name: ")
    marks = []

    for subject in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {subject} (0-100): "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    percentage = total / len(marks)
    grade = calculate_grade(percentage)

    print("\n--- Student Result ---")
    print(f"Name: {name}")
    print(f"Total Marks: {total:g}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
