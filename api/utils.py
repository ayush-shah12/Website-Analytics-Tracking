"""utils"""
from api.models import User, Location
from mailjet_rest import Client
import os
import logfire
import requests

from dotenv import load_dotenv
load_dotenv()

api_key = os.environ['MAIL_API_KEY']
api_secret = os.environ['MAIL_SECRET_KEY']
email = os.environ["EMAIL_ADDR"]

location_url = os.environ["LOCATION_URL"]
fields_number = os.environ["FIELDS_NUMBER"]

def email_logged_visitor(user: User):
    """
    Email me the logged user information
    """
    try:
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')

        data = {
        'Messages': [
                        {
                                "From": {
                                        "Email": email,
                                        "Name": "Site Visitor Service"
                                },
                                "To": [
                                        {
                                                "Email": email,
                                                "Name": "Ayush Shah"
                                        }
                                ],
                                "Subject": "New Site Visitor!",
                                "TextPart": f"""Received a site visitor!\n{user.model_dump_json()}""",
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
            """)


def get_ip_info(ip: str | None = None) -> Location | None:
    """
    get location of request
    """
    try:
        
        if not ip:
            return None
        
        response = requests.get(url=f"{location_url}/ip?fields={fields_number}")
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
    