#!/usr/bin/env python3
# coding: utf-8
#
# LGPL
#
# SM_Translate.py

import os
import FreeCADGui as Gui
import FreeCAD as App
import smwb_locator

smWBpath = os.path.dirname(smwb_locator.__file__)
smWB_icons_path =  os.path.join( smWBpath, 'Resources', 'icons')
Gui.addLanguagePath(os.path.join(smWBpath, "Resources/translations"))


def _atr(context: str, text: str) -> str:
    """Wrap strings which should be translated in in this function."""
    return App.Qt.translate(context, text)


def QT_TRANSLATE_NOOP(context: str, text: str) -> str:
    """NOP Marker Macro Alias for strings for which FreeCAD/Qt handles translations."""
    return text
