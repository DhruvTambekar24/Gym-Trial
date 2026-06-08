from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    project_name: str = "Gym WhatsApp Agent"
    twilio_account_sid: Optional[str] = None
    twilio_auth_token: Optional[str] = None
    twilio_from_number: Optional[str] = None

settings = Settings()
