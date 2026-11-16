def calc_area_rectangular(width: float, height: float, room_type: str = "unknown") -> float | None:
    area = width * height
    if width <= 0 or height <= 0:
        print("Dimensions can't be negative or zero")
        return None
    return area


bedroom1 = calc_area_rectangular(width=5, height=4)
bedroom2 = calc_area_rectangular(width=4, height=7)
kitchen = calc_area_rectangular(width=4, height=9)

total_area = bedroom1 + bedroom2 + kitchen
print(f"The total area is {total_area}")