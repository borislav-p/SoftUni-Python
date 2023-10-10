def is_palindrome(input_string):
    num_list = [x for x in input_string.split(', ')]

    reverse = lambda x: x[::-1]

    for num in num_list:
        if num == reverse(num):
            result = True
        else:
            result = False
        print(result)




input_string = input()
is_palindrome(input_string)