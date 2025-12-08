def find_common_elements(list1, list2):
    # Convert to sets for 0(n) average performance
    return list(set(list1) & set(list2))