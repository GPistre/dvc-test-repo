# from git import Repo
from dvc.api import DVCFileSystem
from dvc.repo import Repo

if __name__ == '__main__':
    tag = '0.0.4'
    repo = Repo('/Users/gpistre/Density/dvc-test-repo/',
                rev=tag
                )
    fs = DVCFileSystem(repo=repo)
    print(fs.ls('./images'))
    # print(fs.ls('./data_from_registry'))
    # print(fs.find("/", detail=False, dvc_only=True))
