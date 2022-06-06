#-*-coding:utf-8-*-
import pybase64
import io,sys
import tkinter as tk
from tkinter import filedialog
import sys,os

# 图片转换成base64
def picture2base(path):
    imageSuffix=path.split('.')[-1]
    path1 = path.split('.')[-2] + ".txt"
    print(path1)
    with open(path, 'rb') as img:
        # 使用base64进行编码
        b64encode = pybase64.b64encode(img.read())
        s = b64encode.decode()
        base64 = 'data:image/{};base64,{}'.format(imageSuffix,s)
        with open(path1, 'wb') as file:
            file.write(base64.encode())
         #返回base64编码字符串
         # return base64


# base64转换成图片
def base2picture(base64,path):
    # 分割字符串
    res=base64.split(',')[1]
    # 使用base64进行解码
    b64decode = pybase64.b64decode(res)
    image = io.BytesIO(b64decode).read()
    #图片输出目录
    with open( path , 'wb' ) as file:
        file.write(image)


if __name__ == '__main__':


    # print('请选择文件夹')
    # root = tk.Tk()
    # root.withdraw()
    # rootpath = filedialog.askdirectory()
    # print('文件夹选择完毕，路径为：', rootpath)

    print('请选择图片')
    waterpath = filedialog.askopenfilename()
    print('水印图片选择完毕，路径为：', waterpath)
    print(picture2base(waterpath))

    # parser = argparse.ArgumentParser(description='Base64转换脚本')
    # sub_parsers = parser.add_subparsers()
    # picture2base_sub = sub_parsers.add_parser('picture2base', help='picture2base 图片转base64')
    # picture2base_sub.add_argument('--path',type=str, default=None, help='图片路径')
    #
    # base2picture_sub = sub_parsers.add_parser('base2picture', help='base2picture base64转图片')
    # base2picture_sub.add_argument('--inputpath', type=str, default=None, help='存放base64字符串文件')
    # base2picture_sub.add_argument('--outoutpath',type=str, default=None, help='输出图片路径及名称')
    #
    # # paser.add_argument()
    # args = parser.parse_args()

    #print(args.to)
    #print(args.subject)
    #print(args.body)
    # print(picture2base(args.path))
    # if sys.argv[1] == "picture2base":
    #     print(picture2base(args.path))
    # else:
    #     with open(args.base64, 'r', encoding='utf-8') as file:
    #         f=file.readline()
    #         base2picture(f,args.path)




