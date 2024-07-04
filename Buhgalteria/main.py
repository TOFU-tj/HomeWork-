from account import accountant
from calculation import BUHGALTERIA
import datetime
        
if __name__ == '__main__':
    print(f"Текущая дата: {datetime.datetime.now()}")
    accountant_name = input('Введите ваше имя: ')
    buhgalteria = BUHGALTERIA(accountant_name)
    buhgalteria.accountant()
    buhgalteria.calculation()
    buhgalteria.final()
