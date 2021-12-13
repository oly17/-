import pandas as pd
df= pd.DataFrame({'Назва показника':['Балансовий прибуток', 'Балансовий прибуток',
                                    'Валовий дохід', 'Валовий дохід',
                                    'Витрати обігу', 'Витрати обігу',
                                    'Рівень валового доходу', 'Рівень валового доходу',
                                    'Рівень витрат обігу', 'Рівень витрат обігу',
                                    'Рівень рентабельності', 'Рівень рентабельності',
                                    'Товарообіг', 'Товарообіг'],
                 'Одиниця виміру':['грн', 'грн',
                                   'грн', 'грн',
                                   'грн', 'грн',
                                   '%', '%',
                                   '%', '%',
                                   '%', '%',
                                   'грн', 'грн'],
                 'Підприємство':['Дніпрянка', 'Універсам 22',
                                 'Дніпрянка', 'Універсам 22',
                                 'Дніпрянка', 'Універсам 22',
                                 'Дніпрянка', 'Універсам 22',
                                 'Дніпрянка', 'Універсам 22',
                                 'Дніпрянка', 'Універсам 22',
                                 'Дніпрянка', 'Універсам 22'],
                 'Базовий рік':[36778.70,1815.50,231711.50,6612.00,19979.40,5026.40,8.30,8.35,7.20,6.35,1.30,2.00,2797552.00,79280.50],
                 'Попередній рік':[91621.20,32013.00,288496.70,86523.80,201597.40,35922.00,17.30,17.80,12.10,7.39,5.50,6.52,1665429.00,486088.80],
                 'Поточний рік':[89377.60,25584.00,553434.90,91429.00,469761.10,51211.00,19.30,19.68,16.40,11.02,3.10,5.38,2861819.00,464588.00],
                 'Відхилення(+,-)абсолютне':[52598.90,23768.50,321723.40,84817.00,269781.70,46184.60,11.00,11.33,9.20,4.67,1.80,3.38,64267.00,385307.50] ,
                 '%':[2.43,14.09,2.39,13.83,2.35,10.19,2.33,2.36,2.28,1.74,2.38,2.69,1.02,5.86],
                 'Відхилення(+,-)абсолютне':[-2243.60,-6429.00,264938.20,4905.20,268163.70,15289.00,2.00,1.88,4.30,3.63,-2.40,-1.14,1196390.00,-21500.80],
                 '%':[0.98,0.80,1.92,1.06,2.33,1.43,1.12,1.11,1.36,1.49,0.56,0.83,1.72,0.96]
                 })
def opentabble_1():
    df.to_excel('./table_1.xlsx')