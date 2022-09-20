msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
op_lst = ["+", "-", "/", "*"]
memory = 0
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
lazy_dict = {
  "10": msg_10,
  "11": msg_11,
  "12": msg_12
}
flag = False
flag_1 = False
flag_2 = False


def is_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


def is_one_digit(v):
    if v.is_integer() and -10 < v < 10:
        return True
    else:
        return False


def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    if (x == 1 or y == 1) and oper == "*":
        msg = msg + msg_7
    if (x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)



while True:
    print(msg_0)
    equation = input()
    elements = equation.split(" ")
    if elements[0] == "M":
        elements[0] = memory
    if elements[2] == "M":
        elements[2] = memory
    condition_1 = is_float(elements[0])
    condition_2 = is_float(elements[2])
    if condition_1 and condition_2:
        if elements[1] in op_lst:
            check(float(elements[0]), float(elements[2]), elements[1])
            if elements[1] == "+":
                result = float(elements[0]) + float(elements[2])
                print(result)
                while True:
                    print(msg_4)
                    answer = input()
                    if answer == "y":
                        if is_one_digit(result):
                            flag = True
                            msg_index = 10
                            while True:
                                print(lazy_dict[str(msg_index)])
                                answer = input()
                                if answer == "y":
                                    if msg_index < 12:
                                        msg_index += 1
                                        continue
                                    else:
                                        memory = result
                                else:
                                    break
                                break
                        else:
                            memory = result
                        print(msg_5)
                        answ = input()
                        if flag:
                            break
                        if answ == "y":
                            break
                        else:
                            flag_2 = True
                            break
                    else:
                        print(msg_5)
                        answ = input()
                        if answ == "y":
                            flag_2 = True
                            break
                        else:
                            flag_1 = True
                            break
                if flag_1 or flag_2:
                    break
                continue
            elif elements[1] == "-":
                result = float(elements[0]) - float(elements[2])
                print(result)
                while True:
                    print(msg_4)
                    answer = input()
                    if answer == "y":
                        if is_one_digit(result):
                            flag = True
                            msg_index = 10
                            while True:
                                print(lazy_dict[str(msg_index)])
                                answer = input()
                                if answer == "y":
                                    if msg_index < 12:
                                        msg_index += 1
                                        continue
                                    else:
                                        memory = result
                                else:
                                    break
                                break
                        else:
                            memory = result
                        print(msg_5)
                        answ = input()
                        if flag:
                            break
                        if answ == "y":
                            break
                        else:
                            flag_2 = True
                            break
                    else:
                        print(msg_5)
                        answ = input()
                        if answ == "y":
                            flag_2 = True
                            break
                        else:
                            flag_1 = True
                            break
                if flag_1 or flag_2:
                    break
                continue
            elif elements[1] == "*":
                result = float(elements[0]) * float(elements[2])
                print(result)
                while True:
                    print(msg_4)
                    answer = input()
                    if answer == "y":
                        if is_one_digit(result):
                            flag = True
                            msg_index = 10
                            while True:
                                print(lazy_dict[str(msg_index)])
                                answer = input()
                                if answer == "y":
                                    if msg_index < 12:
                                        msg_index += 1
                                        continue
                                    else:
                                        memory = result
                                else:
                                    break
                                break
                        else:
                            memory = result
                        print(msg_5)
                        answ = input()
                        if flag:
                            break
                        if answ == "y":
                            break
                        else:
                            flag_2 = True
                            break
                    else:
                        print(msg_5)
                        answ = input()
                        if answ == "y":
                            flag_2 = True
                            break
                        else:
                            flag_1 = True
                            break
                if flag_1 or flag_2:
                    break
                continue
            elif elements[1] == "/" and float(elements[2]) != 0:
                result = float(elements[0]) / float(elements[2])
                print(result)
                while True:
                    print(msg_4)
                    answer = input()
                    if answer == "y":
                        if is_one_digit(result):
                            flag = True
                            msg_index = 10
                            while True:
                                print(lazy_dict[str(msg_index)])
                                answer = input()
                                if answer == "y":
                                    if msg_index < 12:
                                        msg_index += 1
                                        continue
                                    else:
                                        memory = result
                                else:
                                    break
                                break
                        else:
                            memory = result
                        print(msg_5)
                        answ = input()
                        if flag:
                            break
                        if answ == "y":
                            break
                        else:
                            flag_2 = True
                            break
                    else:
                        print(msg_5)
                        answ = input()
                        if answ == "y":
                            flag_2 = True
                            break
                        else:
                            flag_1 = True
                            break
                if flag_1 or flag_2:
                    break
                continue
            else:
                print(msg_3)
                continue
        else:
            print(msg_2)
            continue
    else:
        print(msg_1)
        continue
