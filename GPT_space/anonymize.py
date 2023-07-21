## This module loads the resume.json from the repo root dir and replaces
## Any Personal Names, Emails, Phone Numbers, Addresses, and Websites with "*redacted*"
## The resulting file is saved to the dir GPT_space/ as resume_anon.json

import json
import re
import os

# Load the resume.json file at the root of the repo
with open("resume.json", "r") as f:
    resume = json.load(f)


# Define the regex patterns to match
name_pattern = re.compile(r"([A-Z][a-z]+)(\s[A-Z][a-z]+)?(\s[A-Z][a-z]+)?")
email_pattern = re.compile(r"[\w\.-]+@[\w\.-]+")
phone_pattern = re.compile(r"\d{3}[-\.\s]\d{3}[-\.\s]\d{4}")
address_pattern = re.compile(r"\d{1,5}\s\w+\s\w+\s\w+")
website_pattern = re.compile(r"www\.\w+\.\w+")

# Define the replacement string
replacement = "|REDACTED|"


# Define the function to anonymize the resume
def anonymize(resume):
    # Anonymize the name
    resume["basics"]["name"] = replacement
    # Anonymize the email
    resume["basics"]["email"] = replacement
    # Anonymize the phone
    resume["basics"]["phone"] = replacement
    # Anonymize the address
    resume["basics"]["location"]["address"] = re.sub(
        address_pattern, replacement, resume["basics"]["location"]["address"]
    )
    # Anonymize the url
    resume["basics"]["url"] = re.sub(
        website_pattern, replacement, resume["basics"]["url"]
    )
    # Redact the username and website from the profiles
    for profile in resume["basics"]["profiles"]:
        profile["username"] = replacement
        profile["url"] = replacement
    # Anonymize the work experience
    for work in resume["work"]:
        work["company"] = replacement


# Call the anonymize function
anonymize(resume)

# Save the anonymized resume to the GPT_space dir
with open("GPT_space/resume_anon.json", "w") as f:
    json.dump(resume, f, indent=4)

# Print the path to the anonymized resume
print(f"REDACTED resume saved to {os.path.abspath('resume_anon.json')}")
