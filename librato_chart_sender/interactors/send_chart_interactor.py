from chart_sender import LibratoChartSender
class SendChartInteractor:

   def run(self, configuration):
       recipient_ids = configuration
       chart_sender = LibratoChartSender([3419, 3420, 3421], ['pawel.krysiak@rupeal.com'], {
           'librato_api_key': 'b4bf0341c8cdd3b429826a18d1a07582895fa12c7fb97eb8f2c6bdb015004b86',
           'mailgun_api_key': 'key-a05af654983f6c57ec99904a3b84c7b3'})
       chart_sender.run()
