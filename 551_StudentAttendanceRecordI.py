#551. Student Attendance Record I

def checkRecord(s):
    return 'LLL' not in s and len([i for i in s if i =='A']) < 2