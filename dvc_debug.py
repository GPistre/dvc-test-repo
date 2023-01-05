from git import Repo
from dvc.api import DVCFileSystem


if __name__ == '__main__':
    tag = '0.0.1'
    fs = DVCFileSystem('.', rev=tag)
    fs.ls('./data_from_repo')
    # print(fs.find("/", detail=False, dvc_only=True))
