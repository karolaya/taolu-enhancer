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
We are going to build opencv with cmake (obviously), and need to make sure to
install it in our desired directory with Python 3 in mind. Run the command as
follows:

    cmake -D CMAKE_TYPE=RELEASE -D CMAKE_PREFIX=/opt/opencv3 -D PYTHON_DEFAULT_EXECUTABLE=$HOME/py-envs/taolu/bin/python3 ..

Then make and install it:

    make
    sudo make install
After that, you won't (probably) have access, yet, to OpenCV in Python (If you
have ignore the following). Look for a file in
`/opt/opencv/lib/python3.6/site-packages` of the form `cv2.XXX.so`. All you need
to do is link it to the correct `site-packages` location.

    ln -s /opt/opencv/lib/python3.6/site-packages/cv2.XXX.so ~/py-envs/taolu/lib/python3.6/site-packages/cv2.so
That should give you a smooth install of OpenCV.

## OpenKinect (libfreenect)
To operate the Kinect in Linux, we need the `libfreenect` library. You will need `libusb`, `glut` and `cython`; you install it more or less like this:

    sudo pacman -S libusb freeglut
    sudo pip install cython
    
For Debian based systems it is (I am not sure):

    sudo apt-get install libusb-dev libusb-1.0-0-dev freeglut3-dev
    
Clone the `libfreenect` repository:

    git clone https://github.com/OpenKinect/libfreenect.git
Create a directory within what you cloned, named `build` and access it:
    
    cd libfreenect
    mkdir build && cd build
    
We need to make sure `libfreenect` installs with Python and OpenCV support. Run `cmake` as follows:

    cmake -D BUILD_PYTHON3=ON -D BUILD_CV=ON ..
    make
    sudo make install
    
For some reason, `sudo make install` does not copy the libraries in `build/lib` to where it should (if you thing it did for you, skip this part). All we need to do is copy them via brute force:
    
    cd lib
    sudo cp -R . /lib
To test your installation (this is important), connect your Kinect and do the following:

    cd /usr/local/bin
    sudo freenect-glview
If you see a video screen activating you are OK.

You are welcome.


























