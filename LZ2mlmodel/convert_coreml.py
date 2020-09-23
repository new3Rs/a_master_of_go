import sys
import tfcoreml as tf_converter
from coremltools.models import MLModel

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python {} source size target_path'.format(sys.argv[0]))
        sys.exit()
    size = int(sys.argv[2])
    tf_converter.convert(
        tf_model_path=sys.argv[1],
        mlmodel_path=sys.argv[3],
        output_feature_names=['fc1:0', 'fc3:0'],
        input_name_shape_dict={'x:0' : [1, size, size, 18]}
    )
    model = MLModel(sys.argv[3])
    version = "1" # Leela Zero
    #version = "2" # ELF OpenGo
    model.user_defined_metadata["version"] = version
    model.user_defined_metadata["size"] = str(size)
    model.user_defined_metadata["komi"] = "7.5"
    model.user_defined_metadata["C_init"] = "0.5" if version == "1" else "0.75"
    model.user_defined_metadata["C_logpuct"] = "0.015"
    model.user_defined_metadata["C_logconst"] = "1.7"
    model.user_defined_metadata["softmax_temperature"] = "1.0"
    model.user_defined_metadata["virtual_loss"] = "3" if version == "1" else "1"
    model.save(sys.argv[3])