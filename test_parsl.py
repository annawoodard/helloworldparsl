import os
import sys

import parsl
from parsl import python_app, bash_app, File
#from parsl.data_provider.files import File

from config import config


@python_app
def cwd():
    import os
    return os.getcwd()

@bash_app
def compress(inputs = [], decompress = "", stderr=parsl.AUTO_LOGNAME, stdout=parsl.AUTO_LOGNAME):
    import os
    print("cwd is: {}".format(os.getcwd()))
    return f"pigz {decompress} {inputs[0]}"

@bash_app
def write_hello(inputs = [], outputs = [], stderr=parsl.AUTO_LOGNAME, stdout=parsl.AUTO_LOGNAME):
    print(outputs)
    return f"cat {inputs[0]} > {outputs[0]}"

# @bash_app
# def echo_hello(msg, stdout="hello.out", stderr="hello.err"):
#     return f"echo {msg}"
if __name__ == "__main__":
    parsl.set_stream_logger()
    parsl.load(config)
    print('main process running in: {}'.format(os.getcwd()))
    print('worker processes running in: {}'.format(cwd().result()))
    out = [File(os.path.join(os.getcwd(), "test.txt"))]
    in_ = [File(os.path.join(os.getcwd(), "hw.txt"))]
    wh = write_hello(inputs = in_, outputs = out)
    with open(wh.outputs[0].result(), 'r') as f:
        print(f.read())
    compress(inputs = wh.outputs)

    parsl.wait_for_current_tasks()
