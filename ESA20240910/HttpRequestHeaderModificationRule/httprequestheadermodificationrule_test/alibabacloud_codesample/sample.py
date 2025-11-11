# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import logging
import os
import sys

from typing import List

from alibabacloud_credentials.client import Client
from alibabacloud_esa20240910 import models as esa20240910_models
from alibabacloud_esa20240910.client import Client as ESA20240910Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from darabonba.core import DaraCore as DaraCore
from darabonba.exceptions import DaraException



class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_esa20240910client() -> ESA20240910Client:
        config = open_api_models.Config()
        config.credential = Client(None)
        # Endpoint please refer to https://api.aliyun.com/product/ESA
        config.endpoint = 'esa.cn-hangzhou.aliyuncs.com'
        return ESA20240910Client(config)

    @staticmethod
    def rate_plan_inst(
        client: ESA20240910Client,
    ) -> esa20240910_models.PurchaseRatePlanResponseBody:
        logging.log(logging.INFO, 'Begin Call PurchaseRatePlan to create resource')
        purchase_rate_plan_request = esa20240910_models.PurchaseRatePlanRequest(
            type = 'NS',
            charge_type = 'PREPAY',
            auto_renew = False,
            period = 1,
            coverage = 'overseas',
            auto_pay = True,
            plan_name = 'high'
        )
        purchase_rate_plan_response = client.purchase_rate_plan(purchase_rate_plan_request)
        describe_rate_plan_instance_status_request = esa20240910_models.DescribeRatePlanInstanceStatusRequest(
            instance_id = purchase_rate_plan_response.body.instance_id
        )
        current_retry = 0
        delayed_time = 10000
        interval = 10000
        while current_retry < 10:
            try :
                sleep_time = 0
                if current_retry == 0:
                    sleep_time = delayed_time
                else:
                    sleep_time = interval

                logging.log(logging.INFO, 'Polling for asynchronous results...')
                DaraCore.sleep(sleep_time)
            except Exception as error :
                raise DaraException({
                    'message': error.message
                })
            
            describe_rate_plan_instance_status_response = client.describe_rate_plan_instance_status(describe_rate_plan_instance_status_request)
            instance_status = describe_rate_plan_instance_status_response.body.instance_status
            if instance_status == 'running':
                logging.log(logging.INFO, 'Call PurchaseRatePlan success, response: ')
                logging.log(logging.INFO, UtilClient.to_jsonstring(purchase_rate_plan_response))
                return purchase_rate_plan_response.body
            current_retry+= 1
        raise DaraException({
            'message': 'Asynchronous check failed'
        })

    @staticmethod
    async def rate_plan_inst_async(
        client: ESA20240910Client,
    ) -> esa20240910_models.PurchaseRatePlanResponseBody:
        logging.log(logging.INFO, 'Begin Call PurchaseRatePlan to create resource')
        purchase_rate_plan_request = esa20240910_models.PurchaseRatePlanRequest(
            type = 'NS',
            charge_type = 'PREPAY',
            auto_renew = False,
            period = 1,
            coverage = 'overseas',
            auto_pay = True,
            plan_name = 'high'
        )
        purchase_rate_plan_response = await client.purchase_rate_plan_async(purchase_rate_plan_request)
        describe_rate_plan_instance_status_request = esa20240910_models.DescribeRatePlanInstanceStatusRequest(
            instance_id = purchase_rate_plan_response.body.instance_id
        )
        current_retry = 0
        delayed_time = 10000
        interval = 10000
        while current_retry < 10:
            try :
                sleep_time = 0
                if current_retry == 0:
                    sleep_time = delayed_time
                else:
                    sleep_time = interval

                logging.log(logging.INFO, 'Polling for asynchronous results...')
                await DaraCore.sleep_async(sleep_time)
            except Exception as error :
                raise DaraException({
                    'message': error.message
                })
            
            describe_rate_plan_instance_status_response = await client.describe_rate_plan_instance_status_async(describe_rate_plan_instance_status_request)
            instance_status = describe_rate_plan_instance_status_response.body.instance_status
            if instance_status == 'running':
                logging.log(logging.INFO, 'Call PurchaseRatePlan success, response: ')
                logging.log(logging.INFO, UtilClient.to_jsonstring(purchase_rate_plan_response))
                return purchase_rate_plan_response.body
            current_retry+= 1
        raise DaraException({
            'message': 'Asynchronous check failed'
        })

    @staticmethod
    def site(
        rate_plan_inst_response_body: esa20240910_models.PurchaseRatePlanResponseBody,
        client: ESA20240910Client,
    ) -> esa20240910_models.CreateSiteResponseBody:
        logging.log(logging.INFO, 'Begin Call CreateSite to create resource')
        create_site_request = esa20240910_models.CreateSiteRequest(
            site_name = 'gositecdn.cn',
            instance_id = rate_plan_inst_response_body.instance_id,
            coverage = 'overseas',
            access_type = 'NS'
        )
        create_site_response = client.create_site(create_site_request)
        get_site_request = esa20240910_models.GetSiteRequest(
            site_id = create_site_response.body.site_id
        )
        current_retry = 0
        delayed_time = 60000
        interval = 10000
        while current_retry < 5:
            try :
                sleep_time = 0
                if current_retry == 0:
                    sleep_time = delayed_time
                else:
                    sleep_time = interval

                logging.log(logging.INFO, 'Polling for asynchronous results...')
                DaraCore.sleep(sleep_time)
            except Exception as error :
                raise DaraException({
                    'message': error.message
                })
            
            get_site_response = client.get_site(get_site_request)
            status = get_site_response.body.site_model.status
            if status == 'pending':
                logging.log(logging.INFO, 'Call CreateSite success, response: ')
                logging.log(logging.INFO, UtilClient.to_jsonstring(create_site_response))
                return create_site_response.body
            current_retry+= 1
        raise DaraException({
            'message': 'Asynchronous check failed'
        })

    @staticmethod
    async def site_async(
        rate_plan_inst_response_body: esa20240910_models.PurchaseRatePlanResponseBody,
        client: ESA20240910Client,
    ) -> esa20240910_models.CreateSiteResponseBody:
        logging.log(logging.INFO, 'Begin Call CreateSite to create resource')
        create_site_request = esa20240910_models.CreateSiteRequest(
            site_name = 'gositecdn.cn',
            instance_id = rate_plan_inst_response_body.instance_id,
            coverage = 'overseas',
            access_type = 'NS'
        )
        create_site_response = await client.create_site_async(create_site_request)
        get_site_request = esa20240910_models.GetSiteRequest(
            site_id = create_site_response.body.site_id
        )
        current_retry = 0
        delayed_time = 60000
        interval = 10000
        while current_retry < 5:
            try :
                sleep_time = 0
                if current_retry == 0:
                    sleep_time = delayed_time
                else:
                    sleep_time = interval

                logging.log(logging.INFO, 'Polling for asynchronous results...')
                await DaraCore.sleep_async(sleep_time)
            except Exception as error :
                raise DaraException({
                    'message': error.message
                })
            
            get_site_response = await client.get_site_async(get_site_request)
            status = get_site_response.body.site_model.status
            if status == 'pending':
                logging.log(logging.INFO, 'Call CreateSite success, response: ')
                logging.log(logging.INFO, UtilClient.to_jsonstring(create_site_response))
                return create_site_response.body
            current_retry+= 1
        raise DaraException({
            'message': 'Asynchronous check failed'
        })

    @staticmethod
    def req_hdr_mod_rule(
        site_response_body: esa20240910_models.CreateSiteResponseBody,
        client: ESA20240910Client,
    ) -> esa20240910_models.CreateHttpRequestHeaderModificationRuleResponseBody:
        logging.log(logging.INFO, 'Begin Call CreateHttpRequestHeaderModificationRule to create resource')
        request_header_modification = esa20240910_models.CreateHttpRequestHeaderModificationRuleRequestRequestHeaderModification(
            type = 'static',
            value = 'add',
            operation = 'add',
            name = 'testadd'
        )
        request_header_modification_1 = esa20240910_models.CreateHttpRequestHeaderModificationRuleRequestRequestHeaderModification(
            operation = 'del',
            name = 'testdel'
        )
        request_header_modification_2 = esa20240910_models.CreateHttpRequestHeaderModificationRuleRequestRequestHeaderModification(
            type = 'dynamic',
            value = 'ip.geoip.country',
            operation = 'modify',
            name = 'testmodify'
        )
        create_http_request_header_modification_rule_request = esa20240910_models.CreateHttpRequestHeaderModificationRuleRequest(
            site_id = site_response_body.site_id,
            rule_enable = 'on',
            rule = '(http.host eq "video.example.com")',
            sequence = 1,
            site_version = 0,
            rule_name = 'test',
            request_header_modification = [
                request_header_modification,
                request_header_modification_1,
                request_header_modification_2
            ]
        )
        create_http_request_header_modification_rule_response = client.create_http_request_header_modification_rule(create_http_request_header_modification_rule_request)
        logging.log(logging.INFO, 'Call CreateHttpRequestHeaderModificationRule success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(create_http_request_header_modification_rule_response))
        return create_http_request_header_modification_rule_response.body

    @staticmethod
    async def req_hdr_mod_rule_async(
        site_response_body: esa20240910_models.CreateSiteResponseBody,
        client: ESA20240910Client,
    ) -> esa20240910_models.CreateHttpRequestHeaderModificationRuleResponseBody:
        logging.log(logging.INFO, 'Begin Call CreateHttpRequestHeaderModificationRule to create resource')
        request_header_modification = esa20240910_models.CreateHttpRequestHeaderModificationRuleRequestRequestHeaderModification(
            type = 'static',
            value = 'add',
            operation = 'add',
            name = 'testadd'
        )
        request_header_modification_1 = esa20240910_models.CreateHttpRequestHeaderModificationRuleRequestRequestHeaderModification(
            operation = 'del',
            name = 'testdel'
        )
        request_header_modification_2 = esa20240910_models.CreateHttpRequestHeaderModificationRuleRequestRequestHeaderModification(
            type = 'dynamic',
            value = 'ip.geoip.country',
            operation = 'modify',
            name = 'testmodify'
        )
        create_http_request_header_modification_rule_request = esa20240910_models.CreateHttpRequestHeaderModificationRuleRequest(
            site_id = site_response_body.site_id,
            rule_enable = 'on',
            rule = '(http.host eq "video.example.com")',
            sequence = 1,
            site_version = 0,
            rule_name = 'test',
            request_header_modification = [
                request_header_modification,
                request_header_modification_1,
                request_header_modification_2
            ]
        )
        create_http_request_header_modification_rule_response = await client.create_http_request_header_modification_rule_async(create_http_request_header_modification_rule_request)
        logging.log(logging.INFO, 'Call CreateHttpRequestHeaderModificationRule success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(create_http_request_header_modification_rule_response))
        return create_http_request_header_modification_rule_response.body

    @staticmethod
    def update_req_hdr_mod_rule(
        site_response_body: esa20240910_models.CreateSiteResponseBody,
        create_http_request_header_modification_rule_response_body: esa20240910_models.CreateHttpRequestHeaderModificationRuleResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call UpdateHttpRequestHeaderModificationRule to update resource')
        request_header_modification = esa20240910_models.UpdateHttpRequestHeaderModificationRuleRequestRequestHeaderModification(
            type = 'static',
            value = 'modify1',
            operation = 'modify',
            name = 'testmodify1'
        )
        update_http_request_header_modification_rule_request = esa20240910_models.UpdateHttpRequestHeaderModificationRuleRequest(
            site_id = site_response_body.site_id,
            rule_enable = 'off',
            rule = '(http.request.uri eq "/content?page=1234")',
            sequence = 1,
            rule_name = 'test_modify',
            request_header_modification = [
                request_header_modification
            ],
            config_id = create_http_request_header_modification_rule_response_body.config_id
        )
        update_http_request_header_modification_rule_response = client.update_http_request_header_modification_rule(update_http_request_header_modification_rule_request)
        logging.log(logging.INFO, 'Call UpdateHttpRequestHeaderModificationRule success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(update_http_request_header_modification_rule_response))

    @staticmethod
    async def update_req_hdr_mod_rule_async(
        site_response_body: esa20240910_models.CreateSiteResponseBody,
        create_http_request_header_modification_rule_response_body: esa20240910_models.CreateHttpRequestHeaderModificationRuleResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call UpdateHttpRequestHeaderModificationRule to update resource')
        request_header_modification = esa20240910_models.UpdateHttpRequestHeaderModificationRuleRequestRequestHeaderModification(
            type = 'static',
            value = 'modify1',
            operation = 'modify',
            name = 'testmodify1'
        )
        update_http_request_header_modification_rule_request = esa20240910_models.UpdateHttpRequestHeaderModificationRuleRequest(
            site_id = site_response_body.site_id,
            rule_enable = 'off',
            rule = '(http.request.uri eq "/content?page=1234")',
            sequence = 1,
            rule_name = 'test_modify',
            request_header_modification = [
                request_header_modification
            ],
            config_id = create_http_request_header_modification_rule_response_body.config_id
        )
        update_http_request_header_modification_rule_response = await client.update_http_request_header_modification_rule_async(update_http_request_header_modification_rule_request)
        logging.log(logging.INFO, 'Call UpdateHttpRequestHeaderModificationRule success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(update_http_request_header_modification_rule_response))

    @staticmethod
    def destroy_req_hdr_mod_rule(
        site_response_body: esa20240910_models.CreateSiteResponseBody,
        create_http_request_header_modification_rule_response_body: esa20240910_models.CreateHttpRequestHeaderModificationRuleResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call DeleteHttpRequestHeaderModificationRule to destroy resource')
        delete_http_request_header_modification_rule_request = esa20240910_models.DeleteHttpRequestHeaderModificationRuleRequest(
            site_id = site_response_body.site_id,
            config_id = create_http_request_header_modification_rule_response_body.config_id
        )
        delete_http_request_header_modification_rule_response = client.delete_http_request_header_modification_rule(delete_http_request_header_modification_rule_request)
        logging.log(logging.INFO, 'Call DeleteHttpRequestHeaderModificationRule success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(delete_http_request_header_modification_rule_response))

    @staticmethod
    async def destroy_req_hdr_mod_rule_async(
        site_response_body: esa20240910_models.CreateSiteResponseBody,
        create_http_request_header_modification_rule_response_body: esa20240910_models.CreateHttpRequestHeaderModificationRuleResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call DeleteHttpRequestHeaderModificationRule to destroy resource')
        delete_http_request_header_modification_rule_request = esa20240910_models.DeleteHttpRequestHeaderModificationRuleRequest(
            site_id = site_response_body.site_id,
            config_id = create_http_request_header_modification_rule_response_body.config_id
        )
        delete_http_request_header_modification_rule_response = await client.delete_http_request_header_modification_rule_async(delete_http_request_header_modification_rule_request)
        logging.log(logging.INFO, 'Call DeleteHttpRequestHeaderModificationRule success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(delete_http_request_header_modification_rule_response))

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # The code may contain api calls involving fees. Please ensure that you fully understand the charging methods and prices before running.
        # Set the environment variable COST_ACK to true or delete the following judgment to run the sample code.
        cost_acknowledged = os.environ.get('COST_ACK')
        if DaraCore.is_null(cost_acknowledged) or not cost_acknowledged == 'true':
            logging.log(logging.WARNING, 'Running code may affect the online resources of the current account, please proceed with caution!')
            return
        # Init client
        esa_20240910client = Sample.create_esa20240910client()
        # Init resource
        rate_plan_inst_resp_body = Sample.rate_plan_inst(esa_20240910client)
        site_resp_body = Sample.site(rate_plan_inst_resp_body, esa_20240910client)
        req_hdr_mod_rule_resp_body = Sample.req_hdr_mod_rule(site_resp_body, esa_20240910client)
        # update resource
        Sample.update_req_hdr_mod_rule(site_resp_body, req_hdr_mod_rule_resp_body, esa_20240910client)
        # destroy resource
        Sample.destroy_req_hdr_mod_rule(site_resp_body, req_hdr_mod_rule_resp_body, esa_20240910client)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # The code may contain api calls involving fees. Please ensure that you fully understand the charging methods and prices before running.
        # Set the environment variable COST_ACK to true or delete the following judgment to run the sample code.
        cost_acknowledged = os.environ.get('COST_ACK')
        if DaraCore.is_null(cost_acknowledged) or not cost_acknowledged == 'true':
            logging.log(logging.WARNING, 'Running code may affect the online resources of the current account, please proceed with caution!')
            return
        # Init client
        esa_20240910client = Sample.create_esa20240910client()
        # Init resource
        rate_plan_inst_resp_body = await Sample.rate_plan_inst_async(esa_20240910client)
        site_resp_body = await Sample.site_async(rate_plan_inst_resp_body, esa_20240910client)
        req_hdr_mod_rule_resp_body = await Sample.req_hdr_mod_rule_async(site_resp_body, esa_20240910client)
        # update resource
        await Sample.update_req_hdr_mod_rule_async(site_resp_body, req_hdr_mod_rule_resp_body, esa_20240910client)
        # destroy resource
        await Sample.destroy_req_hdr_mod_rule_async(site_resp_body, req_hdr_mod_rule_resp_body, esa_20240910client)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
