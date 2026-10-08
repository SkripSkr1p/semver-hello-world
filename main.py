def main():
    name = input("Введите ваше имя: ").strip()
    language = input("Выберите язык (ru/en): ").strip().lower()

    if language == "ru":
        greeting = "Привет"
    else:
        greeting = "Hello"

    if name:
        print(f"{greeting}, {name}!")
    else:
        print(f"{greeting}, World!")


if __name__ == "__main__":
    main()