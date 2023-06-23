from time import sleep

def talk(message):
    return "Talk " + message


def main():
    print(talk("Hello World"))
    sleep(10)

if __name__ == "__main__":
    main()
