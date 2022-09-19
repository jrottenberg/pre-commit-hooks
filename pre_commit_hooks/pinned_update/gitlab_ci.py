# gitlab_ci functionnality


from urllib.parse import urlparse

import ruamel.yaml

from pre_commit_hooks.utils import cmd_output, get_all_tags, highest_version

yaml = ruamel.yaml.YAML()

yaml.indent(mapping=2, sequence=4, offset=2)


def update_gitlab_ci(gitlab_ci: str) -> int:
    retval = 0

    with open(gitlab_ci, "r") as gitlab_ci_file:
        original_gitlab_ci_object = yaml.load(
            gitlab_ci_file,
        )
    updated_gitlab_ci_object = original_gitlab_ci_object

    if "include" not in original_gitlab_ci_object:
        return retval

    _, gitlab_origin, _ = cmd_output("git", "remote", "get-url", "origin")
    if gitlab_origin.startswith("http"):
        url = urlparse(gitlab_origin)
        prefix = f"{url.scheme}://{url.netloc}/"
    else:
        prefix = gitlab_origin.split(":")[0] + ":"

    for elt in updated_gitlab_ci_object["include"]:
        if "ref" in elt:
            position = updated_gitlab_ci_object["include"].index(elt)
            all_tags = get_all_tags(prefix + elt["project"])
            latest = highest_version(all_tags)
            if elt["ref"] != latest:
                elt["ref"] = latest
                updated_gitlab_ci_object["include"][position] = elt
                retval += 1

    if retval > 0:
        with open(gitlab_ci, "w") as gitlab_ci_file:
            yaml.dump(updated_gitlab_ci_object, gitlab_ci_file)

    return retval
