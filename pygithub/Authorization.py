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

import pygithub.AuthorizationApplication


class Authorization(pygithub.GithubObject.CompletableGithubObject):
    """
    This class represents Authorizations as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def app(self):
        """
        :type: :class:`pygithub.AuthorizationApplication.AuthorizationApplication`
        """
        self._completeIfNotSet(self._app)
        return self._app.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def note(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._note)
        return self._note.value

    @property
    def note_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._note_url)
        return self._note_url.value

    @property
    def scopes(self):
        """
        :type: list of string
        """
        self._completeIfNotSet(self._scopes)
        return self._scopes.value

    @property
    def token(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._token)
        return self._token.value

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    def delete(self):
        """
        :calls: `DELETE /authorizations/:id <http://developer.github.com/v3/oauth>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url
        )

    def edit(self, scopes=pygithub.GithubObject.NotSet, add_scopes=pygithub.GithubObject.NotSet, remove_scopes=pygithub.GithubObject.NotSet, note=pygithub.GithubObject.NotSet, note_url=pygithub.GithubObject.NotSet):
        """
        :calls: `PATCH /authorizations/:id <http://developer.github.com/v3/oauth>`_
        :param scopes: list of string
        :param add_scopes: list of string
        :param remove_scopes: list of string
        :param note: string
        :param note_url: string
        :rtype: None
        """
        assert scopes is pygithub.GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in scopes), scopes
        assert add_scopes is pygithub.GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in add_scopes), add_scopes
        assert remove_scopes is pygithub.GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in remove_scopes), remove_scopes
        assert note is pygithub.GithubObject.NotSet or isinstance(note, (str, unicode)), note
        assert note_url is pygithub.GithubObject.NotSet or isinstance(note_url, (str, unicode)), note_url
        post_parameters = dict()
        if scopes is not pygithub.GithubObject.NotSet:
            post_parameters["scopes"] = scopes
        if add_scopes is not pygithub.GithubObject.NotSet:
            post_parameters["add_scopes"] = add_scopes
        if remove_scopes is not pygithub.GithubObject.NotSet:
            post_parameters["remove_scopes"] = remove_scopes
        if note is not pygithub.GithubObject.NotSet:
            post_parameters["note"] = note
        if note_url is not pygithub.GithubObject.NotSet:
            post_parameters["note_url"] = note_url
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=post_parameters
        )
        self._useAttributes(data)

    def _initAttributes(self):
        self._app = pygithub.GithubObject.NotSet
        self._created_at = pygithub.GithubObject.NotSet
        self._id = pygithub.GithubObject.NotSet
        self._note = pygithub.GithubObject.NotSet
        self._note_url = pygithub.GithubObject.NotSet
        self._scopes = pygithub.GithubObject.NotSet
        self._token = pygithub.GithubObject.NotSet
        self._updated_at = pygithub.GithubObject.NotSet
        self._url = pygithub.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "app" in attributes:  # pragma no branch
            self._app = self._makeClassAttribute(pygithub.AuthorizationApplication.AuthorizationApplication, attributes["app"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "note" in attributes:  # pragma no branch
            self._note = self._makeStringAttribute(attributes["note"])
        if "note_url" in attributes:  # pragma no branch
            self._note_url = self._makeStringAttribute(attributes["note_url"])
        if "scopes" in attributes:  # pragma no branch
            self._scopes = self._makeListOfStringsAttribute(attributes["scopes"])
        if "token" in attributes:  # pragma no branch
            self._token = self._makeStringAttribute(attributes["token"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
