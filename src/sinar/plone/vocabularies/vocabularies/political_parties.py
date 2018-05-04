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
            VocabItem('amanah', _(u'Amanah')),
            VocabItem('bn', _(u'Barisan Nasional')),
            VocabItem('berjasa', _(u'Berjasa')),
            VocabItem('dap', _(u'Democratic Action Party')),
            VocabItem('gerakan', _(u'Gerakan')),
            VocabItem('mic', _(u'Kongres India Malaysia/MIC')),
            VocabItem('mca', _(u'Persatuan China Malaysia/MCA')),
            VocabItem('mu', _(u'Parti Bersama Malaysia')),
            VocabItem('myppp', _(u'Parti Progresif Penduduk')),
            VocabItem('ldp', _(u'Parti Liberal Demokratik')),
            VocabItem('pap', _(u'Parti Alterntif Rakyat')),
            VocabItem('pas', _(u'Parti Islam Se-Malaysia')),
            VocabItem('pan', _(u'Parti Anak Negeri')),
            VocabItem('pbb', _(u'Parti Pesaka Bumiputera Bersatu')),
            VocabItem('pbk', _(u'Parti Bumi Kenyalang')),
            VocabItem('pbsm', _(u'Parti Bersama Malaysia')),
            VocabItem('pbdsb', _(u'Parti Bansa Dayak Sarawak Baru')),
            VocabItem('pbs', _(u'Parti Bersatu Sabah')),
            VocabItem('pcm', _(u'Parti Cinta Malaysia')),
            VocabItem('pcs', _(u'Parti Cinta Sabah')),
            VocabItem('phrs', _(u'Parti Bersatu Rakyat Sabah')),
            VocabItem('ppbm', _(u'Parti Pribumi Bersatu Malaysia')),
            VocabItem('pkr', _(u'Parti Keadilan Rakyat')),
            VocabItem('prm', _(u'Parti Rakyat Malaysia')),
            VocabItem('psm', _(u'Parti Sosialis Malaysia')),
            VocabItem('spdp', _(u'Parti Demokratik Progresif Sarawak')),
            VocabItem('umno', _(u'United Malays National Organisation')),
            VocabItem('warisan', _(u'Warisan')), 
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
