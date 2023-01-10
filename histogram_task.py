import codecs

def histogramm(string: str) -> dict:
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1

    return sym_dict


def gen_line(file_name) -> dict:
    for row in codecs.open(file_name, 'r', 'utf-8'):
        yield histogramm(row)


for i_sym in gen_line('150gb_file.txt'):
    for i in sorted(i_sym.items()):
        print(i)
    
