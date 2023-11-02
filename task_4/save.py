def read_file(name):
    f = open(f"{name}", mode="r", encoding="utf8")
    strings = f.read().splitlines()
    strings_list = [strings[i].split(' ') for i in range(len(strings))]
    clear_strings_list = []
    for i in range(len(strings_list)):
        for word in strings_list[i]:
            word = ''.join(filter(str.isalnum, word)).lower()
            if len(word) > 0:
                clear_strings_list.append(word)
    words_set = set(clear_strings_list)
    return sorted(words_set)

words = read_file('data.txt')

def save_file(name, words):
    new = open(f"{name}", mode='w', encoding='utf8')
    new.write(f"{(len(words))} \n")
    for i in range(len(words)):
        new.write(f"{(words[i])} \n")


save_file('itog.txt', words)