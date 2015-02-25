import fff_dqmtools
import fff_cluster
import fff_deleter
import logging

@fff_dqmtools.fork_wrapper(__name__)
@fff_cluster.host_wrapper(allow = ["bu-c2f13-31-01"])
@fff_dqmtools.lock_wrapper
def __run__(opts, **kwargs):
    log = kwargs["logger"]

    ramdisk = "/fff/output/transfer/"
    tag = "fff_deleter_transfer"

    service = fff_deleter.FileDeleter(
        top = ramdisk,
        app_tag = tag,
        thresholds = {
            'rename': 60,
            'delete': 80,
        },
        log = log,
        report_directory = opts["path"],
        fake = opts["deleter.fake"],
    )
    service.delay_seconds = 15*60

    service.run_greenlet()
