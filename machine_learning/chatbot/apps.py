from django.apps import AppConfig
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from .signals import creating_answer_function


class ChatbotConfig(AppConfig):
    name = 'chatbot'
    verbose_name = _('ChatBot')

    def ready(self):
        myccl = self.get_model('Question')
        post_save.connect(creating_answer_function, sender=myccl, dispatch_uid="my_unique_identifier")
