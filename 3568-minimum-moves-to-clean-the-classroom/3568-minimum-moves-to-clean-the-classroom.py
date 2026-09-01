from collections import deque
class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m, n = len(classroom), len(classroom[0])
        start_r = start_c = -1
        litter_coords = []
        for r in range(m):
            for c in range(n):
                cell=classroom[r][c]
                if cell == 'S':
                    start_r, start_c = r, c
                elif cell == 'L':
                    litter_coords.append((r, c))
        num_litter = len(litter_coords)
        if num_litter == 0:
            return 0  
        full_mask = (1 << num_litter) - 1
        litter_map = {pos: i for i, pos in enumerate(litter_coords)}
        best_energy = [[[-1] * (1 << num_litter) for _ in range(n)] for _ in range(m)]
        queue = deque([(start_r, start_c, 0, energy, 0)])
        best_energy[start_r][start_c][0] = energy
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c, mask, cur_energy, steps = queue.popleft()  
            if mask == full_mask:
                return steps  
            if cur_energy < best_energy[r][c][mask]:
                continue      
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = cur_energy - 1   
                    if next_energy >= 0:
                        next_mask = mask
                        cell_type = classroom[nr][nc]      
                        if cell_type == 'R':
                            next_energy = energy
                        elif cell_type == 'L':
                            litter_idx = litter_map[(nr, nc)]
                            next_mask |= (1 << litter_idx)      
                        if next_energy > best_energy[nr][nc][next_mask]:
                            best_energy[nr][nc][next_mask]=next_energy
                            queue.append((nr,nc,next_mask,next_energy,steps + 1))          
        return -1