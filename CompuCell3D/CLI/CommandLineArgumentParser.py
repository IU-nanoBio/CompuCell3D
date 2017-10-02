import argparse
import ProjectFileStore

class CommandLineArgumentParser:

    def __init__(self):
        self.__argumentParser =  None
        self.__isInitialized = False


    def initialize(self):
        """
        This method initialized creates the argument parser and and initializes with the arguments.

        :return: None
        """
        argumentParser = argparse.ArgumentParser(description='*** CompuCell3D Command-Line Interface ***')

        argumentParser.add_argument('-i', '--input', required=True, action='store',
                                    help='path to the CC3D project file (*.cc3d)')

        argumentParser.add_argument('-o', '--outputDir', required=True, action='store',
                                    help='output directory path to store results')

        argumentParser.add_argument('-f', '--outputFrequency', required=False, action='store', default=1, type=int,
                                    help='simulation snapshot output frequency')

        self.__argumentParser = argumentParser
        self.__isInitialized = True

    def parseArguments(self):
        """
        This method uses the parser created in the initialize method and parse the arguments
        and store the arguments in specified variables

        :return: None
        """
        if not self.__isInitialized:
            self.initialize()

        arguments = self.__argumentParser.parse_args()

        ProjectFileStore.projectFilePath = arguments.input
        ProjectFileStore.outputDirectoryPath = arguments.outputDir
        ProjectFileStore.outputFrequency = arguments.outputFrequency