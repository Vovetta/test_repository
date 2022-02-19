from datetime import date
from typing import Optional, List, Set

from fastapi import Query


class PerformanceMetricsRequest:
    relational_fields = ('channel', 'country', 'os')
    grouping_fields = {'date', 'channel', 'country', 'os'}
    filtering_fields = {
        'date_from': 'date__gte',
        'date_to': 'date__lte',
        'channel': 'channel__name__in',
        'country': 'country__name__in',
        'os': 'os__name__in'
    }

    def __init__(
        self,
        date_from: Optional[date] = Query(None, description='Start of the filtering period'),
        date_to: Optional[date] = Query(None, description='End of the filtering period'),
        channel: List[str] = Query([], description='Channels for filtering'),
        country: List[str] = Query([], description='Countries for filtering'),
        os: List[str] = Query([], description='Operating systems for filtering'),
        group_by: Set[str] = Query(set(), description='Grouping by columns'),
        order_by: List[str] = Query(
            [],
            description='Ordering in ascending order ("column") and descending order ("-column")'
        ),
        columns: List[str] = Query([], description='Columns that need to be returned')
    ):
        local_variables = locals()
        self.filters = {
            value: local_variables[key]
            for key, value in PerformanceMetricsRequest.filtering_fields.items()
            if local_variables[key]
        }
        self.group_by = self.to_orm_fields(
            group_by & PerformanceMetricsRequest.grouping_fields,
            PerformanceMetricsRequest.relational_fields
        )
        self.order_by = self.to_orm_fields(order_by, PerformanceMetricsRequest.relational_fields)
        self.return_columns = self.to_orm_fields(columns, PerformanceMetricsRequest.relational_fields)

    def to_orm_fields(self, columns, relational_fields):
        return [
            column
            if column.lstrip('-') not in relational_fields
            else column + '__name'
            for column in columns
        ]
