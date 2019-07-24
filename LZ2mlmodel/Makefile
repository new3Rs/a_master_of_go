GRAPH = tmp/graph.pb
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
	gunzip ${DOWNLOADED}

${GRAPH}: ${EXPANDED}
	python3 save_graph.py ${SIZE} ${EXPANDED}

${CHECK_POINT}: ${EXPANDED} ${GRAPH}
	python3 save_graph.py ${SIZE} ${EXPANDED}

${FROZEN_MODEL}: ${GRAPH} ${CHECK_POINT}.index
	freeze_graph --input_graph=${GRAPH} --input_checkpoint=${CHECK_POINT} --output_graph=${FROZEN_MODEL} --output_node_names=fc1,fc3

${OPTIMIZED_MODEL}: ${FROZEN_MODEL}
	python3 optimize.py ${FROZEN_MODEL} ${OPTIMIZED_MODEL}

${TARGET}: ${OPTIMIZED_MODEL}
	python3 convert_coreml.py ${OPTIMIZED_MODEL} ${SIZE} ${TARGET}

${TARGET_FP16}: ${TARGET}
	python3 convert_fp16.py ${TARGET} ${TARGET_FP16}

clean:
	rm -rf tmp *.mlmodel