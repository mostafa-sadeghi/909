# TODO   برنامه ای بنویسید ک هیک عدد از ورودی دریافت نماید و تمام ارقام آن را جداگانه نمایش دهد
# برنامه ای بنویسید که دو عدد از ورودی بگیرد و تعداد ارقام مشترک ان ها را محاسب هو نمایش دهد


# def my_function(number):
#     while number:
#         print(number % 10)
#         number //= 10

# my_function(678)

# def my_function(number):
#     number = str(number)
#     for i in range(len(number)-1, -1, -1):
#         print(number[i])
# my_function(678)

# def my_function(number1, number2):
#     number1 = str(number1)
#     number2 = str(number2)
#     count = 0

#     for i in range(len(number1)):
#         for j in range(len(number2)):
#             if number1[i] == number2[j]:
#                 count += 1

#     return count


# print(my_function(623, 153))


# TODO
"""
بازی bagels
برنامه یک عدد سه رقمی تولید می نماید و بازیکن ده بار فرصت حدس زدن عدد را دارد
اگر عدد را درست حدس بزند برنامه با پیغامی مناسب خاتمه می یابد
اما اگر عدد را اشتباه حدس بزند برنامه پیام را به صورت زیر نمایش می دهد
اگر هر سه رقم عددی که کاربر حدس زده است اشتباه باشد
برنامه
bagels را نمایش می دهد
اگر رقم درست باشد اما سرجایش نباشد
برنامه پیام
pico را نمایش دهد

اگر رقم درست باشد و سر جایش باشد
برنامه پیغام
fermi را نمایش دهد

123

678  => bagels
145 => fermi
451 => pico

126 => fermi, fermi
351 => pico, pico


"""

from random import randint
from random import shuffle


def create_secret_number(num_of_digits):
    all_digits = list('0123456789')
    shuffle(all_digits)
    number = ''
    for i in range(num_of_digits):
        number += all_digits[:num_of_digits][i]
    return number


def generate_result(user_guess, secret_number):
    if user_guess == secret_number:
        return 'You Won!!!'
    res = ''
    for i in range(len(user_guess)):
        if user_guess[i] == secret_number[i]:
            res += 'Fermi, '
        elif user_guess[i] in secret_number:
            res += 'Pico, '
    if len(res) == 0:
        return 'bagels'
    return res


secret_number = create_secret_number(3)
print("secret_number", secret_number)
counter = 1
while counter <= 10:
    print(f'Time #{counter}')

    user_guess = input("Enter your guess: ")
    res = generate_result(user_guess, secret_number)
    if user_guess == secret_number:
        print("You Won!!!")
        break
    print(res)
    counter += 1
