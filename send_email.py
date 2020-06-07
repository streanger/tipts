from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText


def send_mail():
    '''send email
    https://stackoverflow.com/questions/64505/sending-mail-from-python-using-smtp
    '''
    # ******* auth data *******
    host = "smtp.wp.pl"
    sender = 'sender@wp.pl'
    password = 'some_password'
    receiver = 'receiver@email.pl'
    destination = [receiver]
    
    
    # ******* msg data *******
    subject = 'Subject'
    text_subtype = 'plain'
    content = """\
    Test message
    """
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = subject
    msg['From'] = sender        # some SMTP servers will do this automatically, not all
    
    
    # ******* sending email *******
    try:
        server = SMTP(host)
        server.login(sender, password)
        server.sendmail(sender, destination, msg.as_string())
        server.quit()
        print("E-mail sent")
        
    except Exception as err:
        print('Error catched: {}'.format(err))
        
    return None
    
    
if __name__ == "__main__":
    send_mail()
