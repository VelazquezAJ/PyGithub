# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
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
import pygithub.PaginatedList

import pygithub.GitCommit
import pygithub.NamedUser
import pygithub.CommitStatus
import pygithub.File
import pygithub.CommitStats
import pygithub.CommitComment


class Commit(pygithub.GithubObject.CompletableGithubObject):
    """
    This class represents Commits. The reference can be found here http://developer.github.com/v3/git/commits/
    """

    @property
    def author(self):
        """
        :type: :class:`pygithub.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._author)
        return self._author.value

    @property
    def comments_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._comments_url)
        return self._comments_url.value

    @property
    def commit(self):
        """
        :type: :class:`pygithub.GitCommit.GitCommit`
        """
        self._completeIfNotSet(self._commit)
        return self._commit.value

    @property
    def committer(self):
        """
        :type: :class:`pygithub.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._committer)
        return self._committer.value

    @property
    def files(self):
        """
        :type: list of :class:`pygithub.File.File`
        """
        self._completeIfNotSet(self._files)
        return self._files.value

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def parents(self):
        """
        :type: list of :class:`pygithub.Commit.Commit`
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
    def stats(self):
        """
        :type: :class:`pygithub.CommitStats.CommitStats`
        """
        self._completeIfNotSet(self._stats)
        return self._stats.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    def create_comment(self, body, line=pygithub.GithubObject.NotSet, path=pygithub.GithubObject.NotSet, position=pygithub.GithubObject.NotSet):
        """
        :calls: `POST /repos/:owner/:repo/commits/:sha/comments <http://developer.github.com/v3/repos/comments>`_
        :param body: string
        :param line: integer
        :param path: string
        :param position: integer
        :rtype: :class:`pygithub.CommitComment.CommitComment`
        """
        assert isinstance(body, (str, unicode)), body
        assert line is pygithub.GithubObject.NotSet or isinstance(line, (int, long)), line
        assert path is pygithub.GithubObject.NotSet or isinstance(path, (str, unicode)), path
        assert position is pygithub.GithubObject.NotSet or isinstance(position, (int, long)), position
        post_parameters = {
            "body": body,
        }
        if line is not pygithub.GithubObject.NotSet:
            post_parameters["line"] = line
        if path is not pygithub.GithubObject.NotSet:
            post_parameters["path"] = path
        if position is not pygithub.GithubObject.NotSet:
            post_parameters["position"] = position
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/comments",
            input=post_parameters
        )
        return pygithub.CommitComment.CommitComment(self._requester, headers, data, completed=True)

    def create_status(self, state, target_url=pygithub.GithubObject.NotSet, description=pygithub.GithubObject.NotSet):
        """
        :calls: `POST /repos/:owner/:repo/statuses/:sha <http://developer.github.com/v3/repos/statuses>`_
        :param state: string
        :param target_url: string
        :param description: string
        :rtype: :class:`pygithub.CommitStatus.CommitStatus`
        """
        assert isinstance(state, (str, unicode)), state
        assert target_url is pygithub.GithubObject.NotSet or isinstance(target_url, (str, unicode)), target_url
        assert description is pygithub.GithubObject.NotSet or isinstance(description, (str, unicode)), description
        post_parameters = {
            "state": state,
        }
        if target_url is not pygithub.GithubObject.NotSet:
            post_parameters["target_url"] = target_url
        if description is not pygithub.GithubObject.NotSet:
            post_parameters["description"] = description
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self._parentUrl(self._parentUrl(self.url)) + "/statuses/" + self.sha,
            input=post_parameters
        )
        return pygithub.CommitStatus.CommitStatus(self._requester, headers, data, completed=True)

    def get_comments(self):
        """
        :calls: `GET /repos/:owner/:repo/commits/:sha/comments <http://developer.github.com/v3/repos/comments>`_
        :rtype: :class:`pygithub.PaginatedList.PaginatedList` of :class:`pygithub.CommitComment.CommitComment`
        """
        return pygithub.PaginatedList.PaginatedList(
            pygithub.CommitComment.CommitComment,
            self._requester,
            self.url + "/comments",
            None
        )

    def get_statuses(self):
        """
        :calls: `GET /repos/:owner/:repo/statuses/:ref <http://developer.github.com/v3/repos/statuses>`_
        :rtype: :class:`pygithub.PaginatedList.PaginatedList` of :class:`pygithub.CommitStatus.CommitStatus`
        """
        return pygithub.PaginatedList.PaginatedList(
            pygithub.CommitStatus.CommitStatus,
            self._requester,
            self._parentUrl(self._parentUrl(self.url)) + "/statuses/" + self.sha,
            None
        )

    @property
    def _identity(self):
        return self.sha

    def _initAttributes(self):
        self._author = pygithub.GithubObject.NotSet
        self._comments_url = pygithub.GithubObject.NotSet
        self._commit = pygithub.GithubObject.NotSet
        self._committer = pygithub.GithubObject.NotSet
        self._files = pygithub.GithubObject.NotSet
        self._html_url = pygithub.GithubObject.NotSet
        self._parents = pygithub.GithubObject.NotSet
        self._sha = pygithub.GithubObject.NotSet
        self._stats = pygithub.GithubObject.NotSet
        self._url = pygithub.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "author" in attributes:  # pragma no branch
            self._author = self._makeClassAttribute(pygithub.NamedUser.NamedUser, attributes["author"])
        if "comments_url" in attributes:  # pragma no branch
            self._comments_url = self._makeStringAttribute(attributes["comments_url"])
        if "commit" in attributes:  # pragma no branch
            self._commit = self._makeClassAttribute(pygithub.GitCommit.GitCommit, attributes["commit"])
        if "committer" in attributes:  # pragma no branch
            self._committer = self._makeClassAttribute(pygithub.NamedUser.NamedUser, attributes["committer"])
        if "files" in attributes:  # pragma no branch
            self._files = self._makeListOfClassesAttribute(pygithub.File.File, attributes["files"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "parents" in attributes:  # pragma no branch
            self._parents = self._makeListOfClassesAttribute(Commit, attributes["parents"])
        if "sha" in attributes:  # pragma no branch
            self._sha = self._makeStringAttribute(attributes["sha"])
        if "stats" in attributes:  # pragma no branch
            self._stats = self._makeClassAttribute(pygithub.CommitStats.CommitStats, attributes["stats"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
