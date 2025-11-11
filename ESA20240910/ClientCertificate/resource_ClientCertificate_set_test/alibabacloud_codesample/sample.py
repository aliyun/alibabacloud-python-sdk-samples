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
    def rate_plan_inst_clt_cert(
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
    async def rate_plan_inst_clt_cert_async(
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
    def site_clt_cert(
        rate_plan_inst_clt_cert_response_body: esa20240910_models.PurchaseRatePlanResponseBody,
        client: ESA20240910Client,
    ) -> esa20240910_models.CreateSiteResponseBody:
        logging.log(logging.INFO, 'Begin Call CreateSite to create resource')
        create_site_request = esa20240910_models.CreateSiteRequest(
            site_name = 'gositecdn.cn',
            instance_id = rate_plan_inst_clt_cert_response_body.instance_id,
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
    async def site_clt_cert_async(
        rate_plan_inst_clt_cert_response_body: esa20240910_models.PurchaseRatePlanResponseBody,
        client: ESA20240910Client,
    ) -> esa20240910_models.CreateSiteResponseBody:
        logging.log(logging.INFO, 'Begin Call CreateSite to create resource')
        create_site_request = esa20240910_models.CreateSiteRequest(
            site_name = 'gositecdn.cn',
            instance_id = rate_plan_inst_clt_cert_response_body.instance_id,
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
    def clt_cert(
        site_clt_cert_response_body: esa20240910_models.CreateSiteResponseBody,
        client: ESA20240910Client,
    ) -> esa20240910_models.CreateClientCertificateResponseBody:
        logging.log(logging.INFO, 'Begin Call CreateClientCertificate to create resource')
        create_client_certificate_request = esa20240910_models.CreateClientCertificateRequest(
            site_id = site_clt_cert_response_body.site_id,
            pkey_type = 'RSA',
            validity_days = 365
        )
        create_client_certificate_response = client.create_client_certificate(create_client_certificate_request)
        logging.log(logging.INFO, 'Call CreateClientCertificate success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(create_client_certificate_response))
        return create_client_certificate_response.body

    @staticmethod
    async def clt_cert_async(
        site_clt_cert_response_body: esa20240910_models.CreateSiteResponseBody,
        client: ESA20240910Client,
    ) -> esa20240910_models.CreateClientCertificateResponseBody:
        logging.log(logging.INFO, 'Begin Call CreateClientCertificate to create resource')
        create_client_certificate_request = esa20240910_models.CreateClientCertificateRequest(
            site_id = site_clt_cert_response_body.site_id,
            pkey_type = 'RSA',
            validity_days = 365
        )
        create_client_certificate_response = await client.create_client_certificate_async(create_client_certificate_request)
        logging.log(logging.INFO, 'Call CreateClientCertificate success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(create_client_certificate_response))
        return create_client_certificate_response.body

    @staticmethod
    def update_clt_cert(
        site_clt_cert_response_body: esa20240910_models.CreateSiteResponseBody,
        create_client_certificate_response_body: esa20240910_models.CreateClientCertificateResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call RevokeClientCertificate to update resource')
        revoke_client_certificate_request = esa20240910_models.RevokeClientCertificateRequest(
            site_id = site_clt_cert_response_body.site_id,
            id = create_client_certificate_response_body.id
        )
        revoke_client_certificate_response = client.revoke_client_certificate(revoke_client_certificate_request)
        logging.log(logging.INFO, 'Call RevokeClientCertificate success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(revoke_client_certificate_response))

    @staticmethod
    async def update_clt_cert_async(
        site_clt_cert_response_body: esa20240910_models.CreateSiteResponseBody,
        create_client_certificate_response_body: esa20240910_models.CreateClientCertificateResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call RevokeClientCertificate to update resource')
        revoke_client_certificate_request = esa20240910_models.RevokeClientCertificateRequest(
            site_id = site_clt_cert_response_body.site_id,
            id = create_client_certificate_response_body.id
        )
        revoke_client_certificate_response = await client.revoke_client_certificate_async(revoke_client_certificate_request)
        logging.log(logging.INFO, 'Call RevokeClientCertificate success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(revoke_client_certificate_response))

    @staticmethod
    def update_clt_cert_1(
        site_clt_cert_response_body: esa20240910_models.CreateSiteResponseBody,
        create_client_certificate_response_body: esa20240910_models.CreateClientCertificateResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call ActivateClientCertificate to update resource')
        activate_client_certificate_request = esa20240910_models.ActivateClientCertificateRequest(
            site_id = site_clt_cert_response_body.site_id,
            id = create_client_certificate_response_body.id
        )
        activate_client_certificate_response = client.activate_client_certificate(activate_client_certificate_request)
        logging.log(logging.INFO, 'Call ActivateClientCertificate success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(activate_client_certificate_response))

    @staticmethod
    async def update_clt_cert_1_async(
        site_clt_cert_response_body: esa20240910_models.CreateSiteResponseBody,
        create_client_certificate_response_body: esa20240910_models.CreateClientCertificateResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call ActivateClientCertificate to update resource')
        activate_client_certificate_request = esa20240910_models.ActivateClientCertificateRequest(
            site_id = site_clt_cert_response_body.site_id,
            id = create_client_certificate_response_body.id
        )
        activate_client_certificate_response = await client.activate_client_certificate_async(activate_client_certificate_request)
        logging.log(logging.INFO, 'Call ActivateClientCertificate success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(activate_client_certificate_response))

    @staticmethod
    def update_clt_cert_2(
        site_clt_cert_response_body: esa20240910_models.CreateSiteResponseBody,
        create_client_certificate_response_body: esa20240910_models.CreateClientCertificateResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call RevokeClientCertificate to update resource')
        revoke_client_certificate_request = esa20240910_models.RevokeClientCertificateRequest(
            site_id = site_clt_cert_response_body.site_id,
            id = create_client_certificate_response_body.id
        )
        revoke_client_certificate_response = client.revoke_client_certificate(revoke_client_certificate_request)
        logging.log(logging.INFO, 'Call RevokeClientCertificate success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(revoke_client_certificate_response))

    @staticmethod
    async def update_clt_cert_2_async(
        site_clt_cert_response_body: esa20240910_models.CreateSiteResponseBody,
        create_client_certificate_response_body: esa20240910_models.CreateClientCertificateResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call RevokeClientCertificate to update resource')
        revoke_client_certificate_request = esa20240910_models.RevokeClientCertificateRequest(
            site_id = site_clt_cert_response_body.site_id,
            id = create_client_certificate_response_body.id
        )
        revoke_client_certificate_response = await client.revoke_client_certificate_async(revoke_client_certificate_request)
        logging.log(logging.INFO, 'Call RevokeClientCertificate success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(revoke_client_certificate_response))

    @staticmethod
    def destroy_clt_cert(
        site_clt_cert_response_body: esa20240910_models.CreateSiteResponseBody,
        create_client_certificate_response_body: esa20240910_models.CreateClientCertificateResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call DeleteClientCertificate to destroy resource')
        delete_client_certificate_request = esa20240910_models.DeleteClientCertificateRequest(
            site_id = site_clt_cert_response_body.site_id,
            id = create_client_certificate_response_body.id
        )
        delete_client_certificate_response = client.delete_client_certificate(delete_client_certificate_request)
        logging.log(logging.INFO, 'Call DeleteClientCertificate success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(delete_client_certificate_response))

    @staticmethod
    async def destroy_clt_cert_async(
        site_clt_cert_response_body: esa20240910_models.CreateSiteResponseBody,
        create_client_certificate_response_body: esa20240910_models.CreateClientCertificateResponseBody,
        client: ESA20240910Client,
    ) -> None:
        logging.log(logging.INFO, 'Begin Call DeleteClientCertificate to destroy resource')
        delete_client_certificate_request = esa20240910_models.DeleteClientCertificateRequest(
            site_id = site_clt_cert_response_body.site_id,
            id = create_client_certificate_response_body.id
        )
        delete_client_certificate_response = await client.delete_client_certificate_async(delete_client_certificate_request)
        logging.log(logging.INFO, 'Call DeleteClientCertificate success, response: ')
        logging.log(logging.INFO, UtilClient.to_jsonstring(delete_client_certificate_response))

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
        rate_plan_inst_clt_cert_resp_body = Sample.rate_plan_inst_clt_cert(esa_20240910client)
        site_clt_cert_resp_body = Sample.site_clt_cert(rate_plan_inst_clt_cert_resp_body, esa_20240910client)
        clt_cert_resp_body = Sample.clt_cert(site_clt_cert_resp_body, esa_20240910client)
        # update resource
        Sample.update_clt_cert(site_clt_cert_resp_body, clt_cert_resp_body, esa_20240910client)
        Sample.update_clt_cert_1(site_clt_cert_resp_body, clt_cert_resp_body, esa_20240910client)
        Sample.update_clt_cert_2(site_clt_cert_resp_body, clt_cert_resp_body, esa_20240910client)
        # destroy resource
        Sample.destroy_clt_cert(site_clt_cert_resp_body, clt_cert_resp_body, esa_20240910client)

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
        rate_plan_inst_clt_cert_resp_body = await Sample.rate_plan_inst_clt_cert_async(esa_20240910client)
        site_clt_cert_resp_body = await Sample.site_clt_cert_async(rate_plan_inst_clt_cert_resp_body, esa_20240910client)
        clt_cert_resp_body = await Sample.clt_cert_async(site_clt_cert_resp_body, esa_20240910client)
        # update resource
        await Sample.update_clt_cert_async(site_clt_cert_resp_body, clt_cert_resp_body, esa_20240910client)
        await Sample.update_clt_cert_1_async(site_clt_cert_resp_body, clt_cert_resp_body, esa_20240910client)
        await Sample.update_clt_cert_2_async(site_clt_cert_resp_body, clt_cert_resp_body, esa_20240910client)
        # destroy resource
        await Sample.destroy_clt_cert_async(site_clt_cert_resp_body, clt_cert_resp_body, esa_20240910client)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
