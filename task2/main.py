from get_cats_info import get_cats_info

path_to_file = './cats.txt'
cats = get_cats_info(path_to_file)

for cat in cats:
    print(cat)