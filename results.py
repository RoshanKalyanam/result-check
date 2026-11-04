"""
Student results data and calculation logic for the Result-Check website.
"""

# Student results database
STUDENT_RESULTS = {
    "21CS001": {"name": "Alice Johnson", "math": 85, "physics": 78, "chemistry": 72, "english": 90, "cs": 88},
    "21CS002": {"name": "Bob Smith", "math": 62, "physics": 55, "chemistry": 48, "english": 70, "cs": 65},
    "21CS003": {"name": "Charlie Brown", "math": 91, "physics": 88, "chemistry": 95, "english": 85, "cs": 92},
    "21CS004": {"name": "Diana Prince", "math": 45, "physics": 38, "chemistry": 42, "english": 55, "cs": 40},
    "21CS005": {"name": "Eve Davis", "math": 78, "physics": 82, "chemistry": 75, "english": 80, "cs": 85},
}


def calculate_result(roll_number):
    """
    Calculate the result for a given roll number.
    Returns a dict with name, marks, total, percentage, and pass/fail status.
    Pass mark per subject: 50. Overall pass: percentage >= 50.
    """
    if roll_number not in STUDENT_RESULTS:
        return None

    student = STUDENT_RESULTS[roll_number]
    subjects = {k: v for k, v in student.items() if k != "name"}
    total = sum(subjects.values())
    percentage = total / len(subjects)
    passed = all(mark >= 50 for mark in subjects.values())

    return {
        "roll_number": roll_number,
        "name": student["name"],
        "subjects": subjects,
        "total": total,
        "percentage": round(percentage, 1),
        "status": "Pass" if passed else "Fail",
    }

