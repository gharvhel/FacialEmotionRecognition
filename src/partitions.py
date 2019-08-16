from aenum import MultiValueEnum


class Partitions(MultiValueEnum):
    Training = 'Training'
    Test = 'PrivateTest', 'PublicTest'
