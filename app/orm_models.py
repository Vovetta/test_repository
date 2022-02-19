from tortoise import Model
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.fields import (
    IntField, CharField, DateField, DecimalField,
    ForeignKeyField,
    ForeignKeyRelation, ReverseRelation,
    RESTRICT
)


class AdvertisingChannel(Model):
    id = IntField(pk=True)
    name = CharField(max_length=30)

    metrics: ReverseRelation['PerformanceMetric']

    class Meta:
        table = 'advertising_channel'


class Country(Model):
    id = IntField(pk=True)
    name = CharField(max_length=2)

    metrics: ReverseRelation['PerformanceMetric']

    class Meta:
        table = 'country'


class OperatingSystem(Model):
    id = IntField(pk=True)
    name = CharField(max_length=7)

    metrics: ReverseRelation['PerformanceMetric']

    class Meta:
        table = 'operating_system'


class PerformanceMetric(Model):
    id = IntField(pk=True)
    date = DateField()
    channel: ForeignKeyRelation[AdvertisingChannel] = ForeignKeyField(
        'models.AdvertisingChannel',
        related_name='metrics',
        on_delete=RESTRICT,
        source_field='channel_id'
    )
    country: ForeignKeyRelation[Country] = ForeignKeyField(
        'models.Country',
        related_name='metrics',
        on_delete=RESTRICT,
        source_field='country_id'
    )
    os: ForeignKeyRelation[OperatingSystem] = ForeignKeyField(
        'models.OperatingSystem',
        related_name='metrics',
        on_delete=RESTRICT,
        source_field='os_id'
    )
    impressions = IntField()
    clicks = IntField()
    installs = IntField()
    spend = DecimalField(max_digits=4, decimal_places=2)
    revenue = DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        table = 'performance_metric'
