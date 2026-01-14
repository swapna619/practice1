def attendance_status(classes_held, classes_attended):
    percentage = (classes_attended / classes_held) * 100
    if percentage >= 75:
        return percentage, "Eligible"
    else:
        return percentage, "Not Eligible"


if __name__ == "__main__":
    classes_held = int(input("Enter number of classes held: "))
    classes_attended = int(input("Enter number of classes attended: "))

    percentage, status = attendance_status(classes_held, classes_attended)

    print(f"Attendance Percentage: {percentage:.2f}%")
    print(status)
