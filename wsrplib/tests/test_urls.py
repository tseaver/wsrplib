import unittest


class Test_rewritableURL(unittest.TestCase):

    def _callFUT(self, *args, **kw):
        from wsrplib.urls import rewritableURL
        return rewritableURL(*args, **kw)

    def _crackURL(self, url):
        PREFIX = 'wsrp_rewrite?'
        SUFFIX = '/wsrp_rewrite'
        self.failUnless(url.startswith(PREFIX))
        self.failUnless(url.endswith(SUFFIX))
        qs = url[len(PREFIX):-len(SUFFIX)]
        result = {}
        pairs = [x.split('=') for x in qs.split('&amp;')]
        self.assertEqual(pairs[0][0], 'wsrp-urlType')
        for name, value in pairs:
            self.failIf(name in result)
            result[name] = value
        return result

    def test_invalid_urlTYpe(self):
        self.assertRaises(ValueError, self._callFUT, 'nonesuch')

    def test_render_with_impossible_extra(self):
        from wsrplib.urls import RENDER
        self.assertRaises(ValueError, self._callFUT, RENDER,
                            resourceURL='http://example.com/resource.css')

    def test_render_no_extras(self):
        from wsrplib.urls import RENDER
        url = self._callFUT(RENDER)
        cracked = self._crackURL(url)
        self.assertEqual(cracked['wsrp-urlType'], RENDER)

    def test_render_w_extras(self):
        from wsrplib.urls import RENDER
        url = self._callFUT(RENDER,
                            navigationalState='/path/to/subfolder',
                            interactionState='DEADBEEF',
                            mode='wsrp:view',
                            windowState='wsrp:normal',
                            fragmentID='fragment',
                            secureURL=True,
                           )
        cracked = self._crackURL(url)
        self.assertEqual(cracked['wsrp-urlType'], RENDER)
        self.assertEqual(cracked['wsrp-navigationalState'],
                                 '%2Fpath%2Fto%2Fsubfolder')
        self.assertEqual(cracked['wsrp-interactionState'], 'DEADBEEF')
        self.assertEqual(cracked['wsrp-mode'], 'wsrp%3Aview')
        self.assertEqual(cracked['wsrp-windowState'], 'wsrp%3Anormal')
        self.assertEqual(cracked['wsrp-fragmentID'], 'fragment')
        self.assertEqual(cracked['wsrp-secureURL'], 'True')

    def test_blockingAction_with_impossible_extra(self):
        from wsrplib.urls import BLOCKING_ACTION
        self.assertRaises(ValueError, self._callFUT, BLOCKING_ACTION,
                            resourceURL='http://example.com/resource.css')

    def test_blockingAction_no_extras(self):
        from wsrplib.urls import BLOCKING_ACTION
        url = self._callFUT(BLOCKING_ACTION)
        cracked = self._crackURL(url)
        self.assertEqual(cracked['wsrp-urlType'], BLOCKING_ACTION)

    def test_resource_without_resourceURL(self):
        from wsrplib.urls import RESOURCE
        self.assertRaises(ValueError, self._callFUT, RESOURCE)

    def test_resource_with_resourceURL(self):
        from wsrplib.urls import RESOURCE
        url = self._callFUT(RESOURCE,
                            resourceURL='http://example.com/resource.css',
                           )
        cracked = self._crackURL(url)
        self.assertEqual(cracked['wsrp-urlType'], RESOURCE)
        self.assertEqual(cracked['wsrp-resourceURL'],
                                 'http%3A%2F%2Fexample.com%2Fresource.css')
        self.assertEqual(cracked['wsrp-resourceRequiresRewrite'], 'False')


