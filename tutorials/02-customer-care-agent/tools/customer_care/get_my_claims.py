from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def get_my_claims() -> list[dict]:
    """Retrieves detailed information about submitted claims.

    The details include claim status, submission and processing dates, amounts claimed and approved,
    provider information, and services included in the claims.

    Returns:
        list[dict]: A list of dictionaries, each containing details about a specific claim:
            - claimId (str): Unique identifier for the claim.
            - submittedDate (str): Date when the claim was submitted.
            - claimStatus (str): Current status of the claim (e.g., 'Processed', 'Pending', 'Rejected').
            - processedDate (str or None): Date when the claim was processed (None if not processed yet).
            - amountClaimed (float): Total amount claimed.
            - amountApproved (float or None): Amount approved for reimbursement (None if pending, 0 if rejected).
            - rejectionReason (str, optional): Reason for rejection if applicable (only present if claimStatus is 'Rejected').
            - provider (str or dict): Provider details, either as a simple string or a dictionary with detailed provider information.
            - services (list[dict]): List of services included in the claim, each with:
                - serviceId (str): Identifier for the service.
                - description (str): Description of the service provided.
                - dateOfService (str): Date the service was provided.
                - amount (float): Amount charged for the service.
    """

    claims_data = [
        {
            "claimId": "CLM1234567",
            "claimStatus": "Processed",
            "amountClaimed": 150.00,
            "amountApproved": 120.00,
            "provider": {
                "name": "Healthcare Clinic ABC",
                "providerId": "PRV001234",
                "providerType": "Clinic"
            },
            "services": [
                {"serviceId": "SVC001", "description": "General Consultation", "dateOfService": "2025-02-28", "amount": 100.00},
                {"serviceId": "SVC002", "description": "Blood Test", "dateOfService": "2025-02-28", "amount": 50.00}
            ]
        },
        {
            "claimId": "CLM7654321",
            "claimStatus": "Pending",
            "amountClaimed": 300.00,
            "amountApproved": None,
            "provider": "City Health Hospital",
            "services": [
                {"serviceId": "SVC003", "description": "X-ray Imaging", "dateOfService": "2025-02-14", "amount": 300.00}
            ]
        },
        {
            "claimId": "CLM9876543",
            "claimStatus": "Rejected",
            "amountClaimed": 200.00,
            "amountApproved": 0.00,
            "rejectionReason": "Service not covered by policy",
            "provider": "Downtown Diagnostics",
            "services": [
                {"serviceId": "SVC003", "description": "MRI Scan", "dateOfService": "2025-02-05", "amount": 200.00}
            ]
        }
    ]

    return claims_data