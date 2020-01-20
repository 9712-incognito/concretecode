dict_sample={
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1994
}
for x, y in dict_sample.items():
    print(x, y)
    print(len(dict_sample))
    dict_sample["color"]= "red"
    print(dict_sample)