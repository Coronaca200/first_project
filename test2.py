dict_1 = {"баба": 12, "клава": 10, "Сәлам": 9}
dict_2 = {"жаба": 2, "b": 15, "嗨夥計": 100, "やあ、相棒": 99}
dict_3 = {**dict_1, **dict_2}
for key, value in dict_1.items():
    if key in dict_2:
        dict_3[key] = dict_1[key] + dict_2[key]

print(dict(sorted(dict_3.items())))
