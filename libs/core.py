import csv
from libs.compare import compare

# dictreader поможет находить значение сущности не по индексу, а по ключу
def csv_columns_to_rows(data: list) -> dict[list]:

    headers = data[0].keys()      # получение заголовков, чтоб можно было находить значчения этих пар по ключу

    output = {}

    for header in headers:                                    
        output[header] = [items[header] for items in data]    # items[header] это определенное поле, например name

    return output


def csv_filter(data: list, filter: str):

    filter = filter.replace(' ', '')

    if not filter: return data

    columns = csv_columns_to_rows(data)   # чтобы брать значение из одной колонки
    filtered_values = []

    for oper in ['=', '<', '>']:    

        if oper in filter:
            key, comparing_value = filter.split(oper)    # знак превращает строку в список имен значений

        else: continue

        if not columns[key]:
            raise KeyError(f'Unknown column header: {columns[key]}')

        for row in data:
            if compare(row[key], oper, comparing_value):
                filtered_values.append(row)   # .append() добавляет вложенный список

    return filtered_values


def csv_aggregate(data: csv.DictReader, aggr: str):
         
    key, aggr = aggr.replace(' ', '').split('=')    # убирает пробелмы, делит выражение на два элемента и берет второй

    if not aggr: return data

    rows = [row for row in data]
    row = [float(row[key]) for row in rows]

    if aggr == 'min':
        return min(row)
        
    if aggr == 'avg':
        return sum(row) / len(row)
        
    if aggr == 'max':
        return max(row)
