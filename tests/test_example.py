import bpy
import pytest
from bl_ext.user_default import addonid


def test_example():
    addonid.assets.import_assets()
    assert True
