# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import Any


@dataclasses.dataclass
class ReportingDescriptorReference(object):
    """Information about how to locate a relevant reporting descriptor."""

    guid: Any
    id: Any
    index: Any
    properties: Any
    tool_component: Any


# flake8: noqa