#!/usr/bin/env python3

import sys
from image_shuffler import Shuffler
image = Shuffler(sys.argv[1])
image.shuffle(matrix=(int(sys.argv[2]),int(sys.argv[3])))
image.save()
