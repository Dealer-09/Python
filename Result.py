def get_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid Marks"
    grade_mapping = {
        10: "O",  
        9: "O",   
        8: "E",   
        7: "A",   
        6: "B",   
        5: "C",   
        4: "D",   
    }
    return grade_mapping.get(marks // 10, "F")  
marks = int(input("Enter Marks (0-100): "))
print("Grade:", get_grade(marks))
