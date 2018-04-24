from aiohttp import web


class WorkerConnection(object):
    def __init__(self, connection: web.WebSocketResponse):
        """Creates bot with 0 tasks and provided connection"""

        self._connection = connection
        self.tasks = 0

    async def send_task(self, task: dict):
        """Sends a task to the bot in JSON encoded string"""

        await self._connection.send_json(task)