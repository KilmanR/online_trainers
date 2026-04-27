import requests

url = "https://gitverse.ru/api/repos/tatakudyago/PYAPI_Homework/raw/branch/master/exercise3/1.txt"
response = requests.get(url)       # 1. Скачиваем
response.encoding = 'utf-8'        # 2. Принудительно задаём кодировку
text1 = response.text               # 3. Только теперь читаем текст
# print(text1)

url = "https://gitverse.ru/api/repos/tatakudyago/PYAPI_Homework/raw/branch/master/exercise3/2.txt"
response = requests.get(url)       
response.encoding = 'utf-8'        
text2 = response.text              
# print(text2)

url = "https://gitverse.ru/api/repos/tatakudyago/PYAPI_Homework/raw/branch/master/exercise3/3.txt"
response = requests.get(url)       
response.encoding = 'utf-8'        
text3 = response.text              
# print(text3)

lines1 = text1.splitlines()  ------рок
lines2 = text2.splitlines()
lines3 = text3.splitlines()
# print(lines2)

count1 = len(lines1)    # Считаем длину каждого списка
count2 = len(lines2)
count3 = len(lines3)
# print(count3)

# Делаем список с кортежами с полученными данными
files_data = [("1.txt", count1, lines1), ("2.txt", count2, lines2), ("3.txt", count3, lines3)]
# print(files_data)

sorted_data = sorted(files_data, key=lambda x: x[1]) # Сортируем по 2-му индексу(длина списка строк)

with open("result.txt", "w", encoding="utf-8") as f: # Создаём, кодировка
    for item in sorted_data:
        f.write(item[0] + "\n")     # Перенос строки возвращаем как было
        f.write(str(item[1]) + "\n")    # Число в строку
        for line in item[2]:
            f.write(line + "\n")

# with open("result.txt", "r", encoding="utf-8") as f:
#     result = f.read()  # Загоняем полученный файл в переменную
#     print(result)                  