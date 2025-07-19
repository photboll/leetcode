#
# @lc app=leetcode id=1233 lang=python3
#
# [1233] Remove Sub-Folders from the Filesystem
#

# @lc code=start

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        strange defintion of subfolders, in ex1 c/d and c/f are not considered subfolder because c is not present as 
        a standdalone folder. even though both c/d and c/f are subfolders of c
        """
        folder.sort()
        result = [folder[0]]
        for path in folder[1:]:
            if not path.startswith(result[-1] + "/"):
                result.append(path)

        return result
# @lc code=end

