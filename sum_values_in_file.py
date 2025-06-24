#!/usr/bin/env python3

def calculate_sum_from_file(filename):
    """
    Read numbers from a file and return their sum. 
    File should be in a format with sign-prefixed nums separated by newlines, like:
    "+13\n-3\n+2..."
    
    Args:
        filename (str): Path to the file containing numbers
        
    Returns:
        int: Sum of all numbers in the file
    """
    total = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                print("%s" % line)
                if line:  # Skip empty lines
                    total += int(line)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    except ValueError as e:
        print(f"Error: Invalid number format in file. {e}")
        return 0
    
    return total

if __name__ == "__main__":
    import sys
    
    # Use command line argument if provided, otherwise default to time_tracking.txt
    filename = sys.argv[1] if len(sys.argv) > 1 else None

    if filename is None:
        print("No valid filename passed.")
    
    result = calculate_sum_from_file(filename)
    print("------------------------------------------------------------------------")
    print(f"Total sum: {result}")
