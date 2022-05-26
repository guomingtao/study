import argparse
paser = argparse.ArgumentParser(description='Hello World!')
paser.add_argument('--to',type=str,default=None,help='收件人邮件地址')
paser.add_argument('--subject',type=str,default=None,help='邮件主题')
paser.add_argument('--body',type=str,default=None,help='邮件内容')
#paser.add_argument()
args = paser.parse_args()
print(args.to)
print(args.subject)
print(args.body)


