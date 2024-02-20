import PyPDF2, requests, os

VOICERSS_URL = "http://api.voicerss.org/"
VOICERSS_API_KEY = os.environ.get("VOICERSS_API_KEY")

print("Opening PDF...\n")
### EXTRACT PDF TEXT ###
file = open("multipage_latin.pdf", mode="rb")

pdf_reader = PyPDF2.PdfReader(file)

number_of_pages = (len(pdf_reader.pages))
doc_text = ""

for page in range(number_of_pages):
    # Loop through pages
    page = pdf_reader.pages[page]
    # Saves selected page content to text
    doc_text += page.extract_text()

file.close()
print(f"PDF text saved to variable.\n\nProceeding to converting to speach using voicerss.org\n")

### CONVERT TEXT TO SPEACH ###
# Run into a HTTPError on line 1021 with multipage text documents. On shorter text uploads, upload succeeds.
# URL is composed of the entire text document returning a long URL.
parameters = {
    "key" : VOICERSS_API_KEY,
    "src" : doc_text,
    "hl" : "en-us",
    "v" : "Mike",
}

response = requests.get(url=VOICERSS_URL, params=parameters)
response.raise_for_status()
print("UPLOAD SUCCESSFUL\n")
print(f"To hear and download converted audio navigate to the following link:\n{response.url}")
