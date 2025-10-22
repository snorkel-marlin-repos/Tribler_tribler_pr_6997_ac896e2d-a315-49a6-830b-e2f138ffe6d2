import pytest

from tribler.core.components.base import Session
from tribler.core.components.ipv8.ipv8_component import Ipv8Component
from tribler.core.components.key.key_component import KeyComponent
from tribler.core.components.libtorrent.libtorrent_component import LibtorrentComponent
from tribler.core.components.metadata_store.metadata_store_component import MetadataStoreComponent
from tribler.core.components.socks_servers.socks_servers_component import SocksServersComponent
from tribler.core.components.tag.tag_component import TagComponent
from tribler.core.components.torrent_checker.torrent_checker_component import TorrentCheckerComponent


# pylint: disable=protected-access
@pytest.mark.asyncio
@pytest.mark.no_parallel
async def test_torrent_checker_component(tribler_config):
    components = [SocksServersComponent(), LibtorrentComponent(), KeyComponent(),
                  Ipv8Component(), TagComponent(), MetadataStoreComponent(), TorrentCheckerComponent()]
    async with Session(tribler_config, components).start():
        comp = TorrentCheckerComponent.instance()
        assert comp.started_event.is_set() and not comp.failed
        assert comp.torrent_checker
