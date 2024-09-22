from django.core.exceptions import ValidationError
from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validation_errors = {}

    def add_validation_error(
        self, message: str, field_name: str = None
    ) -> None:
        if field_name is None:
            if "__all__" not in self.validation_errors:
                self.validation_errors["__all__"] = []
            self.validation_errors["__all__"].append(message)
        else:
            self.validation_errors[field_name] = message

    @property
    def has_validation_errors(self) -> bool:
        return bool(self.validation_errors)

    def clean(self):
        super().clean()
        if self.has_validation_errors:
            raise ValidationError(self.validation_errors)

    def update(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.full_clean()
        self.save()
