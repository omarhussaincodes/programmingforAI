def check_list(data_list, num, val):
    if (len(data_list) != num):
        msg = f"Your input list is not size {num}"
    else:
        msg = f"Passed integer {num} is equal to {len(data_list)}"

    result_dict = dict()
    for i in range(len(data_list)):
        if (data_list[i] in result_dict):
            result_dict[data_list[i]] = result_dict[data_list[i]] + 1
        else:
            result_dict[data_list[i]] = 1

    keys = []
    values = []
    for key, value in result_dict.items():
        print(key, value)
        keys.append(key)
        values.append(value)

    zipped_data = list(zip(keys, values))
    result = max(zipped_data, key=lambda x: x[1])
    result_msg = f"The passed value {val or result[0]} appears {result[1]} times"

    return (msg, result_msg)


print(check_list([1, 4, 2, 3, 4], 3, 4))
