def main():
    print('python prcatice')

def to_decimal_degrees(deg, min, sec):
    result = deg/60 + min/(60) + sec/(60*60)
    return result

a = to_decimal_degrees(59,10,45)
print(a)


if __name__ == "__main__":
    main()