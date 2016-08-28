import os
import inspect
import string

from . import logger
from . import exc


def free_path(dir, ext='', prefix=''):
    ''' 
      Finds unexisted path inside the given directory  
      
      Parameters
      ----------
        dir     <str>  Dir to findings. If dir not exists - will be raised DirNotEixstsError exception
        ext     <str>  File extension (with '.' or without it)
        prefix  <str>  File name prefix
    '''

    assert isinstance(dir,    str)
    assert isinstance(ext,    str)
    assert isinstance(prefix, str)

    dir = os.path.expanduser(dir)
    dir = os.path.expandvars(dir)

    if not os.path.exists(dir): 
        raise exc.DirNotEixstsError(dir)

    while True: 
        filename = __random_filename(ext=ext, prefix=prefix)
        abs_path = os.path.abspath(os.path.join(dir, filename))

        if not os.path.exists(abs_path): 
            return abs_path
    

def __random_filename(ext, prefix='', rnd_key_len=16): 
    '''
      Generates random filename in the format: {prefix}{key}.{ext} 

      Parameters
      ----------
        ext          <str>  Generated filename extension (with '.' or without it)
        prefix       <str>  Generated filename prefix
        rnd_key_len  <int>  Length of the random part of the generated filename 
    '''

    assert isinstance(ext,         str)
    assert isinstance(prefix,      str)
    assert isinstance(rnd_key_len, int)
    assert rnd_key_len >= 0

    if '.' in prefix: 
        tmpl = '[{file}:{line} {func}] Detected \'.\' in filename prefix - be carefull'
        stack_frame = inspect.stack()[0]

        logger.warning(tmpl.format(file=stack_frame.filename, 
                                   line=stack_frame.lineno,
                                   func=stack_frame.function))


    key = ''.join([random.choice(string.hexdigits) for _ in range(rnd_key_len)])

    return '{prefix}{key}{ext}'.format(prefix=prefix, key=key, ext=ext)