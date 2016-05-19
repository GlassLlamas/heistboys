# Heistboys

## Installation

### Requirements

* Python 3.4+
* Pygame 1.9.2
    * SDL 1.2
    * SDL 1.2 image
    * SDL 1.2 mixer
    * SDL 1.2 ttf
    * These are probably packages called libsdl, libsdl_image, sdl1.2, sdl1.2-dev, etc.
* Buffalo

### Quick Start

```
pip install -r requirements.txt
```

^^^this should work

### Quick Start didn't work because of Pygame

1. `hg clone https://bitbucket.org/pygame/pygame`
2. Make sure you have SDL 1.2, SDL 1.2 Image, SDL 1.2 Mixer, SDL 1.2 TTF, and a bunch of other dependencies
    * If you don't have all the dependencies, go to the next step anyways. The installer will list all the dependencies that aren't satisfied if you don't have them, otherwise it will install.
3. (probably sudo) `python setup.py install`

### Quick Start didn't work because of Buffalo

1. `git clone https://github.com/gragas/buffalo`
2. (probably sudo) `python setup.py install`

## Running the progrum

`python main.py`