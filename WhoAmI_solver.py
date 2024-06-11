from statistics import median


def clean(str):
    """
    gets string, return only hebrew unicode characters
    """
    # remove punctuation:
    str = str.translate([None, " .,"])
    chars = str.split("u05")[1:]
    # remove garbage characters
    for i, chr in enumerate(chars):
        chars[i] = chr[:2]
    return chars


def gematria(letter):
    """
    gets a hebrew letter, returns it's gematria
    """
    value = {"d0": 1, "d1": 2, "d2": 3, "d3": 4, "d4": 5, "d5": 6, "d6": 7, "d7": 8, "d8": 9, "d9": 10, "db": 20, "dc": 30, "de": 40, "e0": 50, "e1": 60, "e2": 70, "e4": 80, "e6": 90, "e7": 100, "e8": 200, "e9": 300, "ea": 400}
    return value[letter]

def calc(text):
    """
    gets list of chars, returns sum of gematria
    """
    text = clean(text)
    sum = 0
    for chr in text:
        sum += gematria(chr)
    return sum




values = []
# whoami: 22 dictionaries (list of dictionaries)
for dict_list in whoami.values():
    # dict list: few dictionaries (text, value pairs)
    for pairs_dict in dict_list:
        g = calc(pairs_dict["text"])
        print("Original value:" + str(pairs_dict["value"]) + "    Calculated vlue:" + str(g))
        # print(calc(sub_dict["text"]))
        values.append(g)
print(values)
print(len(values))
print("Sum of values below median:")
print(sum(filter(lambda x: x<median(values), values)))
