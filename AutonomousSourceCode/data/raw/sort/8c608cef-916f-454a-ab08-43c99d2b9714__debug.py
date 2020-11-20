#coding: utf-8

import db

def inter_operation(): #ввод операции
    op = input('Enter operation: insert/out/search power/search model/edit car/delete car/move car: ')
    return op

def incorrect_operation(): #сообщение в случае ошибки ввода комманды
    print('Error! Incorrect operation.')

def out_cars(): #напечатать содержимое базы данных
    data,is_empty = db.load_from_pickle()
    
    if is_empty == False:
        data_sorted = data[:]
        data_sorted.sort(key=lambda i:i['model'])
        for i in range (len(data_sorted)): # выводим автомобили по алфавиту
            print(data_sorted[i]['model'],data_sorted[i]['power'],data_sorted[i]['sign'],data_sorted[i]['x'],data_sorted[i]['y'],data_sorted[i]['d'])
            
