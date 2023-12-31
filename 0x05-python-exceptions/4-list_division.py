#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    result_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
            continue
        except ZeroDivisionError:
            print("division by 0")
            result = 0
            continue
        except IndexError:
            print("out of range")
            result = 0
            continue
        finally:
            result_list.append(result)
    return result_list
