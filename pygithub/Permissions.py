# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
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

import pygithub.GithubObject


class Permissions(pygithub.GithubObject.NonCompletableGithubObject):
    """
    This class represents Permissionss as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def admin(self):
        """
        :type: bool
        """
        return self._admin.value

    @property
    def pull(self):
        """
        :type: bool
        """
        return self._pull.value

    @property
    def push(self):
        """
        :type: bool
        """
        return self._push.value

    def _initAttributes(self):
        self._admin = pygithub.GithubObject.NotSet
        self._pull = pygithub.GithubObject.NotSet
        self._push = pygithub.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "admin" in attributes:  # pragma no branch
            self._admin = self._makeBoolAttribute(attributes["admin"])
        if "pull" in attributes:  # pragma no branch
            self._pull = self._makeBoolAttribute(attributes["pull"])
        if "push" in attributes:  # pragma no branch
            self._push = self._makeBoolAttribute(attributes["push"])
