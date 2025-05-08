a = {"один": "1"}
b = [["один", "1"]]
# c = ["один", "1"]
d = [("один", "1")]
# e = ("один", "1")
# f = (["один", "1"])
g = (("один", "1"),)
h = ({"один": "1"},)

lst = [a, b, d, g, h]
# for e in lst:
#     print(type(dict(e)))

# e = ("один", "1")
# # fr = dict(e)
# # print(type(fr))
# lst1 = []
# try:
#     for e in lst:
#         if
#         lst1.append(dict(e))
# except ValueError:
#     print("Некорректное значение")
# print(lst1)
h = ({"один": "1"},)
try:
    my_data = dict(h)
except ValueError:
    raise TypeError("Некорректный тип данных для data")

