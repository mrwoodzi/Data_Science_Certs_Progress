import pandas as pd
import numpy as np


def text_formatter(start, stop):
    def delete_list_gen(start, stop):
        l_array = np.linspace(start, stop)
        float_list = l_array.astype(float)
        round_list = float_list.round(1)
        unique_list = np.unique(round_list)
        py_list = str(unique_list.tolist())
        quote_list = ["Save"]
        for iter in unique_list:
            quote_list.append("%s" % iter)
        delete_list = quote_list
        return delete_list
    delete_list = delete_list_gen(start, stop)
    #infile = "unformatted.txt"
    #outfile = "cleaned_file.txt"
    #with open(infile) as fin, open(outfile, "w+") as fout:
        #for line in fin:
            #for word in delete_list:
                #line = line.replace(word, "")
            #fout.write(line)
    return delete_list


print(text_formatter(1.5, 5.0))

