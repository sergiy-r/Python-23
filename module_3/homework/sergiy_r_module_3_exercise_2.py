# Module 3 Exercise 2
# Author: Sergiy R


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    # This function returns a random sample of 'quantity' numbers from a range of integer numbers between 'min' & 'max',
    # where 1>= min < max, max <= 1000 and 'quantity' <= (max - min). If conditions are met, a sorted list is returned.
    # Otherwise, an empty list is returned.

    import random  # import random module

    try:
        if min < 1:  # check if min < 1
            print("The 'min' parameter cannot be lower than 1.")
            selected_numbers = []

        elif max > 1000:  # check if max > 1000
            print("The 'max' parameter cannot be greater than 1000.")
            selected_numbers = []

        elif min >= max:  # check if min >= max
            print("The 'min' parameter cannot be greater than or equal to the 'max' parameter.")
            selected_numbers = []

        elif quantity >= (max - min):  # check if quantity >= (max - min)
            print("The 'quantity' parameter cannot be greater than or equal to the difference of 'max' and 'min'.")
            selected_numbers = []

        else:  # input parameters satisfy conditions

            population = set(
                (range(min, max + 1)))  # create a set for with lower limit of 'min' and upper limit of 'max'
            selected_numbers = sorted(
                random.sample(sorted(population), quantity))  # select 'quantity' of numbers from \
            # the range from 'min' to 'max'
            print(f"The randomly selected numbers are: {selected_numbers}.")

    except:  # return error message if input is incorrect
        print("Error - all parameters must be integers.")  #
        selected_numbers = []

    return selected_numbers  # output selected numbers


print(get_numbers_ticket(1, 1000, 4))
