import os


def CreateTest(TN: str, TC: str) -> "files":

    """
    Функция для создания директории для решения задания ЕГЭ
    :param TN: НОМЕР ЗАДАНИЯ
    :param TC: СОДЕРЖАНИЕ ЗАДАНИЯ
    :return: СОЗДАЁТ ФАЙЛЫ
    """

    Number_NumberTest = 1
    while True:
        try:
            os.mkdir(f"Задание ЕГЭ номер {TN}.{Number_NumberTest}")
            break
        except FileExistsError:
            Number_NumberTest += 1
            pass

    NewFolder = f"Задание ЕГЭ номер {TN}.{Number_NumberTest}"
    FolderPath = str(os.getcwd()) + str(f"\\{NewFolder}")
    Filepath = os.path.join(FolderPath, f"{NewFolder}.txt")
    with open(Filepath, "w") as f:
        f.write(TC)
    Filepath = os.path.join(FolderPath, f"{NewFolder}.py")
    with open(Filepath, "w") as f:
        f.write("")


TestNumber = input("Напишите номер задания:  ")
TestContent = input("Напишите содержание задания:  ")

CreateTest(TestNumber, TestContent)
