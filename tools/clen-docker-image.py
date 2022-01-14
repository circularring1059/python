from operator import itemgetter
from urllib import parse
import requests
import json

import datetime
# import maya

import logging

logging.basicConfig(filename='harbor_clean.txt', filemode="w", level=logging.INFO)

logger = logging.getLogger(__name__)

"""
清理 Harbor 仓库的老镜像
"""


class HarborCleaner(object):
    delete_status = {
        200: "Delete tag successfully.",
        400: "Invalid repo_name.",
        401: "Unauthorized.",
        403: "Forbidden.",
        404: "Repository or tag not found.",
    }

    def __init__(self, user: str, password: str, hostname: str, port: int, use_https=True):
        scheme = "https" if use_https else "http"
        api_base = f"{scheme}://{hostname}:{port}/api/v2.0"
        self.search_api = api_base + "/search?q={key_word}"
        self.projects_api = api_base + "/projects"
        self.repository_query_api = api_base + "/projects/{project}/repositories"
        # repo_name 一般为 "project_name/repo_name" 格式，必须做转义处理（因为中间有斜杠）
        self.repository_tags_api = api_base + "/projects/{project}/repositories/{repo}/artifacts"
        self.repository_tag_api = self.repository_tags_api + "/{tag}"

        self.session = requests.Session()
        # self.session.verify = False  # 如果公司是使用自签名证书，不能通过 SSL 验证，就需要设置这个
        self.session.headers = {
            "Accept": "application/json"
        }

        self.session.auth = (user, password)
    #
    # def get_all_projects(self):
    #     resp = self.session.get(self.projects_api)
    #
    #     success = resp.status_code == 200
    #     for i in resp.json():
    #         if i.get("metadata").get("public") == "false":
    #             print(i.get("name"), i.get("project_id"))
    #
    #     return {
    #         "success": success,
    #         "data": resp.json() if success else resp.text
    #     }

    def delete_tag(self):
        print("**")
        print(self.session.delete("https://harbor.ricequant.com/api/v2.0/projects/wz/repositories/nginx/artifacts/sha256:d34ba54b4dfdb8a2adacd44927633395406593b7680524bd28b62add466f4bed/tags?with_signature=true&with_immutable_status=true&page_size=15&page=1"))

    def get_all_repos(self, project: str):
        j = 1
        repo = []
        while True:
            url = self.repository_query_api.format(project=project) + "?page={}".format(j)
            resp = self.session.get(url)
            j += 1
            if not resp.json():
                break
            for i in resp.json():
                repo.append(i.get("name").split("/", 1)[1])
        return repo

    def get_all_tags(self, project, repo_name,n):
        """repo_name 需要做转义"""
        # repo_name = self.get_all_repos(project)
        repo_name = repo_name.replace("/", "%252F")
        i, tag = 1, []
        while True:
            url = self.repository_tags_api.format(project=project, repo=repo_name) + "?with_signature=true&with_immutable_status=true&page_size=8&page={}".format(i)
            resp = self.session.get(url)
            i += 1
            if not resp.json():
                break
            tag.extend([i for i in resp.json() if i.get("tags")])
        print(len(tag))
        if len(tag) <= n:
            return None
        return sorted(tag, key=lambda x:datetime.datetime.strptime(x["tags"][0]["pull_time"], r'%Y-%m-%dT%H:%M:%S.%fZ'))[0:len(tag)-n]

    def get_tags_except_lastest_n(self, repo, n: int):
        """获取除了最新的 n 个 tag 之外的所有 tags"""

        # 如果 镜像 tags 数小于 n+1，说明该镜像很干净，不需要做清理。
        tags = self.get_all_tags(repo, n)
        # print(tags["nginx"][0]["tags"])
        print(tags["nginx"])
        for tag  in tags:
            # print(tags[tag][0]["tags"][0]["pull_time"])
            print(tag)
            tagss = sorted(tags[tag], key=lambda x: datetime.datetime.strptime(x["tags"][0]["pull_time"], r'%Y-%m-%dT%H:%M:%S.%fZ'), )
            print({tag:tagss})
        # if repo['tags_count'] <= n + 1:  # +1 是因为 latest 是重复的 tag
        #     return []

        # result = self.get_all_tags(repo)
        # tags: list = result['data']
        # for tag in tags:
        #     # tag['time'] = maya.MayaDT.from_iso8601(tag['created'])
        #
        #     # '2019-04-09T11:33:49.296960745Z'
        #     # # python 自带的解析函数，只能处理 6 位小数，下面截去多余的三位
        #     timestamp = tag['created'][:-4] + 'Z'
        #     tag['time'] = dt.datetime.strptime(timestamp, r'%Y-%m-%dT%H:%M:%S.%fZ')
        #
        # tags.sort(key=itemgetter('time'))  # 使用 time 键进行原地排序
        # return tags[:-n - 1]  # expect the latest n tags, -1 是因为 latest 是重复的 tag

    def soft_delete_tag(self, repo: dict, tag: dict):
        """repo_name 需要做转义
        这里删除后，还需要进行一次 GC，才能真正地清理出可用空间。
        """
        repo_name = parse.quote(repo['name'], safe="")
        url = self.repository_tag_api.format(repo_name=repo_name, tag=tag['name'])
        resp = self.session.delete(url)

        return {
            "success": resp.status_code == 200,
            "message": self.delete_status.get(resp.status_code)
        }

    # def soft_delete_all_tags_except_latest_n(self, n):
    #     """从每个仓库中，删除所有的 tags，只有最新的 n 个 tag 外的所有 tags 除外"""
    #     res_projects = self.get_all_projects()
    #     if not res_projects['success']:
    #         logger.warning("faild to get all projects, message: {}".format(res_projects['data']))
    #
    #     logger.info("we have {} projects".format(len(res_projects['data'])))
    #     for p in res_projects['data']:
    #         res_repos = self.get_all_repos(p)
    #         if not res_projects['success']:
    #             logger.warning(
    #                 "faild to get all repos in project: {}, message: {}".format(p['name'], res_repos['data']))
    #
    #         logger.info("we have {} repos in project:{}".format(len(res_repos['data']), p['name']))
    #         for repo in res_repos['data']:
    #             logger.info("deal with repo: {}".format(repo['name']))
    #
    #             old_tags = self.get_tags_except_lastest_n(repo, n)
    #             logger.info("we have {} tags to delete in repo: {}".format(len(old_tags), repo['name']))
    #             for tag in old_tags:
    #                 logger.info("try to delete repo:{}, tag: {}, create_time: {}".format(repo['name'], tag['name'],
    #                                                                                      tag['created']))
    #                 result = self.soft_delete_tag(repo, tag)
    #                 if result['success']:
    #                     logger.info("success delete it.")
    #                 else:
    #                     logger.warning("delete failed!, message: {}".format(result['message']))


