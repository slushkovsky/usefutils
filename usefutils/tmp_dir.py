import os
import shutil

from . import logger


class TmpDir(object): 
    def __init__(self, dir): 
        assert os.path.exists(dir) # TODO exception

        self.path = os.path.join(dir, free_path(dir))

    def __enter__(self):
        assert not os.path.exists(self.path)
        
        logger.debug('Created tmp dir: {}'.format(self.path))
        os.mkdir(self.path)

        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb): 
        assert os.path.exists(self.path)

        shutil.rmtree(self.path)
        logger.debug('Tmp dir removed: {}'.format(self.path))