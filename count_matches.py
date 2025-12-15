def count_matches_for_threshold(numbers, binary_string, threshold):
    count = 0
    length = len(numbers)
    for i in range(length):
        if numbers[i] > threshold and binary_string[i] == '1':
            count += 1
    return count


def find_best_threshold(numbers, binary_string):
    # Create array of all thresholds (number+1 and number-1 for each number)
    thresholds = []
    for num in numbers:
        thresholds.append(num + 1)
        thresholds.append(num - 1)
    
    max_count = 0
    best_threshold = None
    
    # Test each threshold and find the one with max count
    for threshold in thresholds:
        count = count_matches_for_threshold(numbers, binary_string, threshold)
        if count > max_count:
            max_count = count
            best_threshold = threshold
    
    return best_threshold, max_count


numbers = [10, 25, 3, 45, 8, 12, 30, 5]
binary_string = "11010101"

best_threshold, max_count = find_best_threshold(numbers, binary_string)
print(best_threshold)
print(max_count) 
# 