x = int(input())
if 1 <= x <= 100:
   if not x % 3 and not x % 5:
       print("Fizz Buzz")
   elif not x % 3:
       print("Fizz")
   elif not x % 5:
       print("Buzz")
   else:
       print(x)
else:
   print("Ошибка, введите число в диапазоне от 1 до 100")
