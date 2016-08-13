The below steps are for v1 api. Current version is v3.


# Steps for Uploading Source code for scan.
1. Auth call first to get the access_token
  /oauth/token
    Request:
    {
    "scope": "https://hpfod.com/tenant",
    "grant_type": "client_credentials",
    "client_id" : "<API_KEY>",
    "client_secret": "<API_SECRET>"
    }

    Response:
    get the "access_token"

2.  Send request for scan and send the file in chunks (probably in a loop)
    /api/v1/release/{RELEASE_ID}/scan/?assessmentType=<ASSESMENT_TYPE>
    &technologyStack=<TECHNOLOGY_STACK>
    &languageLevel=<LANGUAGE_LEVEL>&fragNo=<FRAG_NO>&len=<LEN>&offset=<OFFSET>

    Request Header :
        "Authorization: Bearer <ACCESS_TOKEN_FROM_FIRST_STEP>"

    Response:
        Check the status code and make sure it is 2XX status code.
        If status code is 4XX that means the token has expired and we need to retrieve it again.
        For last chunk make sure server has sent "ACK" string in response.


3. Retire the token
    /oauth/retireToken

    Request Header:
         "Authorization: Bearer <ACCESS_TOKEN_FROM_FIRST_STEP>"

# Steps to get Scan status