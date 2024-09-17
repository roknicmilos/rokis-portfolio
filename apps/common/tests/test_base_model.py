from django.core.exceptions import ValidationError

from apps.common.models import BaseModel
from apps.common.tests import AbstractModelTestCase


class ConcreteModel(BaseModel):
    class Meta:
        app_label = "concrete_model"
        db_table = "concrete_model"
        verbose_name = "Concrete Model"


class TestBaseModel(AbstractModelTestCase):
    model_class = ConcreteModel

    def setUp(self):
        super().setUp()
        self.model = ConcreteModel()

    def test_adds_global_validation(self):
        self.model.add_validation_error('A global error occurred')
        self.assertIn(
            'A global error occurred',
            self.model.validation_errors['__all__']
        )
        self.assertTrue(self.model.has_validation_errors)

    def test_adds_field_validation_error(self):
        self.model.add_validation_error('Field error', 'test_field')
        self.assertEqual(
            self.model.validation_errors['test_field'],
            'Field error'
        )
        self.assertTrue(self.model.has_validation_errors)

    def test_has_validation_errors_false(self):
        self.assertFalse(self.model.has_validation_errors)

    def test_has_validation_errors_true(self):
        self.model.add_validation_error('A global error occurred')
        self.assertTrue(self.model.has_validation_errors)

    def test_clean_raises_no_error(self):
        """
        Test that clean does not raise an error
        when there are no validation errors
        """
        self.model.clean()

    def test_clean_raises_error(self):
        """
        Test that clean raises ValidationError
        when there are validation errors
        """
        self.model.add_validation_error('A global error occurred')
        with self.assertRaises(ValidationError) as cm:
            self.model.clean()
        self.assertIn(
            'A global error occurred',
            cm.exception.message_dict['__all__']
        )
