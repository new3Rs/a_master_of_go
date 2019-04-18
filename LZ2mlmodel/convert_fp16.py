import sys
import coremltools

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python {} fp32_path fp16_path'.format(sys.argv[0]))
        sys.exit()

    # Load a model, lower its precision, and then save the smaller model.
    model_spec = coremltools.utils.load_spec(sys.argv[1])
    model_fp16_spec = coremltools.utils.convert_neural_network_spec_weights_to_fp16(model_spec)
    coremltools.utils.save_spec(model_fp16_spec, sys.argv[2])
