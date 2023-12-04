from bs4 import BeautifulSoup
import os
import requests
from art import tprint

tprint("AUTHOR: ALYX")
N = int(input("Сколько задач хотите решить:   "))


def CreatbyPrefers():
    """
    Создание файлов формато py и md + парсинг и запись данных
    на файл формата md
    :return:
    """
    TN = input("Введите номер задания:  ")
    url = input("Введите ссылку на задание:  ")

    responce = requests.get(url)  # парсинг
    soup = BeautifulSoup(responce.text, "lxml")
    issueSoup = soup.find_all("p", class_="left_margin")
    issue = ''
    for char in issueSoup:
        issue += char.text.replace("­", "")

    Number_NumberTest = 1
    while True:  # Создание папки
        try:
            os.mkdir(f"Задание ЕГЭ номер {TN}.{Number_NumberTest}")
            break
        except FileExistsError:
            Number_NumberTest += 1
            pass

    NewFolder = f"Задание ЕГЭ номер {TN}.{Number_NumberTest}"
    FolderPath = str(os.getcwd()) + str(f"\\{NewFolder}")
    Filepath = os.path.join(FolderPath, f"{NewFolder}.py")
    with open(Filepath, "w") as f:  # Создание файла формата py в этой папке
        f.write(f"")
    Filepath = os.path.join(FolderPath, f"{NewFolder}.md") # Создание файла формата md в этой папке
    with open(Filepath, "w", encoding="utf-8") as f:
        f.write(issue)


def CreatbyRandom():
    pass


while True:
    try:
        print("Выберите способ создания:  \n 1.Простой (Вы сами вводите желаемое задание) \n 2.Рандомный")
        choose = int(input("->  "))
        if choose == 1:
            for i in range(N):
                CreatbyPrefers()
            break
        elif choose == 2:
            CreatbyRandom()
            break
    except ValueError:
        print("Сделайте выбор 1 или 2")
