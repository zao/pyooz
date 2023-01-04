import os
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup, Extension

ooz_sources = [
    os.path.join('ooz/dep/ooz/', x) for x in [
        "bitknit.cpp",
        "kraken.cpp",
        "lzna.cpp",
    ]
]

ext_modules = [
    Pybind11Extension(
        'ooz',
        sources=['ooz/ooz_bindings.cpp'] + ooz_sources,
        define_macros=[('OOZ_BUILD_DLL', 1)],
        include_dirs=['ooz/dep/ooz/simde'],
    ),
]

from pathlib import Path
long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name='pyooz',
    version='0.0.6',
    description="ooz decompression bindings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
    ],
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
)
