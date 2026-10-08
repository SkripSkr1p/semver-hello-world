def main():
    name = input("Введите ваше имя: ").strip()

    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")


if __name__ == "__main__":
    main()