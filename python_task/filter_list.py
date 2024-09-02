"""
This script filters a list of integers based on specific conditions.

The `filter_list` function ensures that the length of the input list is a multiple of 10.
If this condition is met, it then filters out items at positions that are multiples of 2 or 3.

Usage:
    The script can be run directly, where it will prompt the user to input a list
    of integers. The script will then filter the list according to the conditions
    specified and output the result. If the input list's length is not a multiple
    of 10, an error will be raised.

Functions:
    filter_list(input_list):
        Filters the input list by removing items at positions that are multiples
        of 2 or 3, and checks that the list's length is a multiple of 10.
        Parameters:
            input_list (list): The list of integers to be filtered.
        Returns:
            list: The filtered list of integers.
        Raises:
            ValueError: If the length of the input list is not a multiple of 10.
    
    main():
        Prompts the user for a list of integers, calls the filter_list function, 
        and prints the filtered result. Handles exceptions for invalid input.
    
Example:
    To run the script, simply execute it in a Python environment:
    
    $ python filter_list.py
    
    Enter a list of integers separated by space: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    Filtered List: [1, 5, 7, 11, 13, 17, 19]

Notes:
    - The list indexing starts at 1 for the filtering conditions (i.e., the first
      element is at position 1, the second at position 2, etc.).
    - The script raises an error if the list length is not a multiple of 10.
"""

def filter_list(input_list):
    """
    Filters the input list by removing items at positions that are multiples
    of 2 or 3, and checks that the list's length is a multiple of 10.

    Parameters:
        input_list (list): The list of integers to be filtered.

    Returns:
        list: The filtered list of integers.

    Raises:
        ValueError: If the length of the input list is not a multiple of 10.
    """
    if len(input_list) % 10 != 0:
        raise ValueError("Error: The length of the list must be a multiple of 10.")

    filtered_list = [x for i, x in enumerate(input_list) if (i + 1) % 2 != 0 and (i + 1) % 3 != 0]

    return filtered_list

if __name__ == "__main__":
    try:
        # Take input from the user
        user_input_str = input("Enter a list of integers separated by space: ")

        # Convert the input string to a list of integers
        user_input_list = list(map(int, user_input_str.split()))

        # Call the filter_list function
        filtered_result = filter_list(user_input_list)

        # Print the filtered list
        print("Filtered List:", filtered_result)
    except ValueError as e:
        print(e)
