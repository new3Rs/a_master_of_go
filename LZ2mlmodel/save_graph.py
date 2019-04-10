#!/usr/bin/env python3
import tensorflow as tf
import os
import sys
from tfprocess import TFProcess
from net2net import read_net

BOARD_SIZE = 19
FEATURES = 18


if __name__ == "__main__":
    data_format = 'NHWC' # for tfcoreml
    BOARD_SIZE = int(sys.argv[1])
    version, blocks, filters, weights = read_net(sys.argv[2])

    if data_format == 'NHWC':
        planes = tf.placeholder(tf.float32, [None, BOARD_SIZE, BOARD_SIZE, FEATURES], name='x')
        probs = tf.placeholder(tf.float32, [None, BOARD_SIZE * BOARD_SIZE + 1])
        winner = tf.placeholder(tf.float32, [None, 1])
    else:
        planes = tf.placeholder(tf.float32, [None, FEATURES, BOARD_SIZE, BOARD_SIZE], name='x')
        probs = tf.placeholder(tf.float32, [None, BOARD_SIZE * BOARD_SIZE + 1])
        winner = tf.placeholder(tf.float32, [None, 1])

    tfprocess = TFProcess()
    tfprocess.TFCOREML = True
    tfprocess.DATA_FORMAT = data_format
    tfprocess.BOARD_SIZE = BOARD_SIZE
    tfprocess.INPUT_DIM = 2
    tfprocess.FEATURES = FEATURES
    tfprocess.RESIDUAL_FILTERS = filters
    tfprocess.RESIDUAL_BLOCKS = blocks
    if BOARD_SIZE == 9:
        tfprocess.VALUE_FULLY_CONNECTED = 64
    tfprocess.training = False # batch normalizationをコンバートするため
    tfprocess.init_net(planes, probs, winner)
    tfprocess.replace_weights(weights)
    tf.train.write_graph(tf.get_default_graph(), './tmp', 'graph.pb', as_text=True)
    with tf.get_default_graph().as_default():
        saver = tf.train.Saver()
        print(saver.save(tfprocess.session, "./tmp/model.ckpt"))
