# Michael Suter
# List & def
# 10.14.19
print("Lets take a look at the Hartwicks bakery sales")
candy = []
cookies = []


def candy_values():
    print("Type in the last 6 months of sales for candy separately")
    for candy_value in range(0, 6):
        candy_sales = int(input("> "))
        candy.append(candy_sales)


candy_values()
print(f"Here is the past 6 months sales of candy{candy}.")  # give some space between the word 'candy' and the variable {candy}
#  you could have added Line 17 or 28 (here is the ... sales) to the definition loop, since it happens multiple times

def cookie_values():
    print("Type in the last 6 months of sales for cookies separately")
    for cookie_value in range(0, 6):
        cookie_sales = int(input("> "))
        cookies.append(cookie_sales)


cookie_values()
print(f"Here is the past 6 months sales of cookies{cookies}.")
print("Now its time to average both the cookies and the candy")
#  I noticed you executed your functions (cookie_values()) etc... directly after your defintions, 
#  you could have a section specifically for definitions, and another for code execution.

def average_candy():
    print("Here is the average sales per month for candy:")
    added_candy = int(candy[0] + candy[1] + candy[2] + candy[3] + candy[4] + candy[5])
    avg_candy = (int(added_candy) / 6)
    print(avg_candy)
#  no return statement? probably not needed anyway

average_candy()


def average_cookies():
    print("Here is the average sales per month for cookies:")
    added_cookies = int(cookies[0] + cookies[1] + cookies[2] + cookies[3] + cookies[4] + cookies[5])
    avg_cookies = (int(added_cookies) / 6)
    print(avg_cookies)
    return


average_cookies()


def min_candy():
    candy.sort()
    print("Here is the minimum sales for candy out of the 6 months", candy[1])


def max_candy():
    candy.sort()
    print("Here is the maximum sales for candy out of the 6 months", candy[-1])


def min_cookies():
    cookies.sort()
    print("Here is the minimum sales for cookies out of the 6 months", cookies[1])


def max_cookies():
    cookies.sort()
    print("Here is the maximum sales for cookies out of the 6 months", cookies[-1])


min_candy()
max_candy()
min_cookies()
max_cookies()

if candy > cookies:
    print("Candy is more popular than cookies.")
elif cookies > candy:
    print("Cookies are more popular than candy")
elif cookies == candy:
    print("Cookies and candy are equally popular")
#  good shit mike
