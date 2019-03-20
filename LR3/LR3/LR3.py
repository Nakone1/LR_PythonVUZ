import  os

def menu():#выводит меню 
    print ("Выберите команду:\n0-Выход из программы\n1-Посчитать количество файлов \n2-Отсортировать файлы по цене\n3-Изменение значения цены\n4-Сохранение файлов")
    n=int(input())
    print("Вы выбрали",n,"-ую команду\n")
    return n


def end():#выводит вопрос после выполнения функции
        print("Желаете продолжить?")
        print("1-yes, 0-no")
        answ=int(input())
        return answ


def firstf():
    print("Количество файлов в папке:", len(os.listdir("newfolder")))
    pass


def secondf():
    print('Желаете отсортировать список? (Да-1 | Нет-0)')
    answ=int(input())
    if answ==1:
        t = input('Отсортировать по возрастанию (0) или по убыванию (1)?\n') 
        t = int(t) 
        s.sort(key=lambda line: int(line[2]), reverse=t) 
        for i in range(0, len(s)): 
            print(s[i])
    pass


def thirdf(max):
        max1=max
        print("Введите id товаров, у которых хотите изменить количество\n stop - остановка ввода\n Максимальный ID-", max1)
        id=[]
        work=True
        while work:
            num=input("#: ")
            if num.isdigit():
                num = int(num)
                if num <=max1:
                    id.append(num-1)
                else:
                    print("Ошибка! Максимальный ID = ", max1)
            elif num.lower() == "stop":
                work=False
            else:
                print("Неверный ввод!")
        count = int(input("Введите на сколько хотите уменьшить количество товара:" ))
        for i in range(0,len(id)):
            if int(s[id[i]][3]) - count >=0:
                s[id[i]][3]= int(s[id[i]][3])-count
            else:
                s[id[i]][3]=0 #ввод id 
        for i in range(0, len(s)): 
            print(s[i])
        pass


def fourthf():
        print("Создать отдельный файл? (1-да 0-нет)")
        answ=int(input())
        if answ==1:
            print("Создаю новый файл....")
            f1 = open('newfolder/productsnew.txt', 'tw', encoding='utf-8')
            with open('newfolder/productsnew.txt','w') as outfile:
                for i in range(0,len(s)):
                    f1.write("\n")
                    for j in range(0,len(s)):
                        f1.write(str(s[i][j]))
                        f1.write(' ')
            f1.close()
        else:
            print("Записываю в старый файл....")
            f2 = open('newfolder/changed.txt', 'tw', encoding='utf-8')
            with open('newfolder/changed.txt','w') as outfile:
                for i in range(0,len(s)):
                    f2.write("\n")
                    for j in range(0,len(s)):
                        f2.write(str(s[i][j]))
                        f2.write(' ')
            f.close()


#начало основной команды
f=open("newfolder/products.txt","r")
s=[]
for line in f:
    line = line.split(";")
    s.append([line[0],line[1],line[2],line[3]])
answ=1
max=-1
for i in range(0, len(s)): 
    if int(s[i][0])>max:
        max=int(s[i][0])
while answ==1:
    
    n=menu() 
    if n!=0: 
        if n==1:#1я функция
            firstf()
        elif n==2:#2я функция
            secondf()
        elif n==3:#3я функция
            thirdf(max)
        elif n==4:#4я функция
            fourthf()
    else:
        print("Выход из программы....")  
        break 
    answ=end() 
f.close()
