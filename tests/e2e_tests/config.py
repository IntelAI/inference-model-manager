import os

TENANT_NAME = os.environ.get('E2E_TENANT_NAME', 'test')
MODEL_NAME = os.environ.get('E2E_MODEL_NAME', 'e2emodel')

RESNET_BUCKET = os.environ.get('E2E_RESNET_BUCKET', 'bucket-model')
RESNET_KEY = os.environ.get('E2E_RESNET_KEY', 'resnet/0/saved_model.pb')
DEST_KEY = os.environ.get('E2E_DEST_KEY', MODEL_NAME + '-1/0/saved_model.pb')

CERT_BAD_CLIENT = "../helm-deployment/certs/bad-client.crt"
CERT_BAD_CLIENT_KEY = "../helm-deployment/certs/bad-client.key"
CERT_CLIENT = "../helm-deployment/certs/client.crt"
CERT_CLIENT_KEY = "../helm-deployment/certs/client.key"
CERT_SERVER = "../helm-deployment/certs/server.crt"
CERT_SERVER_KEY = "..helm-deployment/certs/server.key"

CERT = os.environ.get('CERT',
                      'LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUZCVENDQXUyZ0F3SUJBZ0lKQUtiOE8wcUR1SlV2TUEwR0NTcUdTSWIzRFFFQkN3VUFNQmt4RnpBVkJnTlYKQkFNTURuTjFjR1Z5TFdocGNHVnlMV05oTUI0WERURTRNRGN6TURBNU16RXhNVm9YRFRFNU1EY3pNREE1TXpFeApNVm93R1RFWE1CVUdBMVVFQXd3T2MzVndaWEl0YUdsd1pYSXRZMkV3Z2dJaU1BMEdDU3FHU0liM0RRRUJBUVVBCkE0SUNEd0F3Z2dJS0FvSUNBUUM4MTdRakJJblkzdkNnRlNDY3lDb1dSYzcwTFJxY29DNHBYS0haeUI3T0lmRGIKc1Fia2FiT1pwMWp0endGQ3VVRGlKNlpRVmNVMUgzUHVnUUJCNjEvdGdCVk9DNmdLRFFibUVmcTYzQXdoeUoyTworcTliK3BTMVhKS2VXYm5iekREQnI3cnRWeVJpQ3NDV1ZUSThhOElyQmpDeWlHU1B6K2Z3STRUSlNkeGZnUnM2CmVZOXpRSFREWGdMUFdQa1Rmb1RIYnRVazlCMThGVEJPNGJHVWg2S3NCU2d3Rk83WU15UDVGOXFaZFBjQTYvMXEKTHo0WCtPcURZUm5XVS8rRUFodXJ3V2djc2thbzRoNUpORnVma3d3TDhzVmhUNHdGWHl6bkllNndkc1RVazFDLwo2T2pYN1oxMllCaW5MVitFdEYwcmJQTlVmdm1KOGN1Mml0c2N0TmV0cC8wUUFqYlN1L1F1Vml5L044UVV0MXVDCm1NVHNTVmdtWXBzZ3RhWi9ZcjR0UkZhOHpySXc1dFdNbFpMamdXUzNCT3VjQTYyemtjQjR0ekZiclFML2xYbnkKaEN3UVpWM3ZmTzVVRTRWTTd2eFhDQlMvVzV1dE4vUmFrR0d3cDgzTHJ3VDhBUEFhQjVIU1VBTXNKUXNqSXVXbQpGUCtSSUZRZlJocHFhRXZHK21rck85VXFkY09ndC83dmVSYk84OWlUVk1EZnlmeXZzclBBeEtramJZSmhuaUxiCm9SOVpid2pSWm9XVlhFZXY0cHpOZHcycWYxZkhybEJaWkZwNmV6eUF1TE1MU3UrTll4NnZvK2tGK0R1ZGRjM2QKa0hDTGMySjF6QUVrcE5RWEJPdldqMnhyaDk1TG5udWR6UGJWQ2pJR2hUNHMyRkJiQUd6ZGxhUHhYWDJrbVFJRApBUUFCbzFBd1RqQWRCZ05WSFE0RUZnUVVSSmNrSjdnOGNnVTVlOXZYR1oyb2ZxMElKblV3SHdZRFZSMGpCQmd3CkZvQVVSSmNrSjdnOGNnVTVlOXZYR1oyb2ZxMElKblV3REFZRFZSMFRCQVV3QXdFQi96QU5CZ2txaGtpRzl3MEIKQVFzRkFBT0NBZ0VBZ0ZwOE4yWENvWmRpWWJZQ3F1b05meXl4SFVpRkVLVURzcStaaWpDU0NEQi9pdWllNjYxTQp4NmpmUGpHRTJqRm5TWlNTenpFRVkyQXVEYUxtMEFsUGhRcXRoVWIrVktOc2JLVFdhalFaRHkzMStoM1dmSlQvCjBsbjBMVjlraFBqT3V5L3hxQy9wTWFrRjJSZDhwdXAyY3V5azZpSmxuZDVidnU1SmVpbXVoWVJnbkpsOE9yWHIKcjlOUUpubWlMWG5mckplVkFYclFLKzVyMHYvQlNhcjh0SUlMU09Pa25FbVdqcU9Yb2E1Vk1jdG05ZlgvcmtITQo5c2xFTnJNNEdUTERSSkFwY29seDdhclM2cWFDQ21TM2JVN1B0Uldua2JSeFJsV0VVSi9PLzNHcGNoc3pvWWF4CmQzZHFNU2RRNnRHMlhXeHQzUk5uQU1zSFdXcWZyazVKZVc5UCsweDUyVUdTa2tYQ2c5QVJUais0VEY5WElsZk4KL2FId1RUeld6VDFYNHFCbm1WeGpiMjI2bDBkaHd5UmxqMXVEQjN4MFZIQzF0T25SYzJHeFEybWY5VDRCT1g0YgorVTdpdnBEYmsvcXpNNkEvZ0oreFFRQVFPYWZkNmI0RmptbDZzUWpWQXp2NGQ2Q04rNk9hVjJQRU9NZnVJdmdYCjBxN1VnVklsNk9SNnhnTXYrUUowRzBRTkVBdmVwOGR5dlpnKzVrZ3NUWkEyeU1BZWJJL2hNWm1OU1R4Rmw4ZEgKSHVqTXZvT0tDM3lrTmJlT2NPZi8zMzhzeUJ1Zm9wR1ZUZWtHY1Y0b1lVVFJ3ZU0zc01IRzBqeVlGOUc3K1ZJSgp1UlhPWVFNTzdQQy9oRmZTR2pJZW9aeHhSOTdETmJ2bWtFbEMzdFRYWm9JVHpkVnk5VU9PRHBVPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCi0tLS0tQkVHSU4gWDUwOSBDUkwtLS0tLQpNSUlDY1RCYkFnRUJNQTBHQ1NxR1NJYjNEUUVCQlFVQU1Ca3hGekFWQmdOVkJBTU1Ebk4xY0dWeUxXaHBjR1Z5CkxXTmhGdzB4T0RBNE1qSXhNVFExTkRaYUZ3MHlNREE0TWpFeE1UUTFORFphb0E0d0REQUtCZ05WSFJRRUF3SUIKQVRBTkJna3Foa2lHOXcwQkFRVUZBQU9DQWdFQU5JY3hzdVRmcXB3aTR2cFo3N0h3alhnWlhxMXdhaXcyYkJOTgpNOFhzcENndThpcWxnQ0NVQW1lRlRSVk5ZM2VsZG0vcHZvYnZWVWpaYThXc2hBSUhtS1hWT1l4aDBmdmJaWlIvCjFqMlFFMllFOFZMRXE4THhnTlRwMEtudWxIOUplYnJPVWZyN3RVNTNKU2R2ZlJ5VTdHZ0U4Y2dRZzRYVEUyK0oKOXFncDJ1ODdZTTFsQnYrR0VGU3BKNFNBWk1ma1VIcGF1cmZDdHRPRXdzczg1ZW1TTmNuTUd5MFZjUGpJWXZJQQp6WGI2cHBxdXQ0RzFiNTdERTQyZGMzR2R1djNTWWt2T1g1YkVuMW9IT2FyRlZJQkptTTZHQU1sREpWbGVXanVQCjNzbGsya0cwcFZNdG1jOTJ6YnMyTVZrOHlnRCtPMXpQcm91d0VZdFNCaFZrZExnZDVodTdnSzFaaytLeWdrM0sKVHN1bngvOUR2NUE3YUtFSUJ2OTgrWmdsdFlicDg2UlJ2aHROWEw2YUhodDdlR2pjUlF0WXJCd3pPa21kYnFPeAorb3c0YkhwZ2dveVhRc1I4MG1YcW1UYXV1QnNUTHV6SXAwZUgvTjBkN01qRGNKb0pQU0U3a09OV0RFdVBzbWlICjVFdzF0Z1Ntd1NOc3FselArVGxWVFlTRzhsUzQrZ2QwRmQ2OXRIc1pnTzAweTFhcXdYM3htaWplSHR6ak05aWsKYXBRK2txRzVSdmF3ZnNlV2VkaXNXZEU3Skh4T2czNjdFSnZVSHNxZDJRbTVQQlN1NHJUWEJkS01oK2RWL09pcAo4VjlqeHZXc1NOckx2NEQ1SHlnSWU5QXlETkUrbytwOVA0bi9lbXowMHBBeVk4QWpMVnFBRUF6TWExVjRJRHRvCk5GMDQzUWc9Ci0tLS0tRU5EIFg1MDkgQ1JMLS0tLS0K')  # noqa