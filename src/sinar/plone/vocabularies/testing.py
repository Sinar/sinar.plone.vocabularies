# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import sinar.plone.vocabularies


class SinarPloneVocabulariesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=sinar.plone.vocabularies)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinar.plone.vocabularies:default')


SINAR_PLONE_VOCABULARIES_FIXTURE = SinarPloneVocabulariesLayer()


SINAR_PLONE_VOCABULARIES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINAR_PLONE_VOCABULARIES_FIXTURE,),
    name='SinarPloneVocabulariesLayer:IntegrationTesting',
)


SINAR_PLONE_VOCABULARIES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINAR_PLONE_VOCABULARIES_FIXTURE,),
    name='SinarPloneVocabulariesLayer:FunctionalTesting',
)


SINAR_PLONE_VOCABULARIES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINAR_PLONE_VOCABULARIES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SinarPloneVocabulariesLayer:AcceptanceTesting',
)
