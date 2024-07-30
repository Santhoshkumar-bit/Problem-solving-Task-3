##

def find_triplets_with_sum(lst, target_sum):
    # First, sort the list
    lst.sort()
    
    n = len(lst)
    triplets = []
    
    # Iterate through the list
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = lst[i] + lst[left] + lst[right]
            
            if current_sum == target_sum:
                triplets.append((lst[i], lst[left], lst[right]))
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    
    return triplets

# Example usage
if __name__ == "__main__":
    lst = [10, 20, 30, 9]
    target_sum = 59
    result = find_triplets_with_sum(lst, target_sum)
    
    if result:
        print("Triplets with the sum equal to", target_sum, "are:", result)
    else:
        print("No triplets found with the sum equal to", target_sum)
