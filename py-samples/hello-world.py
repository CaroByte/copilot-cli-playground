MESSAGE = "Hello from the Copilot CLI playground!"


def greet(name: str = "developer") -> None:
    print(f"{MESSAGE} Nice to meet you, {name}.")


if __name__ == "__main__":
    greet()
