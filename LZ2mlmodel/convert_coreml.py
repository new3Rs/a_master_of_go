import sys
import tfcoreml as tf_converter

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python {} source size target_path'.format(sys.argv[0]))
        sys.exit()
    size = int(sys.argv[2])
    tf_converter.convert(
        tf_model_path=sys.argv[1],
        mlmodel_path = sys.argv[3],
        output_feature_names = ['fc1:0', 'fc3:0'],
        input_name_shape_dict = {'x:0' : [1, size, size, 18]}
    )