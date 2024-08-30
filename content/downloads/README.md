# Adding Downloads
The downloads page is automatically generated when the webpage is deployed via GitHub actions. It pulls releases from [this repo's releases page](https://github.com/esdlab/openfcst-site/releases).

For instructions on how to create a new release, [see GitHub's documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release).

If you wish to change which GitHub repository that releases are pulled from, edit the `github_repo` parameter in [hugo.toml](/hugo.toml). The format is `repo_owner/repo_name`.
