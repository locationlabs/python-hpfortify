# Python client for HPfortify v3 api.
This client exposes different methods which can be hooked up to your application to directly interact with the HPfortify. This can also be used to automated to process to initiate a scan.

## Steps
There are basically three steps to use the APIs.

1. Initiate the AuthApi and call authorize() method. 

  ```
  auth_api = AuthApi(api_key=api_key,
                     api_secret=api_secret)
  auth_response = auth_api.authorize()                   
  ```
  
2. Get the access token from the response and use it to initialize other API.

  ```
  tenant_api = TenantApi(access_token=auth_response.access_token)
  entitlements = tenant_api.get_tenant_entitlements()
  print entitlements
  ```
  
3. Once you are done then expire the access token for clean way of shutting it down.

  ```
  auth_api.expire_access_token()
  ```
  
### Hello world!
Here is a simple script which uses the exposed method. You can use it as a reference.
  ```
  from json import dumps
  from hpfortify.api.application import ApplicationApi
  from hpfortify.api.tenants import TenantApi
  API_KEY = "<API_KEY>"
  API_SECRET = "<API_SECRET>"
  def main():
      # Initialize the Auth api for authentication.
      auth_api = AuthApi(api_key=API_KEY,
                         api_secret=API_SECRET)
                       
      # Aurhoize and get the access token
      auth_response = auth_api.authorize()
    
      # Use the access token to initialize other API. 
      # Similar construct can be used of different Api.
      tenant_api = TenantApi(access_token=auth_response.access_token)
    
      # Query for entitlements
      entitlements = tenant_api.get_tenant_entitlements()
    
      # Print the response
      print_response(entitlements)
    
      # Once you are done expire the access token a clean way to terminate the session.
      auth_api.expire_access_token()
   
   
  def print_response(response, message=None):
      """
      This method prints the response model object in pretty format.
      """
      if message:
          print message

      print dumps(response.to_dict(), indent=3, sort_keys=True)
      
      
  if __name__ == "__main__":
    main()
  ```
  
## Command Line Tool
This library also comes with a command line tool for initiating the static code analysis. You can automate the process of initating the code scan by hooking up with the build system. So your build system can run this command to initiate the code scan. Here is an example command:
  ```
  start-static-scan --api-key "<API_KEY>" --api-secret "<API_SECRET> --app-name "<APP_NAME>" --release-name "<RELEASE_NAME>" --sdlc-status QA --technology-stack ANDROID --entitlement-id <ENTITLEMENT_ID> --entitlement-frequency-type SUBSCRIPTION --file-path <FULLY_QUALIFIED_FILE_PATH>
  
  # Example
  start-static-scan --api-key "abadeet-7a3d-465c-ad18-e9a02484ae00" --api-secret '889daab34abdead' --app-name 'Android test app' --release-name '1.0' --sdlc-status QA --technology-stack ANDROID --entitlement-id 12345 --entitlement-frequency-type SUBSCRIPTION --file-path /Users/wavemarket/locationlabs/afm-10.0.1-v2-src.zip
  ```
  
## Install
This project is not yet published to the Pypi, but it will be available soon. You can install the ap by cloning the project and running the following command in the root directory of the project.
  ```
  pip install -U -e .
  ``` 
  
## Contributing
We welcome your constructive code contribution. Please go through our [contribution](CONTRIBUTE.md) guideline before your start actively developing.
