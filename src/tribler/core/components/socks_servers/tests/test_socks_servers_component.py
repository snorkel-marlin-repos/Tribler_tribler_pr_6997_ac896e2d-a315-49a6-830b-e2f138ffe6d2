import pytest

from tribler.core.components.base import Session
from tribler.core.components.socks_servers.socks_servers_component import SocksServersComponent


# pylint: disable=protected-access
@pytest.mark.asyncio
@pytest.mark.no_parallel
async def test_socks_servers_component(tribler_config):
    components = [SocksServersComponent()]
    async with Session(tribler_config, components).start():
        comp = SocksServersComponent.instance()
        assert comp.started_event.is_set() and not comp.failed
        assert comp.socks_ports
        assert comp.socks_servers
