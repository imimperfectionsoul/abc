{
  "github_url": "https://gist.github.com/imimperfectionsoul/5386a0c9b832350b885a512867eff6bc",
  "contact_email": "ashwanikr.raja@gmail.com",
  "solution_language": "python"
}
//
import requests
import json
import hmac
import hashlib
import time

# Set up the request headers and body
url = "https://api.challenge.hennge.com/challenges/003"
content_type = "application/json"
userid = "ashwanikr.raja@gmail.com"
shared_secret = userid + "HENNGECHALLENGE003"
payload = {"github_url": "https://gist.github.com/imimperfectionsoul/5386a0c9b832350b885a512867eff6bc"}

# Generate the TOTP password using HMAC-SHA-512
totp_time = int(time.time() // 30)
totp_secret = shared_secret.encode()
totp_counter = totp_time.to_bytes(8, byteorder="big")
hmac_obj = hmac.new(totp_secret, totp_counter, hashlib.sha512)
totp_password = hmac_obj.hexdigest()[-10:]

# Set up the HTTP Basic Authentication header
auth_header = userid + ":" + totp_password
auth_header_b64 = auth_header.encode("ascii").hex()

# Make the HTTP POST request
headers = {
    "Content-Type": content_type,
    "Authorization": "Basic " + auth_header_b64,
}
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check the response status code
if response.status_code == 200:
    print("POST request succeeded!")
else:
    print("POST request failed with status code:", response.status_code)


//

import requests
import json
import hmac
import hashlib
import time

# Define the userid and shared secret
userid = "your_email_address@example.com"
shared_secret = userid + "HENNGECHALLENGE003"

# Define the TOTP parameters
timestep = 30
t0 = 0
digits = 10
hash_func = hashlib.sha512

# Generate the TOTP password
counter = int(time.time() / timestep) - t0
counter_bytes = counter.to_bytes(8, byteorder="big")
secret_bytes = bytes(shared_secret, "utf-8")
hmac_digest = hmac.new(secret_bytes, counter_bytes, hash_func).digest()
offset = hmac_digest[-1] & 0xf
truncated_hash = hmac_digest[offset : offset + 4]
otp = int.from_bytes(truncated_hash, byteorder="big") & 0x7fffffff
totp_password = str(otp).zfill(digits)

# Define the JSON string
json_string = json.dumps({
    "github_url": "https://github.com/yourusername/yourrepository"
})

# Define the URL and headers
url = "https://api.challenge.hennge.com/challenges/003"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {userid}:{totp_password}"
}

# Make the HTTP POST request
response = requests.post(url, headers=headers, data=json_string)

# Check the response status code
if response.status_code == 200:
    print("Request succeeded!")
else:
    print(f"Request failed with status code {response.status_code}")

//
#In this example, you need to replace "your_email_address@example.com" with your actual email address, and "https://github.com/yourusername/yourrepository" with the URL of your GitHub repository.

#Note that the TOTP password is generated using the hmac and hashlib libraries in Python, based on the TOTP parameters specified in the challenge description. You may need to adjust these parameters if you are using a different programming language or TOTP library.
