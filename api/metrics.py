from typing import List

from fastapi import APIRouter, Depends
from tortoise.expressions import F
from tortoise.functions import Sum

from app.orm_models import PerformanceMetric
from app.request_models import PerformanceMetricsRequest
from app.response_models import PerformanceMetricsResponse

metrics_router = APIRouter(
    prefix='/metrics'
)


@metrics_router.get(
    '',
    response_model=List[PerformanceMetricsResponse],
    response_model_exclude_unset=True,
    response_model_by_alias=False
)
async def metrics_query(args: PerformanceMetricsRequest = Depends()):
    """"""
    query = PerformanceMetric.filter(**args.filters).annotate(cpi=F('spend') / F('installs'))
    if args.order_by:
        query = query.order_by(*args.order_by)
    if args.group_by:
        query = query.annotate(
            impressions=Sum('impressions'),
            clicks=Sum('clicks'),
            installs=Sum('installs'),
            spend=Sum('spend'),
            revenue=Sum('revenue')
        ).group_by(*args.group_by)
    if args.return_columns:
        query = query.values(*args.return_columns)
    result = await query
    return result
