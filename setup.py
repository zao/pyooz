import os
import pybind11
from setuptools import setup, Extension

ooz_sources = [
    os.path.join('ooz/dep/ooz/', x) for x in [
        "bitknit.cpp",
        "bits_rev_table.h",
        "compr_entropy.cpp",
        "compr_entropy.h",
        "compr_kraken.cpp",
        "compr_kraken.h",
        "compr_leviathan.cpp",
        "compr_leviathan.h",
        "compr_match_finder.cpp",
        "compr_match_finder.h",
        "compr_mermaid.cpp",
        "compr_mermaid.h",
        "compr_multiarray.cpp",
        "compr_tans.cpp",
        "compr_util.h",
        "compress.cpp",
        "compress.h",
        "kraken.cpp",
        "log_lookup.h",
        "lzna.cpp",
        "match_hasher.h",
        "qsort.h",
        "stdafx.h"
        "targetver.h",
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