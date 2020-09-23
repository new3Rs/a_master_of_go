GRAPH = tmp/graph.pbtxt
CHECK_POINT = tmp/model.ckpt
FROZEN_MODEL = tmp/frozen_model.pb
OPTIMIZED_MODEL = tmp/optimized.pb
#SIZE = should_be_given_as_environment_variable
#URL = should_be_given_as_environment_variable
DOWNLOADED = $(notdir ${URL})
EXPANDED = $(basename ${DOWNLOADED})
TARGET = ${EXPANDED}.mlmodel
TARGET_FP16 = ${EXPANDED}_fp16.mlmodel

all: ${TARGET_FP16}

${DOWNLOADED}:
	curl -OL ${URL}

${EXPANDED}: ${DOWNLOADED}
	gunzip -k -f ${DOWNLOADED}

${GRAPH}: ${EXPANDED} save_graph.py
	python save_graph.py ${SIZE} $< $@

${CHECK_POINT}: ${EXPANDED} ${GRAPH} save_graph.py
	python save_graph.py ${SIZE} $< ${GRAPH}

${FROZEN_MODEL}: ${GRAPH} ${CHECK_POINT}.index
	freeze_graph --input_graph=$< --input_checkpoint=${CHECK_POINT} --output_graph=$@ --output_node_names=fc1,fc3

${OPTIMIZED_MODEL}: ${FROZEN_MODEL} optimize.py
	python optimize.py $< $@

${TARGET}: ${OPTIMIZED_MODEL} convert_coreml.py
	python convert_coreml.py $< ${SIZE} $@

${TARGET_FP16}: ${TARGET} convert_fp16.py
	python convert_fp16.py $< $@

clean:
	rm -rf tmp *.mlmodel