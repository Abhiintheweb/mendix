import logging

from asyncworker.tasks import merge_s3_files
from pyramid.view import view_config


logger = logging.getLogger(__name__)


@view_config(route_name="initiate", renderer="json", request_method="POST")
def initiate(request):
    """This function is called when a POST request is made to /initiate.

    According to the assignment the expected POST input is:
    {
        "start_date": "<date in ISO8601 format>",
        "end_date": "<date in ISO8601 format>"
    }
    For example:
    {
        "start_date": "2019-08-18",
        "end_date": "2019-08-25"
    }

    The function should initiate the merging of files on S3 with names between
    the given dates. The actual merging should be offloaded to the async
    executor service.

    The return data is a download ID that the /download endpoint digests:
    {
        "download_id": "<id>"
    }
    For example:
    {
        "download_id": "b0952099-3536-4ea0-a613-98509f4087cd"
    }
    """
    logger.info("Initiate called")
    task_result = merge_s3_files.delay()
    logger.info("Task result is %s", task_result.get())
    return {"route": "initiate"}


@view_config(route_name="download", renderer="json")
def download(request):
    """This function is called when a GET request is made to /download.

    According to the assignment this endpoint accepts the dowload ID as a URL
    parameter and returns the merged file for download if the merging is done.
    If the merging is not done yet, the appropriate HTTP code is returned, so
    the calling client can continue polling.
    """
    logger.info("Download called")
    return {"route": "download"}
