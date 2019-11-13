GO_EP1_ID = "25fbda1e-5ae6-11e5-b577-22000b47140e"
GO_EP2_ID = "25fbda23-5ae6-11e5-b577-22000b47140e"
GO_EP3_ID = "b88da93e-4186-11e7-8e40-22000b508383"
GO_S3_ID = "cf9bcaa5-6d04-11e5-ba46-22000b92c6ec" # not on sandbox
GO_EP1_SERVER_ID = 207976

# ------ #
# tokens #
# ------ #
# sdktester1a@globusid.org transfer refresh token for Native App 1
SDKTESTER1A_NATIVE1_TRANSFER_RT = (
    "Ag40M0dwG41040wVjGvlOQKmbkYqXdq9KY2jVk5P03qBVaXkeMiYUy7n77KwzNalkXW5wdBlx"
    "9v2Q5Qvo3G7krJyEXwOw")
# sdktester1a@globusid.org auth refresh token for Native App 1
SDKTESTER1A_NATIVE1_AUTH_RT = (
    "Ag6GYye6KOvXrYK9JlrmvV70d3ojBO2M4xvr7xOvMEG1l0rPb5SPUP2lw8gr1wgY2vD8v4dj"
    "N9GK5DWv6nnKaY6ObKoMd")
# openid JWT gotten from Native App 1 login flow, expired
SDKTESTER1A_NATIVE1_ID_TOKEN = (
    "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJmYmU5NTdkMy1mYzY1LTRkOGMt"
    "YThiMS03OGQxY2FmZWYwNzUiLCJpZGVudGl0eV9wcm92aWRlcl9kaXNwbGF5X25hbWUiOiJHb"
    "G9idXMgSUQiLCJzdWIiOiIxMjNmYWM4My04OGU2LTRjYTYtOGQ0My1hZmZmNDA3ODZmYjEiLC"
    "Jpc3MiOiJodHRwczovL2F1dGguc2FuZGJveC5nbG9idXNjcy5pbmZvIiwicHJlZmVycmVkX3"
    "VzZXJuYW1lIjoic2RrdGVzdGVyMWFAZ2xvYnVzaWQub3JnIiwiYXRfaGFzaCI6ImdacW1MOC"
    "1vSkM4QjlvZ2ZZeUZWazlYZkdqZUVQYWZBclR1WkJsV2FhLVUiLCJpZGVudGl0eV9wcm92aW"
    "RlciI6IjQxMTQzNzQzLWYzYzgtNGQ2MC1iYmRiLWVlZWNhYmE4NWJkOSIsImV4cCI6MTU3Mz"
    "g0NTMwMSwiaWF0IjoxNTczNjcyNTAxLCJvcmdhbml6YXRpb24iOiJHbG9idXMiLCJlbWFpbCI"
    "6ImFhc2NoYWVyK3Nka3Rlc3RlckBnbG9idXMub3JnIiwibmFtZSI6IlNESyBUZXN0ZXIifQ.d"
    "IJMKs4SFfDxyk7-IPCvc_whDWlPP8Fobo6Yh5QPUa2jvLqmGxxfyqMC1MQy_kanrlE4GRj1x"
    "XJiaru4E4K-xUaaCpOc0BGp2QTcoHlmSAcI1NIrT0VQtrLH5w7PSMZrT8hAnu0KHARHlNJly"
    "VA6iSAPFSxBI2Svy5g6Bgu4IW9TnKYIx9o6QfwocKLns5ZOdAOo21S8PEPE85e3PIYVlndI"
    "RLpEgTs8K--JhLX3_TEheJZr5hvzB1PmFP0vqY7djP1Aj-jDen8ESlFEpgB-1s_SNhT3Btc"
    "OFd4oBiCSWK3xOELYXQkUbsEjbPbKXobzaSHVUdWw97Ppa_b9mQQUew")
# access token returned  along with id_token, expired
SDKTESTER1A_ID_ACCESS_TOKEN = (
    "Ag16K1bnqdX14g0egzzNOJYg6Wed74YYV7gJPzKJV7OK4mlEgDt2C53B6yg0bjrgNB93Mz48"
    "5G722gu4E6xgWSM7ofq3Vc01g")
# sdktester2b@globusid.org transfer refresh token for Native App 1
SDKTESTER2B_NATIVE1_TRANSFER_RT = (
    "AgM8D8Pw6nD6lE39kJJN7NDyqPWobBwX3PXmG4b0qqVY7zjaO6S6UBa3wjX1kn74Qp3XyyvDK"
    "qnQm6EoyBQlG6Dy5PBM")
# ---------- #
# end tokens #
# ---------- #


# TransferClient task_wait parameters
# 2 minutes
DEFAULT_TASK_WAIT_TIMEOUT = 120
# every 3 seconds
DEFAULT_TASK_WAIT_POLLING_INTERVAL = 3
