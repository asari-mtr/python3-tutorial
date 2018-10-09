#!/usr/bin/env python3

import sys, tempfile, os
from datetime import datetime
from subprocess import call

EDITOR = os.environ.get('EDITOR', 'vim')

initial_message = "Write comment"

with tempfile.NamedTemporaryFile(mode="w+", suffix='.tmp') as tf:
    tf.write(initial_message)
    tf.flush()
    call([EDITOR, tf.name])

    with open(tf.name, mode='r') as f:
        edited_message = f.read()

        print(edited_message.strip())
