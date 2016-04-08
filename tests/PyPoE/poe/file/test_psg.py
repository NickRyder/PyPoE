"""
Tests for PyPoE.poe.file.psg

Overview
===============================================================================

+----------+------------------------------------------------------------------+
| Path     | tests/PyPoE/poe/file/test_psg.py                                 |
+----------+------------------------------------------------------------------+
| Version  | 1.0.0a0                                                          |
+----------+------------------------------------------------------------------+
| Revision | $Id$                  |
+----------+------------------------------------------------------------------+
| Author   | Omega_K2                                                         |
+----------+------------------------------------------------------------------+

Description
===============================================================================



Agreement
===============================================================================

See PyPoE/LICENSE
"""

# =============================================================================
# Imports
# =============================================================================

# Python
from PyPoE.poe.file import psg
from PyPoE.poe.file.dat import DatFile

# 3rd-party
import pytest

# self

# =============================================================================
# Setup
# =============================================================================

# =============================================================================
# Fixtures
# =============================================================================

# =============================================================================
# Tests
# =============================================================================

def test_psg(ggpkfile, rr):
    f = psg.PSGFile(passive_skills_dat_file=rr)
    f.read(ggpkfile['Metadata/PassiveSkillGraph.psg'].record.extract())

    import pprint
    print(pprint.pprint(f.groups))