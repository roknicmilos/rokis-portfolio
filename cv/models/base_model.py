from django.core.exceptions import ValidationError
from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validation_errors = {
            '__all__': []
        }

    def add_validation_error(
        self,
        message: str,
        field_name: str = None
    ) -> None:
        if field_name is None:
            self.validation_errors['__all__'].append(message)
        else:
            self.validation_errors[field_name] = message

    def has_validation_errors(self) -> bool:
        return bool(
            self.validation_errors['__all__']
            or len(self.validation_errors) > 1
        )

    def clean(self):
        super().clean()
        if self.validation_errors:
            raise ValidationError(self.validation_errors)
