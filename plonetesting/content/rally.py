from five import grok
from zope.component import queryMultiAdapter
from collective.geo.kml.interfaces import IFeature

from plone.directives import form
from plone.namedfile.interfaces import IImageScaleTraversable

from plone.dexterity.content import Container
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from collective.geo.kml.browser.kmldocument import KMLBaseDocument


from plonetesting.content import MessageFactory as _


class IRally(form.Schema, IImageScaleTraversable):
    """
    Rally event
    """

    form.model("models/rally.xml")

    # Additional field to implement functionality for adding places
    places = RelationList(
        title=_(u'Places'),
        default=[],
        value_type=RelationChoice(
            title=_(u"Link to places"),
            source=ObjPathSourceBinder(
                portal_type="plonetesting.content.place")),
        required=False,)


class Rally(Container):
    grok.implements(IRally)


class KMLRallyMap(KMLBaseDocument):
    """ KML document render """

    @property
    def features(self):
        for item in self.context.places:
            feature = queryMultiAdapter(
                (item.to_object, self.request), IFeature)
            yield feature


sourceBinderForPlaces = ObjPathSourceBinder(
    portal_type="plonetesting.content.place")
