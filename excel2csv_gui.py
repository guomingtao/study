#-*-coding:utf-8-*-
import pandas as pd
import os
#获取excl,本脚本要和excel文件放在同一目录下
excl_files = []
path = r"C:\Users\cm\Desktop\test"
files = os.listdir(path)
print(files)
for file in files:
     file=path+'\\'+file
     # print(file)
     # print(file.split(".")[-1])
     if file.split(".")[-1] == 'xlsx' or file.split(".")[-1] == 'xls':
         excl_files.append(file)

print(excl_files)
# #创建文件夹
input_dir = os.path.exists(os.path.join(path,'csv'))

if input_dir is False:
     os.mkdir(os.path.join(path,'csv'))
print(input_dir)
# os.system('cd C:\\Users\\cm\\Desktop\\test')
# #读取文件
for excl_file in excl_files:

    datas = pd.read_excel(excl_file,sheet_name=None)

    #转换文件
    for name,data in datas.items():
        # print(name)
        # print(data)
        input_name = str(excl_file.split("\\")[-1]).split('.')[0]+'_'+name+'.csv'
        csv_path = os.path.join(path,'csv',input_name)
        if not data.empty:
            data.to_csv(csv_path,encoding='utf-8',index=False)
os.chdir(os.path.join(path,'csv'))
os.system('copy *.csv out.csv')


# 多个excel文件合并成一个excel表的方法二、使用CMD命令
#
# 1、将需要合并的excel文件格式修改为“csx”文件格式;
#
#
# 2、打开excel文件所在路径，按下“shift”+右键，然后点击“此处打开命令窗口”;
#
# 3、在其中输入“copy *.csv out.csv”，就会把该路径下的所有csv文件合并到“out.csv”文件中;
#
# 4、新生成的out.csv文件也在改路径下。
#
# 以上就是小编今天为大家带来的多个excel文件合并成一个excel表的方法以及如何快速合并多个excel文件全部内容，希望能够帮助到大家。