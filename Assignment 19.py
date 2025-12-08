def sort_list(numbers):
    nums = numbers[:] # make a copy so original isn't modified
    sorted_list = []

    while nums:
        smallest = nums[0]
        for n in nums:
            if n < smallest:
                smallest = n
            sorted_list.append(smallest)
            nums.remove(smallest)

        return sorted_list