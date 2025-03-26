import bpy
import pytest
from bl_ext.user_default import addonname


def test_example():
    addonname.assets.import_assets()
    assert True
