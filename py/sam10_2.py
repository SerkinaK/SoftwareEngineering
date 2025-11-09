def read_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content.strip():
                raise Exception("файл пустой")
            print(f"Содержимое файла: {content}")
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    read_file_content('txt1.txt')
    read_file_content('txt2.txt')