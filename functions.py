from function_registry import haystack_functions


@haystack_functions
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


@haystack_functions
def function_grote(haystack, needles):
    last_needle = 0
    for needle in needles:
        if needle in haystack[last_needle:]:
            last_needle += haystack[last_needle:].index(needle) + 1
        else:
            return False
    return True


@haystack_functions
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


@haystack_functions
def function_eivl(haystack, needles):
    hay_iter = iter(haystack)
    return all(n in hay_iter for n in needles)


@haystack_functions
def function_scragly(haystack, needles):
    i = 0
    for n in haystack:
        if n in needles[i:i+1]:
            i += 1
    return needles[i:] == []


@haystack_functions
def function_shirayuki(haystack: list, needles: list) -> bool:
    try:
        found, _index = -1, haystack.index
        for i in needles:
            found = _index(i, found + 1)
    except ValueError:
        return False
    return True


@haystack_functions
def function_bytecommander(hs, ns):
    try:
        hi = iter(hs)
        for n in ns:
            while n != next(hi): pass
        return True
    except StopIteration:
        return False


@haystack_functions
def function_bast_reduce(haystack: list, needles: list) -> bool:
    return [i for i in haystack if i in needles] == needles
