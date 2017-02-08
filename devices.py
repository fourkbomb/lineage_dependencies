import json

with open('out.json') as f:
    mapping = json.load(f)

devices = {}

def simplify_reverse_deps(repo):
    if repo not in mapping or len(mapping[repo]) == 0:
        return {repo,}
    res = set()
    for i in mapping[repo]:
        res.update(simplify_reverse_deps(i))
    res.add(repo)
    return res

for repo in reverse_deps:
    if 'device' in repo and 'common' not in repo:
        codename = repo.split('_', maxsplit=3)[-1]
        if codename in devices:
            print("warning: dupe: %s"%codename)

        devices[codename] = list(simplify_reverse_deps(repo))

with open('devices.json', 'w') as f:
    json.dump(devices, f, indent=4)
