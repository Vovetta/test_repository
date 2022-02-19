from datetime import date
from decimal import Decimal
from typing import Optional, Any

from pydantic import BaseModel, Field


class PerformanceMetricsResponse(BaseModel):
    id: Optional[int]
    date: Optional[date]
    channel: Optional[Any] = Field(None, alias='channel__name')
    country: Optional[Any] = Field(None, alias='country__name')
    os: Optional[Any] = Field(None, alias='os__name')
    impressions: Optional[int]
    clicks: Optional[int]
    installs: Optional[int]
    spend: Optional[Decimal]
    revenue: Optional[Decimal]
    cpi: Optional[Decimal]
