
import logging

class ServiceHandler(object):
    def __init__(self, service, exclusion=True):
        self._service = service
        self._handlers = []
        self._enable_exclusion = exclusion

    def collect_alive_thread(self):
        new_handlers = []
        for service in self._handlers:
            if service.is_alive():
                new_handlers.append(service)

        self._handlers = new_handlers


    def start(self):
        self.collect_alive_thread()

        if not self._enable_exclusion or len(self._handlers) == 0:
            logging.debug("running new thread")
            service_handler = self._service()
            service_handler.start()
            self._handlers.append(service_handler)

        else:
            logging.debug("thread is lock")
