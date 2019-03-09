def function_ves(haystack, needles):
    try:
        iterstack = iter(haystack)
        for needle in needles:
            hay = next(iterstack)
            while hay != needle:
                hay = next(iterstack)
    except StopIteration:
        return False

    return True


def function_grote(haystack, needles):
    last_needle = 0
    for needle in needles:
        if needle in haystack[last_needle:]:
            last_needle += haystack[last_needle:].index(needle) + 1
        else:
            return False
    return True


def function_kosa(haystack, needles):
    hay_left = len(haystack)
    iterstack = iter(haystack)
    for needle in needles:
        while hay_left:
            hay_left -= 1
            if needle == next(iterstack):
                break
        else:
            return False
    return True


def function_eivl(haystack, needles):
    hay_iter = iter(haystack)
    return all(n in hay_iter for n in needles)


def function_scragly(haystack, needles):
    i = 0
    for n in haystack:
        if n in needles[i:i+1]:
            i += 1
    return needles[i:] == []
