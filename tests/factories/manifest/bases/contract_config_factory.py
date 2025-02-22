import factory

from tidy.manifest.bases.contract_config import ContractConfig


class ContractConfigFactory(factory.Factory):
    class Meta:
        model = ContractConfig

    checksum = factory.Faker("sha256")
