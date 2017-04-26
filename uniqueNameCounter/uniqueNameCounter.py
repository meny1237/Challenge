max_typo_mistakes = 1
nickname_db = {}


def prepare_nickname_db():
    """
    This function loads the nickname db as a dictionary
    key: name
    value: list of possible nicknames
    :return: True if the initialize was successful, false otherwise.
    """
    global nickname_db
    previous_name = ""
    try:
        with open('nicknames.csv') as nickname_file:
            for line in nickname_file:
                _, curr_name, curr_nickname = line.split(', ')  # Splitting the curr line (id, name, nickname)
                curr_nickname = curr_nickname.replace('\n', '')  # Replacing the \n at the end of the line
                if not curr_name == previous_name:
                    nickname_db[curr_name] = []  # If we have a new key (new name) with need to init it's value
                    previous_name = curr_name
                nickname_db[curr_name].append(curr_nickname)  # adding the nickname
    except IOError:
        return False
    return True


def is_nickname(name, possible_nickname):
    """
    This function checks if the nickname for the following name is in the db
    :param name: the key in the db, represents the actual name
    :param possible_nickname: represents the nickname that should be checked
    :return: True if the nickname exists, false otherwise
    """
    global nickname_db
    if name in nickname_db.keys():  # Not a linear search, uses hash
        if possible_nickname in nickname_db[name]:
            return True
    return False


def parse_name(name):
    """
    This function parses the given name to two strings
    :param name: represents the name that should be parsed
    :return: tuple that represents the parsed name
    """
    if ' ' in name:  # Checking for space in order to split the name
        first_name, second_name = name.split(' ')
    else:
        first_name = name
        second_name = ""
    return first_name, second_name


def typo_mistake(first_name, second_name):
    """
    This function checks if there might be a typo mistake between the two strings
    :param first_name: represents the first string
    :param second_name: represents the second string
    :return: True - if it's a typo mistake, false otherwise
    """
    diff_in_len = abs(len(first_name) - len(second_name))  # Checking for len difference
    # We need to get the min len in order to check for differences in the string
    min_len = min(len(first_name), len(second_name))
    if diff_in_len > 1:
        # The names are different in their length more than acceptable.
        return False
    else:
        # Checking char by char differences
        mistakes_num = diff_in_len
        for x in xrange(min_len):
            if first_name[x] != second_name[x]:
                mistakes_num += 1
    # if the counted mistakes are more than accepted than it's not a typo
    return not (mistakes_num > max_typo_mistakes)


def check_unique(first_name, last_name, second_first_name, second_last_name):
    """
    This function checks if the given names represents two unique persons
    :param first_name: represents the first name of the first arg
    :param last_name: represents the last name of the first arg
    :param second_first_name: represents the first name of the second arg
    :param second_last_name: represents the last name of the second arg
    :return: True if they represents unique persons, false otherwise
    """
    first_names_equal = True
    last_names_equal = True
    if first_name != second_first_name:
        # First we will check for a typo mistake and then we will check for nickname.
        if not typo_mistake(first_name, second_first_name):
            if not is_nickname(first_name, second_first_name):
                first_names_equal = False
    if first_names_equal:
        # If the first names represents the same persons, then we move to the last names
        if last_name != second_last_name:
            if not typo_mistake(last_name, second_last_name):
                last_names_equal = False
    return not (first_names_equal and last_names_equal)


def count_unique_names(bill_first_name, bill_last_name, ship_first_name, ship_last_name, bill_name_on_card):
    """
    This function checks if the given arguments represents the same person
    :param bill_first_name: the first name in the billing address form (could include middle names)
    :param bill_last_name: the last name in the billing address form
    :param ship_first_name: the first name in the shipping address form (could include middle names)
    :param ship_last_name: the last name in the shipping address form
    :param bill_name_on_card: the full name as it appears on the credit card. (could be flipped)
    :return: number that represents how many names are unique and not belong to the same person
    """
    if not prepare_nickname_db():
        return -1
    unique_names = 1
    middle_names_unique = False

    # parsing middle names
    parsed_first_bill, parsed_middle_bill = parse_name(bill_first_name)
    parsed_first_ship, parsed_middle_ship = parse_name(ship_first_name)

    # Checking if middle name is present both in bill and ship name
    if parsed_middle_bill != "" and parsed_middle_ship != "":
        if len(parsed_middle_bill) > 1 and len(parsed_middle_ship) > 1:
            # First we will check if the names are equal and if not we will check for typo
            if parsed_middle_ship != parsed_middle_bill:
                if not typo_mistake(parsed_middle_bill, parsed_middle_ship):
                    # It's not a typo mistake, it's a different person
                    unique_names += 1
                    middle_names_unique = True
        else:
            # Means that one of them is one char long, so we will check the first char
            if parsed_middle_bill[0] != parsed_middle_ship[0]:
                # if one one char middle name is different, it's a different person
                unique_names += 1
                middle_names_unique = True

    if not middle_names_unique:
        # If the middle names represents the same person we need to make sure that the ship and bill names
        # represents the same person.
        if check_unique(parsed_first_bill, bill_last_name, parsed_first_ship, ship_last_name):
            unique_names += 1

    # Last thing to do, we need to check that both the bill name matches the name on the card,
    # and the ship name matches the name on the card.
    # We need to also flip the card name (because the bill card name might be flipped).
    first_name_card, last_name_card = parse_name(bill_name_on_card)  # Parse card name
    if check_unique(parsed_first_bill, bill_last_name, first_name_card, last_name_card):
        # If the bill name don't match the name on card we need to check if ship name matches the card name
        if check_unique(parsed_first_ship, ship_last_name, first_name_card, last_name_card):
            # Flipping the name on card
            first_name_card, last_name_card = last_name_card, first_name_card
            if check_unique(parsed_first_bill, bill_last_name, first_name_card, last_name_card):
                # Checking both bill name and ship name with the flipped card name
                if check_unique(parsed_first_ship, ship_last_name, first_name_card, last_name_card):
                    unique_names += 1
    return unique_names
