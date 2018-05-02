# -*- coding: utf-8 -*-

# from plone import api
from sinar.plone.vocabularies import _
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value

@implementer(IVocabularyFactory)
class PoliticalParties(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem(value=u'bn', title=_(u'Barisan Nasional')),
            VocabItem(value=u'pbsm', title=_(u'Parti Bersama Malaysia')),
            VocabItem(value=u'pas', title=_(u'Parti Islam Se-Malaysia')),
            VocabItem(value=u'pkr', title=_(u'Parti Keadilan Rakyat')),
            VocabItem(value=u'prm', title=_(u'Parti Rakyat Malaysia')),
            VocabItem(value=u'psm', title=_(u'Parti Sosialis Malaysia')),
            VocabItem(value=u'warisan', title=_(u'Warisan')), 
        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


PoliticalPartiesFactory = PoliticalParties()
