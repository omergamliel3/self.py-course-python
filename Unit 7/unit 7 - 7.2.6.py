def get_product_list():
    """
    get input from user and return a list from the input (split key = ',')
    :rtype: list
    :return: list of splited products
    """
    products = input('\nEnter products:\t').lower()
    return products.split(',')


def print_products_list(product_list=[]):
    """
    print product_list
    :param product_list: products list
    :type product_list: list
    """
    print('Your Products List:\t', ' ,'.join(product_list) + '.')


def print_products_length(product_list=[]):
    """
    print product_list length
    :param product_list: products list
    :type product_list: list
    """
    print('Products List Length:\t', len(product_list))


def is_product_in_list(product_list=[]):
    """
    get product name from the user and print if product in product_list
    :param product_list: products list
    :type product_list: list
    """
    product_name = input('Enter product to check if it\'s on the list:\t').lower()
    if product_name in product_list:
        print(product_name, 'is in your products list')
    else:
        print(product_name, 'is not in your products list')


def num_of_product_appears(product_list=[]):
    """
     get product name from the user and print num of appears in product_list
     :param product_list: products list
     :type product_list: list
     """
    product_name = input('Enter product to check how much times it appear in your list:\t').lower()
    product_appears = product_list.count(product_name)
    if product_appears == 0:
        print(product_name, 'is not in products list')
    else:
        print(product_name, f'appears {product_appears} times products list ')


def remove_product(product_list=[]):
    """
     get product name from the user and remove it from product_list if in it
     :param product_list: products list
     :type product_list: list
     """
    product_name = input('Enter product to remove from products list:\t').lower()
    if product_name in product_list:
        product_list.remove(product_name)


def add_product(product_list=[]):
    """
     get product name from the user and append it to product_list
     :param product_list: products list
     :type product_list: list
     """
    product_name = input('Enter product to add to products list:\t').lower()
    product_list.append(product_name)


def invalid_products(product_list=[]):
    """
     print invalid products in product_list.
     product is invalid of his length is lower then 3 or one of his chars is non alphabet
     :param product_list: products list
     :type product_list: list
     """
    not_valid_products = []
    for product in product_list:
        if len(product) < 3:
            not_valid_products.append(product)
        else:
            for letter in product:
                if not letter.isalpha():
                    not_valid_products.append(product)
                    break
    print('Invalid products: ', ' ,'.join(not_valid_products))


def remove_duplicate(product_list=[]):
    """
    remove duplicates from product_list argument, and print the new products list
    :param product_list: products list
    :type product_list: list
    :return: product list with no duplicated
    :rtype: list
     """
    # create dict fromkeys to ignore duplicate keys, and create a non-duplicate list from the dict
    removed_product_list = list(dict.fromkeys(product_list))
    print('Remove all duplicate products from list')
    print('Products list after remove duplicates: ', ' ,'.join(removed_product_list))
    return removed_product_list


def print_menu():
    """
    print program menu
    """
    print("""
    Menu:\n
    1:\t Print products list\n
    2:\t Print products length\n
    3:\t Is product in the list\n
    4:\t Num of appears in the list\n
    5:\t Remove product\n
    6: \t Add product\n
    7:\t Invalid products\n
    8:\t Remove duplicate products\n
    9:\t Quit program\n
        """)


def manage_products():
    """
    take input from the user. loop products menu until break ('9' input)
    call functions according to the user input (menu num)
    """
    product_list = get_product_list()
    print_menu()

    while True:
        menu_num = int(input('Enter a digit between 1 and 9:\t'))
        if menu_num == 1:
            print_products_list(product_list)
        elif menu_num == 2:
            print_products_length(product_list)
        elif menu_num == 3:
            is_product_in_list(product_list)
        elif menu_num == 4:
            num_of_product_appears(product_list)
        elif menu_num == 5:
            remove_product(product_list)
        elif menu_num == 6:
            add_product(product_list)
        elif menu_num == 7:
            invalid_products(product_list)
        elif menu_num == 8:
            product_list = remove_duplicate(product_list)
        elif menu_num == 9:
            quit()
        else:
            print('Sorry! Invalid input')


def main():
    # call func manage_product
    manage_products()


if __name__ == '__main__':
    main()
