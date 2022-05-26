

import pandas as pd
import os
#获取excl,本脚本要和excel文件放在同一目录下
excl_files = []
df_list = []
path = r"C:\Users\cm\Desktop\test"
files = os.listdir(path)
print(files)
for file in files:

     file=path+'\\'+file
     # print(file)
     # print(file.split(".")[-1])
     if file.split(".")[-1] == 'xlsx' or file.split(".")[-1] == 'xls':
         excl_files.append(file)


for excl_file in excl_files:
    datas = pd.read_excel(excl_file,sheet_name=None)
    for name, data in datas.items():
        data["来源"] = name
        df_list.append(data)
    result = pd.concat(df_list, ignore_index=True)
    result.to_excel(os.path.join(path,"reslut.xls"), encoding="utf-8")
    #
    #
    # for name,data in datas.items():
    #     # print(name)
    #     # print(data)
    #     input_name = str(excl_file.split("\\")[-1]).split('.')[0]+'_'+name+'.csv'
    #     csv_path = os.path.join(path,'csv',input_name)
    #     if not data.empty:
    #         data.to_csv(csv_path,encoding='utf-8',index=False)

