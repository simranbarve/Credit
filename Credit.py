def check_my_card(arg):

    def input_card_number():
        card = raw_input("please enter your card number:")
        check_input_is_number(card)
        return(card)

    def check_input_is_number(card):
        card_no = str(card)
        length = len(card_no)
        if card.isdigit() and length == 16:
            convert_input(card_no)
        else:
            print("that is not valid")
            input_card_number()
        return(card_no)

    def convert_input(card_no):
        number = [int(i) for i in (card_no)]
        Luhn_algorithm(number)
        return number

    def Luhn_algorithm(number):
        multers = (number[::2])
        adders = (number[1::2])
        multiplied = [i * 2 for i in multers]
        join_digits(multiplied)
        return (multiplied)
        return (adders)

    def join_digits(multiplied):
        join = ''.join(map(str, multiplied))
        split_digits(join)
        return (join)

    def split_digits(join):
        split = [int(i) for i in (join)]
        sum_list(split)
        return (split)

    def sum_list(split):
        SUM = sum(split)
        return (SUM)

    def final_sum(SUM, )



input_card_number()
