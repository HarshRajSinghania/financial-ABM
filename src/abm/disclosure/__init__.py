"""Multi-asset market for disclosure games: firms with a true and a reported
attribute, investors who may price the reported attribute, and a regulator.

The core is domain-free. A domain is a JSON specification under
``configs/domains/`` loaded by ``domain.py``; nothing in the core modules
names a particular domain.
"""

from .config import MarketConfig, load_market_config
from .harness import CrossSectionMarket, CrossSectionResult, run_market

__all__ = [
    "CrossSectionMarket",
    "CrossSectionResult",
    "MarketConfig",
    "load_market_config",
    "run_market",
]