class Test_rewrittenURL(unittest.TestCase):

    def _callFUT(self,
                 urlType, 
                 secure,
                 runtime_ctx,
                 portlet_ctx=None,
                 user_ctx=None,
                 **kw):
        from wsrplib.urls import rewrittenURL
        if portlet_ctx is None:
            portlet_ctx = Dummy(portletHandle='testing')
        if user_ctx is None:
            user_ctx = Dummy(userContextKey='user')
        return rewrittenURL(urlType, secure,
                            runtime_ctx, portlet_ctx, user_ctx, **kw)

    def _makeRuntimeContext(self,
                            portletInstanceKey='PIK',
                            namespacePrefix='pfx:',
                            sessionID='SESSION',
                            **templates
                           ):
        templates = DummyTemplates(**templates)
        return Dummy(portletInstanceKey='PIK',
                     namespacePrefix='pfx:',
                     sessionID='SESSION',
                     templates=templates,
                    )

    def test_invalid_urlTYpe(self):
        self.assertRaises(ValueError, self._callFUT, 'nonesuch', False, None)

    def test_render_with_impossible_extra(self):
        from wsrplib.urls import RENDER
        self.assertRaises(ValueError, self._callFUT, RENDER, False, None,
                            resourceURL='http://example.com/resource.css')

    def test_render_w_explicit_template_not_secure_required_values(self):
        from wsrplib.urls import RENDER
        TEMPLATE = ('http://example.com/render?'
                    'navstate={wsrp-navigationalState}&amp;'
                    'mode={wsrp-mode}&amp;'
                    'winstate={wsrp-windowState}&amp;'
                    'portlet={wsrp-portletHandle}&amp;'
                    'user={wsrp-userContextKey}&amp;'
                    'pinst={wsrp-portletInstanceKey}&amp;'
                    'session={wsrp-sessionID}'
                   )
        runtime_ctx = self._makeRuntimeContext(renderTemplate=TEMPLATE)

        url = self._callFUT(RENDER, False, runtime_ctx,
                            navigationalState='/path/to/subfolder',
                            mode='wsrp:view',
                            windowState='wsrp:normal',
                           )

        self.assertEqual(url, 'http://example.com/render?'
                              'navstate=%2Fpath%2Fto%2Fsubfolder&amp;'
                              'mode=wsrp%3Aview&amp;'
                              'winstate=wsrp%3Anormal&amp;'
                              'portlet=testing&amp;'
                              'user=user&amp;'
                              'pinst=PIK&amp;'
                              'session=SESSION')

    def test_render_w_explicit_template_secure_required_values(self):
        from wsrplib.urls import RENDER
        TEMPLATE = ('https://example.com/renderSecure?'
                    'navstate={wsrp-navigationalState}&amp;'
                    'mode={wsrp-mode}&amp;'
                    'winstate={wsrp-windowState}&amp;'
                    'portlet={wsrp-portletHandle}&amp;'
                    'user={wsrp-userContextKey}&amp;'
                    'pinst={wsrp-portletInstanceKey}&amp;'
                    'session={wsrp-sessionID}'
                   )
        runtime_ctx = self._makeRuntimeContext(secureRenderTemplate=TEMPLATE)

        url = self._callFUT(RENDER, True, runtime_ctx,
                            navigationalState='/path/to/subfolder',
                            mode='wsrp:view',
                            windowState='wsrp:normal',
                           )

        self.assertEqual(url, 'https://example.com/renderSecure?'
                              'navstate=%2Fpath%2Fto%2Fsubfolder&amp;'
                              'mode=wsrp%3Aview&amp;'
                              'winstate=wsrp%3Anormal&amp;'
                              'portlet=testing&amp;'
                              'user=user&amp;'
                              'pinst=PIK&amp;'
                              'session=SESSION')

    def test_render_w_default_template_not_secure_required_values(self):
        from wsrplib.urls import RENDER
        TEMPLATE = ('http://example.com/default?'
                    'navstate={wsrp-navigationalState}&amp;'
                    'mode={wsrp-mode}&amp;'
                    'winstate={wsrp-windowState}&amp;'
                    'portlet={wsrp-portletHandle}&amp;'
                    'user={wsrp-userContextKey}&amp;'
                    'pinst={wsrp-portletInstanceKey}&amp;'
                    'session={wsrp-sessionID}'
                   )
        runtime_ctx = self._makeRuntimeContext(defaultTemplate=TEMPLATE)

        url = self._callFUT(RENDER, False, runtime_ctx,
                            navigationalState='/path/to/subfolder',
                            mode='wsrp:view',
                            windowState='wsrp:normal',
                           )

        self.assertEqual(url, 'http://example.com/default?'
                              'navstate=%2Fpath%2Fto%2Fsubfolder&amp;'
                              'mode=wsrp%3Aview&amp;'
                              'winstate=wsrp%3Anormal&amp;'
                              'portlet=testing&amp;'
                              'user=user&amp;'
                              'pinst=PIK&amp;'
                              'session=SESSION')

    def test_render_w_default_template_secure_required_values(self):
        from wsrplib.urls import RENDER
        TEMPLATE = ('https://example.com/defaultSecure?'
                    'navstate={wsrp-navigationalState}&amp;'
                    'mode={wsrp-mode}&amp;'
                    'winstate={wsrp-windowState}&amp;'
                    'portlet={wsrp-portletHandle}&amp;'
                    'user={wsrp-userContextKey}&amp;'
                    'pinst={wsrp-portletInstanceKey}&amp;'
                    'session={wsrp-sessionID}'
                   )
        runtime_ctx = self._makeRuntimeContext(secureDefaultTemplate=TEMPLATE)

        url = self._callFUT(RENDER, True, runtime_ctx,
                            navigationalState='/path/to/subfolder',
                            mode='wsrp:view',
                            windowState='wsrp:normal',
                           )

        self.assertEqual(url, 'https://example.com/defaultSecure?'
                              'navstate=%2Fpath%2Fto%2Fsubfolder&amp;'
                              'mode=wsrp%3Aview&amp;'
                              'winstate=wsrp%3Anormal&amp;'
                              'portlet=testing&amp;'
                              'user=user&amp;'
                              'pinst=PIK&amp;'
                              'session=SESSION')

    def test_blockingAction_with_impossible_extra(self):
        from wsrplib.urls import BLOCKING_ACTION
        self.assertRaises(ValueError, self._callFUT,
                            BLOCKING_ACTION, False, None,
                            resourceURL='http://example.com/resource.css')

    def test_blockingAction_w_explicit_template_not_secure_required_vals(self):
        from wsrplib.urls import BLOCKING_ACTION
        TEMPLATE = ('http://example.com/blockingAction?'
                    'navstate={wsrp-navigationalState}&amp;'
                    'mode={wsrp-mode}&amp;'
                    'winstate={wsrp-windowState}&amp;'
                    'portlet={wsrp-portletHandle}&amp;'
                    'user={wsrp-userContextKey}&amp;'
                    'pinst={wsrp-portletInstanceKey}&amp;'
                    'session={wsrp-sessionID}'
                   )
        runtime_ctx = self._makeRuntimeContext(blockingActionTemplate=TEMPLATE)

        url = self._callFUT(BLOCKING_ACTION, False, runtime_ctx,
                            navigationalState='/path/to/subfolder',
                            mode='wsrp:view',
                            windowState='wsrp:normal',
                           )

        self.assertEqual(url, 'http://example.com/blockingAction?'
                              'navstate=%2Fpath%2Fto%2Fsubfolder&amp;'
                              'mode=wsrp%3Aview&amp;'
                              'winstate=wsrp%3Anormal&amp;'
                              'portlet=testing&amp;'
                              'user=user&amp;'
                              'pinst=PIK&amp;'
                              'session=SESSION')

    def test_blockingAction_w_explicit_template_secure_required_values(self):
        from wsrplib.urls import BLOCKING_ACTION
        TEMPLATE = ('https://example.com/blockingActionSecure?'
                    'navstate={wsrp-navigationalState}&amp;'
                    'mode={wsrp-mode}&amp;'
                    'winstate={wsrp-windowState}&amp;'
                    'portlet={wsrp-portletHandle}&amp;'
                    'user={wsrp-userContextKey}&amp;'
                    'pinst={wsrp-portletInstanceKey}&amp;'
                    'session={wsrp-sessionID}'
                   )
        runtime_ctx = self._makeRuntimeContext(
                                secureBlockingActionTemplate=TEMPLATE)

        url = self._callFUT(BLOCKING_ACTION, True, runtime_ctx,
                            navigationalState='/path/to/subfolder',
                            mode='wsrp:view',
                            windowState='wsrp:normal',
                           )

        self.assertEqual(url, 'https://example.com/blockingActionSecure?'
                              'navstate=%2Fpath%2Fto%2Fsubfolder&amp;'
                              'mode=wsrp%3Aview&amp;'
                              'winstate=wsrp%3Anormal&amp;'
                              'portlet=testing&amp;'
                              'user=user&amp;'
                              'pinst=PIK&amp;'
                              'session=SESSION')

    def test_blockingAction_w_default_template_not_secure_required_values(self):
        from wsrplib.urls import BLOCKING_ACTION
        TEMPLATE = ('http://example.com/default?'
                    'navstate={wsrp-navigationalState}&amp;'
                    'mode={wsrp-mode}&amp;'
                    'winstate={wsrp-windowState}&amp;'
                    'portlet={wsrp-portletHandle}&amp;'
                    'user={wsrp-userContextKey}&amp;'
                    'pinst={wsrp-portletInstanceKey}&amp;'
                    'session={wsrp-sessionID}'
                   )
        runtime_ctx = self._makeRuntimeContext(defaultTemplate=TEMPLATE)

        url = self._callFUT(BLOCKING_ACTION, False, runtime_ctx,
                            navigationalState='/path/to/subfolder',
                            mode='wsrp:view',
                            windowState='wsrp:normal',
                           )

        self.assertEqual(url, 'http://example.com/default?'
                              'navstate=%2Fpath%2Fto%2Fsubfolder&amp;'
                              'mode=wsrp%3Aview&amp;'
                              'winstate=wsrp%3Anormal&amp;'
                              'portlet=testing&amp;'
                              'user=user&amp;'
                              'pinst=PIK&amp;'
                              'session=SESSION')

    def test_blockingAction_w_default_template_secure_required_values(self):
        from wsrplib.urls import BLOCKING_ACTION
        TEMPLATE = ('https://example.com/defaultSecure?'
                    'navstate={wsrp-navigationalState}&amp;'
                    'mode={wsrp-mode}&amp;'
                    'winstate={wsrp-windowState}&amp;'
                    'portlet={wsrp-portletHandle}&amp;'
                    'user={wsrp-userContextKey}&amp;'
                    'pinst={wsrp-portletInstanceKey}&amp;'
                    'session={wsrp-sessionID}'
                   )
        runtime_ctx = self._makeRuntimeContext(secureDefaultTemplate=TEMPLATE)

        url = self._callFUT(BLOCKING_ACTION, True, runtime_ctx,
                            navigationalState='/path/to/subfolder',
                            mode='wsrp:view',
                            windowState='wsrp:normal',
                           )

        self.assertEqual(url, 'https://example.com/defaultSecure?'
                              'navstate=%2Fpath%2Fto%2Fsubfolder&amp;'
                              'mode=wsrp%3Aview&amp;'
                              'winstate=wsrp%3Anormal&amp;'
                              'portlet=testing&amp;'
                              'user=user&amp;'
                              'pinst=PIK&amp;'
                              'session=SESSION')

    def test_resource_without_resourceURL(self):
        from wsrplib.urls import RESOURCE
        self.assertRaises(ValueError, self._callFUT, RESOURCE, False, None)

    def test_resource_w_explicit_template_not_secure_required_values(self):
        from wsrplib.urls import RESOURCE
        TEMPLATE = ('http://example.com/resource?'
                    'navstate={wsrp-navigationalState}&amp;'
                    'mode={wsrp-mode}&amp;'
                    'winstate={wsrp-windowState}&amp;'
                    'portlet={wsrp-portletHandle}&amp;'
                    'user={wsrp-userContextKey}&amp;'
                    'pinst={wsrp-portletInstanceKey}&amp;'
                    'session={wsrp-sessionID}&amp;'
                    'resurl={wsrp-resourceURL}&amp;'
                    'rewrite={wsrp-resourceRequiresRewrite}'
                   )
        runtime_ctx = self._makeRuntimeContext(resourceTemplate=TEMPLATE)

        url = self._callFUT(RESOURCE, False, runtime_ctx,
                            navigationalState='/path/to/subfolder',
                            mode='wsrp:view',
                            windowState='wsrp:normal',
                            resourceURL='http://example.com/resource.css',
                           )

        self.assertEqual(url, 'http://example.com/resource?'
                              'navstate=%2Fpath%2Fto%2Fsubfolder&amp;'
                              'mode=wsrp%3Aview&amp;'
                              'winstate=wsrp%3Anormal&amp;'
                              'portlet=testing&amp;'
                              'user=user&amp;'
                              'pinst=PIK&amp;'
                              'session=SESSION&amp;'
                              'resurl=http%3A%2F%2Fexample.com'
                                      '%2Fresource.css&amp;'
                              'rewrite=False')

    def test_resource_w_explicit_template_secure_required_values(self):
        from wsrplib.urls import RESOURCE
        TEMPLATE = ('https://example.com/resourceSecure?'
                    'navstate={wsrp-navigationalState}&amp;'
                    'mode={wsrp-mode}&amp;'
                    'winstate={wsrp-windowState}&amp;'
                    'portlet={wsrp-portletHandle}&amp;'
                    'user={wsrp-userContextKey}&amp;'
                    'pinst={wsrp-portletInstanceKey}&amp;'
                    'session={wsrp-sessionID}&amp;'
                    'resurl={wsrp-resourceURL}&amp;'
                    'rewrite={wsrp-resourceRequiresRewrite}'
                   )
        runtime_ctx = self._makeRuntimeContext(
                                secureResourceTemplate=TEMPLATE)

        url = self._callFUT(RESOURCE, True, runtime_ctx,
                            navigationalState='/path/to/subfolder',
                            mode='wsrp:view',
                            windowState='wsrp:normal',
                            resourceURL='http://example.com/resource.css',
                           )

        self.assertEqual(url, 'https://example.com/resourceSecure?'
                              'navstate=%2Fpath%2Fto%2Fsubfolder&amp;'
                              'mode=wsrp%3Aview&amp;'
                              'winstate=wsrp%3Anormal&amp;'
                              'portlet=testing&amp;'
                              'user=user&amp;'
                              'pinst=PIK&amp;'
                              'session=SESSION&amp;'
                              'resurl=http%3A%2F%2Fexample.com'
                                      '%2Fresource.css&amp;'
                              'rewrite=False')

    def test_resource_w_default_template_not_secure_required_values(self):
        from wsrplib.urls import RESOURCE
        TEMPLATE = ('http://example.com/default?'
                    'navstate={wsrp-navigationalState}&amp;'
                    'mode={wsrp-mode}&amp;'
                    'winstate={wsrp-windowState}&amp;'
                    'portlet={wsrp-portletHandle}&amp;'
                    'user={wsrp-userContextKey}&amp;'
                    'pinst={wsrp-portletInstanceKey}&amp;'
                    'session={wsrp-sessionID}'
                    'resurl={wsrp-resourceURL}&amp;'
                    'rewrite={wsrp-resourceRequiresRewrite}'
                   )
        runtime_ctx = self._makeRuntimeContext(defaultTemplate=TEMPLATE)

        url = self._callFUT(RESOURCE, False, runtime_ctx,
                            navigationalState='/path/to/subfolder',
                            mode='wsrp:view',
                            windowState='wsrp:normal',
                            resourceURL='http://example.com/resource.css',
                           )

        self.assertEqual(url, 'http://example.com/default?'
                              'navstate=%2Fpath%2Fto%2Fsubfolder&amp;'
                              'mode=wsrp%3Aview&amp;'
                              'winstate=wsrp%3Anormal&amp;'
                              'portlet=testing&amp;'
                              'user=user&amp;'
                              'pinst=PIK&amp;'
                              'session=SESSION'
                              'resurl=http%3A%2F%2Fexample.com'
                                      '%2Fresource.css&amp;'
                              'rewrite=False')

    def test_resource_w_default_template_secure_required_values(self):
        from wsrplib.urls import RESOURCE
        TEMPLATE = ('https://example.com/defaultSecure?'
                    'navstate={wsrp-navigationalState}&amp;'
                    'mode={wsrp-mode}&amp;'
                    'winstate={wsrp-windowState}&amp;'
                    'portlet={wsrp-portletHandle}&amp;'
                    'user={wsrp-userContextKey}&amp;'
                    'pinst={wsrp-portletInstanceKey}&amp;'
                    'session={wsrp-sessionID}'
                    'resurl={wsrp-resourceURL}&amp;'
                    'rewrite={wsrp-resourceRequiresRewrite}'
                   )
        runtime_ctx = self._makeRuntimeContext(secureDefaultTemplate=TEMPLATE)

        url = self._callFUT(RESOURCE, True, runtime_ctx,
                            navigationalState='/path/to/subfolder',
                            mode='wsrp:view',
                            windowState='wsrp:normal',
                            resourceURL='http://example.com/resource.css',
                           )

        self.assertEqual(url, 'https://example.com/defaultSecure?'
                              'navstate=%2Fpath%2Fto%2Fsubfolder&amp;'
                              'mode=wsrp%3Aview&amp;'
                              'winstate=wsrp%3Anormal&amp;'
                              'portlet=testing&amp;'
                              'user=user&amp;'
                              'pinst=PIK&amp;'
                              'session=SESSION'
                              'resurl=http%3A%2F%2Fexample.com'
                                      '%2Fresource.css&amp;'
                              'rewrite=False')


class Dummy(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)


class DummyTemplates(Dummy):
    renderTemplate = None
    secureRenderTemplate = None
    blockingActionTemplate = None
    secureBlockingActionTemplate = None
    resourceTemplate = None
    secureResourceTemplate = None
    defaultTemplate = None
    secureDefaultTemplate = None
