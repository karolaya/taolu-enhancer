# Dependencies Installation (Arch Linux)
This file is an example (probably useful) of how to install the dependencies of
this project. Most packages will be built from source so, as a whole, this guide
can be replicated in other Linux flavours; `pip` is assumed.

## VirtualEnvironment
First off install `virtualenv` and `virtualenvwrapper` (optional):

    sudo pip3 install virtualenv virtualenvwrapper

Create a custom folder in your home directory, where you will save all your
environments:

    cd
    mkdir py-envs

`virtualenvwrapper` requires an aditional configuration step. Copy the following
in your `~/.bashrc` file:

    export WORKON_HOME=$HOME/py-envs
    source /usr/bin/virtualenvwrapper.sh # this location may change

then source it: `source ~/.bashrc`.
Navigate to your environments' directory and create a brand new one and access
it:

    virtualenv taolu && workon taolu
The rest will assume you have your virtualenv active.

## OpenCV 3
To build OpenCV you need a series of dependencies, I will not cover that here
(worry not, if you are reading this you probably already have OpenCV2 ;) ).
Previous to anything, determine where you want to build OpenCV (as you already
have a running version). I will do it in `/opt`:

    cd /opt
    sudo mkdir opencv3
First clone, somewhere (like in your Downloads directory), the code from github:

    git clone https://github.com/opencv/opencv.git
Enter the created directory, create a new one named `release` and access it:

    cd opencv
    mkdir release && cd release
We are going to build opencv with cmake (obviously), and need to make your to
install it in our desired directory with Python 3 in mind. Run the command as
follows:

    cmake -D CMAKE_TYPE=RELEASE -D CMAKE_PREFIX=/opt/opencv3 -D PYTHON_DEFAULT_EXECUTABLE=$HOME/py-envs/taolu/bin/python3

Then make and install it:

    make
    sudo make install
After that, you won't (probably) have access, yet, to OpenCV in Python (If you
have ignore the following). Look for a file in
`/opt/opencv/lib/python3.6/site-packages` of the form `cv2.XXX.so`. All you need
to do is link it to the correct `site-packages` location.



























