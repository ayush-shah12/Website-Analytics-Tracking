"""utils"""

from api.models import User, Location
from mailjet_rest import Client
import os
import logfire
import requests
import ipaddress

from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["MAIL_API_KEY"]
api_secret = os.environ["MAIL_SECRET_KEY"]
email = os.environ["EMAIL_ADDR"]

location_url = os.environ["LOCATION_URL"]
fields_number = os.environ["FIELDS_NUMBER"]


def email_logged_visitor(user: User):
    """
    Email me the logged user information
    """
    try:
        mailjet = Client(auth=(api_key, api_secret), version="v3.1")

        # Customize subject and body based on source
        if user.source:
            subject = f"New Site Visitor from {user.source}!"
            body = f"""Received a site visitor from {user.source}!
Campaign: {user.campaign if user.campaign else 'N/A'}
Timestamp: {user.timestamp}

Location Info:
{'-' * 50}
City: {user.location.city if user.location and user.location.city else 'N/A'}
Zip: {user.location.zip if user.location and user.location.zip else 'N/A'}
Country: {user.location.country if user.location and user.location.country else 'N/A'}
{'-' * 50}

Full User Details:
{user.model_dump_json()}"""
        else:
            subject = "New Site Visitor!"
            body = f"""Received a site visitor!
Timestamp: {user.timestamp}

Location Info:
{'-' * 50}
City: {user.location.city if user.location and user.location.city else 'N/A'}
Zip: {user.location.zip if user.location and user.location.zip else 'N/A'}
Country: {user.location.country if user.location and user.location.country else 'N/A'}
{'-' * 50}

Full User Details:
{user.model_dump_json()}"""

        data = {
            "Messages": [
                {
                    "From": {"Email": email, "Name": "Site Visitor Service"},
                    "To": [{"Email": email, "Name": "Ayush Shah"}],
                    "Subject": subject,
                    "TextPart": body,
                }
            ]
        }
        result = mailjet.send.create(data=data)
        
        logfire.info(
            f"""
            Mailjet Delivery Status Code: {result.status_code},
            Mailjet Response JSON: {result.json()}
            """
        )
    except Exception as e:
        logfire.error(
            f"""
            Error in Mailjet Delivery. 
            Error: {e}
            """
        )


def get_ip_info(ips_list: str | None = None) -> Location | None:
    """
    get location of request
    """

    def _get_public_ip() -> str | None:
        """trying to get the first public ip"""
        ips = [ip.strip() for ip in ips_list.split(",")]

        for ip_str in ips:
            try:
                ip = ipaddress.ip_address(ip_str)
                if not (
                    ip.is_private
                    or ip.is_loopback
                    or ip.is_reserved
                    or ip.is_link_local
                ):
                    return ip_str
            except ValueError:
                continue
        return None

    try:
        if not ips_list:
            return None

        public_ip = _get_public_ip()

        if not public_ip:
            return None

        response = requests.get(
            url=f"{location_url}/{public_ip}?fields={fields_number}"
        )
        response.raise_for_status()
        response = response.json()
        location_info: Location = Location(**response)
        return location_info
    except Exception as e:
        logfire.error(
            f"""
			Could Not Obtain Location Info.
			Error: {e}
   			"""
        )
        return None
