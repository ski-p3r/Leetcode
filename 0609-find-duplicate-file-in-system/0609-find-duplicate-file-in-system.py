class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = {}
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            files_info = parts[1:]

            for file_info in files_info:
                file_parts = file_info.split("(")
                filename = file_parts[0]
                content = file_parts[1][:-1]

                full_path = directory + "/" + filename
                if content in content_to_paths:
                    content_to_paths[content].append(full_path)
                else:
                    content_to_paths[content] = [full_path]

        duplicate_groups = []
        for paths in content_to_paths.values():
            if len(paths) > 1:
                duplicate_groups.append(paths)

        return duplicate_groups