if __name__ == "__main__":
    # 1. 通过 harbor 的 restful api 进行软删除
    harbor_cleaner = HarborCleaner(
        user="wz",
        password="Weizhong123",
        hostname="harbor.ricequant.com",
        port=443
    )
    # harbor_cleaner.soft_delete_all_tags_except_latest_n(10)  # 每个镜像只保留最新的十个 tag
    # print(harbor_cleaner.get_all_projects())
    # print(harbor_cleaner.get_all_repos("newdaq"))
    # print(harbor_cleaner.get_all_tags("wz", "nginx", 4))
    # harbor_cleaner.get_tags_except_lastest_n("newdaq", 1)
    harbor_cleaner.delete_tag()

# s = [{'addition_links': {'build_history': {'absolute': False, 'href': '/api/v2.0/projects/newdaq/repositories/market-search/artifacts/sha256:86a0a7cc99bbb47353c07eb0070c2178088dc90fd24bb384fd2b0e740e9774d1/additions/build_history'}, 'vulnerabilities': {'absolute': False, 'href': '/api/v2.0/projects/newdaq/repositories/market-search/artifacts/sha256:86a0a7cc99bbb47353c07eb0070c2178088dc90fd24bb384fd2b0e740e9774d1/additions/vulnerabilities'}}, 'digest': 'sha256:86a0a7cc99bbb47353c07eb0070c2178088dc90fd24bb384fd2b0e740e9774d1', 'extra_attrs': {'architecture': 'amd64', 'author': 'Ryan <zhang.rui@ricequant.com>', 'config': {'Entrypoint': ['/bin/sh', '-c', 'uvicorn market_search.main:app --host $SERVER_HOST --port $SERVER_PORT --workers $WORKERS     --log-config /tmp/logging_config.json'], 'Env': ['PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'LC_ALL=en_US.UTF-8', 'LANG=en_US.UTF-8', 'LANGUAGE=en_US.UTF-8', 'TZ=Asia/Shanghai', 'PYTHONIOENCODING=utf-8', 'PYTHONOPTIMIZE=1', 'LD_PRELOAD=/usr/lib64/libjemalloc.so.2', 'PIP_DISABLE_PIP_VERSION_CHECK=true', 'PIP_NO_CACHE_DIR=true', 'PIP_DISABLE_CACHE=true', 'PIP_INDEX_URL=https://pypi.douban.com/simple', 'PIP_DEFAULT_TIMEOUT=60', 'WORKERS=2', 'SERVER_HOST=0.0.0.0', 'SERVER_PORT=12033'], 'Labels': {'org.label-schema.build-date': '20200504', 'org.label-schema.license': 'GPLv2', 'org.label-schema.name': 'CentOS Base Image', 'org.label-schema.schema-version': '1.0', 'org.label-schema.vendor': 'CentOS', 'org.opencontainers.image.created': '2020-05-04 00:00:00+01:00', 'org.opencontainers.image.licenses': 'GPL-2.0-only', 'org.opencontainers.image.title': 'CentOS Base Image', 'org.opencontainers.image.vendor': 'CentOS'}, 'User': 'rice', 'WorkingDir': '/tmp'}, 'created': '2021-12-14T06:41:51.414619883Z', 'os': 'linux'}, 'icon': 'sha256:0048162a053eef4d4ce3fe7518615bef084403614f8bca43b40ae2e762e11e06', 'id': 5813, 'labels': None, 'manifest_media_type': 'application/vnd.docker.distribution.manifest.v2+json', 'media_type': 'application/vnd.docker.container.image.v1+json', 'project_id': 19, 'pull_time': '2022-01-06T07:48:37.800Z', 'push_time': '2022-01-06T07:48:32.671Z', 'references': None, 'repository_id': 807, 'size': 290510713, 'tags': [{'artifact_id': 5813, 'id': 5789, 'immutable': False, 'name': '0.0.1.post1.dev24.gd020c0e', 'pull_time': '2022-01-06T07:48:37.800Z', 'push_time': '2022-01-06T07:48:32.687Z', 'repository_id': 807, 'signed': False}], 'type': 'IMAGE'}, {'addition_links': {'build_history': {'absolute': False, 'href': '/api/v2.0/projects/newdaq/repositories/market-search/artifacts/sha256:0afef0d74d5481d8a481feda14efa244a464a70eed12664559b4381bacaded14/additions/build_history'}, 'vulnerabilities': {'absolute': False, 'href': '/api/v2.0/projects/newdaq/repositories/market-search/artifacts/sha256:0afef0d74d5481d8a481feda14efa244a464a70eed12664559b4381bacaded14/additions/vulnerabilities'}}, 'digest': 'sha256:0afef0d74d5481d8a481feda14efa244a464a70eed12664559b4381bacaded14', 'extra_attrs': {'architecture': 'amd64', 'author': 'Ryan <zhang.rui@ricequant.com>', 'config': {'Entrypoint': ['/bin/sh', '-c', 'uvicorn market_search.main:app --host $SERVER_HOST --port $SERVER_PORT --workers $WORKERS     --log-config /tmp/logging_config.json'], 'Env': ['PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'LC_ALL=en_US.UTF-8', 'LANG=en_US.UTF-8', 'LANGUAGE=en_US.UTF-8', 'TZ=Asia/Shanghai', 'PYTHONIOENCODING=utf-8', 'PYTHONOPTIMIZE=1', 'LD_PRELOAD=/usr/lib64/libjemalloc.so.2', 'PIP_DISABLE_PIP_VERSION_CHECK=true', 'PIP_NO_CACHE_DIR=true', 'PIP_DISABLE_CACHE=true', 'PIP_INDEX_URL=https://pypi.douban.com/simple', 'PIP_DEFAULT_TIMEOUT=60', 'WORKERS=2', 'SERVER_HOST=0.0.0.0', 'SERVER_PORT=12033'], 'Labels': {'org.label-schema.build-date': '20200504', 'org.label-schema.license': 'GPLv2', 'org.label-schema.name': 'CentOS Base Image', 'org.label-schema.schema-version': '1.0', 'org.label-schema.vendor': 'CentOS', 'org.opencontainers.image.created': '2020-05-04 00:00:00+01:00', 'org.opencontainers.image.licenses': 'GPL-2.0-only', 'org.opencontainers.image.title': 'CentOS Base Image', 'org.opencontainers.image.vendor': 'CentOS'}, 'User': 'rice', 'WorkingDir': '/tmp'}, 'created': '2021-08-20T02:05:18.315164956Z', 'os': 'linux'}, 'icon': 'sha256:0048162a053eef4d4ce3fe7518615bef084403614f8bca43b40ae2e762e11e06', 'id': 5275, 'labels': None, 'manifest_media_type': 'application/vnd.docker.distribution.manifest.v2+json', 'media_type': 'application/vnd.docker.container.image.v1+json', 'project_id': 19, 'pull_time': '2021-09-08T02:42:09.913Z', 'push_time': '2021-08-20T02:20:20.702Z', 'references': None, 'repository_id': 807, 'size': 289411175, 'tags': None, 'type': 'IMAGE'}]
# print(len(s))

# s = "2021-03-30T07:40:36.137Z"
# s3 = "2021-03-30T07:40:36.137Z"
# import time,  datetime
# s1 = datetime.datetime.strptime(s, r'%Y-%m-%dT%H:%M:%S.%fZ')
# s4 = datetime.datetime.strptime(s3, r'%Y-%m-%dT%H:%M:%S.%fZ')
#
# print(s4 >= s1)
# print(itemgetter(s1), s1)
# print(time.localtime(),s1)
# print(time.ctime(1231888736.445134))


list3 = [{"one":1}, {"one":2}]
list4 = [i for i in list3 if i.get("one") != 1]
print(list4)
print(sorted(list3,  key = lambda x:x["one"], reverse=True))



s = "dev-20210322134124"

