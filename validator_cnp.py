def validate_gender(code):
    try:
        gender_code = int(code)
        if 1 <= gender_code <= 9:
            return True
        return False
    except ValueError:
        return False


def validate_day(code):
    try:
        if len(code) != 6:
            return False

        year = int(code[:2])
        month = int(code[2:4])
        day = int(code[4:6])

        if not 1 <= month <= 12:
            return False
        else:
            if 1 <= month <= 12 and month != 2:
                if day > 31:
                    return False
            elif month == 2:
                if year % 4 == 0:
                    if day > 28:
                        return False
                else:
                    if day > 29:
                        return False
            else:
                if day > 30:
                    return False
        return True

    except ValueError:
        return False


def validate_region(code):
    try:
        if len(code) != 2:
            return False

        region_code = int(code)
        if 1 <= region_code <= 52:
            return True
        return False

    except ValueError:
        return False


def validate_code(code):
    try:
        if len(code) != 3:
            return False

        code_int = int(code)
        if 1 <= code_int <= 999:
            return True
        return False

    except ValueError:
        return False


def validate_control_digit(code, control_digit):
    if len(code) != 12:
        return False

    number = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    result = 0
    for index in range(len(code)):
        try:
            result += int(code[index]) * number[index]
        except ValueError:
            return False

    reminder = result % 11
    if reminder == 10:
        try:
            if int(control_digit) == 1:
                return True
            return False
        except ValueError:
            return False

    try:
        if int(control_digit) == reminder:
            return True
        return False
    except ValueError:
        return False


def validate(code):

    if len(code) != 13:
        return False

    if not validate_gender(code[0]):
        return False

    if not validate_day(code[1:7]):
        return False

    if not validate_region(code[7:9]):
        return False

    if not validate_code(code[9:12]):
        return False

    if not validate_control_digit(code[0:12], code[12]):
        return False

    return True
