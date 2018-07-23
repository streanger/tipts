#!/usr/bin/python3
#edited from smtpTask.py
import time, smtplib, sys, socket

def smtp_address(address):
    if "@gmail.com" in address:
        host = "smtp.gmail.com"
    elif "@wp.pl" in address:
        host = "smtp.wp.pl"
    elif "@o2.pl" in address:
        host = "poczta.o2.pl"
    else:
        print("use 'gmail.com', 'wp.pl', or 'o2.pl' address...")
        sys.exit()
    return host

def mail_smtp(yourMail, yourPass, spamList, content):
    host = smtp_address(yourMail)
    subject = content[0]
    mainText = content[1]
    print("Data:\n\tsender: {}\n\tsmtp_address: {}\n\tsubject: {}\n\tmainText: {}\n{}".format(yourMail, host, subject, mainText, "-"*40))
    for receiver in spamList:
        print("receiver: {}".format(receiver))
        if receiver:
            body = "\r\n".join(("From: %s" % yourMail,"To: %s" % receiver,"Subject: %s" % subject, "", mainText))
            try:
                server = smtplib.SMTP(host)
                server.login(yourMail, yourPass)
                server.sendmail(yourMail, [receiver], body)
                server.quit()
                print("Sending finished...")
                time.sleep(0.1)
                break
            except smtplib.SMTPAuthenticationError:
                print('\nWrong data or server error. Try again later...')
                break
            except smtplib.SMTPServerDisconnected:
                print('\nConnection broken by host computer...')
                time.sleep(0.1)
                break
            except socket.gaierror:
                print('\nConnection error. Finishing...')
                time.sleep(0.1)
                break
        else:
            print("no receiver...")
    else:
        print("empty spamList...")


if __name__ == "__main__":
    content = ["Subject example", "Put some text here"]
    spamList = []
    yourMail = input("put your email address:\n")
    yourPass = input("put password:\n")
    mail_smtp(yourMail, yourPass, spamList, content)   #iterating over spamList
