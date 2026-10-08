def main():
    name = input("Введите ваше имя: ").strip()
    language = input("Выберите язык (ru/en): ").strip().lower()
    uppercase = input("Использовать верхний регистр? (y/n): ").strip().lower()

    if language == "ru":
        greeting = "Привет"
    else:
        greeting = "Hello"

    if name:
        message = f"{greeting}, {name}!"
    else:
        message = f"{greeting}, World!"

    if uppercase == "y":
        message = message.upper()

    print(message)


if __name__ == "__main__":
    main()