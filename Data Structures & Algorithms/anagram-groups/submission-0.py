class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Đếm các ký tự trong từng từ và sử dụng các index trong bảng chữ cái (26 ký tự)
        làm key, số count sẽ làm value. Tổng thể tạo thành hashMaps để tìm được từ đó

        args:
            List strs: là mảng các chuỗi
        """

        maps = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                # Sử dụng ord là ASCII để lấy index của các ký tự
                count[(ord(c) - ord("a"))] += 1

            maps[tuple(count)].append(s)

        return list(maps.values())
