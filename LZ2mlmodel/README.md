# LZ2mlmodel
A converter which converts a Leela Zero weight file to a .mlmodel(Core ML) file.

## requirements
curl
gunzip
pyenv
pipenv

## Usage
```
./make.sh <board size> <URL of weight>
```

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