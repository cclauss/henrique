# -*- coding: utf-8 -*-

import smtplib

from models import ReportModel
from email.mime.text import MIMEText
from datetime import datetime

class MainWindowHelper(object):

    def __init__(self, ui, report):
        self.ui = ui
        self.report = report

    def refreshUi(self):
        self.ui.ReportText.setText(self.report['content'])
        self.updateStatus()

    def updateStatus(self):
        text = 'This report wasn\'t sent'
        style = 'color: red'

        if self.report['status'] == ReportModel.STATUS_SENT:
            text = 'This report was already sent'
            style = 'color: green'

        self.ui.StatusLabel.setText(text)
        self.ui.StatusLabel.setStyleSheet(style)

class InvalidEmailSetings(ValueError):
    pass

class EmailHelper(object):

    def __init__(self, smtp_settings, email_settings):
        self.smtp_settings = smtp_settings
        self.email_settings = email_settings

    def getReportTitle(self, report):
        date = datetime.strptime(report['date'], ReportModel.DATETIME_FORMAT)
        return date.strftime(self.email_settings['subject'])

    def makeSMTP(self):
        classname = 'SMTP_SSL' if self.smtp_settings['security'] == 'ssl' else 'SMTP'
        address = str(self.smtp_settings['address'])
        port = str(self.smtp_settings['port'])
        smtp = getattr(smtplib, classname)(address, port)

        if self.smtp_settings['security'] == 'starttls':
            smtp.starttls()

        return smtp

    def sendReport(self, report):
        smtp = self.makeSMTP()
        message = MIMEText(report['content'], _charset='utf-8')
        message['From'] = self.email_settings['from']
        message['Subject'] = self.getReportTitle(report)

        smtp.set_debuglevel(True)
        smtp.login(self.smtp_settings['username'], self.smtp_settings['password'])
        smtp.sendmail(self.email_settings['from'], self.email_settings['to'], message.as_string())
        smtp.close()

