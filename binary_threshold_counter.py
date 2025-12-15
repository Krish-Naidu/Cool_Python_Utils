# Array of numbers with binary increment based on threshold

def count_matches(numbers, binary_string, threshold):
    count = 0
    
    # Iterate through both array and binary string
    for i in range(len(numbers)):
        # If number is above threshold AND binary digit is '1', increment count
        if numbers[i] > threshold and binary_string[i] == '1':
            count += 1
    
    return count


# Example usage
numbers = [10, 25, 3, 45, 8, 12, 30, 5]
binary_string = "11010101"  # Same length as numbers array
threshold = 15

print(count_matches(numbers, binary_string, threshold))