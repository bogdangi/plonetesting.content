from zope.interface import implements

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.geo.mapwidget.browser.widget import MapWidget

from plonetesting.content import MessageFactory as _


class IPlacesMapPortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IPlacesMapPortlet)

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return _(u"Place map portlet")


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('placesmapportlet.pt')

    @property
    def cgmap(self):
        mapwidget = MapWidget(self, self.request, self.context)
        mapwidget.mapid = 'rally-map-portlet'
        return mapwidget

    @property
    def available(self):
        # Show this portlet for logged in users only
        return self.context.portal_type == 'plonetesting.content.rally'


class AddForm(base.NullAddForm):
    """Portlet add form.
    """
    def create(self):
        return Assignment()
