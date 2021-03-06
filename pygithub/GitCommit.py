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

import pygithub.GitAuthor
import pygithub.GitTree


class GitCommit(pygithub.GithubObject.CompletableGithubObject):
    """
    This class represents GitCommits as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def author(self):
        """
        :type: :class:`pygithub.GitAuthor.GitAuthor`
        """
        self._completeIfNotSet(self._author)
        return self._author.value

    @property
    def committer(self):
        """
        :type: :class:`pygithub.GitAuthor.GitAuthor`
        """
        self._completeIfNotSet(self._committer)
        return self._committer.value

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def message(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._message)
        return self._message.value

    @property
    def parents(self):
        """
        :type: list of :class:`pygithub.GitCommit.GitCommit`
        """
        self._completeIfNotSet(self._parents)
        return self._parents.value

    @property
    def sha(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._sha)
        return self._sha.value

    @property
    def tree(self):
        """
        :type: :class:`pygithub.GitTree.GitTree`
        """
        self._completeIfNotSet(self._tree)
        return self._tree.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def _identity(self):
        return self.sha

    def _initAttributes(self):
        self._author = pygithub.GithubObject.NotSet
        self._committer = pygithub.GithubObject.NotSet
        self._html_url = pygithub.GithubObject.NotSet
        self._message = pygithub.GithubObject.NotSet
        self._parents = pygithub.GithubObject.NotSet
        self._sha = pygithub.GithubObject.NotSet
        self._tree = pygithub.GithubObject.NotSet
        self._url = pygithub.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "author" in attributes:  # pragma no branch
            self._author = self._makeClassAttribute(pygithub.GitAuthor.GitAuthor, attributes["author"])
        if "committer" in attributes:  # pragma no branch
            self._committer = self._makeClassAttribute(pygithub.GitAuthor.GitAuthor, attributes["committer"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "message" in attributes:  # pragma no branch
            self._message = self._makeStringAttribute(attributes["message"])
        if "parents" in attributes:  # pragma no branch
            self._parents = self._makeListOfClassesAttribute(GitCommit, attributes["parents"])
        if "sha" in attributes:  # pragma no branch
            self._sha = self._makeStringAttribute(attributes["sha"])
        if "tree" in attributes:  # pragma no branch
            self._tree = self._makeClassAttribute(pygithub.GitTree.GitTree, attributes["tree"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
