# Задание 2

def get_unique_ids(ids):
    num_list = []
    for id_ in ids.values():
        num_list.extend(id_)
    result = list(set(num_list))
    return result

# Задание 3


def get_stats(list_stats):
    queries_list = []
    for words in list_stats:
        queries_list.append(len(words.split()))
    queries_max = max(queries_list)
    dict_queries = {}
    for i in range(queries_max+1):
        percent = round(queries_list.count(i)/len(list_stats)*100, 2)
        if percent != 0:
            dict_queries.setdefault(i, percent)
    return dict_queries


# Задание 5(Необязательное)


def transformation_list(list_data):
    count = 0
    len_list = len(list_data) - 1
    new_dict = {}
    while count < len_list:
        for i in reversed(list_data[0:len_list]):
            key = i
            value = list_data[-1]
            new_dict = dict(zip([key], [value]))
            list_data.pop()
            list_data.append(new_dict)
            count += 1
    return new_dict
