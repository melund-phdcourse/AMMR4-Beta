# -*- coding: utf-8 -*-
r"""
Arm curl
===============================

Example of an Arm Curl fitness machine.

**Main file:** :file:`Application/Examples/ArmCurl/ArmCurl.main.any`

The objective of this example is to adjust the eccentricity of the cable wheel
such that the arm muscles experience a constant effort throughout the elbow
flexion taking the change of moment arms of the muscles into account. 

It is not possible to obtain a completely constant muscle effort with only the
eccentricity as parameter. However, if more parameters were introduced into an
actual design optimization, then it is likely that an almost completely uniform
effort profile could be obtained.

By chaning between the files "EnvironmentOptimized.any" and "Environment.any" it
is possible to to see the machine with adjusted eccentricity and the one with
zero eccentricity

"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/ArmCurl.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()