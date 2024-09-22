from django.db import connection
from django.test import TransactionTestCase

from apps.common.models import BaseModel


class AbstractModelTestCase(TransactionTestCase):
    model_class: type[BaseModel]

    @classmethod
    def setUpClass(cls):
        # Dynamically create the table for the test model
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(cls.model_class)

        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        # Dynamically destroy the table for the test model
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(cls.model_class)

        super().tearDownClass()
