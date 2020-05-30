import re


def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print("Длина строки равна " + str(len(content)) + " символам")
        print("В тексте " + str(len(re.findall(r'\w+', content))) + " слов")
        new_content=content.replace('.', '!')


    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    print(main())
