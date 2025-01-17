from myterial import (
    light_blue,
    light_blue_darker,
    orange,
    orange_darker,
    indigo,
    indigo_darker,
    salmon,
    salmon_darker,
    blue_grey,
    blue_grey_darker,
)
import numpy as np

sensors = ["fl", "fr", "hl", "hr"]

colors = dict(
    fr=light_blue, fl=orange, hr=indigo, hl=salmon, tot_weight=blue_grey, CoG=blue_grey,
)

dark_colors = dict(
    fr=light_blue_darker,
    fl=orange_darker,
    hr=indigo_darker,
    hl=salmon_darker,
    tot_weight=blue_grey_darker,
    CoG=blue_grey_darker,
)

# XY coordinates in CM of each sensor from the center of the array
sensors_vectors = dict(
    fr=np.array([0.75, 1.625]),
    fl=np.array([-0.75, 1.625]),
    hr=np.array([1, -1.625]),
    hl=np.array([-1, -1.625]),
)
