# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import Any


@dataclasses.dataclass
class Node(object):
    """Represents a node in a graph."""

    id: Any
    children: Any
    label: Any
    location: Any
    properties: Any


# flake8: noqa