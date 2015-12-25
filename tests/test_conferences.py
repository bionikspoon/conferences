#!/usr/bin/env python
# coding=utf-8

"""
test_conferences
----------------------------------

Tests for `conferences` module.
"""
from pytest import fixture

@fixture
def boilerplate():
    from conferences.conferences import Boilerplate

    return Boilerplate()


def test_cookiecutter_automates_boilerplate(boilerplate):
    assert str(boilerplate) == "Success"
