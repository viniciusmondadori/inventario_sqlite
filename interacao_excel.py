import pandas as pd

def excel_data_extraction(path):
    excel_file = path
    df= pd.read_excel(excel_file)
    dict = df.to_dict() 

    i = 0

    data=[]
    form_data = []
    keys = list(dict.keys())

    while i < len(dict[keys[0]]):
        for key, value in dict.items():
            data.append(value[i])
        
        form_data.append(tuple(data))
        data.clear()
        i += 1

    return form_data
