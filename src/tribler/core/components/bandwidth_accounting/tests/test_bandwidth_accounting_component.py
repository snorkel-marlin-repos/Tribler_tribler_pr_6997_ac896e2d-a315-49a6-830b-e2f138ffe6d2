import pytest

from tribler.core.components.bandwidth_accounting.bandwidth_accounting_component import BandwidthAccountingComponent
from tribler.core.components.base import Session
from tribler.core.components.ipv8.ipv8_component import Ipv8Component
from tribler.core.components.key.key_component import KeyComponent

# pylint: disable=protected-access


@pytest.mark.asyncio
@pytest.mark.no_parallel
async def test_bandwidth_accounting_component(tribler_config):
    components = [KeyComponent(), Ipv8Component(), BandwidthAccountingComponent()]
    async with Session(tribler_config, components).start():
        comp = BandwidthAccountingComponent.instance()
        assert comp.started_event.is_set() and not comp.failed
        assert comp.community
        assert comp._ipv8_component
