# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:29:37 2019

@author: 智源
"""

#! /usr/bin/env python
#coding=utf-8
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

from email.mime.multipart import MIMEMultipart

'''
sending pure text
'''
def send_emails( receivers, mail_title, mail_content ):
    #qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    #sender_qq为发件人的qq号码
    sender_qq = '2514574092'
    #pwd为qq邮箱的授权码
    pwd = '填写自己的相关授权码' ## h**********bdc
    #发件人的邮箱
    sender_qq_mail = '2514574092@qq.com'
    
    
    #ssl登录
    # 这里使用默认端口，25
    smtp = SMTP_SSL(host_server) 
    
    #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(0) 
    smtp.ehlo(host_server) #除非想要调用has_extn(), 否则不必call this method explicitly
    smtp.login(sender_qq, pwd)
    
    msg = MIMEText(mail_content, _subtype="plain", _charset='utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    #msg["To"] = Header("接收者测试", 'utf-8') ## 接收者的别名, 由于这里是群发，就先不填了
        
    smtp.sendmail(sender_qq_mail, receivers, msg.as_string())
    smtp.quit()

'''
sending email with attach file.
'''
def send_emails_attach( receivers, mail_title, mail_content, attach_file ):
    sender = '2514574092'
    sender_mail = '2514574092@qq.com'
    pwd = 'tgxfyztqymdkdjbi'
    smtp_server = 'smtp.qq.com'
    
    # prepare the email
    msg = MIMEMultipart()
    msg['from'] = sender
    msg['to'] = ' '
    msg['Subject'] = Header( mail_title, 'utf-8' )
    # content
    msg.attach( MIMEText( mail_content , 'plain', 'utf-8' ) )

    att1 = MIMEText( open(attach_file, 'r').read(), 'base64', 'utf-8' )
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="hello.pdf" '
    msg.attach( att1 )
    
    print( "hello" )
    smtp = SMTP_SSL( smtp_server )
    #smtp.connect( smtp_server )
    smtp.login( sender , pwd )
    smtp.sendmail(sender_mail, receivers, msg.as_string() )
    print( "FINISH" )
    smtp.quit()


'''
这里要求email_file中每一行为一个邮箱
'''
def read_receivers( email_file='people2email.txt'):
    with open(email_file ) as f :
        ans = []
        for line in f.readlines() :
            ans.append( line.strip() )
    return ans 
    
if __name__ == '__main__' :
    #收件人邮箱
    receivers = ['lizhy_sysu@126.com']
    #邮件的正文内容
    mail_content = """
你好，我叫xxx，是xxx。
    麻烦你能在收到邮件后抽出时间，在xxx，谢谢合作。
    """
    #邮件标题
    mail_title = 'SYSU-关于xxx去向统计'
    #receivers = read_receivers( 'people2email.txt')
    #receivers.append('lizhy_sysu@126.com')
    print( receivers )
    #send_emails(receivers, mail_title, mail_content)
    attach_file = "people2email.txt"
    attach_file = "0190.pdf" 
    attach_file = "单词.docx"
    send_emails_attach(receivers, mail_title, mail_content, attach_file )
    print( "success." )
    

'''
# 定义SMTP服务器地址:
smtp_server = 'smtp.qq.com'
from_addr = '2514574092@qq.com'
# 定义登录邮箱的密码
password = 'tgxfyztqymdkdjbi'
'''
