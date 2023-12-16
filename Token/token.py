import configparser
import secrets
import string


def generate_token(length=16, include_uppercase=True, include_lowercase=True, include_digits=True,
                   include_symbols=True):
    characters = ""

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be included.")

    # 生成令牌
    token = ''.join(secrets.choice(characters) for _ in range(length))
    return token


def read_config(config_file_path='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file_path)
    return config['TokenGenerator']


def main():
    config = read_config()

    # 从配置文件中读取参数
    length = int(config.get('length', 16))
    include_uppercase = config.getboolean('include_uppercase', True)
    include_lowercase = config.getboolean('include_lowercase', True)
    include_digits = config.getboolean('include_digits', True)
    include_symbols = config.getboolean('include_symbols', True)

    # 生成令牌
    custom_token = generate_token(length, include_uppercase, include_lowercase, include_digits, include_symbols)
    print("生成了新的Token，并将Token保存到了token.txt：", custom_token)
    # 写入到token.txt
    with open('token.txt', 'w') as f:
        f.write(custom_token)
        f.close()


if __name__ == "__main__":
    main()
