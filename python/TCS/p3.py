# Count Sundays in a Month

def count_sundays(start, N):
    days = {
        "mon": 0,
        "tue": 1,
        "wed": 2,
        "thu": 3,
        "fri": 4,
        "sat": 5,
        "sun": 6
    }
    
    start_day = days[start.lower()]
    count = 0
    
    for d in range(1, N + 1):
        if (start_day + (d - 1)) % 7 == 6:  # 6 = Sunday
            count += 1
    
    return count

print(count_sundays("mon", 13)) 
print(count_sundays("sun", 30))  # 5 Sundays
print(count_sundays("fri", 28))  # 4 Sundays
print(count_sundays("wed", 31))  # 4 or 5
print(count_sundays("sat", 1))   # 0 or 1