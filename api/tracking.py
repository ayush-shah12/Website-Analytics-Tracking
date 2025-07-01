"""Tracking Logic"""

from fastapi import APIRouter, Request, BackgroundTasks
import logfire
from typing import Any
from datetime import datetime
import pytz

from api.models import User, Location
from api.utils import email_logged_visitor, get_ip_info, email_icon_visited

SOURCE_LOOKUP: dict[str, Any] = {
    "ah12dX": {
        "source": "LinkedIn",
        "campaign": "Social Media",
    },
    "b93ZaM": {
        "source": "GitHub",
        "campaign": "Social Media",
    },
    "q1k7ZP": {
        "source": "Resume",
        "campaign": "Internship/Job Application",
    },
    "jX9q3R": {
        "source": "Email",
        "campaign": "Personal",
    },
}

router = APIRouter()


@router.post("/sddsdax")
async def log_visit(request: Request, background_tasks: BackgroundTasks):
    try:
        headers = request.headers

        now = datetime.now(pytz.timezone("America/New_York"))
        formatted_time = now.strftime("%B %d, %Y %I:%M %p %Z")

        user = User(
            user_agent=headers.get("user-agent"),
            referer=headers.get("referer"),
            accept_language=headers.get("accept-language"),
            host=headers.get("host"),
            forwarded_proto=headers.get("x-forwarded-proto"),
            cookies=headers.get("cookie"),
            content_type=headers.get("content-type"),
            method=request.method,
            path=request.url.path,
            query_string=request.url.query,
            timestamp=formatted_time,
        )

        location_info: Location = get_ip_info(headers.get("x-forwarded-for", None))

        if location_info:
            user.location = location_info

        key = None
        try:
            body_data = await request.json()
            key = body_data.get("asd", None)
        except Exception as e:
            logfire.warn(
                f"""
                Error trying to get JSON body of request.
                Error: {e}
                """
            )

        if not key:
            background_tasks.add_task(email_logged_visitor, user)
        else:
            info = SOURCE_LOOKUP.get(key, None)
            if info:
                user.source = info.get("source", None)
                user.campaign = info.get("campaign", None)
            background_tasks.add_task(email_logged_visitor, user)
        
        background_tasks.add_task(logfire.info, f"""
        Logging User Visit:
        {user.model_dump_json(indent=3)}
        """)
        
        return

    except Exception as e:
        logfire.error(
            f"""
            Error in API Response:
            {e}
        """
        )
        return


@router.post("/sdfc")
async def log_icon_visit(request: Request, background_tasks: BackgroundTasks):
    try:
        body_data = await request.json()
        key = body_data.get("icon", None)
        if key:
            background_tasks.add_task(email_icon_visited, key)
        
        return
    except Exception as e:
        logfire.error(f"Error in icon visit logging: {e}")
        return