from pathlib import Path
import pandas as pd
path = Path(r"C:\Users\cm\Desktop\test")
excel_data = [(i.stem, pd.read_excel(i)) for i in path.glob("*.xls")]
df_list = []
for name, data in excel_data :
    print(name)
    data["来源"] = name # df增加一列，存入数据所在的文件名
    df_list.append(data)
result = pd.concat(df_list, ignore_index=True)
result.to_excel(path.joinpath("reslut.xlsx"), encoding="utf-8")