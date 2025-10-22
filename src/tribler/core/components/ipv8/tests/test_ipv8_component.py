import pytest

from tribler.core.components.base import Session
from tribler.core.components.ipv8.ipv8_component import Ipv8Component
from tribler.core.components.key.key_component import KeyComponent


# pylint: disable=protected-access
@pytest.mark.asyncio
@pytest.mark.no_parallel
async def test_ipv8_component(tribler_config):
    async with Session(tribler_config, [KeyComponent(), Ipv8Component()]).start():
        comp = Ipv8Component.instance()
        assert comp.started_event.is_set() and not comp.failed
        assert comp.ipv8
        assert comp.peer
        assert not comp.dht_discovery_community
        assert comp._task_manager
        assert not comp._peer_discovery_community


@pytest.mark.asyncio
@pytest.mark.no_parallel
async def test_ipv8_component_dht_disabled(tribler_config):
    tribler_config.ipv8.enabled = True
    tribler_config.dht.enabled = True
    async with Session(tribler_config, [KeyComponent(), Ipv8Component()]).start():
        comp = Ipv8Component.instance()
        assert comp.dht_discovery_community


@pytest.mark.asyncio
@pytest.mark.no_parallel
async def test_ipv8_component_discovery_community_enabled(tribler_config):
    tribler_config.ipv8.enabled = True
    tribler_config.gui_test_mode = False
    tribler_config.discovery_community.enabled = True
    async with Session(tribler_config, [KeyComponent(), Ipv8Component()]).start():
        comp = Ipv8Component.instance()
        assert comp._peer_discovery_community
