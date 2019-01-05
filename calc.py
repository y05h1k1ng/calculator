import re
import math

def math_func(part):
    if 'sin' in part:
        a = re.match(r'\d+', part)
        result = math.sin(int(a.group()))
    elif 'cos' in part:
        a = re.match(r'\d+', part)
        result = math.cos(int(a.group()))
    elif 'tan' in part:
        a = re.match(r'\d+', part)
        result = math.tan(int(a.group()))
    return result

def calc(part):
    if '*' in part:
        a = part.split('*')
        result = int(a[0]) * int(a[1])
    elif '/' in part:
        a = part.split('/')
        result = int(a[0]) / int(a[1])
    elif '+' in part:
        a = part.split('+')
        result = int(a[0]) + int(a[1])
    elif '-' in part:
        a = part.split('-')
        result = int(a[0]) - int(a[1])
    return result

def matching(sentence):
    if re.search(r'sin\(\d+\)|cos\(\d+\)|tan\(\d+\)', sentence):
        match_list = re.findall(r'sin\(\d+\)|cos\(\d+\)|tan\(\d+\)', sentence)
        calc_result = math_func(match_list[0])
    elif re.search(r'\d+[*/]\d+', sentence):
        match_list = re.findall(r'\d+[*/]\d+', sentence)
        calc_result = calc(match_list[0])
    return calc_result

def main():
    message = 'Hello. If you give q-key to me, I finish.\nAvailable : +, -, *, /, sin(), con(), tan()\nNote : Don\'t include space!'
    print(message)

    while True:
        sentence = input('>>')

        if 'q' == sentence:
            print('Goodbye!!!')
            break
        
        result = matching(sentence)
        
        print(result)

if __name__ == "__main__":
    main()
