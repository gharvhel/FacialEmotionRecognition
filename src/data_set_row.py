from src.image import Image


class DataSetRow:
    def __init__(self, emotion, pixels, partition):
        self.emotion = emotion
        self.image = Image(pixels)
        self.partition = partition

    def __str__(self):
        return self.to_csv()

    def to_csv(self):
        return ','.join([self.emotion.name, str(self.image), self.partition.name])
