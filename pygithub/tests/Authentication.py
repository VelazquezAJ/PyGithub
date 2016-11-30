# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/          #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
# ##############################################################################

import Framework
import pygithub


class Authentication(Framework.BasicTestCase):
    def testNoAuthentication(self):
        g = pygithub.Github()
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    def testBasicAuthentication(self):
        g = pygithub.Github(self.login, self.password)
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    def testOAuthAuthentication(self):
        g = pygithub.Github(self.oauth_token)
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    # Warning: I don't have a scret key, so the requests for this test are forged
    def testSecretKeyAuthentication(self):
        g = pygithub.Github(client_id=self.client_id, client_secret=self.client_secret)
        self.assertListKeyEqual(g.get_organization("BeaverSoftware").get_repos("public"), lambda r: r.name, ["FatherBeaver", "PyGithub"])

    def testUserAgent(self):
        g = pygithub.Github(user_agent="PyGithubTester")
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    def testAuthorizationHeaderWithLogin(self):
        # See special case in Framework.fixAuthorizationHeader
        g = pygithub.Github("fake_login", "fake_password")
        try:
            g.get_user().name
        except pygithub.GithubException:
            pass

    def testAuthorizationHeaderWithToken(self):
        # See special case in Framework.fixAuthorizationHeader
        g = pygithub.Github("ZmFrZV9sb2dpbjpmYWtlX3Bhc3N3b3Jk")
        try:
            g.get_user().name
        except pygithub.GithubException:
            pass
