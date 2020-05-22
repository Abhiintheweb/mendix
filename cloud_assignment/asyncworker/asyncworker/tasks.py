from asyncworker.celery import app


@app.task
def merge_s3_files():
    """Async task to download files from S3, merge them and upload the result.

    The lines in the merged file should be ordered.
    """
    return "dummy-value"
