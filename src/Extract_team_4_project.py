from csv import reader

def extract_csv_info(file_name, list_to_append_to):
    with open(file_name) as the_file:
        cafe_list = reader(the_file)
        for items in cafe_list:
            list_to_append_to.append(items)
