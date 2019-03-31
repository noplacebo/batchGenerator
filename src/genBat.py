import os
import yaml

EXTENSION = ".bat"
CONFIG_FILE = "config.yml"
PACKAGES = [
    "progression",
    "amptest"
]
VERSIONS = [
    "deploy",
    "dev",
    "staging"
]


class Generator:
    """

    """
    def __init__(self, config_file, package, version, python='default', verbose=False, architecture=64):
        with open(config_file, 'r') as input_file:
            self.config = yaml.load(input_file, Loader=yaml.FullLoader)
        assert package.lower() in PACKAGES
        self.package = package.lower()
        assert version.lower() in VERSIONS
        self.version = version.lower()
        if python == 'default':
            self.python = self.config[package][version]['python']
        else:
            self.python = python
        self.archtecture = architecture
        self.verbose = verbose

    def generate_batch(self, path=None, filename=None):
        if path is None:
            path = os.getcwd()
        if filename is None:
            filename = '_'.join([self.package, self.version, str(self.python), str(self.archtecture)])
            filename += EXTENSION
        print(path)
        print(filename)


for pack in PACKAGES:
    for ver in VERSIONS:
        try:
            test = Generator(CONFIG_FILE, pack, ver)
            test.generate_batch()
        except Exception:
            pass
