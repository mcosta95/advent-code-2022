def read_data(folder, filename, split="\n", extra_clean=""):
    # opening the file in read mode
    my_file = open(f"{folder}/{filename}.txt", "r")
    
    # reading the file
    data = my_file.read()

    # prepare the data
    data_into_list = data.split(split)

    if extra_clean != "":
        data_into_list = [iter_.split(extra_clean) for iter_ in data_into_list]

    return data_into_list