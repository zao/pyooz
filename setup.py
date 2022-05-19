import os
import pybind11
from setuptools import setup, Extension

ooz_sources = [
    os.path.join('ooz/dep/ooz/', x) for x in [
        "bitknit.cpp",
        "compr_entropy.cpp",
        "compr_kraken.cpp",
        "compr_leviathan.cpp",
        "compr_match_finder.cpp",
        "compr_mermaid.cpp",
        "compr_multiarray.cpp",
        "compr_tans.cpp",
        "compress.cpp",
        "kraken.cpp",
        "lzna.cpp",
    ]
]

ext_modules = [
    Extension(
        'ooz',
        sources=['ooz/ooz_bindings.cpp'] + ooz_sources,
        include_dirs=[
            pybind11.get_include(),
        ],
        language="c++",
    ),
]

setup(
    name='pyooz',
    version='0.0.3',
    license='GPL-2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
    ],
    ext_modules=ext_modules,
)