# -*- coding: cp1252 -*-
"""Citrusbyte's challenge
The problem is to flatten an array of arbitrarily nested arrays of integers
into a flat array of integers. e.g. [[1,2,[3]],4] -> [1,2,3,4].

Input arguments:
array -- List to be flattened

As output, the program lists the flattened array.
"""

import argparse
import ast


def flatten(array):
    """Recursively flattens an array.

    Keyword arguments:
    array -- Array to be flattened

    Returns a flattened array
    """
    flat = []
    
    for element in array:
        if not type(element) is list:
            flat.append(element)
        else:
            for inner_element in flatten(element):
                flat.append(inner_element)
    
    return flat


def main():
    """Main function."""
    try:
        # Convert argument to list
        array_to_convert = ast.literal_eval(args.array)
    
        # Flatten array and print it to the screen
        flat_array = flatten(array_to_convert)

        # Print flattened array
        print ''
        print 'Flattened array: ' + str(flat_array)
    except:
        print ''
        print 'Error converting input argument to list'


if __name__ == "__main__":
    """Arguments checking and main function call."""
    # Arguments parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--array',
                        help='Array to be flattened, without spaces' +
                        'eg. --array [1,2,[3,4]]',
                        required=True)
    args = parser.parse_args()

    # Call main function
    main()
