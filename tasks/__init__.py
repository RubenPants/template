"""Package tasks."""

from invoke import Collection

from tasks.logging import configure_root_logger
from tasks.tasks import app, docs, lab, lint, test

configure_root_logger()

ns = Collection()
ns.add_task(app)
ns.add_task(docs)
ns.add_task(lab)
ns.add_task(lint)
ns.add_task(test)
