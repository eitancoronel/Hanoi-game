# FILE : ex3.py
# WRITER : eitan_coronel , eitancoronel , 315468132
# EXERCISE : intro2cs2 ex7 2021
# DESCRIPTION: 8 functions

# the first function: print_to_n(n)

def print_to_n(n):
    """
    this function print all the number from 0 to n included
    :param n: number from 0 to n to print
    :return:None
    """
    if n >= 1:
        my_print_to_n(n, 1)


def my_print_to_n(maxi, current):
    """
    this function will calculate by recursion
    :param maxi: this function will get the maximum
    :param current: the current number
    :return: None
    """
    print(current)

    if current < maxi:
        my_print_to_n(maxi, current+1)


# the second function:digit_sum(n)


def add_smallest_digit(n, result):
    """
    this function separates the numbers and put them into a list .
    Then it will be easier for us to do the addition of each digit into the list.
    :param result: the result of the division
    :param n:the digit of each number
    :return:result
    """

    if n >= 10:
        result += n % 10
        return add_smallest_digit(n//10, result)

    else:
        result += int(n)
    return result


def digit_sum(n):
    """
    this function get by the past function a list of digits.
    And then it calculates the addition of each one.
    :param n:the number that we want
    :return:the smallest digit by recursion
    """
    result = 0
    return add_smallest_digit(n, result)

# the third function :is_prime(n)


def has_divisor_smaller_than(n, i):
    """
    this function chek if n is a prime number
    :param n: the number we want to chek if he is prime
    :param i: i will use us to divide the number
    :return: True if the number is prime , False if the number isn't prime
    """
    if n < 1:
        return False
    if n == 2:
        return True
    elif n == 1:
        return False
    if i > n/2:
        return True
    if n//i != n/i:
        if i == 2:
            next_val = 3
        else:
            next_val = i+2
        return has_divisor_smaller_than(n, next_val)
    else:
        return False


def is_prime(n):
    """
    this function call the past function by recursion
    :param n: n is the number that we want to chek if he is prime
    :return: call the past function by recursion
    """
    i = 2
    return has_divisor_smaller_than(n, i)

# the forth function : play_hanoi


def do_play_hanoi(n, src, dst, temp, hanoi, a=1, b=2, c=3):
    """
    this function plays the hanoi game
    :param n: the number of disks
    :param src: first rod
    :param dst: second rod
    :param temp: third rod
    :param hanoi: hanoi
    :param a: a=1
    :param b: b=2
    :param c: c=3
    :return: None
    """
    if n > 0:
        do_play_hanoi(n-1, src, dst, temp, hanoi, a, c, b)
        show_the_mouvements([a - 1, c - 1], src, dst, temp, hanoi)
        do_play_hanoi(n-1, src, dst, temp, hanoi, b, a, c)
    else:
        return


def play_hanoi(hanoi, n, src, dst, temp):
    """
    play the hanoi game
    :param hanoi: hanoi game
    :param n: number of disk
    :param src: first rod
    :param dst: second rod
    :param temp: third rod
    :return: None
    """
    do_play_hanoi(n, src, dst, temp, hanoi)


def show_the_mouvements(mvt, src, dst, temp, hanoi):
    """
    this function is doing the movements of the game of hanoi
    :param mvt: the movement
    :param src: first rod
    :param dst: second rod
    :param temp: third rod
    :param hanoi: hanoi game
    :return: None
    """
    if mvt[0] == 0:
        the_from = src
    elif mvt[0] == 1:
        the_from = dst
    elif mvt[0] == 2:
        the_from = temp
    if mvt[1] == 0:
        the_to = src
    elif mvt[1] == 1:
        the_to = dst
    elif mvt[1] == 2:
        the_to = temp
    hanoi.move(the_from, the_to)


# fifth function : print_sequences(char_list,n)


def print_sequences_recur(char_list, n, str_output):
    """
    this function gets all the different possibilities of a sequence from the char list with a length of n
    :param char_list:the different letters that we will use
    :param n:the length of each words that we want
    :param str_output:the output
    :return:None
    """
    if n > 0:
        for i in char_list:
            print_sequences_recur(char_list, n-1, f"{str_output}{i}")
    else:
        print(str_output)


def print_sequences(char_list, n):
    """
    this function call the past function
    :param char_list: the list of letter
    :param n: number of letters of each list
    :return:None
    """
    print_sequences_recur(char_list, n, "")


# sixth function : print_no_repetition_sequences(char_list, n)


def print_with_check(str_output):
    """
    print the str output
    :param str_output: the output
    :return: None
    """
    i = 0
    for x in str_output:
        str_copy = str_output[:i] + str_output[i+1:]
        i += 1
        if x in str_copy:
            return
    print(str_output)


def print_no_repetition_sequences_recur(char_list, n, str_output):
    """
    This function is the same as the function before .
    But this time doesn't take the words that  are already in the list
    :param char_list: the list of letter
    :param n: number of letters of each list
    :param str_output: the output
    :return: None
    """
    if n > 0:
        for i in char_list:
            print_no_repetition_sequences_recur(char_list, n-1, f"{str_output}{i}")
    else:
        print_with_check(str_output)


def print_no_repetition_sequences(char_list, n):
    """
    this function call the past function with recursion
    :param char_list: the list of letter
    :param n: number of letters of each list
    :return: None
    """
    print_no_repetition_sequences_recur(char_list, n, "")


# seventh function : parentheses(n)


def print_with_check_parentheses(str_output, n, list_output):
    """
    this function as the functions before chek the different combination of parentheses
    :param str_output: the string output
    :param n: number of letter of each list
    :param list_output: the list output
    :return: None
    """
    i = 0
    for x in str_output:
        if x == "(":
            i += 1
        elif x == ")":
            i -= 1
        if i < 0:
            return
    if i != 0:
        return
    list_output.append(str_output)


def parentheses_recur(char_list, n, str_output, list_output):
    """
    this is the recursion part of the parentheses exercise
    :param char_list: the list of letter
    :param n: number of letters of each list
    :param str_output: the string output
    :param list_output: the list output
    :return: None
    """
    if n > 0:
        for i in char_list:
            parentheses_recur(char_list, n-1, f"{str_output}{i}", list_output)
    else:
        print_with_check_parentheses(str_output, n, list_output)


def parentheses(n):
    """
    The main part of the parentheses functions.
    :param n: number of letters of each list
    :return: list_output
    """
    list_output = []
    parentheses_recur(["(", ")"], n * 2, "", list_output)
    return list_output


# eight function : flood_fill(image, start)


def check_pos(image, pos):
    """
    this function chek the position
    :param image: the image of "*" and "."
    :param pos: the position
    :return: True or False
    """
    if pos[1] >= len(image)-1 or pos[0] >= len(image[0])-1 or pos[0] == 0 or pos[1] == 0:
        return False
    if "*" == image[pos[1]][pos[0]]:
        return False
    return True


def change_pos(image, pos):
    """
    this function change the position by calling the next function fill around
    :param image: the image
    :param pos: the position
    :return:None
    """
    if check_pos(image, pos):
        fill_around(image, pos)


def fill_around(image, pos):
    """
    this function is doing the movements up down right and left
    :param image: the image
    :param pos: the position
    :return: None
    """
    image[pos[1]][pos[0]] = "*"
    pos_up = (pos[0], pos[1]-1)
    change_pos(image, pos_up)
    pos_down = (pos[0], pos[1] + 1)
    change_pos(image, pos_down)
    pos_left = (pos[0]-1, pos[1])
    change_pos(image, pos_left)
    pos_right = (pos[0]+1, pos[1])
    change_pos(image, pos_right)


def flood_fill(image, start):
    """
    this function call fill around
    :param image: the image
    :param start: the position that we start with
    :return: None
    """
    fill_around(image, start)
