# 2022-05-29 20:13:21
# Runtime 36ms(70.2%)
# Memory 15.1mb(29.6%)

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        Neither = "Neither"
        IPv4 = "IPv4"
        IPv6 = "IPv6"
        valid_hex_chars = {"a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"}
        
        if "." in queryIP and ":" not in queryIP:
            isIPV4 = True
        elif ":" in queryIP and "." not in queryIP:
            isIPV4 = False
        else:
            return Neither
        
        for i in queryIP:
            if not i.isalnum():
                if i != ":" and i != ".":
                    return Neither
        
        if isIPV4:
            segments = queryIP.split(".")
            if len(segments) != 4:
                return Neither
            for i in segments:
                if not i.isdigit():
                    return Neither
                if i != "0" and i.startswith("0"):
                    return Neither
                if not 0 <= int(i) <= 255:
                    return Neither
            return IPv4
        else:
            segments = queryIP.split(":")
            if len(segments) != 8:
                return Neither
            for i in segments:
                for j in i:
                    if j.isalpha():
                        if j not in valid_hex_chars:
                            return Neither
                if not 1 <= len(i) <= 4:
                    return Neither
            return IPv6
