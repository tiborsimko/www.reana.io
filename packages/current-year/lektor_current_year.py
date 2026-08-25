# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Lektor plugin exposing the current year to the templates."""

from datetime import datetime, timezone

from lektor.pluginsystem import Plugin


class CurrentYearPlugin(Plugin):
    """Expose the year of the site build to the templates."""

    name = "current-year"
    description = "Exposes the year of the site build as ``current_year``."

    def on_setup_env(self, **extra):
        """Add the ``current_year`` global to the Jinja environment."""
        self.env.jinja_env.globals["current_year"] = datetime.now(timezone.utc).year
