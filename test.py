def count_char(text: str) -> dict:
    count_dict = {}
    for char in text:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict


print(count_char("Hellow"))
