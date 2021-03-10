# -*- coding: utf-8 -*-
# --------------------------
# Copyright © 2014 -            Qentinel Group.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ---------------------------


"""Keywords for browser cookie handling.

When Selenium gets cookies from browser, it return them as dictionaries
in a list. This list can be searched for key - value pairs.
"""

from robot.api import logger
from QWeb.internal import cookies


def delete_all_cookies():
    """Delete all cookies in browser.

    Cookies can be only deleted when browser is open. Cookies are automatically
    deleted when you Close All Browsers

    Examples
    --------
    .. code-block:: robotframework

        DeleteAllCookies
    """
    cookies.delete_all_cookies()


def list_cookies():
    """List all cookies in browser.

    Cookies can be only listed when browser is open. Cookies are automatically
    deleted when you Close All Browsers

    Examples
    --------
    .. code-block:: robotframework

        ListCookies
    """
    cookies_list = cookies.get_cookies()
    logger.info(cookies_list)
    return cookies_list


def is_cookie(name, value):
    """Return True if cookie with name and value is found.

    Cookies are a good way to detect if user has already logged in.
    This keyword can be used in appstate.

    Examples
    --------
    .. code-block:: robotframework

        IsCookie    domain    google.fi

    Parameters
    ----------
    name : str
        Cookie dictionary key name
    value : str
        Expected value for key name

    """
    cookies_list = cookies.get_cookies()
    for cookie in cookies_list:
        if name in cookie.keys():
            if cookie[name] == value:
                return True
    return False
