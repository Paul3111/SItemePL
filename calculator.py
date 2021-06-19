def operations(nr1: int, operation: str, nr2: int) -> (str, float):
    result_text = "The result is: "
    if operation == "+":
        return result_text, (nr1 + nr2)
    elif operation == "-":
        return result_text, (nr1 - nr2)
    elif operation == "*":
        return result_text, (nr1 * nr2)
    elif operation == "/" and nr2 != 0:
        return result_text, (nr1 / nr2)
    elif operation == "/" and nr2 == 0:
        print("Cannot divide by 0!")


def calculator() -> tuple:
    dict_operations = {"subtraction": "-", "addition": "+", "multiplication": "*", "division": "/"}
    print("\nAvailable operations: ")

    for key, value in dict_operations.items():
        print(f"{key} {value}")

    a = int(input("\nInsert first nr.: "))
    op = input("\nChoose a mathematical operation: ")
    b = int(input("\nInsert the second number nr.: "))

    result = operations(a, op, b)
    return result


def run() -> tuple:
    while True:
        [print(x) for x in calculator()]
        restart = input("\nDo you wish to perform another mathematical operation?(y/n) ")
        if restart.lower() == "y":
            [print(x) for x in calculator()]
        else:
            break

    return calculator()


run()
