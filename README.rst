plonetesting.content
====================

.. image:: https://travis-ci.org/bogdangi/plonetesting.content.png?branch=master
   :target: https://travis-ci.org/bogdangi/plonetesting.content

.. image:: https://coveralls.io/repos/bogdangi/plonetesting.content/badge.png
   :target: https://coveralls.io/r/bogdangi/plonetesting.content

.. contents::

Introduction
------------

This product contains two dexterity content types `Rally`_, `Place`_ and portlet
`Rally Map Portlet`_.

Place
-----

This contet is attacheble for others events and marks their position on the map.

Place contains GEO coordinate field, standard title and description.

Rally
-----

Rally is a type of event.

It contains multyple referance field for Places, two image fields, standard 
title and description.

It has attached portlet `Rally Map Portlet`_ which shows map with setted Places.

Rally Map Portlet
-----------------

Portlet automatically assign on Pally type and show attached Places on
`Google map`.
If portlet is assigned on another content or there is not any Places it
shows nothing.
