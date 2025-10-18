import math

def rotate_gcode(input_file, output_file, angle_deg):
    angle_rad = math.radians(angle_deg)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)

    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        for line in f_in:
            # Process only G0/G1 moves that include X or Y
            if line.startswith(("G0", "G1")) and ("X" in line or "Y" in line):
                parts = line.split()
                x = y = None
                for p in parts:
                    if p.startswith("X"):
                        try:
                            x = float(p[1:])
                        except ValueError:
                            pass
                    elif p.startswith("Y"):
                        try:
                            y = float(p[1:])
                        except ValueError:
                            pass

                if x is not None or y is not None:
                    new_parts = [parts[0]]
                    for p in parts[1:]:
                        if not (p.startswith("X") or p.startswith("Y")):
                            new_parts.append(p)
                    if x is None:
                        x = 0.0
                    if y is None:
                        y = 0.0
                    new_x = x * cos_a - y * sin_a
                    new_y = x * sin_a + y * cos_a
                    new_parts.insert(1, f"X{new_x:.3f}")
                    new_parts.insert(2, f"Y{new_y:.3f}")
                    f_out.write(" ".join(new_parts) + "\n")
                else:
                    f_out.write(line)
            else:
                f_out.write(line)

    print(f"Rotated {input_file} by {angle_deg}° and saved as {output_file}")

if __name__ == "__main__":
    input_file = input("Enter full (with file extension) input G-code filename: ").strip()
    output_file = input("Enter full (with file extension)  output G-code filename: ").strip()
    angle = float(input("Enter rotation angle (degrees, e.g., 45): ").strip())
    rotate_gcode(input_file, output_file, angle)
