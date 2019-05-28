# LZ2mlmodel
A converter which converts a Leela Zero weight file to a .mlmodel(Core ML) file.

## requirements
curl
gunzip
pyenv
pipenv

## How to prepare downloadable weight file set
You need to prepare two files on the Internet, one is a JSON file for information, the other is .mlmodel file.
The below is an example using GX89 in [Leela Master](https://github.com/pangafu/LeelaMasterWeight) by 章鱼围棋(Octopus Go) & 袁泉(pangafu@github).

### JSON file
```json:LeelaMaster_GX89_fp16.json
{
    "url": "https://dl.dropboxusercontent.com/s/66xjj1uuk3yv8b7/LeelaMaster_GX89_fp16.mlmodel",
    "size": 19,
    "komi": 7.5,
    "version": 1
}
```
The property "size" means board size, "komi" is target komi of the weight, "version" means Leela Zero weight format version, which is extended "3" for PhoenixGo (17 input planes), "4" for minigo (17 input planes, value for black).

### .mlmodel file
See Usage to make .mlmodel file.
About file name, the app shows the head part of file name of .mlmodel, which is from head upto before the second underscore "_". The example model is shown as "LeelaMaster_GX89".
So please put user-recognizable name in the head part and detail info such as "_fp16" or hash in the rest part.

## Try to download the example
Put "https://dl.dropboxusercontent.com/s/4ue9d86yaglengl/LeelaMaster_GX89_fp16.json" into the URL field in setting model on the app and press enter key.

## Usage of the resources in this directory
### simple instruction to make .mlmodel file
```
./make.sh <board size> <URL of weight>
```
An example for Leela Zero #221
```
./make.sh 19 https://zero.sjeng.org/networks/92f828bf13087837dfed4058df85afe634a028492e29418cbff41ab47023d42e.gz
```

Then please prepare JSON file according to the above information.
You can download Leela Zero #221 as "https://dl.dropboxusercontent.com/s/i5zjw56v5i9vo21/LeelaZero_221_fp16.json"

## Detail
<dl>
<dt>convert_coreml.py</dt>
<dd>converts TensorFlow model to .mlmodel format</dd>
<dt>convert_fp16.py</dt>
<dd>converts .mlmodel to fp16 .mlmodel</dd>
<dt>save_graph.py</dt>
<dd>saves TensorFlow graph and checkpoint from Leela Zero text weight file</dd>
<dt>Makefile</dt>
<dd>process flow from downloading Leela Zero wight file to fp16 .mlmodel</dd>
</dl>

# License
GPL v3 or later. (same as Leela Zero project(https://github.com/leela-zero/leela-zero))