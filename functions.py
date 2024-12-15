# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    lst = lst[::-1]
    return lst
     # Implement this

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    c = lst.count(element)
    return c



def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    pass
    # Implement this

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    new_list = []
    for i in lst1:
        new_list.append(i)
    for k in lst2:
        new_list.append(k)
            
    ls = sorted(new_list)

    return ls
            
    # Implement this

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    # max1 = max2 = float

    # for i in numbers:
    #     if i > max1:
    #         max2 = max1  
    #         max1 = i  
    #     elif i > max2 and i != max1:
    #         max2 = i  
    #     else:
    #         return None

    # return max2
    pass
    # Implement this

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    for i in str1:
        if i  in str2:
            return True
        else:
            return False
     # Implement this


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    # nested_list = nested_list.slpit(",")
    flat_list = []
    
    for i in nested_list:
        for n in i:
            flat_list.append(n)
    return flat_list
    # Implement this


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    non_dup = []
    for i in lst:
        if i not in non_dup:
            non_dup.append(i)
    return non_dup
    # Implement this

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    common = []
    for i in lst1:
        if i in lst2:
            common.append(i)
    return common
         
 # Implement this