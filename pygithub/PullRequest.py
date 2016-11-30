# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2012 Michael Stead <michael.stead@gmail.com>                       #
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

import pygithub.PullRequestMergeStatus
import pygithub.NamedUser
import pygithub.PullRequestPart
import pygithub.PullRequestComment
import pygithub.File
import pygithub.IssueComment
import pygithub.Commit


class PullRequest(pygithub.GithubObject.CompletableGithubObject):
    """
    This class represents PullRequests. The reference can be found here http://developer.github.com/v3/pulls/
    """

    @property
    def additions(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._additions)
        return self._additions.value

    @property
    def assignee(self):
        """
        :type: :class:`pygithub.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._assignee)
        return self._assignee.value

    @property
    def base(self):
        """
        :type: :class:`pygithub.PullRequestPart.PullRequestPart`
        """
        self._completeIfNotSet(self._base)
        return self._base.value

    @property
    def body(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._body)
        return self._body.value

    @property
    def changed_files(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._changed_files)
        return self._changed_files.value

    @property
    def closed_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._closed_at)
        return self._closed_at.value

    @property
    def comments(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._comments)
        return self._comments.value

    @property
    def comments_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._comments_url)
        return self._comments_url.value

    @property
    def commits(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._commits)
        return self._commits.value

    @property
    def commits_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._commits_url)
        return self._commits_url.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def deletions(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._deletions)
        return self._deletions.value

    @property
    def diff_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._diff_url)
        return self._diff_url.value

    @property
    def head(self):
        """
        :type: :class:`pygithub.PullRequestPart.PullRequestPart`
        """
        self._completeIfNotSet(self._head)
        return self._head.value

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def issue_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._issue_url)
        return self._issue_url.value

    @property
    def merge_commit_sha(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._merge_commit_sha)
        return self._merge_commit_sha.value

    @property
    def mergeable(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._mergeable)
        return self._mergeable.value

    @property
    def mergeable_state(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._mergeable_state)
        return self._mergeable_state.value

    @property
    def merged(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._merged)
        return self._merged.value

    @property
    def merged_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._merged_at)
        return self._merged_at.value

    @property
    def merged_by(self):
        """
        :type: :class:`pygithub.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._merged_by)
        return self._merged_by.value

    @property
    def milestone(self):
        """
        :type: :class:`pygithub.Milestone.Milestone`
        """
        self._completeIfNotSet(self._milestone)
        return self._milestone.value

    @property
    def number(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._number)
        return self._number.value

    @property
    def patch_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._patch_url)
        return self._patch_url.value

    @property
    def review_comment_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._review_comment_url)
        return self._review_comment_url.value

    @property
    def review_comments(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._review_comments)
        return self._review_comments.value

    @property
    def review_comments_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._review_comments_url)
        return self._review_comments_url.value

    @property
    def state(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._state)
        return self._state.value

    @property
    def title(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._title)
        return self._title.value

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

    @property
    def user(self):
        """
        :type: :class:`pygithub.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._user)
        return self._user.value

    def create_comment(self, body, commit_id, path, position):
        """
        :calls: `POST /repos/:owner/:repo/pulls/:number/comments <http://developer.github.com/v3/pulls/comments>`_
        :param body: string
        :param commit_id: :class:`pygithub.Commit.Commit`
        :param path: string
        :param position: integer
        :rtype: :class:`pygithub.PullRequestComment.PullRequestComment`
        """
        return self.create_review_comment(body, commit_id, path, position)

    def create_review_comment(self, body, commit_id, path, position):
        """
        :calls: `POST /repos/:owner/:repo/pulls/:number/comments <http://developer.github.com/v3/pulls/comments>`_
        :param body: string
        :param commit_id: :class:`pygithub.Commit.Commit`
        :param path: string
        :param position: integer
        :rtype: :class:`pygithub.PullRequestComment.PullRequestComment`
        """
        assert isinstance(body, (str, unicode)), body
        assert isinstance(commit_id, pygithub.Commit.Commit), commit_id
        assert isinstance(path, (str, unicode)), path
        assert isinstance(position, (int, long)), position
        post_parameters = {
            "body": body,
            "commit_id": commit_id._identity,
            "path": path,
            "position": position,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/comments",
            input=post_parameters
        )
        return pygithub.PullRequestComment.PullRequestComment(self._requester, headers, data, completed=True)

    def create_issue_comment(self, body):
        """
        :calls: `POST /repos/:owner/:repo/issues/:number/comments <http://developer.github.com/v3/issues/comments>`_
        :param body: string
        :rtype: :class:`pygithub.IssueComment.IssueComment`
        """
        assert isinstance(body, (str, unicode)), body
        post_parameters = {
            "body": body,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self._parentUrl(self._parentUrl(self.url)) + "/issues/" + str(self.number) + "/comments",
            input=post_parameters
        )
        return pygithub.IssueComment.IssueComment(self._requester, headers, data, completed=True)

    def edit(self, title=pygithub.GithubObject.NotSet, body=pygithub.GithubObject.NotSet, state=pygithub.GithubObject.NotSet):
        """
        :calls: `PATCH /repos/:owner/:repo/pulls/:number <http://developer.github.com/v3/pulls>`_
        :param title: string
        :param body: string
        :param state: string
        :rtype: None
        """
        assert title is pygithub.GithubObject.NotSet or isinstance(title, (str, unicode)), title
        assert body is pygithub.GithubObject.NotSet or isinstance(body, (str, unicode)), body
        assert state is pygithub.GithubObject.NotSet or isinstance(state, (str, unicode)), state
        post_parameters = dict()
        if title is not pygithub.GithubObject.NotSet:
            post_parameters["title"] = title
        if body is not pygithub.GithubObject.NotSet:
            post_parameters["body"] = body
        if state is not pygithub.GithubObject.NotSet:
            post_parameters["state"] = state
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=post_parameters
        )
        self._useAttributes(data)

    def get_comment(self, id):
        """
        :calls: `GET /repos/:owner/:repo/pulls/comments/:number <http://developer.github.com/v3/pulls/comments>`_
        :param id: integer
        :rtype: :class:`pygithub.PullRequestComment.PullRequestComment`
        """
        return self.get_review_comment(id)

    def get_review_comment(self, id):
        """
        :calls: `GET /repos/:owner/:repo/pulls/comments/:number <http://developer.github.com/v3/pulls/comments>`_
        :param id: integer
        :rtype: :class:`pygithub.PullRequestComment.PullRequestComment`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self._parentUrl(self.url) + "/comments/" + str(id)
        )
        return pygithub.PullRequestComment.PullRequestComment(self._requester, headers, data, completed=True)

    def get_comments(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/comments <http://developer.github.com/v3/pulls/comments>`_
        :rtype: :class:`pygithub.PaginatedList.PaginatedList` of :class:`pygithub.PullRequestComment.PullRequestComment`
        """
        return self.get_review_comments()

    def get_review_comments(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/comments <http://developer.github.com/v3/pulls/comments>`_
        :rtype: :class:`pygithub.PaginatedList.PaginatedList` of :class:`pygithub.PullRequestComment.PullRequestComment`
        """
        return pygithub.PaginatedList.PaginatedList(
            pygithub.PullRequestComment.PullRequestComment,
            self._requester,
            self.url + "/comments",
            None
        )

    def get_commits(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/commits <http://developer.github.com/v3/pulls>`_
        :rtype: :class:`pygithub.PaginatedList.PaginatedList` of :class:`pygithub.Commit.Commit`
        """
        return pygithub.PaginatedList.PaginatedList(
            pygithub.Commit.Commit,
            self._requester,
            self.url + "/commits",
            None
        )

    def get_files(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/files <http://developer.github.com/v3/pulls>`_
        :rtype: :class:`pygithub.PaginatedList.PaginatedList` of :class:`pygithub.File.File`
        """
        return pygithub.PaginatedList.PaginatedList(
            pygithub.File.File,
            self._requester,
            self.url + "/files",
            None
        )

    def get_issue_comment(self, id):
        """
        :calls: `GET /repos/:owner/:repo/issues/comments/:id <http://developer.github.com/v3/issues/comments>`_
        :param id: integer
        :rtype: :class:`pygithub.IssueComment.IssueComment`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self._parentUrl(self._parentUrl(self.url)) + "/issues/comments/" + str(id)
        )
        return pygithub.IssueComment.IssueComment(self._requester, headers, data, completed=True)

    def get_issue_comments(self):
        """
        :calls: `GET /repos/:owner/:repo/issues/:number/comments <http://developer.github.com/v3/issues/comments>`_
        :rtype: :class:`pygithub.PaginatedList.PaginatedList` of :class:`pygithub.IssueComment.IssueComment`
        """
        return pygithub.PaginatedList.PaginatedList(
            pygithub.IssueComment.IssueComment,
            self._requester,
            self._parentUrl(self._parentUrl(self.url)) + "/issues/" + str(self.number) + "/comments",
            None
        )

    def is_merged(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/merge <http://developer.github.com/v3/pulls>`_
        :rtype: bool
        """
        status, headers, data = self._requester.requestJson(
            "GET",
            self.url + "/merge"
        )
        return status == 204

    def merge(self, commit_message=pygithub.GithubObject.NotSet):
        """
        :calls: `PUT /repos/:owner/:repo/pulls/:number/merge <http://developer.github.com/v3/pulls>`_
        :param commit_message: string
        :rtype: :class:`pygithub.PullRequestMergeStatus.PullRequestMergeStatus`
        """
        assert commit_message is pygithub.GithubObject.NotSet or isinstance(commit_message, (str, unicode)), commit_message
        post_parameters = dict()
        if commit_message is not pygithub.GithubObject.NotSet:
            post_parameters["commit_message"] = commit_message
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            self.url + "/merge",
            input=post_parameters
        )
        return pygithub.PullRequestMergeStatus.PullRequestMergeStatus(self._requester, headers, data, completed=True)

    def _initAttributes(self):
        self._additions = pygithub.GithubObject.NotSet
        self._assignee = pygithub.GithubObject.NotSet
        self._base = pygithub.GithubObject.NotSet
        self._body = pygithub.GithubObject.NotSet
        self._changed_files = pygithub.GithubObject.NotSet
        self._closed_at = pygithub.GithubObject.NotSet
        self._comments = pygithub.GithubObject.NotSet
        self._comments_url = pygithub.GithubObject.NotSet
        self._commits = pygithub.GithubObject.NotSet
        self._commits_url = pygithub.GithubObject.NotSet
        self._created_at = pygithub.GithubObject.NotSet
        self._deletions = pygithub.GithubObject.NotSet
        self._diff_url = pygithub.GithubObject.NotSet
        self._head = pygithub.GithubObject.NotSet
        self._html_url = pygithub.GithubObject.NotSet
        self._id = pygithub.GithubObject.NotSet
        self._issue_url = pygithub.GithubObject.NotSet
        self._merge_commit_sha = pygithub.GithubObject.NotSet
        self._mergeable = pygithub.GithubObject.NotSet
        self._mergeable_state = pygithub.GithubObject.NotSet
        self._merged = pygithub.GithubObject.NotSet
        self._merged_at = pygithub.GithubObject.NotSet
        self._merged_by = pygithub.GithubObject.NotSet
        self._milestone = pygithub.GithubObject.NotSet
        self._number = pygithub.GithubObject.NotSet
        self._patch_url = pygithub.GithubObject.NotSet
        self._review_comment_url = pygithub.GithubObject.NotSet
        self._review_comments = pygithub.GithubObject.NotSet
        self._review_comments_url = pygithub.GithubObject.NotSet
        self._state = pygithub.GithubObject.NotSet
        self._title = pygithub.GithubObject.NotSet
        self._updated_at = pygithub.GithubObject.NotSet
        self._url = pygithub.GithubObject.NotSet
        self._user = pygithub.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "additions" in attributes:  # pragma no branch
            self._additions = self._makeIntAttribute(attributes["additions"])
        if "assignee" in attributes:  # pragma no branch
            self._assignee = self._makeClassAttribute(pygithub.NamedUser.NamedUser, attributes["assignee"])
        if "base" in attributes:  # pragma no branch
            self._base = self._makeClassAttribute(pygithub.PullRequestPart.PullRequestPart, attributes["base"])
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
        if "changed_files" in attributes:  # pragma no branch
            self._changed_files = self._makeIntAttribute(attributes["changed_files"])
        if "closed_at" in attributes:  # pragma no branch
            self._closed_at = self._makeDatetimeAttribute(attributes["closed_at"])
        if "comments" in attributes:  # pragma no branch
            self._comments = self._makeIntAttribute(attributes["comments"])
        if "comments_url" in attributes:  # pragma no branch
            self._comments_url = self._makeStringAttribute(attributes["comments_url"])
        if "commits" in attributes:  # pragma no branch
            self._commits = self._makeIntAttribute(attributes["commits"])
        if "commits_url" in attributes:  # pragma no branch
            self._commits_url = self._makeStringAttribute(attributes["commits_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "deletions" in attributes:  # pragma no branch
            self._deletions = self._makeIntAttribute(attributes["deletions"])
        if "diff_url" in attributes:  # pragma no branch
            self._diff_url = self._makeStringAttribute(attributes["diff_url"])
        if "head" in attributes:  # pragma no branch
            self._head = self._makeClassAttribute(pygithub.PullRequestPart.PullRequestPart, attributes["head"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "issue_url" in attributes:  # pragma no branch
            self._issue_url = self._makeStringAttribute(attributes["issue_url"])
        if "merge_commit_sha" in attributes:  # pragma no branch
            self._merge_commit_sha = self._makeStringAttribute(attributes["merge_commit_sha"])
        if "mergeable" in attributes:  # pragma no branch
            self._mergeable = self._makeBoolAttribute(attributes["mergeable"])
        if "mergeable_state" in attributes:  # pragma no branch
            self._mergeable_state = self._makeStringAttribute(attributes["mergeable_state"])
        if "merged" in attributes:  # pragma no branch
            self._merged = self._makeBoolAttribute(attributes["merged"])
        if "merged_at" in attributes:  # pragma no branch
            self._merged_at = self._makeDatetimeAttribute(attributes["merged_at"])
        if "merged_by" in attributes:  # pragma no branch
            self._merged_by = self._makeClassAttribute(pygithub.NamedUser.NamedUser, attributes["merged_by"])
        if "milestone" in attributes:  # pragma no branch
            self._milestone = self._makeClassAttribute(pygithub.Milestone.Milestone, attributes["milestone"])
        if "number" in attributes:  # pragma no branch
            self._number = self._makeIntAttribute(attributes["number"])
        if "patch_url" in attributes:  # pragma no branch
            self._patch_url = self._makeStringAttribute(attributes["patch_url"])
        if "review_comment_url" in attributes:  # pragma no branch
            self._review_comment_url = self._makeStringAttribute(attributes["review_comment_url"])
        if "review_comments" in attributes:  # pragma no branch
            self._review_comments = self._makeIntAttribute(attributes["review_comments"])
        if "review_comments_url" in attributes:  # pragma no branch
            self._review_comments_url = self._makeStringAttribute(attributes["review_comments_url"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "title" in attributes:  # pragma no branch
            self._title = self._makeStringAttribute(attributes["title"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(pygithub.NamedUser.NamedUser, attributes["user"])
