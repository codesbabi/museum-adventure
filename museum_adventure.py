entrance = input("choose your entrance to the museum\nfront - service - rooftop:\n")

if entrance == "front":
    numbers = input(
        "\nenter three values, two integers and one decimal (a, b, c):\n"
        "(correct if a * b = 294 and c = 3.14):\n"
    ).split()

    if len(numbers) != 3:
        print("defeat")
        exit()

    a = int(numbers[0])
    b = int(numbers[1])
    c = float(numbers[2])

    if a * b == 294 and c == 3.14:
        print("correct")
    else:
        print("defeat")
        exit()

elif entrance == "service":
    integers = input(
        "\nenter two integer numbers (a, b):\n"
        "(correct if a is even, b is odd, and a > b):\n"
    ).split()

    if len(integers) != 2:
        print("defeat")
        exit()

    int1 = int(integers[0])
    int2 = int(integers[1])

    if int1 % 2 == 0 and int2 % 2 == 1 and int1 > int2:
        print("correct")
    else:
        print("defeat")
        exit()

elif entrance == "rooftop":
    decimals = input(
        "\nenter three decimal values:\n"
        "(correct if they satisfy the triangle inequality):\n"
    ).split()

    if len(decimals) != 3:
        print("defeat")
        exit()

    d1 = float(decimals[0])
    d2 = float(decimals[1])
    d3 = float(decimals[2])

    if (d1 + d2 > d3) and (d1 + d3 > d2) and (d2 + d3 > d1):
        print("correct")
    else:
        print("defeat")
        exit()

else:
    print("defeat")
    exit()

items = input(
    "\nchoose two items:\n"
    "(on a single line, separated by a space)\n"
    "flashlight - key - rope:\n"
).split()

if len(items) != 2:
    print("defeat")
    exit()

if (items[0] != "flashlight" and items[0] != "key" and items[0] != "rope") or \
   (items[1] != "flashlight" and items[1] != "key" and items[1] != "rope"):
    print("defeat")
    exit()

if entrance == "front":
    if "flashlight" in items and "key" in items:
        print("excellent ending")
    elif "flashlight" in items:
        print("neutral ending")
    else:
        print("bad ending")

elif entrance == "service":
    if "key" in items and "rope" in items:
        print("perfect ending")
    elif "key" in items:
        print("neutral ending")
    else:
        print("bad ending")

elif entrance == "rooftop":
    if "flashlight" in items and "rope" in items:
        print("ninja ending")
    elif "flashlight" in items:
        print("neutral ending")
    else:
        print("bad ending")
```
