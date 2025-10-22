import pytest

from tribler.core.components.base import Session
from tribler.core.components.gigachannel_manager.gigachannel_manager_component import GigachannelManagerComponent
from tribler.core.components.ipv8.ipv8_component import Ipv8Component
from tribler.core.components.key.key_component import KeyComponent
from tribler.core.components.libtorrent.libtorrent_component import LibtorrentComponent
from tribler.core.components.metadata_store.metadata_store_component import MetadataStoreComponent
from tribler.core.components.socks_servers.socks_servers_component import SocksServersComponent
from tribler.core.components.tag.tag_component import TagComponent

# pylint: disable=protected-access


@pytest.mark.asyncio
@pytest.mark.no_parallel
async def test_gigachannel_manager_component(tribler_config):
    components = [Ipv8Component(), TagComponent(), SocksServersComponent(), KeyComponent(), MetadataStoreComponent(),
                  LibtorrentComponent(), GigachannelManagerComponent()]
    async with Session(tribler_config, components).start():
        comp = GigachannelManagerComponent.instance()
        assert comp.started_event.is_set() and not comp.failed
        assert comp.gigachannel_manager
