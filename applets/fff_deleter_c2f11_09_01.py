import fff_dqmtools
import fff_cluster
import fff_deleter
import logging

@fff_cluster.host_wrapper(allow = ["bu-c2f11-09-01"])
@fff_dqmtools.fork_wrapper(__name__)
@fff_dqmtools.lock_wrapper
def __run__(opts, **kwargs):
    log = kwargs["logger"]

    ramdisk = "/fff/ramdisk/"
    tag = "fff_deleter_c2f11_09_01"

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
    service.delay_seconds = 30

    service.run_greenlet()

