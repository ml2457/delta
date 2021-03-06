# Copyright (C) 2017 Beijing Didi Infinity Technology and Development Co.,Ltd.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""The model tests Delta_delta FE."""

import delta.compat as tf
from delta.data.frontend.delta_delta import DeltaDelta
import numpy as np
import tempfile
from kaldiio import WriteHelper


class Delta_delta_Test(tf.test.TestCase):
  """
  Delta_delta extraction test.
  """

  def test_delta_delta(self):

    self.feat_dim = 80
    self.data = np.arange(self.feat_dim, dtype=np.float32).reshape((8, 10))

    # compute from kaldi `add-detlas` tools
    self.output_true = np.array([
        0.0000000e+00,
        1.0000000e+00,
        2.0000000e+00,
        3.0000000e+00,
        4.0000000e+00,
        5.0000000e+00,
        6.0000000e+00,
        7.0000000e+00,
        8.0000000e+00,
        9.0000000e+00,
        1.0000000e+01,
        1.1000000e+01,
        1.2000000e+01,
        1.3000000e+01,
        1.4000000e+01,
        1.5000000e+01,
        1.6000000e+01,
        1.7000000e+01,
        1.8000000e+01,
        1.9000000e+01,
        2.0000000e+01,
        2.1000000e+01,
        2.2000000e+01,
        2.3000000e+01,
        2.4000000e+01,
        2.5000000e+01,
        2.6000000e+01,
        2.7000000e+01,
        2.8000000e+01,
        2.9000000e+01,
        3.0000000e+01,
        3.1000000e+01,
        3.2000000e+01,
        3.3000000e+01,
        3.4000000e+01,
        3.5000000e+01,
        3.6000000e+01,
        3.7000000e+01,
        3.8000000e+01,
        3.9000000e+01,
        4.0000000e+01,
        4.1000000e+01,
        4.2000000e+01,
        4.3000000e+01,
        4.4000000e+01,
        4.5000000e+01,
        4.6000000e+01,
        4.7000000e+01,
        4.8000000e+01,
        4.9000000e+01,
        5.0000000e+01,
        5.1000000e+01,
        5.2000000e+01,
        5.3000000e+01,
        5.4000000e+01,
        5.5000000e+01,
        5.6000000e+01,
        5.7000000e+01,
        5.8000000e+01,
        5.9000000e+01,
        6.0000000e+01,
        6.1000000e+01,
        6.2000000e+01,
        6.3000000e+01,
        6.4000000e+01,
        6.5000000e+01,
        6.6000000e+01,
        6.7000000e+01,
        6.8000000e+01,
        6.9000000e+01,
        7.0000000e+01,
        7.1000000e+01,
        7.2000000e+01,
        7.3000000e+01,
        7.4000000e+01,
        7.5000000e+01,
        7.6000000e+01,
        7.7000000e+01,
        7.8000000e+01,
        7.9000000e+01,
        0.0000000e+00,
        -1.4901161e-08,
        -2.9802322e-08,
        0.0000000e+00,
        -5.9604645e-08,
        0.0000000e+00,
        0.0000000e+00,
        1.1920929e-07,
        -1.1920929e-07,
        1.1920929e-07,
        0.0000000e+00,
        -2.3841858e-07,
        0.0000000e+00,
        2.3841858e-07,
        2.3841858e-07,
        0.0000000e+00,
        -2.3841858e-07,
        -2.3841858e-07,
        2.3841858e-07,
        2.3841858e-07,
        0.0000000e+00,
        4.7683716e-07,
        -4.7683716e-07,
        4.7683716e-07,
        0.0000000e+00,
        0.0000000e+00,
        4.7683716e-07,
        -4.7683716e-07,
        4.7683716e-07,
        -4.7683716e-07,
        0.0000000e+00,
        4.7683716e-07,
        -4.7683716e-07,
        4.7683716e-07,
        -4.7683716e-07,
        0.0000000e+00,
        4.7683716e-07,
        -4.7683716e-07,
        4.7683716e-07,
        -4.7683716e-07,
        0.0000000e+00,
        9.5367432e-07,
        9.5367432e-07,
        0.0000000e+00,
        -9.5367432e-07,
        0.0000000e+00,
        9.5367432e-07,
        9.5367432e-07,
        0.0000000e+00,
        -9.5367432e-07,
        0.0000000e+00,
        9.5367432e-07,
        9.5367432e-07,
        0.0000000e+00,
        -9.5367432e-07,
        0.0000000e+00,
        9.5367432e-07,
        9.5367432e-07,
        -9.5367432e-07,
        -9.5367432e-07,
        0.0000000e+00,
        9.5367432e-07,
        9.5367432e-07,
        -9.5367432e-07,
        -9.5367432e-07,
        0.0000000e+00,
        9.5367432e-07,
        9.5367432e-07,
        -9.5367432e-07,
        -9.5367432e-07,
        0.0000000e+00,
        9.5367432e-07,
        9.5367432e-07,
        -9.5367432e-07,
        -9.5367432e-07,
        0.0000000e+00,
        9.5367432e-07,
        9.5367432e-07,
        -9.5367432e-07,
        -9.5367432e-07,
        0.0000000e+00,
        0.0000000e+00,
        0.0000000e+00,
        0.0000000e+00,
        0.0000000e+00,
        5.9604645e-08,
        0.0000000e+00,
        5.9604645e-08,
        0.0000000e+00,
        0.0000000e+00,
        1.1920929e-07,
        5.9604645e-08,
        0.0000000e+00,
        0.0000000e+00,
        1.1920929e-07,
        0.0000000e+00,
        0.0000000e+00,
        2.3841858e-07,
        0.0000000e+00,
        2.3841858e-07,
        2.3841858e-07,
        0.0000000e+00,
        1.1920929e-07,
        2.3841858e-07,
        0.0000000e+00,
        2.3841858e-07,
        0.0000000e+00,
        0.0000000e+00,
        2.3841858e-07,
        0.0000000e+00,
        0.0000000e+00,
        0.0000000e+00,
        0.0000000e+00,
        0.0000000e+00,
        4.7683716e-07,
        0.0000000e+00,
        0.0000000e+00,
        4.7683716e-07,
        4.7683716e-07,
        2.3841858e-07,
        4.7683716e-07,
        4.7683716e-07,
        0.0000000e+00,
        0.0000000e+00,
        2.3841858e-07,
        0.0000000e+00,
        4.7683716e-07,
        2.3841858e-07,
        0.0000000e+00,
        4.7683716e-07,
        4.7683716e-07,
        9.5367432e-07,
        0.0000000e+00,
        4.7683716e-07,
        0.0000000e+00,
        4.7683716e-07,
        4.7683716e-07,
        4.7683716e-07,
        0.0000000e+00,
        4.7683716e-07,
        0.0000000e+00,
        4.7683716e-07,
        0.0000000e+00,
        4.7683716e-07,
        0.0000000e+00,
        4.7683716e-07,
        0.0000000e+00,
        4.7683716e-07,
        9.5367432e-07,
        4.7683716e-07,
        0.0000000e+00,
        4.7683716e-07,
        0.0000000e+00,
        4.7683716e-07,
        9.5367432e-07,
        4.7683716e-07,
        9.5367432e-07,
        0.0000000e+00,
        4.7683716e-07,
        4.7683716e-07,
    ],
                                dtype=np.float32)

    with self.cached_session(use_gpu=False, force_gpu=False):

      self.order = 2
      self.window = 2
      feat = tf.constant(self.data, dtype=tf.float32)
      delta_delta = DeltaDelta.params().instantiate()
      delta_delta_test = delta_delta(feat, self.order, self.window)

      self.assertEqual(delta_delta_test.shape, (8, 10, self.order + 1))


if __name__ == '__main__':
  tf.test.main()
