##Rated and sorted list

def find_minimum_element(sorted_list):
    if not sorted_list:
        raise ValueError("The list is empty, cannot find minimum element.")
    return sorted_list[0]

# Example usage
if __name__ == "__main__":
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    try:
        min_element = find_minimum_element(sorted_list)
        print(f"The minimum element in the sorted list is: {min_element}")
    except ValueError as e:
        print(e)
