import os


# TF serving tests
TFSERVING_HOST_NAME = os.environ.get('HOST_NAME', "serving-service.kube.cluster")
TFSERVING_HOST_PORT = os.environ.get('HOST_PORT', 443)

# Management API tests
DEFAULT_HEADERS = {
    'accept': 'application/json',
    'Authorization': 'gg',
    'Content-Type': 'application/json',
}

MANAGEMENT_API_URL = os.environ.get('MANAGEMENT_API_URL', 'http://localhost:5000/tenants')

TENANT_NAME = os.environ.get('TENANT_NAME', 'test')

WRONG_TENANT_NAMES = [
    ('_', """{"title": "Tenant name _ is not valid: must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character (e.g. 'my-name', or '123-abc')"}"""), 
    ('ten_name', """{"title": "Tenant name ten_name is not valid: must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character (e.g. 'my-name', or '123-abc')"}"""),
    ('a', """{"title": "Tenant name a is not valid: too short. Provide a tenant name which is at least 3 character long"}"""),
    ('veryveryveryveryveryveryveryveryveryveryveryveryverylongtenantname', """{"title": "Tenant name veryveryveryveryveryveryveryveryveryveryveryveryverylongtenantname is not valid: too long. Provide a tenant name which is max 63 character long"}""")
]

CERT = os.environ.get('CERT', 'LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURJVENDQWdtZ0F3SUJBZ0lKQUw1ZGxQc3pYTFlMTUEwR0NTcUdTSWIzRFFFQkN3VUFNQ2N4SlRBakJnTlYKQkFNTUhITmxjblpwYm1jdGMyVnlkbWxqWlM1cmRXSmxMbU5zZFhOMFpYSXdIaGNOTVRnd05qSTJNRGN5TmpJNQpXaGNOTVRrd05qSTJNRGN5TmpJNVdqQW5NU1V3SXdZRFZRUUREQnh6WlhKMmFXNW5MWE5sY25acFkyVXVhM1ZpClpTNWpiSFZ6ZEdWeU1JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBTUlJQkNnS0NBUUVBNzl0ZE1QS3kKZmpDVkdFbHNMNXRMcDVUeUR0aDhrSFczcUlTU3ZHRVAvVHVzSk9tM1hxbkhoQ1c2aFpSN2tNcWRyd1ZSZUNzVQp6OTVDSnVod0p0TFpSMGVxTVBKbW5EbnhEVmMxb0VVUzE2UTNhOWpqOTBIWTIzZ2h2cXFrcXlYN3cvZzliZnF5CmxuaE16OElYT1JiM0hKVTVWR3V2Q2xMR3ZxNjBOTUxBT3NRZUg3YS9lOU5qdVVWSXdJQTcyenZrQnI0OHcrUWYKMHVGMGVCYUNtOUpobEZLb3d5b3hsN2lWN0FKeHBuS0EyL3M4aHlrMEVoYVhJVE1sUjFmblpnTWF6UEIrV1AvTwpZamJzdmdMNmpNUzR2eTVBbXFXSXJyNkdna2tRdzhOektiRDRSV1U3MWFzenBPQlFVTjlDaE5aVTlzdDkzVjhTCnc4VkFkYWN5WDZXQ2J3SURBUUFCbzFBd1RqQWRCZ05WSFE0RUZnUVVJblc2QWJvbVdmYW05QVROUW1Kc3hVY1YKRnlzd0h3WURWUjBqQkJnd0ZvQVVJblc2QWJvbVdmYW05QVROUW1Kc3hVY1ZGeXN3REFZRFZSMFRCQVV3QXdFQgovekFOQmdrcWhraUc5dzBCQVFzRkFBT0NBUUVBRjNLSWVrZzl3bndibzhNalhab3Z5ZnIzTXZGT0NiSnIrWkRiCldyajVMSVlSemJkN05BNHZRQkxXeXN1SFVzTVF6UGZUVWJzU3JSTFNEQzdKMGE4c0FaUHYwU1RCL2hpQzRuRDYKVVloWU9uVE95eDFNeUVzQUNUWDJGbWNyQk9wdXliVFlhekdoRXh3QXlEVjFqSmZnanZlMjh0L1RNbVhOeFdJbgpLc0g4S09icTVoTit2bXdnajljakdWbGxSdUdaZFIrZVdoK0ppbEh3dGxaME1URG1jcUd6WDZPclhQZmZnNHJjCkFXN0FtVlpBVnQzSEF4N1FkZ2xxMkZJMGVCa0FFSEVHb0hvM0xsOGU0Z01rUUIyMDhaZmFvdFFSb2xHYkRLb3EKeENMd3NBd3hXVnlhMHl0aElKMUhhRFJmOWRDSUxOcVZCM29TNThiSEFWMEZGV2o5aVE9PQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==')

SCOPE_NAME = os.environ.get('SCOPE_NAME', 'scope_name')

QUOTA = {
    'requests.cpu': '1',
    'requests.memory': '1Gi',
    'limits.cpu': '1',
    'limits.memory': '1Gi',
    'maxEndpoints': '1',
}

