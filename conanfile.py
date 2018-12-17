#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires

base = python_requires("boost_base/1.69.0@bincrafters/testing")


class BoostSafeNumericsConan(base.BoostBaseConan):
    name = "boost_safe_numerics"
    url = "https://github.com/bincrafters/conan-boost_safe_numerics"
    lib_short_names = ["safe_numerics"]
    header_only_libs = ["safe_numerics"]
    b2_requires = [
        "boost_concept_check",
        "boost_config",
        "boost_core",
        "boost_integer",
        "boost_logic",
        "boost_mp11",
        "boost_mpl"
    ]
