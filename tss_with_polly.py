import PyPDF2, boto3, os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_KEY")
REGION = "us-east-1"
AWS_S3_BUCKET = os.environ.get("AWS_BUCKET")

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
print(f"PDF text saved to variable.\n\nProceeding to converting to speach using Amazon Polly and upload to '{AWS_S3_BUCKET}' S3 bucket.\n")

### CONVERT TEXT TO SPEACH ###
polly_client = boto3.Session(
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                region_name=REGION).client("polly")

response = polly_client.start_speech_synthesis_task(
    VoiceId = 'Joanna',
    OutputS3BucketName = AWS_S3_BUCKET,
    OutputS3KeyPrefix = 'tts-',
    OutputFormat = 'mp3', 
    Text = doc_text,Engine='standard')

taskId = response['SynthesisTask']['TaskId']

print("SUCCESS\n")

task_status = polly_client.get_speech_synthesis_task(TaskId = taskId)

print(task_status)