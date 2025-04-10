def count_words(text):
    num_words = len(text.split())

    return num_words

def get_count_of_chars(text):
    chars_dict = {}

    for word in text:
            lower_letter = word.lower()

            if lower_letter in chars_dict:
                chars_dict[lower_letter] +=1
            else:
                chars_dict[lower_letter] =1

    return chars_dict

def sort_dictionary(list_of_tuples):
    sorted_tuples = sorted(list_of_tuples, key=lambda item: item[1], reverse=True)
    sorted_dict_list = []

    for char, count in sorted_tuples:
        sorted_dict_list.append({"char": char, "count": count})

    return sorted_dict_list
