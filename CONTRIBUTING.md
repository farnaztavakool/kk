# Contribution Guide
- Before beginning to write **any** code, please ``git checkout master`` and ``git pull``, so that you always locally have access to the latest working master branch.
- Use ``git commit -a -m "My commit message here"`` to commit changes to files that are already staged. If the file has not been staged, please use ``git add myFileName`` (or alternatively ``git add -A`` although less recommended) in order to add the file to the staging area.
- After doing any commit, please ``git push`` so that the rest of the group knows that you have committed changes to that feature branch.
- After each major merge request between feature branches or to the master branch, please update the changelog located in ``CHANGELOG.md`` in ``/``.