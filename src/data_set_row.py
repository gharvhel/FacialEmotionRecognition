class DataSetRow:
    def __init__(self, emotion, image, partition):
        self.emotion = emotion
        self.image = image
        self.partition = partition

    def __str__(self):
        return self.to_csv()

    def to_csv(self):
        return ','.join([self.emotion.name, self.image, self.partition.name])
