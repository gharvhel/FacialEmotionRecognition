from src.constants import DATA_SET1_PATH, DATA_SET2_PATH, DATA_SET3_PATH, DATA_SET4_PATH
from src.data_set_row import DataSetRow
from src.emotions import Emotions
from src.partitions import Partitions


class DataSet:
    def __init__(self, csv_file_paths):
        """
        Training and Test data set
        :param csv_file_paths: list of data set paths
        """
        self.training_set = []
        self.test_set = []
        self.combine_fer2013_data_set(csv_file_paths)

    def combine_fer2013_data_set(self, csv_file_paths):
        """
        Combines the separated fer2013 data set
        :param csv_file_paths: list of data set paths
        :return: Nothing
        """
        for csv_file_path in csv_file_paths:
            csv_file = open(csv_file_path, 'r')
            csv_file_lines = csv_file.readlines()
            for line in csv_file_lines:
                line = line.strip()
                emotion_number, pixels, partition = line.split(',')
                data_set_row = DataSetRow(Emotions(emotion_number), pixels, Partitions(partition))
                if Partitions(partition) == Partitions.Training:
                    self.training_set.append(data_set_row)
                elif Partitions(partition) == Partitions.Test:
                    self.test_set.append(data_set_row)


DATA_SET = DataSet([DATA_SET1_PATH, DATA_SET2_PATH, DATA_SET3_PATH, DATA_SET4_PATH])
