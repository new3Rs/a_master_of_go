import sys
import tensorflow as tf
from tensorflow.python.tools import optimize_for_inference_lib

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Usage: python {} source destination".format(sys.argv[0])) 
    sys.exit()

  inputGraph = tf.GraphDef()
  with tf.gfile.Open(sys.argv[1], "rb") as f:
    data2read = f.read()
    inputGraph.ParseFromString(data2read)
    
  outputGraph = optimize_for_inference_lib.optimize_for_inference(
                inputGraph,
                ["x"], # an array of the input node(s)
                ["fc1", "fc3"], # an array of output nodes
                tf.float32.as_datatype_enum)

  tf.train.write_graph(outputGraph,".",sys.argv[2],as_text=False)
