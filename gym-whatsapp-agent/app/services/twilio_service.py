class TwilioService:
    @staticmethod
    def send_message(to: str, body: str):
        # Stub: in production integrate with Twilio REST API
        print(f"[Twilio] Sending to {to}: {body}")
