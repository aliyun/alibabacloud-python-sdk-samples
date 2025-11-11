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
    def sched_preload_job(
        site_response_body: esa20240910_models.CreateSiteResponseBody,
        client: ESA20240910Client,
    ) -> esa20240910_models.CreateScheduledPreloadJobResponseBody:
        logging.log(logging.INFO, 'Begin Call CreateScheduledPreloadJob to create resource')
        create_scheduled_preload_job_request = esa20240910_models.CreateScheduledPreloadJobRequest(
            insert_way = 'oss',
            site_id = site_response_body.site_id,
            oss_url = 'https://yandanpub.oss-cn-hangzhou.aliyuncs.com/1.txt',
            name = 'testscheduledpreloadjob'
        )
        create_scheduled_preload_job_response = client.create_scheduled_preload_job(create_scheduled_preload_job_request)
        logging.log(logging.INFO, 'Call CreateScheduledPreloadJob success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(create_scheduled_preload_job_response))
        return create_scheduled_preload_job_response.body

    @staticmethod
    async def sched_preload_job_async(
        site_response_body: esa20240910_models.CreateSiteResponseBody,
        client: ESA20240910Client,
    ) -> esa20240910_models.CreateScheduledPreloadJobResponseBody:
        logging.log(logging.INFO, 'Begin Call CreateScheduledPreloadJob to create resource')
        create_scheduled_preload_job_request = esa20240910_models.CreateScheduledPreloadJobRequest(
            insert_way = 'oss',
            site_id = site_response_body.site_id,
            oss_url = 'https://yandanpub.oss-cn-hangzhou.aliyuncs.com/1.txt',
            name = 'testscheduledpreloadjob'
        )
        create_scheduled_preload_job_response = await client.create_scheduled_preload_job_async(create_scheduled_preload_job_request)
        logging.log(logging.INFO, 'Call CreateScheduledPreloadJob success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(create_scheduled_preload_job_response))
        return create_scheduled_preload_job_response.body

    @staticmethod
    def destroy_sched_preload_job(
        create_scheduled_preload_job_response_body: esa20240910_models.CreateScheduledPreloadJobResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call DeleteScheduledPreloadJob to destroy resource')
        delete_scheduled_preload_job_request = esa20240910_models.DeleteScheduledPreloadJobRequest(
            id = create_scheduled_preload_job_response_body.id
        )
        delete_scheduled_preload_job_response = client.delete_scheduled_preload_job(delete_scheduled_preload_job_request)
        logging.log(logging.INFO, 'Call DeleteScheduledPreloadJob success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(delete_scheduled_preload_job_response))

    @staticmethod
    async def destroy_sched_preload_job_async(
        create_scheduled_preload_job_response_body: esa20240910_models.CreateScheduledPreloadJobResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call DeleteScheduledPreloadJob to destroy resource')
        delete_scheduled_preload_job_request = esa20240910_models.DeleteScheduledPreloadJobRequest(
            id = create_scheduled_preload_job_response_body.id
        )
        delete_scheduled_preload_job_response = await client.delete_scheduled_preload_job_async(delete_scheduled_preload_job_request)
        logging.log(logging.INFO, 'Call DeleteScheduledPreloadJob success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(delete_scheduled_preload_job_response))

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
        sched_preload_job_resp_body = Sample.sched_preload_job(site_resp_body, esa_20240910client)
        # destroy resource
        Sample.destroy_sched_preload_job(sched_preload_job_resp_body, esa_20240910client)

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
        sched_preload_job_resp_body = await Sample.sched_preload_job_async(site_resp_body, esa_20240910client)
        # destroy resource
        await Sample.destroy_sched_preload_job_async(sched_preload_job_resp_body, esa_20240910client)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
