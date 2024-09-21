from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from apps.portfolio.models import Education, Portfolio


class PortfolioFactory(DjangoModelFactory):
    class Meta:
        model = Portfolio


class EducationFactory(DjangoModelFactory):
    class Meta:
        model = Education

    portfolio = SubFactory(PortfolioFactory)
    school = Faker('company')
    degree = Faker('job')
    start = Faker('date_this_decade')
    end = Faker('date_this_decade', before_today=True, after_today=False)
    location = Faker('city')
    description = Faker('paragraph')
