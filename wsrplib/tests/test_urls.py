import unittest

class Test_generateConsumerRewritableURL(unittest.TestCase):

    def _callFUT(self, *args, **kw):
        from wsrplib.urls import generateConsumerRewritableURL
        return generateConsumerRewritableURL(*args, **kw)

    def _crackURL(self, url):
        PREFIX = 'wsrp_rewrite?'
        SUFFIX = '/wsrp_rewrite'
        self.failUnless(url.startswith(PREFIX))
        self.failUnless(url.endswith(SUFFIX))
        qs = url[len(PREFIX):-len(SUFFIX)]
        if '&amp;' in qs:
            amp = '&amp;'
        else:
            amp = '&';
        result = {}
        pairs = [x.split('=') for x in qs.split(amp)]
        self.assertEqual(pairs[0][0], 'wsrp-urlType')
        for name, value in pairs:
            self.failIf(name in result)
            result[name] = value
        return result

    def test_invalid_urlTYpe(self):
        self.assertRaises(ValueError, self._callFUT, 'nonesuch')

    def test_render_no_extras(self):
        from wsrplib.urls import RENDER
        url = self._callFUT(RENDER)
        cracked = self._crackURL(url)
        self.assertEqual(cracked['wsrp-urlType'], RENDER)

    def test_render_with_impossible_extra(self):
        from wsrplib.urls import RENDER
        self.assertRaises(ValueError, self._callFUT, RENDER,
                            resourceURL='http://example.com/resource.css')

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
