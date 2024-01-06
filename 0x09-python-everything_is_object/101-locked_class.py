#!/usr/bin/python3
"""Defination of a locked class."""


class LockedClass:
    """
    Prevent the user from dynamically creating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
