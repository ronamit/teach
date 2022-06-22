The code is based on https://github.com/google-research/google-research/tree/master/social_rl

Please see the README file in the social_rl subdirectory for more details.


## Installation
* requires linux
* create Python 3.8 environment, e.g. with  $ conda create -n tsg -python=3.8
* activate the environment, e.g. with $ conda activate tsg
* For GPU support: set CUDA+CudNN, e.g. $ conda install -c conda-forge cudatoolkit cudnn 
* $ pip3 install --upgrade pip
*  Install TensorFlow 2 , e.g. $ pip install tensorflow-gpu

* Install rest of the requirements $ pip3 install -r social_rl/requirements.txt

* Run test: $ python3 -m social_rl.adversarial_env.test_adversarial_env
