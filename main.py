#UwU-Stalin-UwU
#Main file of lab

import capsule as caps


def main():
    user_choice = int(input("Для функции логгирования выберите 1, для списка сонибоев выберите 2: "))
    if user_choice == 1:
        caps.hello()

if __name__ == "__main__":
    main()