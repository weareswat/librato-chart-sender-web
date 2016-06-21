from ..models import Configuration
class ConfigDB:

    @classmethod
    def find_by_id(cls, config_id):
        return Configuration.objects.get(id=config_id)

    @classmethod
    def create_configuration(cls, config_params):
        new_config = Configuration(librato_user=config_params['email_username'],
                                   librato_api_key=config_params['api_key'],
                                   recipients_emails=','.join(config_params['recipients']),
                                   chart_ids=','.join(config_params['chart_ids']),
                                   interval=1,
                                   duration=2,
                                   template='something to change')
        new_config.save()
        return new_config

    @classmethod
    def update_configuration(cls, config_id, update_params):
        config = Configuration.objects.filter(id=config_id).update(
            librato_user=update_params['email_username'],
            librato_api_key=update_params['api_key'],
            recipients_emails=','.join(update_params['recipients']),
            chart_ids=','.join(update_params['chart_ids']),
            interval=1,
            duration=2,
            template='something to change'
        )
        return config

    @classmethod
    def delete_configuration(cls, config_id):
        config = Configuration.objects.get(id=config_id)
        config.delete()
        return config
