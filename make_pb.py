import tensorflow as tf
import pathlib


def make_pb():

    # define version and args
    tf.app.flags.DEFINE_integer('version', 0, 'version')
    tf.app.flags.DEFINE_integer('x', 0, 'x')
    tf.app.flags.DEFINE_integer('y', 0, 'y')

    # define info about model
    MODULE_NAME = 'default'
    VERSION = tf.app.flags.FLAGS.version
    SERVING_HOST = 'localhost'
    SERVING_PORT = 9000
    EXPORT_DIR = pathlib.Path('saved_model').resolve() / str(VERSION)

    X = tf.app.flags.FLAGS.x
    Y = tf.app.flags.FLAGS.y

    with tf.Graph().as_default() as graph:
        x = tf.placeholder(dtype=tf.int64, shape=(), name='x')
        y = tf.placeholder(dtype=tf.int64, shape=(), name='y')
        add_fn = tf.add(x=x, y=y)

        builder = tf.saved_model.builder.SavedModelBuilder(EXPORT_DIR)
        with tf.Session(graph=graph) as sess:
            builder.add_meta_graph_and_variables(
                sess, [tf.saved_model.tag_constants.SERVING],
                signature_def_map={
                    'add_fn':
                    tf.saved_model.signature_def_utils.build_signature_def(
                        inputs={
                            'x': tf.saved_model.utils.build_tensor_info(x),
                            'y': tf.saved_model.utils.build_tensor_info(y)
                        },
                        outputs={
                            'add_fn':
                            tf.saved_model.utils.build_tensor_info(add_fn)
                        },
                        method_name=tf.saved_model.signature_constants.
                        PREDICT_METHOD_NAME)
                })
            builder.save()


if __name__ == '__main__':
    make_pb()