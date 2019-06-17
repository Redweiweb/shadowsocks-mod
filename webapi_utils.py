#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

import requests

from configloader import get_config


class WebApi(object):
    def __init__(self):
        self.session_pool = requests.Session()

    def get_api(self, uri, params=None):
        if params is None:
            params = {}
        try:
            uri_params = params.copy()
            uri_params["key"] = get_config().WEBAPI_TOKEN
            res = self.session_pool.get(
                "%s/mod_mu/%s" % (get_config().WEBAPI_URL, uri),
                params=uri_params,
                timeout=10,
            )
            try:
                data = res.json()
            except Exception:
                if res:
                    logging.error("Error data:%s" % res.text)
                raise Exception("error data!")
            if data["ret"] == 0:
                logging.error("Error data:%s" % res.text)
                logging.error("request %s error!wrong ret!" % uri)
                raise Exception("wrong ret!")
            return data["data"]
        except Exception:
            import traceback

            trace = traceback.format_exc()
            logging.error(trace)
            raise Exception("network issue or server error!")

    def post_api(self, uri, params=None, raw_data=None):
        if params is None:
            params = {}
        if raw_data is None:
            raw_data = {}
        try:
            uri_params = params.copy()
            uri_params["key"] = get_config().WEBAPI_TOKEN
            res = self.session_pool.post(
                "%s/mod_mu/%s" % (get_config().WEBAPI_URL, uri),
                params=uri_params,
                json=raw_data,
                timeout=10,
            )
            try:
                data = res.json()
            except Exception:
                if res:
                    logging.error("Error data:%s" % res.text)
                raise Exception("error data!")
            if data["ret"] == 0:
                logging.error("Error data:%s" % res.text)
                logging.error("request %s error!wrong ret!" % uri)
                raise Exception("wrong ret!")
            return data["data"]
        except Exception:
            import traceback

            trace = traceback.format_exc()
            logging.error(trace)
            raise Exception("network issue or server error!")
