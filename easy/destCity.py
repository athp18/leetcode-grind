class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if not paths:
            return ""
        incoming = [path[0] for path in paths]
        outgoing = [path[1] for path in paths]
        for city in outgoing:
            if city not in incoming:
                return city
            
        
