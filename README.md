# NanoGPT TR

This is a PyTorch implementation of NanoGPT, a tiny version of GPT-2. The model is trained on a very simple Turkish dataset parsed from Wikipedia which consists of 500.000 characters. Karpathy uses a dataset named tinyshakespeare which is about 1.000.000 characters long. So, this dataset is about half of the tinyshakespeare dataset.

This is just a lecture follow-up code, no real life usage is intended. The model is trained on a single GPU for 5000 steps. The training takes about 1 hour on a single GPU. The model is not tested on any other dataset. The model is not tested on any other language.

Model also performs very badly 😂

## Training results

- step 0: train loss 4.6877, val loss 4.6818
- step 500: train loss 1.6895, val loss 1.8506
- step 1000: train loss 1.1792, val loss 1.5876
- step 1500: train loss 0.8968, val loss 1.6050
- step 2000: train loss 0.6589, val loss 1.6902
- step 2500: train loss 0.4667, val loss 1.8505
- step 3000: train loss 0.3229, val loss 2.0277
- step 3500: train loss 0.2284, val loss 2.1829
- step 4000: train loss 0.1675, val loss 2.3626
- step 4500: train loss 0.1390, val loss 2.4900
- step 4999: train loss 0.1192, val loss 2.6184 