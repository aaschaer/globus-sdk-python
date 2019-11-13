#!/usr/bin/env python
from __future__ import unicode_literals
import globus_sdk

import os
os.environ["GLOBUS_SDK_ENVIRONMENT"] = "sandbox"


# removes all endpoints, bookmarks, and files/folders on tutorial enpdoints
# intended to be used to clean the testing areas for the SDK Tester user
def clean():

    # constants
    SDK_USER_ID = "123fac83-88e6-4ca6-8d43-afff40786fb1"
    GO_EP1_ID = "25fbda1e-5ae6-11e5-b577-22000b47140e"
    GO_EP2_ID = "25fbda23-5ae6-11e5-b577-22000b47140e"
    GO_EP3_ID = "b88da93e-4186-11e7-8e40-22000b508383"
    CLIENT_ID = "fbe957d3-fc65-4d8c-a8b1-78d1cafef075"
    SCOPES = 'urn:globus:auth:scope:transfer.api.globus.org:all'
    get_input = getattr(__builtins__, 'raw_input', input)

    # create an authorized transfer client
    client = globus_sdk.NativeAppAuthClient(client_id=CLIENT_ID)
    client.oauth2_start_flow(requested_scopes=SCOPES)
    url = client.oauth2_get_authorize_url()

    print("Login with SDK Tester: \n{}".format(url))
    auth_code = get_input("Enter auth code: ").strip()

    # get tokens and make a transfer client
    tokens = client.oauth2_exchange_code_for_tokens(
        auth_code).by_resource_server
    globus_transfer_data = tokens['transfer.api.globus.org']
    transfer_rt = globus_transfer_data['refresh_token']
    transfer_at = globus_transfer_data['access_token']
    expires_at_s = globus_transfer_data['expires_at_seconds']

    authorizer = globus_sdk.RefreshTokenAuthorizer(
        transfer_rt, client, access_token=transfer_at, expires_at=expires_at_s)
    tc = globus_sdk.TransferClient(authorizer=authorizer)

    # prevent accidental cleaning of a personal account
    auth_client = globus_sdk.AuthClient(authorizer=authorizer)
    res = auth_client.get('/p/whoami')
    if res['identities'][0]["id"] != SDK_USER_ID:  # assume the primary ID
        print("The primary ID {} was not the SDK Tester, stopping clean".format(res['identities'][0]["id"]))
        return

    # now clean test assets

    # clean SDK Tester's home /~/ on go#ep1 go#ep2 and go#ep3
    ep_ids = [GO_EP1_ID, GO_EP2_ID, GO_EP3_ID]
    task_ids = []
    file_deletions = 0
    for ep_id in ep_ids:
        kwargs = {"notify_on_succeeded": False}  # prevent email spam
        ddata = globus_sdk.DeleteData(tc, ep_id, recursive=True,
                                      **kwargs)
        r = tc.operation_ls(ep_id)
        for item in r:
            ddata.add_item("/~/" + item["name"])
            print("deleting {}: {}".format(item["type"], item["name"]))
            file_deletions += 1
        if len(ddata["DATA"]):
            r = tc.submit_delete(ddata)
            task_ids.append(r["task_id"])

    # clean SDK Tester's bookmarks
    bookmark_deletions = 0
    r = tc.bookmark_list()
    for bookmark in r:
        tc.delete_bookmark(bookmark["id"])
        print("deleting bookmark: {}".format(bookmark["name"]))
        bookmark_deletions += 1

    # clean endpoints owned by SDK Tester
    endpoint_deletions = 0
    cleaning = True
    while(cleaning):
        cleaning = False
        r = tc.endpoint_search(filter_scope="my-endpoints", num_results=None)
        for ep in r:
            tc.delete_endpoint(ep["id"])
            print("deleting endpoint: {}".format(ep["display_name"]))
            endpoint_deletions += 1
            cleaning = True

    # wait for deletes to complete
    for task_id in task_ids:
        tc.task_wait(task_id, polling_interval=1)

    print("{} files or folders cleaned".format(file_deletions))
    print("{} endpoints cleaned".format(endpoint_deletions))
    print("{} bookmarks cleaned".format(bookmark_deletions))


if __name__ == "__main__":
    clean()
