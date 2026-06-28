# ---- Tests ----
print(rearrange_name("Turing, Alan"))        # Expected: Alan Turing
print(rearrange_name("Curie, Marie"))        # Expected: Marie Curie
print(rearrange_name("Einstein, Albert"))    # Expected: Albert Einstein

# Edge case: no coma
print(rearrange_name("Ada Lovelace"))        # Expected: Ada Lovelace
