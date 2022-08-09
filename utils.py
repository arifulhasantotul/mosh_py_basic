def find_max(num_list):
    max_value = num_list[0]
    for num in num_list:
        if max_value < num:
            max_value = num

    return max_value


