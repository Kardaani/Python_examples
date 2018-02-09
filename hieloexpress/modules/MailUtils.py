import smtplib

class MailUtils:
    def send_mail(subject, body):
        print("sending mail: {subject: " +
              subject +
              ", body: " +
              body +
              "}");
        username = 'sgvinci@gmail.com'
        password = '98ikj7uiol'
        subject = "Subject: " + subject
        msg = "\r\n".join([
          "From: sgvinci@gmail.com",
          "To: sgvinci@gmail.com",
          subject,
          "",
          body
          ])
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(username, username, msg)
        server.quit()
