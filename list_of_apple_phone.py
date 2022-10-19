phone_list = ["Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro", "Apple iPhone 13", "Apple iPhone 11",
              "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro"]

apple_list = (apple for apple in phone_list if "Apple" in apple)
for i in apple_list:
    print(i)