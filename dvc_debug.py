import pandas as pd
import numpy as np
from git import Repo
from dvc.api import DVCFileSystem


if __name__ == '__main__':
    tag = '1.3.2'
    repo = Repo('../../')
    # fs = DVCFileSystem('git@github.com:DensityCo/mmwave-tracker.git')
    # fs = DVCFileSystem('https://github.com/DensityCo/dvc-data-registry', rev=tag if tag != 'workspace' else None)
    fs = DVCFileSystem('.', rev='0.1.32')
    # fs = DVCFileSystem('/Users/gpistre/Density/dvc-data-registry')
    # fs.find("/", detail=False, dvc_only=True)
    print()
