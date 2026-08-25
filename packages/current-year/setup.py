# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Lektor plugin exposing the current year to the templates."""

from setuptools import setup

setup(
    name="lektor-current-year",
    version="1.0.0",
    description="Lektor plugin exposing the current year to the templates",
    license="MIT",
    py_modules=["lektor_current_year"],
    entry_points={
        "lektor.plugins": [
            "current-year = lektor_current_year:CurrentYearPlugin",
        ],
    },
)
