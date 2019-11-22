"""Crypto: tool for encrypting and decrypting messages.

Exercises

1. Review 'ord' and 'chr' functions and letter-to-number mapping.
2. Explain what happens if you use key 26.
3. Find a way to decode a message without a key.
4. Encrypt numbers.
5. Make the encryption harder to decode.


"""
# 非字母 加密不行，36行分配机制
#凯撒密码

def encrypt(message, key):#加密消息，密钥-加密解密
    "Encrypt message with key."
    result = ''#生成结果

    # Iterate letters in message and encrypt each individually.

    for letter in message:
        if letter.isalpha():

            # Letters are numbered like so:
            # A, B, C - Z is 65, 66, 67 - 90
            # a, b, c - z is 97, 98, 99 - 122

            num = ord(letter)

            if letter.isupper():
                base = ord('A')
            elif letter.islower():
                base = ord('a')

            # The encryption equation:

            num = (num - base + key) % 26 + base

            result += chr(num)

        elif letter.isdigit():

            # TODO: Encrypt digits.
            result += letter

        else:
            result += letter

    return result#返回接收结果进行

def decrypt(message, key):
    "Decrypt message with key."#密钥解密
    return encrypt(message, -key)#接收密文，解密密钥

def decode(message):#未实现
    "Decode message without key."
    pass  # TODO

def get_key():
    "Get key from user."#设置密钥以及输入解密密钥
    try:
        text = input('Enter a key (1 - 25): ')#明文加密=输入设置的密钥范围(1 - 25)
        key = int(text)#密钥接收=加密成功生成密文
        return key#密钥接收
    except:#超出范围
        print('Invalid key. Using key: 0.')#无效密钥
        return 0

print('Do you wish to encrypt, decrypt, or decode a message?')
choice = input()#两个选项：1加密=“encrypt”，2解密=“decrypt”  3选项未实现
###########################                ###################################
if choice == 'encrypt':#条件判断是否选择加密  输入选项1 ，1加密=“encrypt”
    phrase = input('Message: ')#短语提示=输入“明文消息”  选择加密密钥数字1-25
    code = get_key()#生成对应  密文
    print('Encrypted message:', encrypt(phrase, code))#状态：  加密消息：密文
elif choice == 'decrypt':#条件判断是否选择解密  输入选项2 ，2解密=“decrypt”
    phrase = input('Message: ')#短语提示=输入“密文”  选择解密密钥数字
    code = get_key()#生成对应  明文
    print('Decrypted message:', decrypt(phrase, code))#状态：  解密消息：明文
elif choice == 'decode':#未实现
    phrase = input('Message: ')
    print('Decoding message:')
    decode(phrase)
else:#超出以上设置选项
    print('Error: Unrecognized Command')#显示报错无法识别命令
