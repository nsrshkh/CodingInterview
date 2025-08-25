from typing import List


def trap_rain_water(height: List[int]) -> int:
    """
    Calculates the total amount of rainwater that can be trapped between bars.

    This function solves the "Trapping Rain Water" problem using an efficient
    two-pointer approach, which achieves O(n) time complexity and O(1) space
    complexity.

    The logic relies on the idea that the amount of water trapped above any
    bar is determined by the minimum of the maximum height of the walls to its
    left and right.

    Args:
        height: A list of non-negative integers representing an elevation map.

    Returns:
        The total amount of water that can be trapped.
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    total_water = 0

    while left < right:
        # The amount of trapped water is limited by the shorter of the two max walls.
        if height[left] < height[right]:
            # The left wall is shorter, so the water level is determined by left_max.
            if height[left] >= left_max:
                # This bar is a new, taller left wall. No water can be trapped here.
                left_max = height[left]
            else:
                # This bar is shorter than the left_max, so it traps water.
                total_water += left_max - height[left]
            left += 1
        else:
            # The right wall is shorter or equal, so the water level is determined by right_max.
            if height[right] >= right_max:
                # This bar is a new, taller right wall.
                right_max = height[right]
            else:
                # This bar is shorter than the right_max, so it traps water.
                total_water += right_max - height[right]
            right -= 1

    return total_water

# Example usage from the classic problem statement:
elevation_map = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
trapped_water = trap_rain_water(elevation_map)
print(f"The elevation map {elevation_map} can trap {trapped_water} units of water.")

# Another example
elevation_map_2 = [4, 2, 0, 3, 2, 5]
trapped_water_2 = trap_rain_water(elevation_map_2)
print(f"The elevation map {elevation_map_2} can trap {trapped_water_2} units of water.")