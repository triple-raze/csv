# csv

примеры команд:
- `cmd.py --file example.csv` - выводит всю таблицу
- `python cmd.py --file example.csv --where 'brand=apple'` - выводит товары от apple
- `python cmd.py --file example.csv --aggregate 'price=avg'` - выводит среднюю стоимость всех товаров
- `python cmd.py --file example.csv --where 'brand=apple' --aggregate 'price=avg'` - выводит среднюю стоимость на все товары apple
- `python cmd.py --file example.csv --where 'brand=xiaomi' --aggregate 'rating=max'` - выводит максиамльную стоимость из всех товаров xiaomi

