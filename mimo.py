# archive = ['Amazing cats', 'Top 10 Dances', 'Breaking news', 'How to: Tips', 'cats dance']
# results = [result for result in archive if result.count('cats') > 0]
# print(results)

# prices = [10, 38, 40, 58, 62]          # изменение всех данных списка по заданым параметрам
# halved = [price/2 for price in prices]
# print(halved)

# print('переводит текст в цыфры и суммирует их все')
# grades_string = '88-77-59-63'   
# total_grade = 0
# grades_list = grades_string.split('-')
# for num in grades_list:
#     total_grade += int(num)
# print(total_grade)

# birthdays_string = '23-09|25-04|05-09|15-07|01-06'
# special_discount ='You are eligible for a 5% discount'
# birthday_list = birthdays_string.split('|')
# # print(birthday_list)
# for bd in birthday_list:
#     if bd == '15-07':
#         special_discount = special_discount.replace('5%', '10%')
# print(special_discount)

# websites = ['mimo.com', 'cooding.com', 'food.org']
# def add_https(site):
#     return 'https://' + site
# auto_add = [add_https(site) for site in websites]
# print(auto_add)

# print('меняем слово в списке')
# old_top_movies = 'The Power of the Dog - Trapped - Tenet'
# new_top_movies = old_top_movies.replace('Trapped', 'Moonfall')
# print(new_top_movies)

# class Car:
#     def __init__(self):
#         self.on = False

#     def injectFuel(self):
#         print('Spraying fuel')

#     def ingiteFuel(self):
#         print('Boom!')
    
#     def startUp(self):
#         self.on = True
#         while self.on:
#             self.injectFuel()
#             self.ingiteFuel()

# car = Car();
# car.injectFuel()
# car.ingiteFuel()
# car.injectFuel()
# car.ingiteFuel()

# class Coffeemaker:
#     def heatWater(self):
#         print('Heating water')

#     def brew(self):
#         print('Adding water to grounds')

#     def filterCoffee(self):
#         print('Filtering coffee')

#     def makeCoffee(self):
#         self.heatWater()
#         self.brew()
#         self.filterCoffee()

# coffeMaker = Coffeemaker()
# coffeMaker.makeCoffee()

# class IceCreamMaker:
#     def churn(self):
#         print('Churning cream')

#     def freeze(self):
#         print('Freezing cream')

#     def makeIceCream(self):
#         self.churn()
#         self.freeze()

# iceCreamMaker = IceCreamMaker()
# iceCreamMaker.makeIceCream()

# class Translator:
#     def record(self):
#         print('Recording audio')
    
#     def transcribeRecording(self):
#         print('Converting audio to text')

#     def translateText(self):
#         print('Translating text')

#     def translateLive(self):
#         self.record()
#         self.transcribeRecording()
#         self.translateText()

# class Slideshow:
#     def __init__(self, slides):
#         self.slides = slides
#         self.current = 1

#     def viewNextSlide(self):
#         self.current += 1

#     def play(self):
#         while self.current <= self.slides:
#             print('Slide', self.current)
#             self.viewNextSlide()
# slideshow = Slideshow()
# slideshow.play()