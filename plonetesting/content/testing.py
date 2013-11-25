# -*- coding: utf-8 -*-
from plone.testing import z2
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import TEST_USER_ID
from plone.app.testing import FunctionalTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import login
from plone.app.testing import setRoles
from zope.configuration import xmlconfig


class PlonetestingContent(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import plone.namedfile
        xmlconfig.file(
            'handler.zcml',
            plone.namedfile,
            context=configurationContext
        )
        import plonetesting.content
        self.loadZCML(package=plonetesting.content)
        xmlconfig.file(
            'configure.zcml',
            plonetesting.content,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetesting.content:default')
        portal.acl_users.userFolderAddUser('admin',
                                           'secret',
                                           ['Manager'],
                                           [])
        login(portal, 'admin')
        portal.portal_workflow.setDefaultChain("simple_publication_workflow")
        setRoles(portal, TEST_USER_ID, ['Manager'])
        portal.invokeFactory(
            "Folder",
            id="acceptance-test-folder",
            title=u"Test Folder"
        )

PLONETESTING_CONTENT = PlonetestingContent()
PLONETESTING_CONTENT_ROBOT = FunctionalTesting(
    bases=(PLONETESTING_CONTENT, z2.ZSERVER_FIXTURE),
    name="PlonetestingContent:Robot")
