# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import Any


@dataclasses.dataclass
class ThreadFlow(object):
    """Describes a sequence of code locations that specify a path through a single thread of execution such as an operating system or fiber."""

    locations: Any
    id: Any
    immutable_state: Any
    initial_state: Any
    message: Any
    properties: Any


# flake8: noqa