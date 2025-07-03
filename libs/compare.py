def compare(arg1: int | float, operator: str, arg2: int | float):
    
    if operator == '=': return arg1 == arg2
    
    if operator == '<': return float(arg1) < float(arg2)
    
    if operator == '>': return float(arg1) > float(arg2)

    raise ValueError(f'Unknown operator: {operator}')