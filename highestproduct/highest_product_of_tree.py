def highest_product_of_3(list_of_ints):
    if len(list_of_ints) <= 2:
        raise ValueError("List must have at least 3 elements.")

    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_product_two = list_of_ints[0] * list_of_ints[1]
    lowest_product_two = list_of_ints[0] * list_of_ints[1]
    highest_product_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]

        highest_product_three = max(highest_product_three, current * highest_product_two, current * lowest_product_two)
        highest_product_two = max(highest_product_two, current * highest, current * lowest)
        lowest_product_two = min(lowest_product_two, current * highest, current * lowest)
        highest = max(current, highest)
        lowest = min(current, lowest)


    return highest_product_three