from typing import Optional
from pydantic import BaseModel, HttpUrl


class Location(BaseModel):
    status: Optional[str] = None
    continent: Optional[str] = None
    continentCode: Optional[str] = None
    country: Optional[str] = None
    countryCode: Optional[str] = None
    region: Optional[str] = None
    regionName: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    zip: Optional[str] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    timezone: Optional[str] = None
    offset: Optional[int] = None
    currency: Optional[str] = None
    isp: Optional[str] = None
    org: Optional[str] = None
    as_: Optional[str] = None
    asname: Optional[str] = None
    mobile: Optional[bool] = None
    proxy: Optional[bool] = None
    hosting: Optional[bool] = None


class User(BaseModel):
    # ip: Optional[str] = None
    user_agent: Optional[str] = None
    referer: Optional[HttpUrl] = None
    accept_language: Optional[str] = None
    host: Optional[str] = None
    # forwarded_for: Optional[str] = None
    forwarded_proto: Optional[str] = None
    cookies: Optional[str] = None
    content_type: Optional[str] = None
    method: Optional[str] = None
    path: Optional[str] = None
    query_string: Optional[str] = None
    source: Optional[str] = None
    campaign: Optional[str] = None
    timestamp: Optional[str] = None
    location: Optional[Location] = None
