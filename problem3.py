def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    temp = str1 + str1
    return str2 in temp


def main():
    str1 = "mineralwater"
    str2 = "ralwatermine"
    print(is_rotation(str1, str2))


if __name__ == "__main__":
    main()