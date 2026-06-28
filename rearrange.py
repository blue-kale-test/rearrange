# code for rearrange, Blue-Kale didn't have it setup in the Repository.

def rearrange_name(name):
    # If unsure about format, we check for a coma
    if "," not in name:
        return name          # No rearranging needed

    last, first = name.split(",")
    return f"{first.strip()} {last.strip()}"