WRONG_BODIES = [
    ({'cert': CERT, 'scope': SCOPE_NAME, 'quota': QUOTA}, """{"title": "'name' parameter required"}"""),
    ({'name': TENANT_NAME, 'cert': CERT, 'quota': QUOTA}, """{"title": "'scope' parameter required"}"""),
    ({'name': TENANT_NAME, 'scope': SCOPE_NAME, 'quota': QUOTA}, """{"title": "'cert' parameter required"}"""),
    ({'name': TENANT_NAME, 'cert': CERT, 'scope': SCOPE_NAME}, """{"title": "'quota' parameter required"}"""),
]


QUOTA_WRONG_VALUES = [
    ({'requests.cpu': '-1', 
      'requests.memory': '1Gi', 
      'limits.cpu': '1', 
      'limits.memory': '1Gi', 
      'maxEndpoints': '1'}, 
       """{"title": "Invalid value -1 of requests.cpu field: must be integer greater than or equal to 0"}"""),

    ({'requests.cpu': '1-', 
      'requests.memory': '1Gi', 
      'limits.cpu': '1', 
      'limits.memory': '1Gi', 
      'maxEndpoints': '1'},
       """{"title": "Invalid value 1- of requests.cpu field: must be integer greater than or equal to 0"}"""),
 
    ({'requests.cpu': 'a', 
      'requests.memory': '1Gi', 
      'limits.cpu': '1', 
      'limits.memory': '1Gi', 
      'maxEndpoints': '1'},
       """{"title": "Invalid value a of requests.cpu field: must be integer greater than or equal to 0"}"""),

    ({'requests.cpu': '1a', 
      'requests.memory': '1Gi', 
      'limits.cpu': '1', 
      'limits.memory': '1Gi', 
      'maxEndpoints': '1'},
       """{"title": "Invalid value 1a of requests.cpu field: must be integer greater than or equal to 0"}"""),

    ({'requests.cpu': '1', 
      'requests.memory': '1Gi', 
      'limits.cpu': '-1', 
      'limits.memory': '1Gi', 
      'maxEndpoints': '1'},
       """{"title": "Invalid value -1 of limits.cpu field: must be integer greater than or equal to 0"}"""),

    ({'requests.cpu': '1', 
      'requests.memory': '1Gi',
      'limits.cpu': '1a', 
      'limits.memory': '1Gi', 
      'maxEndpoints': '1'},
       """{"title": "Invalid value 1a of limits.cpu field: must be integer greater than or equal to 0"}"""),

    ({'requests.cpu': '1', 
      'requests.memory': '1Gi', 
      'limits.cpu': '1', 
      'limits.memory': '1Gi', 
      'maxEndpoints': '-1'},
       """{"title": "Invalid value -1 of maxEndpoints field: must be integer greater than or equal to 0"}"""),

    ({'requests.cpu': '1', 
      'requests.memory': '1Gi', 
      'limits.cpu': '1', 
      'limits.memory': '1Gi', 
      'maxEndpoints': 'a'}, 
       """{"title": "Invalid value a of maxEndpoints field: must be integer greater than or equal to 0"}"""),

    ({'requests.cpu': '1', 
      'requests.memory': '-1Gi', 
      'limits.cpu': '1', 
      'limits.memory': '1Gi', 
      'maxEndpoints': '1'},
       """{"title": "Invalid value -1Gi of requests.memory field. Please provide value that matches Kubernetes convention. Some example values: '1Gi', '200Mi', '300m'"}"""),

    ({'requests.cpu': '1', 
      'requests.memory': '1Gi-', 
      'limits.cpu': '1', 
      'limits.memory': '1Gi', 
      'maxEndpoints': '1'},
       """{"title": "Invalid value 1Gi- of requests.memory field. Please provide value that matches Kubernetes convention. Some example values: '1Gi', '200Mi', '300m'"}"""),

    ({'requests.cpu': '1', 
      'requests.memory': '1Ga', 
      'limits.cpu': '1', 
      'limits.memory': '1Gi', 
      'maxEndpoints': '1'},
       """{"title": "Invalid value 1Ga of requests.memory field. Please provide value that matches Kubernetes convention. Some example values: '1Gi', '200Mi', '300m'"}"""),

    ({'requests.cpu': '1', 
      'requests.memory': 'a1', 
      'limits.cpu': '1', 
      'limits.memory': '1Gi', 
      'maxEndpoints': '1'},
       """{"title": "Invalid value a1 of requests.memory field. Please provide value that matches Kubernetes convention. Some example values: '1Gi', '200Mi', '300m'"}"""),

    ({'requests.cpu': '1', 
      'requests.memory': '1Gi', 
      'limits.cpu': '1', 
      'limits.memory': '1-Gi', 
      'maxEndpoints': '1'},
       """{"title": "Invalid value 1-Gi of limits.memory field. Please provide value that matches Kubernetes convention. Some example values: '1Gi', '200Mi', '300m'"}"""),
]