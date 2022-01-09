# https://www.codewars.com/kata/55466989aeecab5aac00003e

def sqInRect(lng, wdth):
    append_list = []
    if lng != wdth:
        def internal_function(lng, wdth):
            if lng < wdth:
                lng, wdth = wdth, lng
            append_list.append(wdth)
            if lng != wdth:
                lng, wdth = wdth, lng - wdth
                return internal_function(lng, wdth)
            else:
                return append_list
    else:
        return None
    return internal_function(lng, wdth)


#   sqInRect(5, 3) should return [3, 2, 1, 1]
print(sqInRect(5, 3))
