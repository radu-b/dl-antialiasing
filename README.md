# Antialias with Deep Learning

Adds antialiasing (smooth edges) to an image containing black & white (1-bit) drawings and text.

Here are some examples, which are ideally viewed without browser scaling. They show the B&W image, followed by the algorithm output, followed by the ground truth (original image, with proper antialiasing):

![Input](https://github.com/radu-b/dl-antialiasing/raw/master/data/test/x/12.png)
![Output](https://github.com/radu-b/dl-antialiasing/raw/master/data/test/y_hat/12.png)
![Truth](https://github.com/radu-b/dl-antialiasing/raw/master/data/test/y/12.png)

![Input](https://github.com/radu-b/dl-antialiasing/raw/master/data/test/x/6.png)
![Output](https://github.com/radu-b/dl-antialiasing/raw/master/data/test/y_hat/6.png)
![Truth](https://github.com/radu-b/dl-antialiasing/raw/master/data/test/y/6.png)

![Input](https://github.com/radu-b/dl-antialiasing/raw/master/data/test/x/11.png)
![Output](https://github.com/radu-b/dl-antialiasing/raw/master/data/test/y_hat/11.png)
![Truth](https://github.com/radu-b/dl-antialiasing/raw/master/data/test/y/11.png)

## Details

The algorithm uses a UNet based on ResNet18.

## Running

Requires Python 3.7, pytorch 1.3.0, fastai 1.0, Pillow 3.1.

The script `src/generate_images.py` will generate training images in `data/train`.

Then you can use `src/fai_learner.py` to train the model and process the test images from `data/test`.
