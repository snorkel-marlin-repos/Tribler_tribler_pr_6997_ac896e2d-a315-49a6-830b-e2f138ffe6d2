import pytest

from tribler.core.components.base import Session
from tribler.core.components.ipv8.ipv8_component import Ipv8Component
from tribler.core.components.key.key_component import KeyComponent
from tribler.core.components.metadata_store.metadata_store_component import MetadataStoreComponent
from tribler.core.components.tag.tag_component import TagComponent

# pylint: disable=protected-access


@pytest.mark.asyncio
@pytest.mark.no_parallel
async def test_metadata_store_component(tribler_config):
    components = [TagComponent(), Ipv8Component(), KeyComponent(), MetadataStoreComponent()]
    async with Session(tribler_config, components).start():
        comp = MetadataStoreComponent.instance()
        assert comp.started_event.is_set() and not comp.failed
        assert comp.mds
