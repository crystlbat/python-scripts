from datetime import datetime

import requests

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpY0JVSWQiOjQ1OTMyOTksIm5hbWUiOiJwcmF0aGFtZXNoLnNhcm9kZUB1bmlwaG9yZS5jb20iLCJpc3MiOiJodHRwczovL2FwaS5pbmNvbnRhY3QuY29tIiwic3ViIjoidXNlcjozMDI5NDA2NCIsImF1ZCI6IlVuaXBob3JlQFVuaXBob3JlIiwiZXhwIjoxNjU0MTU1OTQ1LCJpYXQiOjE2NTQxNTIzNDYsImljU2NvcGUiOiI4IiwiaWNDbHVzdGVySWQiOiJDNiIsImljQWdlbnRJZCI6MzAyOTQwNjQsImljU1BJZCI6MjE0NSwiZ2l2ZW5fbmFtZSI6IlByYXRoYW1lc2giLCJmYW1pbHlfbmFtZSI6IlNhcm9kZSIsInRlbmFudElkIjoiMTFlOWVmZDEtNGQ3Ny1mNjE3LTgwZWEtMDA1MDU2YTEwYzlkIiwibmJmIjoxNjU0MTUyMzQ1fQ.Q5pmHpVmrnkpe5H0UzQuo-HEMw3_cUeaIY7_zyl7c_rXG-CL1lifgtvM-Y7CJjroVCx4MpWXQYiVwXiD2D1PdSnMZHIfBeshDlI-CwrTckwFuqhnb_CbltuCGeWchvb6LXNxhCdH9eCPdA6C3kZWOqWp-_KuQeNt36jPOLb6eXta24I732QL_9Xx4PQYXjL6CemdMetGsyHtXX2US-ebP5iJaTyQGp36N1XC2CRbERIvHbrNoAzOiZPJEhUhEU0s00sJn_4LXyo8hhNFaWhgS8BLAMIc8NpBNGx4_gBob4t6IM_uStrCiS9Fr3kl_B1Ab8o6lggHAAo3MLF_h0KrlA',
    'accept': 'application/json',
}

params = {
    'startDate': '2022-05-31T12:06:20.760Z',
    'endDate': '2022-05-31T13:59:20.760Z',
    'isLogged': 'true',
}

response = requests.get('https://api-c6.incontact.com/inContactAPI/services/v24.0/contacts/completed', params=params, headers=headers)