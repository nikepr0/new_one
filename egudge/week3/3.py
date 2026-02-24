"""Problem 303: 393933. String calculator with functions.

Calculate the result of the sum, subtraction, or multiplication of two numbers, but digits are given as triplets of uppercase English characters. For example, ONETWOSEV will be equal to . And you should print the answer in the same way as the given numbers, using triplets of characters.
Input format

You’re given a string consisting only of uppercase English letters, denoting the expression you need to calculate.
Output format

Output the result of the given expression using triplets of letters"""
#Словарь триплет → цифра

triplet_to_digit = {
    'ONE': '1',
    'TWO': '2',
    'THR': '3',
    'FOU': '4',
    'FIV': '5',
    'SIX': '6',
    'SEV': '7',
    'EIG': '8',
    'NIN': '9',
    'ZER': '0'
}

# Обратный словарь: цифра → триплет
#digit_to_triplet = {v: k for k, v in triplet_to_digit.items()}
digit_to_triplet={}
for k, v in triplet_to_digit.items():
    digit_to_triplet[v]=k

def parse_number(s: str) -> int:
    """Преобразует строку из триплетов в обычное число"""
    if len(s) % 3 != 0:
        raise ValueError("Длина строки должна быть кратна 3")
    
    num_str = ''
    for i in range(0, len(s), 3):
        triplet = s[i:i+3]
        if triplet not in triplet_to_digit:
            raise ValueError(f"Неизвестный триплет: {triplet}")
        num_str += triplet_to_digit[triplet]
    
    return int(num_str)


def number_to_triplets(n: int) -> str:
    """Преобразует число обратно в строку из триплетов"""
    if n == 0:
        return 'ZER'
    
    s = str(n)
    result = ''
    for digit in s:
        result += digit_to_triplet[digit]
    return result


def evaluate_expression(expr: str) -> str:
    """
    #Главная функция: разбирает выражение вида A+B, A-B или A*B
    #и возвращает результат в виде триплетов
    """
    # Убираем возможные пробелы (на всякий случай)
    expr = expr.replace(' ', '')
    
    # Ищем оператор
    if '+' in expr:
        op = '+'
        a_str, b_str = expr.split('+')
    elif '-' in expr:
        op = '-'
        a_str, b_str = expr.split('-')
    elif '*' in expr:
        op = '*'
        a_str, b_str = expr.split('*')
    else:
        raise ValueError("Не найден оператор (+, -, *)")
    
    # Парсим оба числа
    a = parse_number(a_str)
    b = parse_number(b_str)
    
    # Вычисляем
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    
    # Преобразуем результат обратно в триплеты
    return number_to_triplets(result)

# Основная программа
if __name__ == "__main__":
    expression = input().strip()
    try:
        answer = evaluate_expression(expression)
        print(answer)
    except Exception as e:
        # В реальном контесте обычно не выводят ошибки, но для отладки полезно
        print("Error:", e)
        
        
        
