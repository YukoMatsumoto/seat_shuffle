# - [] リストを用意する

# 　- [] リストからランダムに出力させるようにしたい

import random


def main():
    with open("member.tex", mode="r") as f:
        member = f.read()
        member_list = member.split("\n")

        random.shuffle(member_list)

        table1 = " ".join(member_list[0:6])

        print(f"Table1:{table1}")

        #    print(f.read())


# f.write("内田\n")
# f.write("大江\n")
# f.write("則也\n")
# f.write("美香子\n")
# f.write("鹿糠\n")
# f.write("川合\n")
# f.write("工藤\n")
# f.write("杉村\n")
# f.write("高橋\n")
# f.write("中川\n")
# f.write("中俣\n")
# f.write("松本\n")
# f.write("三村\n")
# f.write("横川\n")
# f.write("吉田")

#   f.close()


if __name__ == "__main__":
    main()
