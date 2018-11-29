import random


def main():
    with open("members.txt", mode="r") as f:
        member = f.read()
        member_list = member.split("\n")

        random.shuffle(member_list)

        table1 = " ".join(member_list[0:6])
        table2 = " ".join(member_list[7:11])
        table3 = " ".join(member_list[12:16])

        print(f"Table1: {table1}")
        print(f"Table2: {table2}")
        print(f"Table3: {table3}")


if __name__ == "__main__":
    main()
