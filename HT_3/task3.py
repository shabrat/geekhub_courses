Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)

def seasons(month):
   if month == 12 or 1 <= month <= 2:
       print("Winter")
   elif  3 <= month <= 5:
       print("Spring")
   elif 6 <= month <= 8:
       print("Summer")
   elif 9 <= month <= 11:
       print("Autumn")
   else:
       print("Not to day!")
n = int(input("Please enter a number of month: "))
seasons(n)
