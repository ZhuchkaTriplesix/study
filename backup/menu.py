def menu_generate(strings_numbers, list_of_names):
    for i in range(1, strings_numbers + 1):
        print(str(i) + ".", list_of_names[i - 1])
        i += 1
