import asyncio


@asyncio.coroutine
def handle_echo(self, reader, writer):
    pass


loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, "127.0.0.1", 8888, loop=loop)
server = loop.run_until_complete(coro)
print("server: {}".format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass


server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
