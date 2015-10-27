"""
Tests for PyPoE.shared.decorators

Overview
-------------------------------------------------------------------------------

+----------+------------------------------------------------------------------+
| Path     | tests/PyPoE/shared/test_decorators.py                            |
+----------+------------------------------------------------------------------+
| Version  | 1.0.0a0                                                          |
+----------+------------------------------------------------------------------+
| Revision | $Id$                                                             |
+----------+------------------------------------------------------------------+
| Author   | Omega_K2                                                         |
+----------+------------------------------------------------------------------+

Description
-------------------------------------------------------------------------------



Agreement
-------------------------------------------------------------------------------

See PyPoE/LICENSE
"""

# =============================================================================
# Imports
# =============================================================================

# Python

# 3rd-party
import pytest

# self
from PyPoE.shared import decorators

# =============================================================================
# Setup
# =============================================================================

# =============================================================================
# Fixtures
# =============================================================================

# =============================================================================
# Tests
# =============================================================================

class TestDeprecated:
    def test_simple_call(self):
        @decorators.deprecated
        def temp(x):
            pass

        pytest.deprecated_call(temp, 5)

    def test_empty_args(self):
        @decorators.deprecated()
        def temp(x):
            pass

        pytest.deprecated_call(temp, 5)

    def test_message_args(self):
        @decorators.deprecated(message='Test')
        def temp(x):
            pass

        pytest.deprecated_call(temp, 5)