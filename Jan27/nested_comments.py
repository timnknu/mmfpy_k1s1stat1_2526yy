comments = {}

comments[0] = (None, "Original author", "Here's my cool post")
comments[12] = (0, "John", "Nice commnet")
comments[15] = (12, "Smith", "Yes indeed")
comments[128] = (12, "Alice", "good topic to discuss")
comments[15] = (128, "Smith", "Do you really think so?")
comments[314] = (0, "Cat", "No, now I think it was a bad post")

k = 15
while k is not None:
    item = comments[k]
    print(k, ':', item)
    k = item[0]