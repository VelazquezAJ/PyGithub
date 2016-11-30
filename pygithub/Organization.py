# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2012 Steve English <steve.english@navetas.com>                     #
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

import datetime

import pygithub.GithubObject
import pygithub.PaginatedList

import pygithub.Plan
import pygithub.Team
import pygithub.Event
import pygithub.Repository
import pygithub.NamedUser


class Organization(pygithub.GithubObject.CompletableGithubObject):
    """
    This class represents Organizations. The reference can be found here http://developer.github.com/v3/orgs/
    """

    @property
    def avatar_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._avatar_url)
        return self._avatar_url.value

    @property
    def billing_email(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._billing_email)
        return self._billing_email.value

    @property
    def blog(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._blog)
        return self._blog.value

    @property
    def collaborators(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._collaborators)
        return self._collaborators.value

    @property
    def company(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._company)
        return self._company.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def disk_usage(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._disk_usage)
        return self._disk_usage.value

    @property
    def email(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._email)
        return self._email.value

    @property
    def events_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._events_url)
        return self._events_url.value

    @property
    def followers(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._followers)
        return self._followers.value

    @property
    def following(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._following)
        return self._following.value

    @property
    def gravatar_id(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._gravatar_id)
        return self._gravatar_id.value

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
    def location(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._location)
        return self._location.value

    @property
    def login(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._login)
        return self._login.value

    @property
    def members_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._members_url)
        return self._members_url.value

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def owned_private_repos(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._owned_private_repos)
        return self._owned_private_repos.value

    @property
    def plan(self):
        """
        :type: :class:`pygithub.Plan.Plan`
        """
        self._completeIfNotSet(self._plan)
        return self._plan.value

    @property
    def private_gists(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._private_gists)
        return self._private_gists.value

    @property
    def public_gists(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._public_gists)
        return self._public_gists.value

    @property
    def public_members_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._public_members_url)
        return self._public_members_url.value

    @property
    def public_repos(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._public_repos)
        return self._public_repos.value

    @property
    def repos_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._repos_url)
        return self._repos_url.value

    @property
    def total_private_repos(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._total_private_repos)
        return self._total_private_repos.value

    @property
    def type(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._type)
        return self._type.value

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

    def add_to_public_members(self, public_member):
        """
        :calls: `PUT /orgs/:org/public_members/:user <http://developer.github.com/v3/orgs/members>`_
        :param public_member: :class:`pygithub.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(public_member, pygithub.NamedUser.NamedUser), public_member
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            self.url + "/public_members/" + public_member._identity
        )

    def create_fork(self, repo):
        """
        :calls: `POST /repos/:owner/:repo/forks <http://developer.github.com/v3/repos/forks>`_
        :param repo: :class:`pygithub.Repository.Repository`
        :rtype: :class:`pygithub.Repository.Repository`
        """
        assert isinstance(repo, pygithub.Repository.Repository), repo
        url_parameters = {
            "org": self.login,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "/repos/" + repo.owner.login + "/" + repo.name + "/forks",
            parameters=url_parameters
        )
        return pygithub.Repository.Repository(self._requester, headers, data, completed=True)

    def create_repo(self, name, description=pygithub.GithubObject.NotSet, homepage=pygithub.GithubObject.NotSet, private=pygithub.GithubObject.NotSet, has_issues=pygithub.GithubObject.NotSet, has_wiki=pygithub.GithubObject.NotSet, has_downloads=pygithub.GithubObject.NotSet, team_id=pygithub.GithubObject.NotSet, auto_init=pygithub.GithubObject.NotSet, gitignore_template=pygithub.GithubObject.NotSet):
        """
        :calls: `POST /orgs/:org/repos <http://developer.github.com/v3/repos>`_
        :param name: string
        :param description: string
        :param homepage: string
        :param private: bool
        :param has_issues: bool
        :param has_wiki: bool
        :param has_downloads: bool
        :param team_id: :class:`pygithub.Team.Team`
        :param auto_init: bool
        :param gitignore_template: string
        :rtype: :class:`pygithub.Repository.Repository`
        """
        assert isinstance(name, (str, unicode)), name
        assert description is pygithub.GithubObject.NotSet or isinstance(description, (str, unicode)), description
        assert homepage is pygithub.GithubObject.NotSet or isinstance(homepage, (str, unicode)), homepage
        assert private is pygithub.GithubObject.NotSet or isinstance(private, bool), private
        assert has_issues is pygithub.GithubObject.NotSet or isinstance(has_issues, bool), has_issues
        assert has_wiki is pygithub.GithubObject.NotSet or isinstance(has_wiki, bool), has_wiki
        assert has_downloads is pygithub.GithubObject.NotSet or isinstance(has_downloads, bool), has_downloads
        assert team_id is pygithub.GithubObject.NotSet or isinstance(team_id, pygithub.Team.Team), team_id
        assert auto_init is pygithub.GithubObject.NotSet or isinstance(auto_init, bool), auto_init
        assert gitignore_template is pygithub.GithubObject.NotSet or isinstance(gitignore_template, (str, unicode)), gitignore_template
        post_parameters = {
            "name": name,
        }
        if description is not pygithub.GithubObject.NotSet:
            post_parameters["description"] = description
        if homepage is not pygithub.GithubObject.NotSet:
            post_parameters["homepage"] = homepage
        if private is not pygithub.GithubObject.NotSet:
            post_parameters["private"] = private
        if has_issues is not pygithub.GithubObject.NotSet:
            post_parameters["has_issues"] = has_issues
        if has_wiki is not pygithub.GithubObject.NotSet:
            post_parameters["has_wiki"] = has_wiki
        if has_downloads is not pygithub.GithubObject.NotSet:
            post_parameters["has_downloads"] = has_downloads
        if team_id is not pygithub.GithubObject.NotSet:
            post_parameters["team_id"] = team_id._identity
        if auto_init is not pygithub.GithubObject.NotSet:
            post_parameters["auto_init"] = auto_init
        if gitignore_template is not pygithub.GithubObject.NotSet:
            post_parameters["gitignore_template"] = gitignore_template
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/repos",
            input=post_parameters
        )
        return pygithub.Repository.Repository(self._requester, headers, data, completed=True)

    def create_team(self, name, repo_names=pygithub.GithubObject.NotSet, permission=pygithub.GithubObject.NotSet):
        """
        :calls: `POST /orgs/:org/teams <http://developer.github.com/v3/orgs/teams>`_
        :param name: string
        :param repo_names: list of :class:`pygithub.Repository.Repository`
        :param permission: string
        :rtype: :class:`pygithub.Team.Team`
        """
        assert isinstance(name, (str, unicode)), name
        assert repo_names is pygithub.GithubObject.NotSet or all(isinstance(element, pygithub.Repository.Repository) for element in repo_names), repo_names
        assert permission is pygithub.GithubObject.NotSet or isinstance(permission, (str, unicode)), permission
        post_parameters = {
            "name": name,
        }
        if repo_names is not pygithub.GithubObject.NotSet:
            post_parameters["repo_names"] = [element._identity for element in repo_names]
        if permission is not pygithub.GithubObject.NotSet:
            post_parameters["permission"] = permission
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/teams",
            input=post_parameters
        )
        return pygithub.Team.Team(self._requester, headers, data, completed=True)

    def edit(self, billing_email=pygithub.GithubObject.NotSet, blog=pygithub.GithubObject.NotSet, company=pygithub.GithubObject.NotSet, email=pygithub.GithubObject.NotSet, location=pygithub.GithubObject.NotSet, name=pygithub.GithubObject.NotSet):
        """
        :calls: `PATCH /orgs/:org <http://developer.github.com/v3/orgs>`_
        :param billing_email: string
        :param blog: string
        :param company: string
        :param email: string
        :param location: string
        :param name: string
        :rtype: None
        """
        assert billing_email is pygithub.GithubObject.NotSet or isinstance(billing_email, (str, unicode)), billing_email
        assert blog is pygithub.GithubObject.NotSet or isinstance(blog, (str, unicode)), blog
        assert company is pygithub.GithubObject.NotSet or isinstance(company, (str, unicode)), company
        assert email is pygithub.GithubObject.NotSet or isinstance(email, (str, unicode)), email
        assert location is pygithub.GithubObject.NotSet or isinstance(location, (str, unicode)), location
        assert name is pygithub.GithubObject.NotSet or isinstance(name, (str, unicode)), name
        post_parameters = dict()
        if billing_email is not pygithub.GithubObject.NotSet:
            post_parameters["billing_email"] = billing_email
        if blog is not pygithub.GithubObject.NotSet:
            post_parameters["blog"] = blog
        if company is not pygithub.GithubObject.NotSet:
            post_parameters["company"] = company
        if email is not pygithub.GithubObject.NotSet:
            post_parameters["email"] = email
        if location is not pygithub.GithubObject.NotSet:
            post_parameters["location"] = location
        if name is not pygithub.GithubObject.NotSet:
            post_parameters["name"] = name
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=post_parameters
        )
        self._useAttributes(data)

    def get_events(self):
        """
        :calls: `GET /orgs/:org/events <http://developer.github.com/v3/activity/events>`_
        :rtype: :class:`pygithub.PaginatedList.PaginatedList` of :class:`pygithub.Event.Event`
        """
        return pygithub.PaginatedList.PaginatedList(
            pygithub.Event.Event,
            self._requester,
            self.url + "/events",
            None
        )

    def get_issues(self, filter=pygithub.GithubObject.NotSet, state=pygithub.GithubObject.NotSet, labels=pygithub.GithubObject.NotSet, sort=pygithub.GithubObject.NotSet, direction=pygithub.GithubObject.NotSet, since=pygithub.GithubObject.NotSet):
        """
        :calls: `GET /orgs/:org/issues <http://developer.github.com/v3/issues>`_
        :rtype: :class:`pygithub.PaginatedList.PaginatedList` of :class:`pygithub.Issue.Issue`
        :param filter: string
        :param state: string
        :param labels: list of :class:`pygithub.Label.Label`
        :param sort: string
        :param direction: string
        :param since: datetime.datetime
        :rtype: :class:`pygithub.PaginatedList.PaginatedList` of :class:`pygithub.Issue.Issue`
        """
        assert filter is pygithub.GithubObject.NotSet or isinstance(filter, (str, unicode)), filter
        assert state is pygithub.GithubObject.NotSet or isinstance(state, (str, unicode)), state
        assert labels is pygithub.GithubObject.NotSet or all(isinstance(element, pygithub.Label.Label) for element in labels), labels
        assert sort is pygithub.GithubObject.NotSet or isinstance(sort, (str, unicode)), sort
        assert direction is pygithub.GithubObject.NotSet or isinstance(direction, (str, unicode)), direction
        assert since is pygithub.GithubObject.NotSet or isinstance(since, datetime.datetime), since
        url_parameters = dict()
        if filter is not pygithub.GithubObject.NotSet:
            url_parameters["filter"] = filter
        if state is not pygithub.GithubObject.NotSet:
            url_parameters["state"] = state
        if labels is not pygithub.GithubObject.NotSet:
            url_parameters["labels"] = ",".join(label.name for label in labels)
        if sort is not pygithub.GithubObject.NotSet:
            url_parameters["sort"] = sort
        if direction is not pygithub.GithubObject.NotSet:
            url_parameters["direction"] = direction
        if since is not pygithub.GithubObject.NotSet:
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return pygithub.PaginatedList.PaginatedList(
            pygithub.Issue.Issue,
            self._requester,
            self.url + "/issues",
            url_parameters
        )

    def get_members(self):
        """
        :calls: `GET /orgs/:org/members <http://developer.github.com/v3/orgs/members>`_
        :rtype: :class:`pygithub.PaginatedList.PaginatedList` of :class:`pygithub.NamedUser.NamedUser`
        """
        return pygithub.PaginatedList.PaginatedList(
            pygithub.NamedUser.NamedUser,
            self._requester,
            self.url + "/members",
            None
        )

    def get_public_members(self):
        """
        :calls: `GET /orgs/:org/public_members <http://developer.github.com/v3/orgs/members>`_
        :rtype: :class:`pygithub.PaginatedList.PaginatedList` of :class:`pygithub.NamedUser.NamedUser`
        """
        return pygithub.PaginatedList.PaginatedList(
            pygithub.NamedUser.NamedUser,
            self._requester,
            self.url + "/public_members",
            None
        )

    def get_repo(self, name):
        """
        :calls: `GET /repos/:owner/:repo <http://developer.github.com/v3/repos>`_
        :param name: string
        :rtype: :class:`pygithub.Repository.Repository`
        """
        assert isinstance(name, (str, unicode)), name
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            "/repos/" + self.login + "/" + name
        )
        return pygithub.Repository.Repository(self._requester, headers, data, completed=True)

    def get_repos(self, type=pygithub.GithubObject.NotSet):
        """
        :calls: `GET /orgs/:org/repos <http://developer.github.com/v3/repos>`_
        :param type: string
        :rtype: :class:`pygithub.PaginatedList.PaginatedList` of :class:`pygithub.Repository.Repository`
        """
        assert type is pygithub.GithubObject.NotSet or isinstance(type, (str, unicode)), type
        url_parameters = dict()
        if type is not pygithub.GithubObject.NotSet:
            url_parameters["type"] = type
        return pygithub.PaginatedList.PaginatedList(
            pygithub.Repository.Repository,
            self._requester,
            self.url + "/repos",
            url_parameters
        )

    def get_team(self, id):
        """
        :calls: `GET /teams/:id <http://developer.github.com/v3/orgs/teams>`_
        :param id: integer
        :rtype: :class:`pygithub.Team.Team`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            "/teams/" + str(id)
        )
        return pygithub.Team.Team(self._requester, headers, data, completed=True)

    def get_teams(self):
        """
        :calls: `GET /orgs/:org/teams <http://developer.github.com/v3/orgs/teams>`_
        :rtype: :class:`pygithub.PaginatedList.PaginatedList` of :class:`pygithub.Team.Team`
        """
        return pygithub.PaginatedList.PaginatedList(
            pygithub.Team.Team,
            self._requester,
            self.url + "/teams",
            None
        )

    def has_in_members(self, member):
        """
        :calls: `GET /orgs/:org/members/:user <http://developer.github.com/v3/orgs/members>`_
        :param member: :class:`pygithub.NamedUser.NamedUser`
        :rtype: bool
        """
        assert isinstance(member, pygithub.NamedUser.NamedUser), member
        status, headers, data = self._requester.requestJson(
            "GET",
            self.url + "/members/" + member._identity
        )
        return status == 204

    def has_in_public_members(self, public_member):
        """
        :calls: `GET /orgs/:org/public_members/:user <http://developer.github.com/v3/orgs/members>`_
        :param public_member: :class:`pygithub.NamedUser.NamedUser`
        :rtype: bool
        """
        assert isinstance(public_member, pygithub.NamedUser.NamedUser), public_member
        status, headers, data = self._requester.requestJson(
            "GET",
            self.url + "/public_members/" + public_member._identity
        )
        return status == 204

    def remove_from_members(self, member):
        """
        :calls: `DELETE /orgs/:org/members/:user <http://developer.github.com/v3/orgs/members>`_
        :param member: :class:`pygithub.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(member, pygithub.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url + "/members/" + member._identity
        )

    def remove_from_public_members(self, public_member):
        """
        :calls: `DELETE /orgs/:org/public_members/:user <http://developer.github.com/v3/orgs/members>`_
        :param public_member: :class:`pygithub.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(public_member, pygithub.NamedUser.NamedUser), public_member
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url + "/public_members/" + public_member._identity
        )

    def _initAttributes(self):
        self._avatar_url = pygithub.GithubObject.NotSet
        self._billing_email = pygithub.GithubObject.NotSet
        self._blog = pygithub.GithubObject.NotSet
        self._collaborators = pygithub.GithubObject.NotSet
        self._company = pygithub.GithubObject.NotSet
        self._created_at = pygithub.GithubObject.NotSet
        self._disk_usage = pygithub.GithubObject.NotSet
        self._email = pygithub.GithubObject.NotSet
        self._events_url = pygithub.GithubObject.NotSet
        self._followers = pygithub.GithubObject.NotSet
        self._following = pygithub.GithubObject.NotSet
        self._gravatar_id = pygithub.GithubObject.NotSet
        self._html_url = pygithub.GithubObject.NotSet
        self._id = pygithub.GithubObject.NotSet
        self._location = pygithub.GithubObject.NotSet
        self._login = pygithub.GithubObject.NotSet
        self._members_url = pygithub.GithubObject.NotSet
        self._name = pygithub.GithubObject.NotSet
        self._owned_private_repos = pygithub.GithubObject.NotSet
        self._plan = pygithub.GithubObject.NotSet
        self._private_gists = pygithub.GithubObject.NotSet
        self._public_gists = pygithub.GithubObject.NotSet
        self._public_members_url = pygithub.GithubObject.NotSet
        self._public_repos = pygithub.GithubObject.NotSet
        self._repos_url = pygithub.GithubObject.NotSet
        self._total_private_repos = pygithub.GithubObject.NotSet
        self._type = pygithub.GithubObject.NotSet
        self._updated_at = pygithub.GithubObject.NotSet
        self._url = pygithub.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "avatar_url" in attributes:  # pragma no branch
            self._avatar_url = self._makeStringAttribute(attributes["avatar_url"])
        if "billing_email" in attributes:  # pragma no branch
            self._billing_email = self._makeStringAttribute(attributes["billing_email"])
        if "blog" in attributes:  # pragma no branch
            self._blog = self._makeStringAttribute(attributes["blog"])
        if "collaborators" in attributes:  # pragma no branch
            self._collaborators = self._makeIntAttribute(attributes["collaborators"])
        if "company" in attributes:  # pragma no branch
            self._company = self._makeStringAttribute(attributes["company"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "disk_usage" in attributes:  # pragma no branch
            self._disk_usage = self._makeIntAttribute(attributes["disk_usage"])
        if "email" in attributes:  # pragma no branch
            self._email = self._makeStringAttribute(attributes["email"])
        if "events_url" in attributes:  # pragma no branch
            self._events_url = self._makeStringAttribute(attributes["events_url"])
        if "followers" in attributes:  # pragma no branch
            self._followers = self._makeIntAttribute(attributes["followers"])
        if "following" in attributes:  # pragma no branch
            self._following = self._makeIntAttribute(attributes["following"])
        if "gravatar_id" in attributes:  # pragma no branch
            self._gravatar_id = self._makeStringAttribute(attributes["gravatar_id"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "location" in attributes:  # pragma no branch
            self._location = self._makeStringAttribute(attributes["location"])
        if "login" in attributes:  # pragma no branch
            self._login = self._makeStringAttribute(attributes["login"])
        if "members_url" in attributes:  # pragma no branch
            self._members_url = self._makeStringAttribute(attributes["members_url"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "owned_private_repos" in attributes:  # pragma no branch
            self._owned_private_repos = self._makeIntAttribute(attributes["owned_private_repos"])
        if "plan" in attributes:  # pragma no branch
            self._plan = self._makeClassAttribute(pygithub.Plan.Plan, attributes["plan"])
        if "private_gists" in attributes:  # pragma no branch
            self._private_gists = self._makeIntAttribute(attributes["private_gists"])
        if "public_gists" in attributes:  # pragma no branch
            self._public_gists = self._makeIntAttribute(attributes["public_gists"])
        if "public_members_url" in attributes:  # pragma no branch
            self._public_members_url = self._makeStringAttribute(attributes["public_members_url"])
        if "public_repos" in attributes:  # pragma no branch
            self._public_repos = self._makeIntAttribute(attributes["public_repos"])
        if "repos_url" in attributes:  # pragma no branch
            self._repos_url = self._makeStringAttribute(attributes["repos_url"])
        if "total_private_repos" in attributes:  # pragma no branch
            self._total_private_repos = self._makeIntAttribute(attributes["total_private_repos"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
