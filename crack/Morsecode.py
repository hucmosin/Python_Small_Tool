# -*- coding:utf-8 -*-
#摩斯密码不能加解密汉字，只能加解密字母


#字典文件
CODE = {
        # 26个字母
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
 
        # 10个数字
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
 
        # 16个标点符号
        ',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.',
        '?': '..--..', '=': '-...-',  "'": '.----.', '/': '-..-.',
        '!': '-.-.--', '-': '-....-', '_': '..--.-', '(': '-.--.',
        ')': '-.--.-', '$': '...-..-','&': '. . . .','@': '.--.-.'

}

#字典反转
UNCODE =  dict(map(lambda t:(t[1],t[0]), CODE.items()))

#莫斯加密
def encode(msg):
    message = ''
    if msg == None:
        print "加密内容错误！请重新输入！"
    else:
        try:
            for char in msg:
                if char == ' ':
                    message +=''
                else:
                    message += CODE[char.upper()] + '/'
        except:
            print "加密内容错误！请重新输入！"
    return message


#莫斯解密
def decode(msg):
    message = ''
    if msg == None:
        print "解密内容错误！请重新输入！"
    else:
        list = msg.split('/')
        try:
            for char in list:
                if char == ' ':
                    message +=''
                else:
                    message += UNCODE[char]
        except:
            pass
    return message


#程序信息
def info():
    
    print '**************************************'
    print '*莫斯密码加解密小程序                  *'
    print '*作者:mosin                          *'
    print '*摩斯密码不能加解密汉字，只能加解密字母   *'
    print '*字典可以随意增加                      *'
    print '**************************************'

def main():
    info()
    while(1):
        msg = raw_input("请选择：\n\r1.莫斯密码加密\n\r2.莫斯密码解密\n\r3.退出\n\r请输入：")
        if int(msg) == 1:
            str1 = raw_input("请输入要加密的内容：")
            en = encode(str1)
            print en
            """
            f = open('result.txt','a')
            f.write('\n\r加密内容：\n\r'+en)
            f.close()
            """
        elif int(msg) == 2:
            str2 = raw_input("请输入要解密的内容：")
            de = decode(str2)
            print de
            """
            f1 = open('result.txt', 'a')
            f1.write('\n\r解密内容：\n\r' + de)
            f1.close()
            """
        elif int(msg) == 3:
            break

if __name__ == "__main__":
    main()
