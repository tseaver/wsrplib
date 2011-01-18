Example:  Implementing a "Hello, World!" Portlet
================================================

:mod:`wsrplib` expects portlets to be objects which conform to the interface,
:class:`wsrplib.interfaces.IPortlet`.  The example portlet in
:mod:`wsrplib.dummy` implements the interface as a simple "Hello, World!":

.. literalinclude:: ../wsrplib/dummy.py
   :linenos:


:class:`wsrplib.dummy.DummyMarkup`
----------------------------------

This class has attributes which map onto :class:`wsrplib.datatypes.MarkupType`.
Each portlet must supply at least one instance of such a class in its
``markupTypes`` attribute.


:class:`wsrplib.dummy.DummyPortlet`
-----------------------------------

An instance of this class is intended to be registered as a utility providing
the ``IPortlet`` interface.

- Line 16 declares that the class implements the ``IPortlet`` interface on
  behalf of its instances.

- Line 17 supplies the required `MarkupType` instance (another portlet might
  support more than one type).

- Lines 18 - 21 supply static metadata about the portlet.

- Line 22 specifies that the portlet does not depend on any user category
  or user profile items.

- Line 23 declares that the portlet does not use any HTML forms whose
  ``method`` attribute is "GET".

- Lines 24 - 25 declare that the portlet does not use or require encryption.

- Lines 26 - 27 declare that the portlet does not store the user context or
  URL templates in the session.

- Line 28 specifies that the template does not store user-specific state in
  the session.

- Line 29 specifies that the portlet does **not** perform URL templating.

- Lines 30 - 43 define the logic for computing markup when the portlet
  is being rendered:

  - Line 35 arranges for returned object to be an instance of
    :class:`wsrplib.datatypes.MarkupContext`, as required by the interface.

  - Line 36 tells the portal server not to use any markup it may have cached  
    for the portlet.

  - Lines 37, 39, and 42 set appropriate metadata for the portlet markup.

  - Line 38 sets the actual markup as a string.

  - Line 40 tells the portal server that it does not need to fix up any
    URLs in the markup.

  - Line 41 tells the portal server not to cache the markup.

The main application might register the named utility in its
``if __name__ == '__main__':`` section:

.. code-block:: python

    provideUtility(DummyPortlet(), IPortlet, name='dummy')

or via ZCML:

.. code-block:: xml

   <utility
    name="dummy"
    provides="wsrplib.interfaces.IPortlet"
    factory=".dummy.DummyPortlet"/>


:class:`wsrplib.dummy.DummyServiceDescriptionInfo`
--------------------------------------------------

An instance of this class is intended to be registered as a utility providing
the :class:`wsrplib.interfaces.IServiceDescriptionInfo` interface:  it defines
"service-wide" properties.

The main application might register the utility in its
``if __name__ == '__main__':`` section:

.. code-block:: python

    provideUtility(DummyServiceDescriptionInfo(), IServiceDescriptionInfo)

or via ZCML:

.. code-block:: xml

   <utility
    provides="wsrplib.interfaces.IServiceDescriptionInfo"
    factory=".dummy.DummyServiceDescriptionInfo"/>
