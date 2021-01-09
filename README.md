# disorganized notes

AWS console: https://us-east-2.console.aws.amazon.com/polly/home/SynthesizeSpeech

## workflow

- write speech text to `text.txt`
- run `.py` file --> output to `ssml.txt`
- copy the file under `ssml` folder 
- add YOMIGANA with `<sub alias="ほげ"></sub>` tag
- upload to AWS Polly
- download mp3 --> save under `audio` folder
- add subitles with Vrew