import time
import typing as t

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from home.models import Message


class Command(BaseCommand):
    URL_SEND_MESSAGE = "https://api.telegram.org/bot{}/sendMessage"
    URL_SEND_FILE = "https://api.telegram.org/bot{}/sendDocument"
    MESSAGE_TEMPLATE = """Имя: {}
    Телефон: {}

    Текст:
    {}
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._settings = settings.ENV_SETTINGS.message_forwarder

        if not self._settings.api_token or not self._settings.chat_id:
            raise RuntimeError("API token or chat id not specified")

        self._url_send_message = self.URL_SEND_MESSAGE.format(
            settings.api_token
        )
        self._url_send_file = self.URL_SEND_FILE.format(settings.api_token)

    def handle(self, *args, **kwargs):
        while True:

            self.stdout.write("Command")
            while True:
                messages = Message.objects.filter(
                    is_acknowledged=False
                )[:self._settings.batch_size]
                if not messages:
                    break

                self._process_messages(messages)

            time.sleep(self._settings.worker_timeout)

    def _process_messages(self, messages: t.Iterable[Message]):
        for message in messages:
            msg = self.MESSAGE_TEMPLATE.format(
                message.name, message.phone, message.text
            )
            try:
                requests.post(
                    self._url_send_message,
                    data={
                        "chat_id": self._settings.chat_id, "text": msg
                    },
                    timeout=self._settings.request_timeout,
                )
                if message.file:
                    requests.post(
                        self._url_send_file,
                        data={
                            "chat_id": self._settings.chat_id,
                            "text": msg,
                        },
                        files={"document": message.file},
                        timeout=self._settings.request_timeout,
                    )
            except requests.exceptions.Timeout:
                self.stdout.write("Timeout error")
                continue

            message.is_acknowledged = True
            message.save()
