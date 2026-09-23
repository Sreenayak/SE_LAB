def get_result(marks):
    if marks < 0 or marks > 100:
        return "Invalid"

    if marks > 40:
        return "Pass"

    return "Fail"
