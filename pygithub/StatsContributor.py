# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
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

import pygithub.NamedUser


class StatsContributor(pygithub.GithubObject.NonCompletableGithubObject):
    """
    This class represents statistics of a contibutor. The reference can be found here http://developer.github.com/v3/repos/statistics/#get-contributors-list-with-additions-deletions-and-commit-counts
    """

    class Week(pygithub.GithubObject.NonCompletableGithubObject):
        """
        This class represents weekly statistics of a contibutor.
        """

        @property
        def w(self):
            """
            :type: datetime.datetime
            """
            return self._w.value

        @property
        def a(self):
            """
            :type: int
            """
            return self._a.value

        @property
        def d(self):
            """
            :type: int
            """
            return self._d.value

        @property
        def c(self):
            """
            :type: int
            """
            return self._c.value

        def _initAttributes(self):
            self._w = pygithub.GithubObject.NotSet
            self._a = pygithub.GithubObject.NotSet
            self._d = pygithub.GithubObject.NotSet
            self._c = pygithub.GithubObject.NotSet

        def _useAttributes(self, attributes):
            if "w" in attributes:  # pragma no branch
                self._w = self._makeTimestampAttribute(attributes["w"])
            if "a" in attributes:  # pragma no branch
                self._a = self._makeIntAttribute(attributes["a"])
            if "d" in attributes:  # pragma no branch
                self._d = self._makeIntAttribute(attributes["d"])
            if "c" in attributes:  # pragma no branch
                self._c = self._makeIntAttribute(attributes["c"])

    @property
    def author(self):
        """
        :type: :class:`pygithub.NamedUser.NamedUser`
        """
        return self._author.value

    @property
    def total(self):
        """
        :type: int
        """
        return self._total.value

    @property
    def weeks(self):
        """
        :type: list of :class:`.Week`
        """
        return self._weeks.value

    def _initAttributes(self):
        self._author = pygithub.GithubObject.NotSet
        self._total = pygithub.GithubObject.NotSet
        self._weeks = pygithub.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "author" in attributes:  # pragma no branch
            self._author = self._makeClassAttribute(pygithub.NamedUser.NamedUser, attributes["author"])
        if "total" in attributes:  # pragma no branch
            self._total = self._makeIntAttribute(attributes["total"])
        if "weeks" in attributes:  # pragma no branch
            self._weeks = self._makeListOfClassesAttribute(self.Week, attributes["weeks"])
