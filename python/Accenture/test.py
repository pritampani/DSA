import sys
import collections

# Set recursion limit higher just in case, though iterative BFS is used
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return

    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # Parse N
        if not input_data: return
        N = int(next(iterator))
        bars = []
        for _ in range(N):
            bars.append((
                int(next(iterator)),
                int(next(iterator)),
                int(next(iterator)),
                int(next(iterator))
            ))
        # Parse Drop Coordinates
        drop_x = int(next(iterator))
        drop_y = int(next(iterator))
    except StopIteration:
        return

    # Store bar properties
    bar_info = []
    for idx, (x1, y1, x2, y2) in enumerate(bars):
        slope = (y2 - y1) // (x2 - x1)
        bar_info.append({
            'id': idx,
            'p1': (x1, y1),
            'p2': (x2, y2),
            'm': slope
        })

    # Identify Intersections and Group into Units
    intersections = {}
    adj = collections.defaultdict(list)
    
    for i in range(N):
        for j in range(i + 1, N):
            b1 = bar_info[i]
            b2 = bar_info[j]
            # Intersect only if slopes are different (1 vs -1)
            if b1['m'] == b2['m']:
                continue
            
            c1 = b1['p1'][1] - b1['m'] * b1['p1'][0]
            c2 = b2['p1'][1] - b2['m'] * b2['p1'][0]
            
            det = b1['m'] - b2['m']
            dx_val = c2 - c1
            
            # Check for integer intersection
            if dx_val % det == 0:
                ix = dx_val // det
                iy = b1['m'] * ix + c1
                
                # Verify intersection is strictly inside both segments
                min_x1, max_x1 = min(b1['p1'][0], b1['p2'][0]), max(b1['p1'][0], b1['p2'][0])
                min_x2, max_x2 = min(b2['p1'][0], b2['p2'][0]), max(b2['p1'][0], b2['p2'][0])
                
                if (min_x1 < ix < max_x1) and (min_x2 < ix < max_x2):
                    intersections[(i, j)] = (ix, iy)
                    intersections[(j, i)] = (ix, iy)
                    adj[i].append(j)
                    adj[j].append(i)

    unit_defs = []
    bar_unit_map = {}
    visited_bars = set()
    
    # Build connected components for Units
    for i in range(N):
        if i in visited_bars:
            continue
        
        stack = [i]
        comp = []
        while stack:
            curr = stack.pop()
            if curr in visited_bars:
                continue
            visited_bars.add(curr)
            comp.append(curr)
            for n in adj[curr]:
                if n not in visited_bars:
                    stack.append(n)
        
        # Define Unit
        if len(comp) == 2:
            # Cross Unit
            piv = intersections[(comp[0], comp[1])]
            uid = len(unit_defs)
            unit_defs.append({
                'type': 'cross',
                'ids': comp,
                'pivot': piv
            })
            for bid in comp:
                bar_unit_map[bid] = uid
        else:
            # Single Bar Unit
            for bid in comp:
                b = bar_info[bid]
                mx = (b['p1'][0] + b['p2'][0]) // 2
                my = (b['p1'][1] + b['p2'][1]) // 2
                uid = len(unit_defs)
                unit_defs.append({
                    'type': 'single',
                    'ids': [bid],
                    'pivot': (mx, my)
                })
                bar_unit_map[bid] = uid

    # Helper: Rotate point around pivot
    def rotate(pt, piv, d):
        px, py = piv
        x, y = pt
        dx, dy = x - px, y - py
        if d == 1: return (px - dy, py + dx) # CW
        if d == 2: return (px + dy, py - dx) # ACW
        return pt

    # Helper: Get current endpoints of a bar
    def get_segment(bid, uid, ustate):
        b = bar_info[bid]
        if ustate == 0:
            return b['p1'], b['p2']
        udef = unit_defs[uid]
        piv = udef['pivot']
        return rotate(b['p1'], piv, ustate), rotate(b['p2'], piv, ustate)

    # BFS Initialization
    # Queue State: (x, y, mode, ctx_id, ustate)
    # mode: 'air', 'bar', 'pivot'
    start_node = (drop_x, drop_y, 'air', -1, 0)
    queue = collections.deque([start_node])
    seen = set([start_node])
    ground_points = set()
    
    while queue:
        x, y, mode, ctx, ustate = queue.popleft()
        
        # Reached Ground
        if y == 0:
            ground_points.add(x)
            continue
            
        if mode == 'air':
            # Fall vertically
            best_y = -1
            best_bid = -1
            best_pt = None
            
            # Check all bars (assumed neutral state 0 initially)
            for bid in range(N):
                uid = bar_unit_map[bid]
                p1, p2 = get_segment(bid, uid, 0)
                
                min_x, max_x = min(p1[0], p2[0]), max(p1[0], p2[0])
                if min_x <= x <= max_x:
                    # Ignore vertical bars (shouldn't exist per problem statement)
                    if p1[0] == p2[0]: continue
                    
                    slope = (p2[1] - p1[1]) // (p2[0] - p1[0])
                    iy = p1[1] + slope * (x - p1[0])
                    
                    # Check if bar is strictly below current pos
                    if iy < y and iy > best_y:
                        best_y = iy
                        best_bid = bid
                        best_pt = (x, iy)
            
            if best_bid != -1:
                # Land on bar
                uid = bar_unit_map[best_bid]
                udef = unit_defs[uid]
                bx, by = best_pt
                
                # Check if landed on Pivot
                is_piv = (udef['type'] == 'cross' and (bx, by) == udef['pivot'])
                
                if is_piv:
                    ns = (bx, by, 'pivot', uid, 0)
                else:
                    ns = (bx, by, 'bar', best_bid, 0)
                
                if ns not in seen: seen.add(ns); queue.append(ns)
            else:
                # Hit Ground
                ns = (x, 0, 'air', -1, 0)
                if ns not in seen: seen.add(ns); queue.append(ns)

        elif mode == 'bar':
            bid = ctx
            uid = bar_unit_map[bid]
            udef = unit_defs[uid]
            
            # Action 1: Slide
            p1, p2 = get_segment(bid, uid, ustate)
            targets = [p1, p2]
            if udef['type'] == 'cross':
                targets.append(udef['pivot'])
            
            valid_targets = [t for t in targets if t[1] < y]
            
            if valid_targets:
                # Move to lowest point
                next_p = max(valid_targets, key=lambda p: p[1])
                
                is_piv = (udef['type'] == 'cross' and next_p == udef['pivot'])
                if is_piv:
                    ns = (next_p[0], next_p[1], 'pivot', uid, ustate)
                else:
                    ns = (next_p[0], next_p[1], 'bar', bid, ustate)
                
                if ns not in seen: seen.add(ns); queue.append(ns)
            else:
                # Action 2: Drop (only if at edge)
                if (x, y) == p1 or (x, y) == p2:
                    ns = (x, y, 'air', -1, 0)
                    if ns not in seen: seen.add(ns); queue.append(ns)
            
            # Action 3: Tilt (if neutral)
            if ustate == 0:
                for d in [1, 2]:
                    nx, ny = rotate((x, y), udef['pivot'], d)
                    ns = (nx, ny, 'bar', bid, d)
                    if ns not in seen: seen.add(ns); queue.append(ns)

        elif mode == 'pivot':
            uid = ctx
            udef = unit_defs[uid]
            
            # Action 1: Tilt (Required if stuck in V-shape/neutral)
            if ustate == 0:
                for d in [1, 2]:
                    ns = (x, y, 'pivot', uid, d)
                    if ns not in seen: seen.add(ns); queue.append(ns)
            else:
                # Action 2: Slide down legs (if tilted)
                for b_id in udef['ids']:
                    bp1, bp2 = get_segment(b_id, uid, ustate)
                    targets = [bp1, bp2]
                    valid_t = [t for t in targets if t[1] < y]
                    
                    if valid_t:
                        ns = (x, y, 'bar', b_id, ustate)
                        if ns not in seen: seen.add(ns); queue.append(ns)

    # Output sorted x coordinates
    sorted_x = sorted(list(ground_points))
    for val in sorted_x:
        print(f"{val} 0")

if __name__ == '__main__':
    solve()