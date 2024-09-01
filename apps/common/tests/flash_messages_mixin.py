from django.contrib import messages
from django.http import HttpResponse
from django.test import TestCase
from django.contrib.messages.storage.base import Message


class FlashMessagesMixin(TestCase):

    def assertFlashMessage(
        self,
        response: HttpResponse,
        message: str,
        level: int = None
    ) -> None:
        actual_message = self._find_flash_message(
            response=response,
            message=message
        )
        if not actual_message:
            self.fail(f'Flash message "{message}" was not found')
        if level and actual_message.level != level:
            self.fail(
                f'Message "{message}" has level "{actual_message.level}", '
                f'but expected level is "{level}"'
            )

    def assertSuccessFlashMessage(
        self,
        response: HttpResponse,
        message: str
    ) -> None:
        self.assertFlashMessage(
            response=response,
            message=message,
            level=messages.SUCCESS
        )

    def assertErrorFlashMessage(
        self,
        response: HttpResponse,
        message: str
    ) -> None:
        self.assertFlashMessage(
            response=response,
            message=message,
            level=messages.ERROR
        )

    @staticmethod
    def _find_flash_message(
        response: HttpResponse,
        message: str
    ) -> Message | None:
        message_list = list(messages.get_messages(response.wsgi_request))
        return next(
            (msg for msg in message_list if msg.message == message),
            None
        )
