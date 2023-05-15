def z1():
    def idb3(number):
        if number % 3 == 0:
            return True
        else:
            return False

def z2():
    def d100bn():
        try:
            number = float(input("Введите число: "))
            if number == 0:
                raise ZeroDivisionError
            result = 100 / number
            return result
        except ValueError:
            print("Вы ввели не число.")
        except ZeroDivisionError:
            print("На ноль делить нельзя.")

def z3():
    def img(date_str):
        day, month, year = map(int, date_str.split("."))
        if day * month == year % 100:
            return True
        else:
            return False

def z4():
    def iln(number):
        length = len(number)
        if length % 2 != 0:
            return False
        half_length = length // 2
        first_half_sum = sum(map(int, number[:half_length]))
        second_half_sum = sum(map(int, number[half_length:]))
        return first_half_sum == second_half_sum
z1()
z2()
z3()
z4()