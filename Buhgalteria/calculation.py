class BUHGALTERIA:
    
    def __init__(self, name):
        self.name = name
        self.share_of_the_balance_sheet_2021 = 0
        self.share_of_the_balance_sheet_2022 = 0
        self.share_of_the_balance_sheet_2023 = 0
        self.changes_in_dynamics_2022_2021 = 0
        self.changes_in_dynamics_2023_2022 = 0
        
    def accountant(self):
        print(f'Добрый день, {self.name}. Давайте рассчитаем вертикальный анализ вашего бухгалтерского баланса')
    
    def calculation(self):
        year_2021 = float(input('Введите сумму дебиторской задолжности вашего предприятия за 2021 год: '))
        year_2022 = float(input('Введите сумму дебиторской задолжности вашего предприятия за 2022 год: '))
        year_2023 = float(input('Введите сумму дебиторской задолжности вашего предприятия за 2023 год: '))
        
        balance_summary_2021 = float(input('Введите итог баланса вашего предприятия за 2021 год: '))
        balance_summary_2022 = float(input('Введите итог баланса вашего предприятия за 2022 год: '))
        balance_summary_2023 = float(input('Введите итог баланса вашего предприятия за 2023 год: '))
        
        self.share_of_the_balance_sheet_2021 = year_2021 / balance_summary_2021 * 100
        self.share_of_the_balance_sheet_2022 = year_2022 / balance_summary_2022 * 100
        self.share_of_the_balance_sheet_2023 = year_2023 / balance_summary_2023 * 100
        
        self.changes_in_dynamics_2022_2021 = self.share_of_the_balance_sheet_2022 - self.share_of_the_balance_sheet_2021
        self.changes_in_dynamics_2023_2022 = self.share_of_the_balance_sheet_2023 - self.share_of_the_balance_sheet_2022
        
    def final(self):
        print('Доля к итогу баланса 2021\tДоля к итогу баланса 2022\tДоля к итогу баланса 2023')
        print(f'{self.share_of_the_balance_sheet_2021}\t\t{self.share_of_the_balance_sheet_2022}\t\t{self.share_of_the_balance_sheet_2023}')
        
        print('Изменения в доле 2022 к 2021\tИзменения в доле 2023 к 2022')
        print(f'{self.changes_in_dynamics_2022_2021}\t\t{self.changes_in_dynamics_2023_2022}')