from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name='Quicksort',
    ext_modules=cythonize(["pyx_files/*.pyx"]),
    zip_safe=False,
    include_dirs=[np.get_include()],
)