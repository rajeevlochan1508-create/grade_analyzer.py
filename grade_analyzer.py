# grade_analyzer.py
grade_analyzer.ipynb

# grade_analyzer.py

def process_scores(students):
    averages = {}
    
    for name in students:
        scores = students[name]
        total = 0
        
        for score in scores:
            total += score
        
        avg = round(total / len(scores), 2)
        averages[name] = avg
    
    return averages


def classify_grades(averages):
    classified = {}
    
    # grading thresholds inside the function
    A = 90
    B = 75
    C = 60
    
    for name in averages:
        avg = averages[name]
        
        if avg >= A:
            grade = "A"
        elif avg >= B:
            grade = "B"
        elif avg >= C:
            grade = "C"
        else:
            grade = "F"
        
        classified[name] = (avg, grade)
    
    return classified


def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")
    
    passed = 0
    failed = 0
    
    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        
        if status == "PASS":
            passed += 1
        else:
            failed += 1
        
        print(f"{name:<10} | Avg: {avg:.2f} | Grade: {grade} | Status: {status}")
    
    total = passed + failed
    
    print("================================")
    print(f"Total Students : {total}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")
    
    return passed


# Main block
if __name__ == "__main__":
    students = {
        "Alice": [85, 90, 88, 82],
        "Bob": [60, 65, 63, 62],
        "Clara": [95, 98, 94, 98]
    }
    
    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)
