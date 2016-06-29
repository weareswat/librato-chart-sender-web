from chart_sender import LibratoChartSender
import os

class SendChartInteractor:

    def __init__(self, config_db):
        self.config_db = config_db

    def run(self, config_id):
        configuration = self.config_db.find_by_id(config_id)
        char_ids = configuration.chart_ids.split(', ')
        recipients = configuration.recipients_emails.split(', ')
        chart_sender = LibratoChartSender(
            configuration.librato_user,
            configuration.duration,
            char_ids,
            recipients,
            {
               'librato_api_key': configuration.librato_api_key,
               'mailgun_api_key': os.environ['MAILGUN_API_KEY']
            }
        )
        chart_sender.run()
