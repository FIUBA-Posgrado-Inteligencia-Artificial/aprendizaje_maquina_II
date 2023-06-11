def funcion():
    return None

def funcion_2():
    return None

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="description of the script")

    parser.add_argument(
        "-f",
        "--argument_1",
        type=int,
        help="first number",
        required=True)

    parser.add_argument(
        "-s",
        "--argument_2",
        default=0,
        type=int,
        help="second number",
        required=False)

    args = parser.parse_args()

    first_num = args.argument_1
    second_num = args.argument_2

    print(first_num + second_num)