For Day 91 of the 100 Days of code course the goal was to create a program that processes a PDF file and converts that file's text into an audio file using an API.

This proejct required a bit more research in finding a viable API option to use. I was a bit hesitant to use AWS at first because I did not want to risk having to pay for any uploads and came across a free API, voicerss.org. I initially worked with this API and was able to successfuly convert text to speach however, when working with larger text files, the program would run into an error. I did this with multiple text files and kept running into that same error with larger files. 

Technically, this fulfilled the requirement for the project however, it felt a bit incomplete knowing that the program would not work with anything longer than a page.

I then decided to give AWS Polly a try and was successful in processing multi-page documents and creating audio files out of them. With AWS, those audio files were also saved to a specified S3 bucket which was an added bonus. With Voicerss, the files were not saved anywhere and the URL they were accessed with, was the voicerss endpoint concatinated with the text that was processed.

The AWS Polly version of this project was implemented using Boto3 following AWS's documentation for Polly. The Polly TTS program was tested with single and multipage documents and worked successfully. Those documents were uploaded to the specified S3 bucket with "tts-" properly appended to the audio file name.
