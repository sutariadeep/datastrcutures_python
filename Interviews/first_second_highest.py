def first_second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    if count >= 2:
        return m1, m2 
    elif count == 1:
        return m1
    else: return None

print first_second_largest([1,1,1,1,1,2])
print first_second_largest([20,67,3,2.6,7,74,2.8,90.8,52.8,4,3,2,5,7])
print first_second_largest([1])
print first_second_largest([1,1])