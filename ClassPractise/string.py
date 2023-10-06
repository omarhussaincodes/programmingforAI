def countAppearances(list_data, val):
    count = 0
    for i in range(len(list_data)):
        if (list_data[i] == val):
            count += 1

    return count

def mostcommon(data_list):
    result_dict = dict()

    for i in range(len(data_list)):
        if (data_list[i] in result_dict):
            result_dict[data_list[i]] = result_dict[data_list[i]] + 1
        else:
            result_dict[data_list[i]] = 1

        print("Result:", result_dict)

        return result_dict


# print(mostcommon([1, 2, 4, 5, 6, 4, 4, 3, 1]))

# check for words in an array that ends with a speicified string of characters.
# return a new array with only those words

def list_ends_with(words_list, val):

    result = []
    for i in range(len(words_list)):
        word = words_list[i]
        if (val in word[-len(val):]):
            result.append(word)

    return result

words = ['fabolous', 'happy', 'content', 'miraculous', 'wild', 'mouse']
print(list_ends_with(words, 'ous'))  # ['faboulous', 'miraculous']
