def calculate_grade(scores):
    # 1. ตรวจสอบว่าลิสต์ว่างหรือไม่ เพื่อป้องกัน ZeroDivisionError
    if not scores:
        return "N/A", 0

    # 2. ใช้ sum() เพื่อความรวดเร็วและอ่านง่าย
    try:
        total = sum(scores)
    except TypeError:
        return "Error: All scores must be numbers", 0

    average = total / len(scores)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade, average

# การทดสอบ
scores = [85, 92, 78, 88, 95]
grade, avg = calculate_grade(scores)
print(f"Grade: {grade}, Average: {avg:.2f}")

# ทดสอบกรณีลิสต์ว่าง
print(calculate_grade([]))
