# from git import Repo
from dvc.api import DVCFileSystem
from dvc.repo import Repo

if __name__ == '__main__':
    tag = '0.0.5'
    repo = Repo('/Users/gpistre/Density/dvc-test-repo/',
                rev=tag
                )
    fs = DVCFileSystem(repo=repo)
    # fs.open('images/test/0/00004.png')
    # print(fs.ls('./images/test/0'))
    # fs.open('./data_from_repo/titanic_train.csv')
    # fs.open('./data_from_registry/titanic_train.csv')
    print(fs.ls('./data_from_registry'))
    # print(fs.find("/", detail=False, dvc_only=True))
