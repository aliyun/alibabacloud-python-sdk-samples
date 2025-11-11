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
    def video_proc(
        site_response_body: esa20240910_models.CreateSiteResponseBody,
        client: ESA20240910Client,
    ) -> esa20240910_models.CreateVideoProcessingResponseBody:
        logging.log(logging.INFO, 'Begin Call CreateVideoProcessing to create resource')
        create_video_processing_request = esa20240910_models.CreateVideoProcessingRequest(
            video_seek_enable = 'on',
            site_id = site_response_body.site_id,
            rule_enable = 'on',
            flv_video_seek_mode = 'by_byte',
            mp_4seek_end = 'end',
            flv_seek_start = 'start',
            rule = '(http.host eq "video.example.com")',
            sequence = 1,
            mp_4seek_start = 'start',
            site_version = 0,
            flv_seek_end = 'end',
            rule_name = 'test'
        )
        create_video_processing_response = client.create_video_processing(create_video_processing_request)
        logging.log(logging.INFO, 'Call CreateVideoProcessing success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(create_video_processing_response))
        return create_video_processing_response.body

    @staticmethod
    async def video_proc_async(
        site_response_body: esa20240910_models.CreateSiteResponseBody,
        client: ESA20240910Client,
    ) -> esa20240910_models.CreateVideoProcessingResponseBody:
        logging.log(logging.INFO, 'Begin Call CreateVideoProcessing to create resource')
        create_video_processing_request = esa20240910_models.CreateVideoProcessingRequest(
            video_seek_enable = 'on',
            site_id = site_response_body.site_id,
            rule_enable = 'on',
            flv_video_seek_mode = 'by_byte',
            mp_4seek_end = 'end',
            flv_seek_start = 'start',
            rule = '(http.host eq "video.example.com")',
            sequence = 1,
            mp_4seek_start = 'start',
            site_version = 0,
            flv_seek_end = 'end',
            rule_name = 'test'
        )
        create_video_processing_response = await client.create_video_processing_async(create_video_processing_request)
        logging.log(logging.INFO, 'Call CreateVideoProcessing success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(create_video_processing_response))
        return create_video_processing_response.body

    @staticmethod
    def update_video_proc(
        site_response_body: esa20240910_models.CreateSiteResponseBody,
        create_video_processing_response_body: esa20240910_models.CreateVideoProcessingResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call UpdateVideoProcessing to update resource')
        update_video_processing_request = esa20240910_models.UpdateVideoProcessingRequest(
            video_seek_enable = 'off',
            site_id = site_response_body.site_id,
            rule_enable = 'off',
            flv_video_seek_mode = 'by_time',
            mp_4seek_end = 'e',
            flv_seek_start = 's',
            rule = '(http.request.uri eq "/content?page=1234")',
            sequence = 1,
            mp_4seek_start = 's',
            flv_seek_end = 'e',
            rule_name = 'test_modify',
            config_id = create_video_processing_response_body.config_id
        )
        update_video_processing_response = client.update_video_processing(update_video_processing_request)
        logging.log(logging.INFO, 'Call UpdateVideoProcessing success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(update_video_processing_response))

    @staticmethod
    async def update_video_proc_async(
        site_response_body: esa20240910_models.CreateSiteResponseBody,
        create_video_processing_response_body: esa20240910_models.CreateVideoProcessingResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call UpdateVideoProcessing to update resource')
        update_video_processing_request = esa20240910_models.UpdateVideoProcessingRequest(
            video_seek_enable = 'off',
            site_id = site_response_body.site_id,
            rule_enable = 'off',
            flv_video_seek_mode = 'by_time',
            mp_4seek_end = 'e',
            flv_seek_start = 's',
            rule = '(http.request.uri eq "/content?page=1234")',
            sequence = 1,
            mp_4seek_start = 's',
            flv_seek_end = 'e',
            rule_name = 'test_modify',
            config_id = create_video_processing_response_body.config_id
        )
        update_video_processing_response = await client.update_video_processing_async(update_video_processing_request)
        logging.log(logging.INFO, 'Call UpdateVideoProcessing success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(update_video_processing_response))

    @staticmethod
    def destroy_video_proc(
        site_response_body: esa20240910_models.CreateSiteResponseBody,
        create_video_processing_response_body: esa20240910_models.CreateVideoProcessingResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call DeleteVideoProcessing to destroy resource')
        delete_video_processing_request = esa20240910_models.DeleteVideoProcessingRequest(
            site_id = site_response_body.site_id,
            config_id = create_video_processing_response_body.config_id
        )
        delete_video_processing_response = client.delete_video_processing(delete_video_processing_request)
        logging.log(logging.INFO, 'Call DeleteVideoProcessing success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(delete_video_processing_response))

    @staticmethod
    async def destroy_video_proc_async(
        site_response_body: esa20240910_models.CreateSiteResponseBody,
        create_video_processing_response_body: esa20240910_models.CreateVideoProcessingResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call DeleteVideoProcessing to destroy resource')
        delete_video_processing_request = esa20240910_models.DeleteVideoProcessingRequest(
            site_id = site_response_body.site_id,
            config_id = create_video_processing_response_body.config_id
        )
        delete_video_processing_response = await client.delete_video_processing_async(delete_video_processing_request)
        logging.log(logging.INFO, 'Call DeleteVideoProcessing success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(delete_video_processing_response))

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
        video_proc_resp_body = Sample.video_proc(site_resp_body, esa_20240910client)
        # update resource
        Sample.update_video_proc(site_resp_body, video_proc_resp_body, esa_20240910client)
        # destroy resource
        Sample.destroy_video_proc(site_resp_body, video_proc_resp_body, esa_20240910client)

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
        video_proc_resp_body = await Sample.video_proc_async(site_resp_body, esa_20240910client)
        # update resource
        await Sample.update_video_proc_async(site_resp_body, video_proc_resp_body, esa_20240910client)
        # destroy resource
        await Sample.destroy_video_proc_async(site_resp_body, video_proc_resp_body, esa_20240910client)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
