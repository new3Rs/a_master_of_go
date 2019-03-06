import sys
import tfcoreml as tf_converter

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python {} target_path'.format(sys.argv[0])) 
    tf_converter.convert(
        tf_model_path='tmp/frozen_model.pb',
        mlmodel_path = sys.argv[1],
        output_feature_names = ['fc1:0', 'fc3:0'],
        input_name_shape_dict = {'x:0' : [1, 19, 19, 18]}
    )