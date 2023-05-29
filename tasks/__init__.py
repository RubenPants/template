"""Package tasks."""

from invoke import Collection

from tasks.logging import configure_root_logger
from tasks.tasks import lab, lint, test

configure_root_logger()

ns = Collection()
ns.add_task(lab)
ns.add_task(lint)
ns.add_task(test)
