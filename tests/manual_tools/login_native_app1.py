#!/usr/bin/env python

from globus_sdk import NativeAppAuthClient

import os
os.environ["GLOBUS_SDK_ENVIRONMENT"] = "sandbox"

CLIENT_ID = "fbe957d3-fc65-4d8c-a8b1-78d1cafef075"
SCOPES = ("openid profile email "
          "urn:globus:auth:scope:transfer.api.globus.org:all")

get_input = getattr(__builtins__, 'raw_input', input)


client = NativeAppAuthClient(client_id=CLIENT_ID)
client.oauth2_start_flow(requested_scopes=SCOPES,
                         refresh_tokens=True)
url = client.oauth2_get_authorize_url()

print("Native App Authorization URL: \n{}".format(url))
auth_code = get_input("Enter the auth code: ").strip()

token_res = client.oauth2_exchange_code_for_tokens(auth_code)
tokens = token_res.by_resource_server

transfer_token = tokens["transfer.api.globus.org"]["refresh_token"]
auth_token = tokens["auth.globus.org"]["refresh_token"]
id_token = token_res["id_token"]
access_token = token_res["access_token"]

print("Transfer Refresh Token: {}".format(transfer_token))
print("Auth Refresh Token    : {}".format(auth_token))
print("Openid id_token       : {}".format(id_token))
print("Access Token          : {}".format(access_token))
