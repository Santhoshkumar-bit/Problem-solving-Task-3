## Non repeating element in integer

from collections import Counter

def first_non_repeating_element(lst):
    counts = Counter(lst)
    
    for element in lst:
        if counts[element] == 1:
            return element
    
    return None

if __name__ == "__main__":
    example_list = [4, 5, 1, 2, 1, 3, 10, 2, 3, 4, 5, 6]
    result = first_non_repeating_element(example_list)
    
    if result is not None:
        print(f"The first non-repeating element is: {result}")
    else:
        print("There are no non-repeating elements in the list.")
