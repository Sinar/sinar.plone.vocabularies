# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from sinar.plone.vocabularies.testing import SINAR_PLONE_VOCABULARIES_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that sinar.plone.vocabularies is properly installed."""

    layer = SINAR_PLONE_VOCABULARIES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sinar.plone.vocabularies is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'sinar.plone.vocabularies'))

    def test_browserlayer(self):
        """Test that ISinarPloneVocabulariesLayer is registered."""
        from sinar.plone.vocabularies.interfaces import (
            ISinarPloneVocabulariesLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ISinarPloneVocabulariesLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SINAR_PLONE_VOCABULARIES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['sinar.plone.vocabularies'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if sinar.plone.vocabularies is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'sinar.plone.vocabularies'))

    def test_browserlayer_removed(self):
        """Test that ISinarPloneVocabulariesLayer is removed."""
        from sinar.plone.vocabularies.interfaces import \
            ISinarPloneVocabulariesLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ISinarPloneVocabulariesLayer,
            utils.registered_layers())
