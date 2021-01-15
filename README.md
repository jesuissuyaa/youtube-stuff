# disorganized notes

AWS console: https://us-east-2.console.aws.amazon.com/polly/home/SynthesizeSpeech

## ライター用仕様

- 「、」「。」では間があく（APIデフォルトの設定）
- 改行では0.2秒の間があく
- 『』の中のスペースは「、」に置換して読ませてる
    e.g. 『劇場版ポケットモンスター 幻のポケモン ルギア爆誕』→『劇場版ポケットモンスター、幻のポケモン、ルギア爆誕』として読む

## READ BEFORE CONVERTING

- UPLOAD LEXICON

## TODO

make a list of pokemon names into JSON

## file locations

- Google Drive: store final videos & info to share  
account is `wanpoke888@gmail.com`
- pokemon-code: stuff that uses code
- pokemon-media: video & audio

## workflow

### updated

- pokemon names are defined inside source code

### old

- write speech text to `text.txt`
- run `.py` file --> output to `ssml.txt`
- copy the file under `ssml` folder 
- add YOMIGANA with `<sub alias="ほげ"></sub>` tag
- upload to AWS Polly
- download mp3 --> save under `audio` folder
- add subitles with Vrew

## notes

- ignores first 3 lines of text 

## pronunciations

```xml
<phoneme alphabet="x-amazon-pron-kana" ph="フ'シギバナ">フシギバナ</phoneme>
```

## snippets

test phoneme

```xml
<phoneme alphabet="ipa" ph="ɸɯɕigʲibana"></phoneme>
```

tweak accents

```xml
<phoneme alphabet="x-amazon-pron-kana" ph="マイニチシ'ンブン">毎日新聞</phoneme>を読む 
```

c.f. https://aws.amazon.com/blogs/machine-learning/optimizing-japanese-text-to-speech-with-amazon-polly/