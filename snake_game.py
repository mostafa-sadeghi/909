# exercise 1:
'''
برنامه ای بنویسید که یک لیست از اعداد بسازد
و اعضای لیست را از انتها به ابتدا نمایش دهد
تعداد اعداد سه تا
حتما از حلقه استفاده کنید
اعداد را از ورودی دریافت نمائید
'''
numbers = []
running = True
counter = 1
while running:
    new_number = float(input(f'Enter number {counter}: '))
    numbers.append(new_number)
    if input('Do you want to quit? (y or n) ') == 'y':
        running = False

    counter += 1

for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i], end=" ")


# exercise 2
'''
برنامه ای بنویسید که اعداد لیست بالا را مرتب نماید 
به صورت صعودی یعنی از کوچک به بزرگ

'''
# number = [1,2,4,6,3,2,1,6,7,88,4,1,88]
# exercise 3:
'''
از لیست بالا تکراری ها را حذف نمائید
یعنی از هر عدد فقط یکی در لیست وجود داشته باشد
'''

# exercise 4:
'''
از لیست بالا مجموع کل تعدا را نمایش دهید
سپس مجموع اعداد فرد را نمایش دهید
سپس مجموع اعدا زوج را نمایش دهید
سپس مجموع اعدا تک رقمی را نمایش دهید
سپس مجموع اعداد دو رقمی را نمایش دهید
تعداد اعداد تک رقمی را نمایش دهید
تعداد اعداد دورقمی را نمایش دهید.
'''

# string = """Welcome to programming languages class. we are going to learn python and java and c++ and javascript.
# python is the king of programming languages. we want to be pro in python and other programming languages.
# """
# exercise 5:
'''
برنامه ای بنویسید که تعداد کلمات موجود در متن بالا را نمایش دهد
سپس تعداد تکرار کلمات زیر ار نمایش دهید:
python
java
programming
'''
 # exercise 6:
'''
برنامه ای بنویسید که نام کاربر را از ورودی دریافت نماید و
دو کاراکتر اول اسم او را نمایش دهد
و نیز کاراکتر های اسم او را از انتها به ابتدا نمایش دهد
'''




# from turtle import Screen, Turtle
# display_surface = Screen()
# display_surface.bgcolor('blue')
# display_surface.title("Snake Game")
# display_surface.setup(width=600, height=600)



# running = True
# while running:
#     display_surface.update()