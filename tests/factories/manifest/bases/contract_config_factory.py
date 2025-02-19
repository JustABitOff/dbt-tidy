from factory import Factory

from tidy.manifest.bases.contract_config import ContractConfig


class ContractConfigFactory(Factory):
    class Meta:
        model = ContractConfig