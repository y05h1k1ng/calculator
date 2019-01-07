import re
from math import sin, cos, tan

def math_func(part):
    '''
    evalの力に圧倒された過去の遺産
    入力にsin(10)とかあったら数字だけ出して，計算する．
    正規表現のところでうまく数字だけ取り出せない．ダメ
    '''
    if 'sin' in part:
        a = re.search(r'\d+', part)
        result = sin(int(a.group()))
    elif 'cos' in part:
        a = re.search(r'\d+', part)
        result = cos(int(a.group()))
    elif 'tan' in part:
        a = re.search(r'\d+', part)
        result = tan(int(a.group()))
    return result

def calc(part):
    '''
    math_func()と同様にevalに負けた遺産
    単純な四則演算ができる．こちらは動く．
    '''
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
    '''
    sentenceから任意のものにマッチングして，計算結果に置換する関数
    置換していって数字以外のものにマッチングしなくなったら終了する．
    三角関数から計算して，次に乗除算，最後に加減算をすることで，計算順序がうまくいくと思ってる．
    長い式を入れると，だめかもしれない．
    evalの存在に気づいてしまったので，きちんとデバッグしてないです．
    '''
    while re.search(r'\D', sentence):
        if re.search(r'sin\(\d+\)|cos\(\d+\)|tan\(\d+\)', sentence):
            match_list = re.findall(r'sin\(\d+\)|cos\(\d+\)|tan\(\d+\)', sentence)
            calc_result = math_func(match_list[0])
        elif re.search(r'\d+[*/]\d+', sentence):
            match_list = re.findall(r'\d+[*/]\d+', sentence)
            calc_result = calc(match_list[0])
            sentence = sentence.replace(match_list[0], str(calc_result))
        elif re.search(r'\d+[+-]\d+', sentence):
            match_list = re.findall(r'\d+[+-]\d+', sentence)
            calc_result = calc(match_list[0])
            sentence = sentence.replace(match_list[0], str(calc_result))
    return sentence

def main():
    message = 'Hello. If you give q-key to me, I finish.\nAvailable : +, -, *, /, %, sin(), con(), tan()\n'
    print(message)

    while True:
        sentence = input('>>')

        if 'q' == sentence:
            print('Goodbye!!!')
            break
        
        #sentenceから空白を抜く，matching()に入れるときに困るから書いていた
        sentence = sentence.replace(' ', '')

        result = eval(sentence)
        
        print(result)

if __name__ == "__main__":
    main()
