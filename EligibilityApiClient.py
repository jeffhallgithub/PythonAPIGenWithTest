from gen_eligibility_api.eligibility_verification_api_client import Client
from gen_eligibility_api.eligibility_verification_api_client.models import VerifyEligibilityBody
from gen_eligibility_api.eligibility_verification_api_client.models import VerifyEligibilityResponse200
from gen_eligibility_api.eligibility_verification_api_client.types import Response
from gen_eligibility_api.eligibility_verification_api_client.api.default import verify_eligibility

class EligibilityApiClient:

    client = None

    def __init__(self, url='http://localhost:4010') -> None:
        self.client = Client(base_url=url)

    def isEligible(self, carrier_name, member_id, full_name, date_of_birth) -> tuple[bool, str]:
        request_body=VerifyEligibilityBody(carrier_name=carrier_name, member_id=member_id, full_name=full_name, dob=date_of_birth)
        response = verify_eligibility.sync_detailed(client=self.client, body=request_body)
        if response.status_code == 200:
            return response.parsed.eligible, response.parsed.message
        elif response.status_code == 400:
            return False, "Invalid Request"
        elif response.status_code == 500:
            return False, "Server error"
        else:
            return False, "Unexpected Status Code: " + response.status_code